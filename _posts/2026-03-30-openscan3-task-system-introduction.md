---
title: "OpenScan3: Task System Introduction"
date: "2026-03-30T17:29:47+02:00"
author: "Elias Stognienko"
description: "This post introduces the OpenScan3 task system and explains how it improves long-running workflows, interface feedback, and extensibility."
shopify_summary_html: |-
  <p data-start="212" data-end="365">This post introduces the OpenScan3 task system and explains how it improves long-running workflows, interface feedback, and extensibility.</p>
categories:
  - "Firmware"
tags:
  - "openscan3"
  - "firmware"
  - "architecture"
  - "task-system"
image:
  path: "/assets/img/posts/2026-03-30-openscan3-task-system-introduction/os3-task-system.jpg"
redirect_from:
  - "/blogs/news/openscan3-task-system-introduction"
  - "https://openscan.eu/blogs/news/openscan3-task-system-introduction"
---

*This is a blog post in a series on the OpenScan3 firmware. Read the [previous post here](https://openscan.eu/blogs/news/openscan3-firmware-smooth-moves). Comments, questions, or suggestions are always very welcome and a great help for future work on the firmware!*

**tl;dr:** OpenScan3 includes a task system for long-running routines such as scanning, calibration, file operations, and future extensions. It keeps the device responsive, makes background work visible, and gives us a clean foundation for custom workflows.

Maybe you have already noticed the new task drawer in recent updates and wondered what it is for. This post gives a high-level overview of the idea behind the OpenScan3 task system, why we built it, and what it means for users.

### Why we needed a task system

At first glance, a scanner seems simple: move a motor, take a picture, repeat.

In practice, a photogrammetry scanner runs longer workflows involving motor movement, camera control, focus stacking, waiting for hardware, saving images, updating progress, handling errors, handling user input, and ... you got it. Somehow all this has to be coordinated.

That is why we built a task system.

### What this means for users

From a user perspective, the task system is mainly about clarity and reliability.

Long-running operations can now be represented as actual tasks with status, progress, and their own place in the interface. Instead of “something is happening somewhere,” the device can communicate what it is currently doing and what state that work is in.

### Why it matters for customization

There is a second reason this system is important to us: extensibility.

One of the goals of OpenScan3 is not just to provide a firmware that works out of the box, but to provide a platform that users can adapt to their own workflows and hardware setups.

That is where the task system becomes especially useful. Tasks are not only an internal implementation detail. They are also a practical structure for modifications and experiments.

Do you want to change how the scan task handles focus stacking? Copy it and adapt it.

Do you want to run image analysis or custom processing on-device? Build a task for it.

Do you want to prototype a new workflow without tangling it into the core scan logic? A task is a clean place to do that.

In that sense, the task system is part of what makes OpenScan3 hackable. It creates boundaries between workflows and makes it easier to extend the firmware in a controlled way. It is your hardware and your workflow so you should be able to modify it as needed.

### In the next posts

This post is only a high-level introduction. In the next parts of the series, we will look more closely at how tasks behave in practice, and how you can build or adapt tasks for your own use cases.

If you have ideas for custom workflows or things you would like to automate on your scanner, this is exactly the kind of foundation that should make that possible.
