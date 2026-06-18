---
title: "OpenScan3 Firmware: Example Tasks"
date: "2026-06-17T10:24:12+02:00"
author: "Elias Stognienko"
description: "A developer-focused walkthrough of OpenScan3 example Tasks, showing Task patterns for custom firmware workflows."
categories:
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "architecture"
  - "task-system"
  - "tasks"
image:
  path: "/assets/img/posts/2026-06-17-openscan3-firmware-example-tasks/os3-example-tasks.png"
redirect_from:
  - "/blogs/news/openscan3-firmware-example-tasks"
  - "https://openscan.eu/blogs/news/openscan3-firmware-example-tasks"
---

In the [previous post of this series](https://blog.openscan.eu/posts/openscan3-firmware-how-tasks-work-in-practice/) I described how Tasks appear to the user. In this post we will look at some example Tasks we've included right in the source code for developers as a practical example. This post is a bit more technical and dedicated to those who are thinking about including their own Tasks as plugins for their specific workflows.

The OpenScan3 Task subsystem is designed flexible and truly hackable. For many simple ideas you might just want to use the API, but if you need deep access to the OpenScan3 system, you can do it with Tasks directly skipping the API layer entirely.

In OpenScan3 we needed some abstraction around long-running procedures or functions. Our design goals had been in no particular order:
- make Tasks easy to add, modify and run especially for non-Python programmers
- treat Tasks like plugins and enable them to get deeper into the firmware than the exposed REST API
- make Tasks versatile, status rich, pausable and like a playground for experiments
- build OpenScan3 features with Tasks to make them exchangeable, easier to maintain and improve

I already explained why we needed Tasks in OpenScan3, and I will not go into details like Task autodiscovery and how the `TaskManager` actually works, because you can find up-to-date information on this in the [developer docs](https://github.com/OpenScan-org/OpenScan3/tree/develop/docs).

Instead, we will look at the `demo_examples.py`[^path] and learn what Tasks are made of and get an idea of the overall design philosophy around Tasks.

<!-- markdownlint-capture -->
<!-- markdownlint-disable -->
> **Support note.** But first, before we add another Task to the queue: if you want to help us keep OpenScan3 moving from pending prototype to completed contraption, you can support OpenScan by [sponsoring us on Patreon](https://www.patreon.com/OpenScan), testing the firmware, reporting issues, or contributing to the open-source code. It helps us keep the background Tasks running: testing, documenting, fixing the boring bits, and providing an extensible foundation for a hackable 3d scanner.
{: .prompt-tip }
<!-- markdownlint-restore -->

## What a Task is made of


### Task Model and `TaskManager`

Before we go into the Tasks themselves, we have to understand that they are executable code units that are orchestrated by the `TaskManager` and have a persistable Pydantic model as state.

In the [previous post](https://blog.openscan.eu/posts/openscan3-firmware-how-tasks-work-in-practice/) we saw that this Pydantic model incorporates status enums, numeric progress and written progress. The full model looks like this:
```python
class Task(BaseModel):
    """Represents a background task."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    task_type: str
    is_exclusive: bool = Field(False, description="Whether this task is exclusive and should not run concurrently")
    is_blocking: bool = Field(False, description="Whether this task is blocking and should run in a separate thread")
    
    status: TaskStatus = TaskStatus.PENDING
    progress: TaskProgress = Field(default_factory=TaskProgress)
    result: Optional[Any] = None
    error: Optional[str] = None
    
    created_at: datetime = Field(default_factory=datetime.now)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    run_args: tuple = Field(default_factory=tuple, description="Positional arguments the task was started with.")
    run_kwargs: dict = Field(default_factory=dict, description="Keyword arguments the task was started with.")
```
Most of the fields are managed by the Task itself and we will learn about them as we go through the examples.

A few fields are not a concern of the Task:
- `status` and `error`,
- as well as `created|started|completed_at`
  are controlled by the `TaskManager`.

The `TaskManager` registers the Tasks, manages a queue of Tasks, and decides when and how to start them. It can also pause and cancel Tasks, provided the Tasks cooperate and implement pause points and checks for cancellation, as we will see in the examples.

A mental image could be that the Task is actual behavior, the Task model is the state the clients see through the API, and the `TaskManager` is responsible for the whole lifecycle.
Or stated differently: The `TaskManager` manages lifecycle, persistence and events; the Task computes and reports progress (and optional result).

### The shared foundation: `BaseTask`

Before we look at *Hello World* like example Tasks, we examine the origin of every Task descendant: The `BaseTask`.


```python
class BaseTask(ABC):
    task_name: ClassVar[str | None] = None
    task_category: ClassVar[str] = "community"
    is_exclusive: ClassVar[bool] = False
    is_blocking: ClassVar[bool] = False

    def __init__(self, task_model: Task):
        self._task_model = task_model

        # Cooperative lifecycle signals used by TaskManager.
        self._stop_event = asyncio.Event()
        self._pause_event = asyncio.Event()
        self._pause_event.set()  # Start unpaused.

    @property
    def id(self) -> str:
        return self._task_model.id

    @property
    def name(self) -> str:
        return self._task_model.name

    @abstractmethod
    async def run(self, *args: Any, **kwargs: Any) -> Any:
        ...

    # Lifecycle hooks called by TaskManager.
    def cancel(self) -> None: ...
    def is_cancelled(self) -> bool: ...
    def pause(self) -> None: ...
    def resume(self) -> None: ...
    async def wait_for_pause(self) -> None: ...
    def is_paused(self) -> bool: ...

    # Convenience helper for simple progress updates.
    def _update_progress(self, current: float, total: float, message: str = "") -> None:
        ...
```

#### Attributes and Properties
Let's understand the attributes first:
- `task_name`: should be unique and is later used by e.g., the API to call this specific Task and must end in `_task`.
- `task_category`: is a string and so far we used `example` / `community` / `core`. You will most likely use the `community` category because we would suggest to reserve `core` Tasks for "official" or canonical Tasks which may be subject to change in future firmware releases.
- `is_exclusive`: flags whether the Task can run alongside other Tasks concurrently (False) or if it needs to run exclusively (True) because it e.g., needs access to hardware like motors.
- `is_blocking`: flags whether the Task is using Python async features (False) or is a piece of synchronous code (True), which may be easier for Python or programming novices.

Also, we have two thin wrappers for properties for convenience around `id` and `name`.

#### `run()`: the Task entrypoint
This is the entry for the Task routine and logic and must be overwritten by custom Tasks. We will examine examples for `run()` methods later, for now we note, that everything a Task does happens here.

#### Cooperative lifecycle controls
To make the lifecycle of Tasks manageable, we have the following methods:
- `cancel()`: Signals the Task to cancel its execution. The `run()` method should periodically check `is_cancelled()` to gracefully terminate.
- `pause()`: Signals the Task to pause execution. The run loop must use `wait_for_pause()` to honor this.
- `resume()`: Signals the Task to continue execution.
-   `async wait_for_pause()`: Pauses Task execution until resume() is called. This should be `awaited` inside the main loop of an async Task (more on that later).

We can also check the status a Task is in currently with:
- `is_cancelled()`: True if a cancellation request has been made.
- `is_paused()`: True if the Task is currently signaled to be in a paused state.

##### Progress updates: direct helper vs. yielded progress

A Task can also update its progress. At the lowest level, BaseTask contains a small _update_progress() helper:

```python
def _update_progress(self, current: float, total: float, message: str = "") -> None:
  self._task_model.progress.current = current
  self._task_model.progress.total = total
  self._task_model.progress.message = message
```

This helper directly mutates the Pydantic model of the Task. That is useful for tiny Tasks, simple internal updates or places where we really just want to set progress on the model.

However, this is not the only progress path and not the one we usually want for long-running async Tasks. For async generator Tasks, the preferred pattern is to yield TaskProgress objects. In that case the Task describes progress, while the TaskManager applies the update, persists state and publishes events to clients.

So, the short version is:

- direct model updates are possible and sometimes convenient
- yielded TaskProgress objects are the cleaner path for streaming progress from async Tasks

### The takeaway

The TaskManager controls the lifecycle of a Task, the BaseTask provides the hooks for this, and our run() methods have to cooperate. A good Task should report useful progress, provide pause points where appropriate and check whether it has been canceled.


## Example Tasks
We included some example Tasks in the OpenScan3 codebase with the name `demo_examples.py`.

When we look at the file, we see the usual Python module import at the top and the setup of our logging system below.

After this we see a bunch of Python classes with descriptive names which all inherit from the class `BaseTask`. Each class is a different Task (we will look at each separately below).

### A simple synchronous Task: `HelloWorldBlockingTask`

This Task is perfect for quick experiments, shorter workflows or as an entrypoint for new developers and programming beginners.

We can see that this Task is class which inherits from `BaseTask`, sets the attributes and overrides the `run()` method.
```python
class HelloWorldBlockingTask(BaseTask):
	task_name = "hello_world_blocking_task"  
	task_category = "example"  
	is_exclusive = False  
	is_blocking = True
		
  def run(self, *args: Any, **kwargs: Any) -> Any:
    """Run the blocking example task.
  
    Args:
      *args: Unused.
      **kwargs: May contain `duration`.
  
    Returns:
      A simple completion string.
    """
    duration = kwargs.get("duration", 3)
    logger.info(f"[{self.id}] Starting blocking task for {duration} seconds. This will run in a thread.")
    time.sleep(duration)
    logger.info(f"[{self.id}] Blocking task finished.")
    return "Blocking task complete."
```
We see that the Task can run beside other Tasks (`is_exclusive=False`) and `is_blocking=True`, which is an important signal for the `TaskManager`. The `TaskManager` will spawn such a Task in an extra thread thus isolating the code from the event loop. They are convenient for simple synchronous workflows, but not the right shape for work that must pause or cancel precisely.

We then have the `run()` function which takes broad arguments in form of keyword arguments or arbitrary dictionaries and has no defined return type. 

As you can see, we first evaluate if we receive a `duration` in the argument dictionary and use it or set it to `3` as default. We then emit a logging message. Then we use the synchronous `time.sleep()` to wait. This is the reason for the name of this Task. Usually the Python program would halt here and the OpenScan device would become unresponsive because of this. This doesn't happen though, because the `TaskManager` spawns blocking Tasks like this one in a separate thread. This makes programming very convenient. You don't have to reason about async code and can just program a Task like you would program a local synchronous script for some workflow on your device. We implemented this also as a good entry point for programming beginners or Python novices to get started quick and without the need to grasp more advanced concepts around `async/await`.
The `run()` function finishes with another logging message and returns the string "Blocking task complete".

### A progress-reporting Task: `HelloWorldProgressTask`
This type of generator Task is ideal for streaming processes like uploads, downloads, scans, focus stacking, and similar multistep workflows that naturally produce progress events while they run.

The important difference to the blocking Task is not just `async def`. This Task is an async generator: it yields `TaskProgress` objects. The `TaskManager` consumes those yielded progress updates, publishes them and persists them according to its own rules.


```python
class HelloWorldProgressTask(BaseTask):
    """Demonstrates the canonical async progress-reporting task pattern."""

    task_name = "hello_world_progress_task"
    task_category = "example"
    is_exclusive = False
    is_blocking = False

    async def run(self, total_steps: int = 10, interval: float = 0.5) -> AsyncGenerator[TaskProgress, None]:
        """Run the async progress example task.

        Args:
            total_steps: The number of steps to complete.
            interval: Sleep interval per step.

        Yields:
            TaskProgress updates.
        """
        if total_steps <= 0:
            yield TaskProgress(current=0, total=0, message="No steps to run.")
            return

        yield TaskProgress(current=0, total=total_steps, message="Starting Hello World progress task.")

        for i in range(1, total_steps + 1):
            await self.wait_for_pause()
            if self.is_cancelled():
                logger.info(f"Task {self.name} ({self.id}) stopping due to cancellation.")
                yield TaskProgress(
                    current=i - 1,
                    total=total_steps,
                    message="Hello World progress task cancelled.",
                )
                return

            await asyncio.sleep(interval)
            yield TaskProgress(
                current=i,
                total=total_steps,
                message=f"Hello World! Step {i} of {total_steps} complete.",
            )

        logger.info(f"[{self.id}] HelloWorldProgressTask finished.")
        self._task_model.result = f"Hello World progress task completed after {total_steps} steps."
```
The `run()` method accepts normal Python arguments. Here we use `total_steps` and `interval`, but a real Task could accept scan settings, file paths, camera names or workflow options.

The actual work happens in the loop. At the beginning of every step we call `await self.wait_for_pause()`. This is the cooperative pause point. If the `TaskManager` pauses the Task, execution waits here until it is resumed.

Right after that we check `self.is_cancelled()`. Cancellation is cooperative too: the `TaskManager` can signal cancellation, but the Task has to check the signal and return cleanly.

Progress is reported with `yield TaskProgress(...)`. This is the canonical progress-reporting path for long-running async Tasks. Instead of calling `_update_progress()` directly, the Task yields progress objects and lets the `TaskManager` update the model, persist state and notify clients.

At the end, the Task sets an optional final result directly on `self._task_model.result`. Generator Tasks cannot return a value in the same way a normal async function can, so setting the result on the model is the intended pattern.


#### An exclusive hardware-using Task: `ExclusiveDemoTask`
The first two examples basically revolved around synchronous and asynchronous code but were both meant to run concurrently with other Tasks because `is_exclusive=False`. 

There are times when you don't want that or when it may be even dangerous to do it. Imagine two Tasks getting into conflict over motor movement or slower hardware like the camera. We need a way to tell the system: this Task consumes hardware, I/O or other resources in a way we do not want other Tasks to interfere with at runtime.

The Scan Task is a perfect example because it involves motor movement, camera access and creates some significant I/O pressure because we write the photos asynchronously to disk.

```python
class ExclusiveDemoTask(BaseTask):
    """Demonstrates an exclusive async task."""

    task_name = "exclusive_demo_task"
    task_category = "example"
    is_exclusive = True
    is_blocking = False

    async def run(self, duration: float = 1.0):
        """Sleep for a given duration to simulate exclusive work.

        Args:
            duration: Duration in seconds to sleep.
        """
        logger.info(f"Starting exclusive task '{self.id}' for {duration}s.")
        self._task_model.progress = TaskProgress(current=0, total=1, message="Starting exclusive lock")
        await asyncio.sleep(duration)
        self._task_model.progress = TaskProgress(current=1, total=1, message="Finished exclusive lock")
        logger.info(f"Finished exclusive task '{self.id}'.")
        return {"status": "completed", "duration": duration}
```

This example is intentionally tiny. It directly assigns `self._task_model.progress`, which is fine for a minimal non-streaming demo where we only set a start and finish state.

Because this is a regular async Task and not an async generator, it can simply
return a value. The TaskManager stores that return value as the Task result.
Generator Tasks are different (as we have seen): if they need a final result, they set
`self._task_model.result` before finishing.

For longer exclusive Tasks, especially Tasks that perform multiple hardware steps, I would usually use the same generator pattern we saw above: `yield TaskProgress(...)`, let the `TaskManager` apply and publish the update, and keep the Task focused on the actual workflow.

One important note: An exclusive Task only starts when no other Task is running (or paused!).[^terminal] If an exclusive Task is pending, later non-exclusive Tasks are queued behind it.


## Outlook

We have now seen the basic shapes of OpenScan3 Tasks: simple blocking Tasks, progress-reporting async Tasks and exclusive Tasks for workflows that need control over hardware.

In one of the next posts, I'm going to show how to add your own Task to the firmware and point out common pitfalls to avoid when developing Tasks.

If this gives you ideas for things OpenScan3 could automate, extend, or connect to, open a [GitHub issue](https://github.com/OpenScan-org/OpenScan3/issues) and sketch the idea there. Even a rough idea can start a useful discussion, help us spot recurring needs and maybe turn into something everyone benefits from later!

## Footnotes

[^path]: The file is in the `openscan_firmware/controllers/services/tasks/examples/` directory in the source code, which you can find [here on GitHub](https://github.com/OpenScan-org/OpenScan3/blob/develop/openscan_firmware/controllers/services/tasks/examples/demo_examples.py).

[^terminal]: It's important to check first for paused Tasks in the queue before debugging an exclusive Task, trust me.
