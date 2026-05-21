---
title: "[Prototype] OpenScan Multi-Camera Rig"
date: "2026-02-24T19:53:27+01:00"
author: "Thomas Megel"
categories:
  - "Projects"
tags:
  - "project"
  - "multicamera"
  - "prototype"
  - "rig"
  - "raspberrypi"
  - "pcb"
image:
  path: "/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/img-3825.jpg"
redirect_from:
  - "/blogs/news/prototype-openscan-multi-camera-rig"
  - "https://62f7a3-4.myshopify.com/blogs/news/prototype-openscan-multi-camera-rig"
---

It's been a long standing idea to get myself a modular multi-camera system based on the Raspberry Pi + IMX519. I took a couple of smaller attempts getting into this subject and doing some initial testing, but it always failed due to a lack of knowledge and/or time and money.

This time, I got approached whether we could build a small-scale rig for capturing static items from 10-20 perspectives. Over the last few weeks (!), I finally got around to work on this system and created multiple components that all past their initial tests (even to my own surprise)..

## Why a static rig?

Many applications require a static rig, the most prominent one is human-size capture rigs, where you fire 100+ cameras within a fraction of a second (usually within <5ms) to minimize motion between frames. Other applications are object captures, where you'd like to digitize a huge amount of pieces in a short time frame. Another factor is that not all objects are allowed to be moved for capturing (e.g. very delicate parts, plants, fur, museum pieces...)

## The architecture

As with all hardware, I opted for a minimalistic and modular design.

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/architecture.png)

I opted for the Raspberry Pi Zero2 + IMX519 (16mpx) cameras as camera nodes and a Raspberry Pi 4 (2GB) as a master). For now, we will go with simple lighting, but cross polarisation might be an option for later experiments. Other sensors could also be added later.

## The Scan-Master :)

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/master-overview.png)

I created a PCB for the master that allows many further developments and experiments. It got 10 USB-C outputs that allow to transfer power to multiple nodes each (probably up to 10 nodes per output) and furthermore utilize two of the data lines for simple GPIO signal transfer. Furthermore there are a couple of switchable voltage outputs (with selectable voltage). The main input is 10-16V which gets relayed to the nodes and converted locally to 5V. Ah, and this time, I did not forget to place some status LEDs on the PCB ;)

## The Camera-Nodes

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/node-overview.png)

Each node converts the incoming voltage to 5V to power the Raspberry Pi Zero and IMX519 (or other) camera. Again, the PCB has selectable and controllabel voltage outputs to optionally control further peripherals like light or polarizers... The main voltage also gets forwarded to the next USB-C output, so that you can connect multiple nodes together (all sharing one power source and the same GPIO signals from the master).

Initial testing with 12 nodes gives me a total power consumption of under 30W, which is roughly 2W per node and 10W for the master!

The USB-trigger signal (GPIO) seems to be surprisingly stable over long distances - I tested the signal with a couple of 3m USB-C cables and there was no issue with longer lines of a total of 20m.

## Software

The goal is to have a very simplistic user interface with only minimal user intervention. Best case would be just one button to start a scan and some signal (e.g. green-yellow-red) to show the state of the machine.

## Software Stack

The system runs on a Python/FastAPI backend with a React single-page application served directly from the master. Each node runs its own FastAPI service (port 8000), while the master API (port 8080) acts as both the control hub and a proxy to individual nodes. The web dashboard is built without a build step — React and JSX are compiled in-browser via Babel, keeping the deployment pipeline as simple as possible.

All services are managed through systemd, so everything starts automatically on boot. Code updates are pushed to nodes via rsync and take about 5 seconds per node, with per-node camera presets preserved across deploys.

## Nodes / Overview Tab

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/2026-02-23-scanmaster-firmware.png)

The master automatically detects nodes in the network, which can be labeled with their position and or metadata. Updates get pushed through the master, so that this is the only point of entry/maintenance. (though setting up the rig took me a bit, since I had to recycle various leftover parts from older projects, always including some broken cameras, cables, sd cards ... each taking quite some painstaking amount of effort to diagnose and fix...). But besides from that, setup is pretty straightforward: just flash the nodes initial raspbian image, connect all the cables and push the updated firmware from the master.

The nodes will appear in the overview window with a live preview (~1fps). Unfortunately, the Pi Zero 1 W does not support a preview stream due to hardware limitations. I'll still use some leftover Pi Zero 1 W, since capturing works well. But overall, I'd prefer using the newer, more capable Raspberry Pi Zero 2 W. All nodes use Arducam IMX519 16mpx cameras with autofocus, but alternative cameras could be implemented easily, especially, but not limited, to those with the same pi camera form factor.

## Node Control Tab

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/gui-cameraview2.png)

Each camera node can be controled and configured individually. It is possible to create capture presets, e.g. focus-stack with individual focus levels for each camera, that later get triggered globally. The node control tabs preview is a bit faster with ~5fps and also gives a bit of debugging output and stats. Furthermore, it is possible to read/set the individual GPIO pins of the nodes to control the optional peripherals at each node.

## Master Control Tab

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/gui-master-control.png)

The master control tab allows to send global commands to all nodes or a subset of nodes. For instance, it is possible to re-calibrate the auto-white balance or fix a specific value on all or some nodes (e.g. shutterspeed) to get more consistent shots.

For now, Wifi seems to hold up pretty well. I just connected all nodes and the master to my main network, sharing the router with other 30 devices (...). Nevertheless, I suspect that Wifi will become unstable and unreliable at some point with more cameras. But that's a later-me problem for now, since at this point of the project 20 cameras should be more than enough.

At this point, I did not even implement the GPIO trigger mechanism (which would results in great synchronicity). Currently all cameras get triggered by one UDP signal from the master which results in captures within +-5ms across all nodes

## Files Tab

![](/assets/img/posts/2026-02-24-prototype-openscan-multi-camera-rig/gui-files.png)

At this point, each camera saves an uncompressed YUV420 image to its micro sd card, which yields roughly 22MB of data per capture. For now, the data needs to be manually pulled to the master, but this will be automated later in the process. I think that an automated process to transfer files sequentially to a NAS during idle will be the mid-term solution.

## Known issues and open questions

- File transfer needs to be optimized
- How many nodes can be powered through the current PCBs
- At what node count does WiFi become unreliable? Is it 20? 30? 50?
- File transfer will be the bottleneck since one capture creates ~300MB of data
- How consistent are photos across multipel sensors? How does this affect the processing pipeline
- Should the nodes convert the YUV420 files to jpeg locally so that the file size gets decreased (slow @~15-20s per image) or should this be done on the master or a dedicated machine?
- How sturdy is this rig and does an initial camera pose calculation hold true through various captures?

## Next Steps

Since our main effort goes into the existing OpenScan Mini / Classic and especially the new firmware [OpenScan3](https://github.com/OpenScan-org/OpenScan3) progress on this multi-cam rig might slow down a bit. Anyway, the next steps are:

- create presets for each camera
- add illumination to the rig
- add 5 more nodes
- test wifi stability and test various file transfer options
- add and evaluate gpio triggering
- more outputs (LED blink pattern for status..), logging system
- ... a lot of backend work :)
- initial testing of various processing pipelines (not only photogrammetry ;)
