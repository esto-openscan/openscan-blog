---
title: "OpenScan3 Firmware: A NodeODX Reconstruction Task"
date: "2026-10-23T10:00:00+02:00"
author: "Elias Stognienko"
description: "Learn how an OpenScan3 community Task connects a scanner to a self-hosted NodeODX pipeline, tracks reconstruction progress, and provides a download link for the resulting 3D model."
categories:
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "task-system"
  - "community-task"
  - "photogrammetry"
  - "nodeodx"
  - "odx"
image:
  path: "/assets/img/posts/2026-10-22-openscan3-nodeodx-reconstruction-task/os3-nodeodx.png"
  alt: "OpenScan3 project dashboard showing an active NodeODX reconstruction Task"
---

Capturing the photos is only the first step in a scanning workflow. They still need to be processed into a 3D model, which often means moving them from the scanner to another machine.

In this example, an OpenScan3 Task sends a completed scan to a [NodeODX](https://github.com/WebODM/NodeODX) server instance on the local network and starts reconstruction. The same Task then reports progress in OpenScan3 and makes the finished 3D model available for download.

NodeODX provides an API for open-source photogrammetry pipelines and is available as a Docker container. Specifically, [ODX](https://github.com/WebODM/ODX) is built to process aerial and ground imagery. Photogrammetry is versatile, though, and ODX can still produce useful results with scanner rigs like OpenScan devices.

## Prerequisites

Before connecting OpenScan3 to NodeODX, prepare three things: a NodeODX server, community Tasks enabled in OpenScan3, and a scan to reconstruct.

### NodeODX server
Run NodeODX on a PC reachable from the scanner. For a local Docker setup, use:
```bash
docker run -d \
  --name nodeodx \
  --restart unless-stopped \
  -p 3000:3000 \
  -v /srv/nodeodx/data:/var/www/data \
  --gpus all \
  webodm/nodeodx:gpu
```

This starts NodeODX with GPU acceleration. Docker must have NVIDIA GPU support enabled.

### Enabled Community Tasks

Use a developer image to add community Tasks; autodiscovery is enabled by default. The [OpenScan3 Task documentation](https://github.com/OpenScan-org/OpenScan3/blob/develop/docs/TASKS.md) explains how Tasks are structured and registered.

On stable images, enable `OPENSCAN_TASK_AUTODISCOVERY=1` in the systemd service file ([see the documentation](https://github.com/OpenScan-org/OpenScan3/blob/develop/docs/TASKS.md#2-enable-autodiscovery-locally)).

### A Scan

Finally, prepare a project with a scan to upload. This example uses a JPG scan without focus stacking: an autofocus capture of the [OpenScan Benchy](https://openscan.eu/pages/openscan-benchy) figurine with 300 photos.

## The connecting OpenScan3 Task

The following example sets up a simple Task and walks through each step.

### What the task needs to do

The Task takes a project name, finds the scan's photos, and sends them to NodeODX. NodeODX responds with a job ID, which OpenScan3 uses to check the reconstruction and report progress in the frontend. The example follows this path from project lookup to the download link.

### Preparing OpenScan3 for a community Task

For OpenScan3 to load the code, Task autodiscovery must be enabled. Development images enable it by default; standard images register only built-in Tasks unless autodiscovery is enabled (see above).

Community Tasks installed outside the firmware package belong in:

```text
/var/openscan3/community-tasks/
```

Save the implementation from the next section in the community Tasks directory with this filename:

```text
/var/openscan3/community-tasks/nodeodx_reconstruction_task.py
```

The file can also be copied to this directory through the scanner's SAMBA share when using a developer image.

When OpenScan3 starts and discovers the file, check the log for a registration message like this. It confirms that the firmware found the module and registered the Task as a community Task:
```log
DEBUG - [task_manager.py:autodiscover_tasks] - Imported module 'openscan_firmware.tasks.community' for autodiscovery.
INFO - [task_manager.py:autodiscover_tasks] - Task 'nodeodx_reconstruction_task' (exclusive: False, blocking: False, category: community) registered via external tasks dir.
INFO - [task_manager.py:autodiscover_tasks] - Autodiscovery complete. Registered tasks: ['cloud_download_task', 'cloud_upload_task', 'external_trigger_run_task', 'focus_stacking_task', 'nodeodx_reconstruction_task', 'qr_scan_task', 'scan_task']
```


### The `NodeodxReconstructionTask`

With the file in place, the implementation has four jobs: locate the project's JPG photos, upload them, poll NodeODX for progress, and store the finished download URL. This implementation was tested with NodeODX API 2.3.1. It reads progress from the `/task/{uuid}/info` response; the current 2.4.0 API schema does not list that field, so verify the response before using this code with newer versions. The complete Task used in this experiment is:

```python
"""Reconstruct an OpenScan project with NodeODX."""

import asyncio
from contextlib import ExitStack

import requests

from openscan_firmware.controllers.services.projects import get_project_manager
from openscan_firmware.controllers.services.tasks.base_task import BaseTask
from openscan_firmware.models.task import TaskProgress


class NodeodxReconstructionTask(BaseTask):
    task_name = "nodeodx_reconstruction_task"

    async def run(self, project_name: str, server_url: str):
        project = get_project_manager().get_project_by_name(project_name)
        images = sorted(project.path_obj.glob("scan*/*.jpg"))
        server_url = server_url.rstrip("/")

        yield TaskProgress(
            total=100,
            message="Uploading images to NodeODX",
        )

        task_uuid = await asyncio.to_thread(
            self._upload, server_url, project_name, images
        )
        task_url = f"{server_url}/task/{task_uuid}"

        while True:
            response = await asyncio.to_thread(
                requests.get, f"{task_url}/info", timeout=30
            )
            response.raise_for_status()
            info = response.json()
            status = info["status"]["code"]
            progress = info["progress"]

            yield TaskProgress(
                current=progress,
                total=100,
                message=f"NodeODX reconstruction: {progress:.0f}%",
            )

            if status == 40:  # COMPLETED
                self._task_model.result = {
                    "uuid": task_uuid,
                    "download_url": f"{task_url}/download/all.zip",
                }
                return

            if status in {30, 50}:  # FAILED or CANCELLED
                raise RuntimeError(f"NodeODX task ended with status {status}")

            await asyncio.sleep(2)

    @staticmethod
    def _upload(server_url, project_name, images):
        with ExitStack() as stack:
            files = [
                ("images", (path.name, stack.enter_context(path.open("rb"))))
                for path in images
            ]
            response = requests.post(
                f"{server_url}/task/new",
                data={"name": project_name},
                files=files,
                timeout=300,
            )
        response.raise_for_status()
        return response.json()["uuid"]
```

The code follows the same sequence from start to finish:

1. find the images belonging to the OpenScan project
2. upload them to NodeODX
3. follow the reconstruction job
4. expose the finished reconstruction as the task result

#### 1. Getting the Photos

The caller passes the OpenScan3 project name to `run()`. The Task resolves that project through the project manager, then collects the JPG files from its scan folders. This gives the upload step the actual photos to send to NodeODX.

#### 2. Sending the Photos

Once collected, the photos are uploaded with `requests`. These HTTP calls are blocking, while OpenScan3 Tasks run asynchronously. `asyncio.to_thread()` runs the upload and status checks without blocking the firmware's event loop.

#### 3. Showing Progress
After the upload, the Task polls NodeODX for the job status. Each response includes a progress percentage, which the Task yields as a `TaskProgress` update. OpenScan3 forwards that update to the frontend, so progress appears there without separate NodeODX queries.


#### 4. Link to the result

When NodeODX reports that the job is complete, the Task stores the job UUID and `all.zip` download URL in its result. OpenScan3 can then expose the URL for downloading the reconstruction.

### Running the Task

#### Starting the Task
To run the Task, use the scanner's hostname `openscan.local` and the NodeODX PC's LAN address, `192.168.178.23`. The project `benchy-odx-task` is already on the scanner. From a PC on the network, send a POST request with the project name and NodeODX URL:

```bash
curl -X POST \
  http://openscan.local/api/latest/tasks/nodeodx_reconstruction_task \
  -H 'Content-Type: application/json' \
  -d '{
    "kwargs": {
      "project_name": "benchy-odx-task",
      "server_url": "http://192.168.178.23:3000"
    }
  }'
```

The same request can be sent from OpenScan3's interactive API documentation at `http://openscan.local/api/latest/docs`. The screenshot shows the endpoint and its input fields in that interface:

![Starting the OpenScan3 NodeODX Task through the API](/assets/img/posts/2026-10-22-openscan3-nodeodx-reconstruction-task/2026-10-15-start-via-API-docs.png){: .w-40}


On success, OpenScan3 returns a Task status object. The `id` identifies this run, `status` starts as `running`, and `run_kwargs` confirms the project and server URL:
```json
{
  "id": "118196ed-5400-41fa-8950-5b8327f3e47c",
  "name": "nodeodx_reconstruction_task",
  "task_type": "nodeodx_reconstruction_task",
  "is_exclusive": false,
  "is_blocking": false,
  "status": "running",
  "progress": {
    "current": 0,
    "total": 0,
    "message": ""
  },
  "result": null,
  "error": null,
  "created_at": "2026-10-22T14:25:04.333444",
  "started_at": "2026-10-22T14:25:04.335686",
  "completed_at": null,
  "depends_on": null,
  "run_args": [],
  "run_kwargs": {
    "project_name": "benchy-odx-task",
    "server_url": "http://192.168.178.23:3000"
  }
}
```




#### Checking Progress

The response includes a Task ID. Use it in a GET request to retrieve the latest status while the reconstruction is running:
```bash
curl "http://openscan.local/api/latest/tasks/<task-id>"
```

The response contains a `progress` object. Here, `current` is the percentage and `message` gives the same value in a human-readable form:
```bash
"progress": {
  "current": 4,
  "total": 100,
  "message": "NodeODX reconstruction: 4%"
}
```

OpenScan3 also forwards these updates to the Task drawer, so the same progress is visible in the frontend:
![OpenScan3 task drawer showing NodeODX reconstruction progress](/assets/img/posts/2026-10-22-openscan3-nodeodx-reconstruction-task/2026-10-152.png){: .w-40}

At the same time, NodeODX shows the reconstruction job running on the server. The two views report the same job from either side of the connection:
![NodeODX reconstruction progress](/assets/img/posts/2026-10-22-openscan3-nodeodx-reconstruction-task/2026-10-15-odx.png){: .w-30}

#### Getting the Results

When NodeODX finishes, the Task stops reporting progress and stores the download details in its result. Query the same OpenScan3 Task status endpoint again; the relevant part of the response now looks like this (the surrounding status fields are omitted):

```jsonc
{
  // ... other fields from the Task status response ...
  "result": {
    "uuid": "030e9daa-6feb-4f34-a52f-455e2c3f8d55",
    "download_url": "http://192.168.178.23:3000/task/030e9daa-6feb-4f34-a52f-455e2c3f8d55/download/all.zip"
  },
  // ... remaining fields omitted ...
}
```

The `download_url` points to a ZIP archive from NodeODX. It contains metadata, reports, and the reconstructed model in the `odm_texturing` folder. The next section shows that model in an interactive viewer.

#### Inspecting the Results
Here is the original mesh before post-processing. Use the model inspector and choose geometry Matcap to inspect the geometry without textures:

<iframe  
title="OpenScan Mini – NodeODX reconstruction"  
src="https://sketchfab.com/models/dc139706008646f9b101b4e22f0b9416/embed?ui_inspector=1"  
style="width:100%; aspect-ratio:16/9; border:0;"  
loading="lazy"  
allow="autoplay; fullscreen; xr-spatial-tracking"  
allowfullscreen>  
</iframe>

The result turned out well, especially considering that the scan used autofocus. In my experience, autofocus can make details such as the text on the socket or the sword difficult to capture.

On the Ubuntu server described in the [appendix](#appendix), reconstruction took about 20 minutes.

## Limitations and Outlook

While preparing this post, I tested several Benchy scans with different photo counts and reran some of the same scans. Reconstruction quality and processing time varied between runs, but none of my attempts failed. This setup is a useful starting point, though results may vary with the scan and NodeODX settings.

I think the result is promising because NodeODX is designed for drone captures rather than a rig like the OpenScan Mini and still produces good 3d models even with default settings.



## Appendix: Setup used
{: #appendix }


CPU: Intel Core i9-12900K (16 Cores, 24 Threads)

RAM: 64 GB RAM

GPU: NVIDIA GeForce RTX 3060 with 12 GB VRAM.

Storage: ADATA LEGEND 800 NVMe-SSD

NodeODX run as GPU-Container (webodm/nodeodx:gpu), NodeODX API 2.3.1, ODX Engine 3.8.4.

<!-- markdownlint-capture -->
<!-- markdownlint-disable -->
> **Support Note.** If you also think that creating and connecting open-source software is valuable, you can support OpenScan by [sponsoring us on Patreon](https://www.patreon.com/OpenScan) or by sharing this post. It helps us maintain and develop the [OpenScan3](https://github.com/OpenScan-org/OpenScan3) project.
{: .prompt-tip }
<!-- markdownlint-restore -->
