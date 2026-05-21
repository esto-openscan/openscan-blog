---
title: "OpenScan3 Firmware: How tasks work in practice"
date: "2026-04-10T11:57:33+02:00"
author: "Elias Stognienko"
description: "A practical look at how tasks work in OpenScan3: lifecycle, states, progress, logs, cancellation, and why some tasks stay in the background while others take over the interface."
shopify_summary_html: |-
  <p data-end="241" data-start="50">A practical look at how tasks work in OpenScan3: lifecycle, states, progress, logs, cancellation, and why some tasks stay in the background while others take over the interface.</p>
  <p data-is-only-node="" data-is-last-node="" data-end="412" data-start="243"> </p>
categories:
  - "OpenScan Blog"
tags:
  - "Firmware"
image:
  path: "/assets/img/posts/2026-04-10-openscan3-firmware-how-tasks-work-in-practice/os3-task-in-practice-d6deff93-1c00-49f4-b400-5b70af9954ca.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-how-tasks-work-in-practice"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-firmware-how-tasks-work-in-practice"
---

*This is a blog post in a series on the OpenScan3 firmware. Read the [previous post here](https://openscan.eu/blogs/news/openscan3-task-system-introduction). Comments, questions, and suggestions are always very welcome and a great help for future work on the firmware.*

In the last blog post, I explained [why we needed a task system](https://openscan.eu/blogs/news/openscan3-task-system-introduction) in OpenScan3. This time, I want to stay closer to the practical side: what tasks look like in daily use, how they behave, and what kind of mental model makes them easier to understand.

### The basic mental model

A good way to think about tasks is this: OpenScan3 treats longer-running operations as named jobs with a lifecycle.

That could be a scan, a calibration routine, a file transfer, or something more specialized in the future. The exact implementation doesn't matter. The important part is that the system knows this work has started, is currently running, may be paused or cancelled, may finish successfully, or may fail.

From the user side, that means less guessing. Instead of asking, “Is the scanner still doing something?” or “Did it get stuck?”, the interface can answer with an actual task state and, in many cases, progress information.

### The task drawer

If you have used recent firmware versions, you may already have seen the task drawer on the right side of the web UI.

![](/assets/img/posts/2026-04-10-openscan3-firmware-how-tasks-work-in-practice/task-drawer-with-red-frame.jpg)

That drawer is the most visible part of the task system in everyday use. It gives long-running work a dedicated place in the interface. Active tasks appear there with their current state and, if available, progress information.

### Task states

One of the most useful parts of the system is that tasks move through explicit states.

In practice, that usually means states such as:

- **pending** — the task exists, but has not started yet
- **running**
- **paused** — if the task supports pausing and resuming

There are also terminal states such as:

- **completed** — everything finished as expected
- **cancelled** — the task was stopped by the user
- **failed** or **interrupted** — something went wrong, or the task could not finish, for example because the device lost power

These states are useful because they turn background work into something visible and understandable. A task is not just “doing something somewhere.” It is in a known state, and the UI can reflect that.

### Progress

Many tasks can also report progress.

A task can show how much work has already been done and how much is left. In many cases, it can also provide a short message about the current step. That might be something like preparing, capturing images, saving files, or moving to the next scan position.

This makes a big difference in practice. Progress does not just tell you that something is happening. It tells you where you are in the workflow.

### Some tasks stay in the background, some take over

Not all tasks feel the same in the interface, and that is intentional.

Some tasks can quietly run in the background and simply appear in the task drawer while they do their work. Others are more central and should clearly take priority.

A scan is the obvious example of the second category. It is not just another small background action. It is a major workflow that uses hardware, takes time, and deserves a focused UI.

![](/assets/img/posts/2026-04-10-openscan3-firmware-how-tasks-work-in-practice/2026-04-10-os3-scan-task-view.jpg)

That is why an active scan is treated differently from smaller side tasks. It gets visible progress in the main area, control actions such as pause or cancel, and its own place in the overall interaction flow.

So if the task drawer is the general overview, the scan overlay is the focused view for a task that currently owns the workflow.

### Logs and details when you need them

Most of the time, you do not want a wall of technical output.

You mainly want to know whether the task is running, whether progress is moving, and whether the result was successful.

But when something behaves unexpectedly, more detail becomes extremely useful. That is why task views can expose logs and raw task details. They are not the main story in everyday use, but they are there when you need more context.

This is especially helpful for debugging, support, and community-driven experimentation. If you are testing a custom workflow or trying to understand a failure, having task-specific information in one place is much better than guessing what happened.

### In the next posts

In later posts, I want to get more concrete: look at individual tasks in more detail, dissect the scan task, show some example tasks, and eventually walk through how to build custom tasks for your own workflows.
