---
title: "Multivid Devlog 1: Automating Multi-Angle Video for OpenScan"
date: "2026-06-02T12:00:12+02:00"
author: "Elias Stognienko"
description: "Can OpenScan document itself? A first devlog about building a Raspberry Pi multicam rig for automated scan videos."
categories:
- "Projects"
tags:
- "openscan"
- "multivid"
- "prototype"
- "multicamera"
- "automation"
- "raspberry pi"
- "ansible"
- "video"
image:
  path: "/assets/img/posts/2026-06-02-multivid-devlog-1/cover-500x500.webp"
---

OpenScan is easy to understand once you see it in action. A scan session can produce a nice object, a satisfying machine movement, interesting camera angles, before/after comparisons, progress shots and plenty of material for tutorials or social media. But recording and arranging all of that by hand is tedious.

For a small open source / open hardware project, that is a real bottleneck. We need attention from potential users, contributors and customers, but we would rather spend our time building hardware, writing software and documenting what we learn than manually producing marketing videos all day.

So the idea behind `multivid` is simple: make OpenScan3 scan sessions easier to film, easier to reproduce and eventually easier to turn into finished video drafts **automatically**.[^xkcd]

That led us to experiment with small camera nodes that can be set up, started and stopped together, so that OpenScan scan sessions can be documented more reliably.

As Thomas went to Berlin to attend the [Open Hardware Summit](https://oshwa.org/events/open-hardware-summit-2026/), I seized the opportunity to repurpose the [prototype of the multicamera rig](https://blog.openscan.eu/posts/prototype-openscan-multi-camera-rig/).

The goal for our first milestone is straightforward: consistently record videos from different viewpoints at the same time with one shell command.

<!-- markdownlint-capture -->
<!-- markdownlint-disable -->
> **Support Note.** But first, before we look at the problem from different angles: if you too want to help us replace the awkward marketing hustle with slightly overengineered open hardware automation, you can support OpenScan by [sponsoring us on Patreon](https://www.patreon.com/OpenScan) or by sharing this post. It helps us keep prototypes public, document the useful bits, and show OpenScan from a few more perspectives.
{: .prompt-tip }
<!-- markdownlint-restore -->

## The Components
We already have camera nodes consisting of Raspberry Pi Zeros with Arducam imx519 cameras on a custom-made PCB.

![Nodes and PCBs of the multicamera rig](/assets/img/posts/2026-06-02-multivid-devlog-1/nodes-1200x900.webp){: width="972" height="589" .w-50 .right}

The current prototype is intentionally simple.

The setup currently includes:

**Raspberry Pi camera nodes**
- a small native Python FastAPI HTTP service on each node
- systemd for running the node service
- Samba shares for accessing the recorded files

**A host PC**
- using Ansible for setting up fresh nodes reproducibly
- a coordinator Python script prepare/start/stop video recordings on all nodes simultaneously

## Why Ansible?
I got into Raspberry Pis with model 1. I can't count how many sd cards I have flashed and `sudo apt update && ...` I have typed. I can't stand this anymore (though with the new raspberry pi imager the process got way nicer to use nowadays!). Besides: If every camera node has to be configured by hand, the setup becomes fragile very quickly. Small differences between nodes can lead to confusing behavior later: different packages, different service files, different camera settings, different folder permissions.

In the beginning, I considered building on top of our [custom OpenScan3 pi-gen images](https://github.com/esto-openscan/OpenScan3-pi-gen), but I figured this would be the wrong approach here.

The idea is that we can start with mostly fresh Raspberry Pi OS Lite images, enable SSH, boot the devices, and then let Ansible turn them into known camera nodes. That includes installing packages and drivers, deploying our Python service, writing configuration files, setting up systemd, creating the recording directory, configuring Samba, and checking whether the node service is reachable.

The best part? When we need to change something in the setup, we do it on the Ansible files (they're called playbooks and roles) on our host and rerun the setup command!

## Sessions, takes and profiles
The important part is not just recording video. We also need the footage to be structured, with machine-readable metadata that makes later automation possible.

If the system knows which scan session is being recorded, which camera angle produced which file, which profile was used, and which take belongs to which attempt, the footage becomes much easier to process later. That is why this prototype is not only about cameras, but also about sessions, takes, profiles and metadata.

The prototype uses three important concepts:

A **session** is one recording context. For example, a specific scan, product demo, tutorial segment or test setup.

A **take** is one recording inside a session. A session can contain multiple takes.

A **profile** describes how a recording should be made. For example, resolution, framerate, bitrate, shutter time, gain, white balance gains or focus behavior.
The resulting folder structure on a camera node looks roughly like this:
```
sessions/
  benchy_scan_session_001/  
    front/                  # <- name of camera node
      prepared_state.json
      take_001/
        recording.h264
        manifest.json
        rpicam-vid.stderr.log
      take_002/
        recording.h264
        manifest.json
        rpicam-vid.stderr.log
```

## Prepare before recording
Before we can record our footage, we have to prepare everything and "warm up" the cameras. For multicam recordings, automatic camera behavior is convenient but problematic. If every camera independently decides exposure, gain, white balance and focus, the different angles can look noticeably different. One camera may be warmer, another colder. One may brighten the scene during the recording. Another may refocus in the middle of the take.
That is especially annoying when cutting between angles.
For this reason, the prototype supports structured recording profiles. A profile can pass explicit camera controls to `rpicam-vid`, such as resolution, framerate, shutter time, gain, focus (=lens) position.

The goal is not to make every setup fully manual from the beginning. Auto modes are still useful for quick tests and calibration. But for final multicam takes, we want the option to lock important parameters. That is exactly what happens in the preparation step.

If the scene, lighting or object distance changes, we can run the prepare step again or request refocusing.

The prepare step happens automatically when needed. Explicit prepare and prepare-reset commands are also available for debugging or deliberate setup changes.

If the same session continues with another take, the prepared state can be reused when the session, profile and relevant camera configuration still match. That is useful because we often want multiple takes from the same setup to look consistent.

The calibration profiles are managed on the host PC for each node individually. This makes it possible to tune each camera separately while keeping the overall recording setup reproducible.

## Aaaand Action!
Now with calibrated and locked controls, we can actually start recording the footage!

From the host PC, the coordinator sends the same start request to all configured camera nodes at roughly the same time. Each node then creates the next take folder, writes its manifest, starts `rpicam-vid`, and records locally to its own storage. When we stop the recording, the coordinator again calls all nodes, and each camera finalizes its manifest with stop time, process result, warnings and the exact command that was used.

This is not frame-perfect synchronization yet. The cameras are started over normal HTTP requests, so a small timing drift between nodes is expected. For this milestone that is acceptable: the goal is not [genlock](https://en.wikipedia.org/wiki/Genlock)-grade multicam capture, but reliably starting all angles together with one command and keeping the resulting files structured enough for later processing.

## What already works
At this stage, the prototype can:
- record multiple takes inside one session
- store files by session, camera and take
- write manifests next to each recording

After manually copying the Samba shares from two camera nodes, `front` and `side`, the combined session folder looks like this:
```
sessions/
  benchy_scan_001/
    front/
      prepared_state.json
      take_001/
        recording.h264
        manifest.json
        rpicam-vid.stderr.log
      take_002/
        recording.h264
        manifest.json
        rpicam-vid.stderr.log
    side/
      prepared_state.json
      take_001/
        recording.h264
        manifest.json
        rpicam-vid.stderr.log   
	  take_002/
        recording.h264
        manifest.json
        rpicam-vid.stderr.log
```

And now we can finally watch the first snippet of our raw footage from inside the multicam rig on our host PC:
![Multivid video side-by-side view](/assets/img/posts/2026-06-02-multivid-devlog-1/2026-06-02-multivid-video-side-by-side.jpg)

As you can see in the two images, the cameras are not perfectly aligned and are even oriented differently. That is fine for this milestone: the basic setup works, and we can record multiple viewpoints together in a structured way.

## What's next?
The next logical layer is automatically harvesting the video files from the nodes and gathering them on our host PC for further editing.

After a session ends, the coordinator could collect all videos and metadata files from the camera nodes and create one central session folder. That folder could include all clips, all manifests and a combined session index.

After that, automatically cutting and light editing will come into focus. Because the system knows the structure of a scan session, it could generate rough cuts automatically, like:
- a 60-second scan timelapse
- a split-screen overview from all camera angles
- a vertical short for social media
- a before/after clip with the final model
- progress overlays based on scan metadata

This is where integrating the `multivid` prototype with an OpenScan3 device becomes especially interesting: a scan session is already a highly structured process. A future pipeline could combine the camera videos with the scan progress and scanner movements to generate first video drafts automatically.

That is the real goal of `multivid`: not replacing good video editing, but removing enough repetitive work that documenting OpenScan becomes part of the scanning workflow instead of a separate marketing chore.

## Reverse Footnote

[^xkcd]: Relevant [xkcd#1319](https://xkcd.com/1319/)
