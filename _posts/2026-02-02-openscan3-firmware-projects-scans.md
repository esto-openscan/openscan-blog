---
title: "OpenScan3 Firmware: Projects & Scans"
date: "2026-02-02T12:11:18+01:00"
author: "Elias Stognienko"
description: "This post explains how OpenScan3 separates Projects and Scans to support multi-pass scanning, flexible capture strategies, and automation-friendly workflows."
shopify_summary_html: |-
  <p data-end="584" data-start="427">This post explains how OpenScan3 separates Projects and Scans to support multi-pass scanning, flexible capture strategies, and automation-friendly workflows.</p>
categories:
  - "Firmware"
tags:
  - "openscan3"
image:
  path: "/assets/img/posts/2026-02-02-openscan3-firmware-projects-scans/os3-projects-and-scans-title-6a2efd02-ab87-4003-9c27-fb19f96c09db.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-projects-scans"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-firmware-projects-scans"
---

*This is the second blogpost of a series on the OpenScan3 firmware. Read the*[*previous post here*](https://openscan.eu/blogs/news/preview-of-the-openscan3-firmware-a-fresh-start-with-modern-architecture)*. Comments, questions, or suggestions are always welcome and a great help for future work on the firmware!*

# OpenScan3: Projects and Scans

*tl;dr:* In OpenScan3, we distinguish between *Projects* and *Scans*. A *Project* represents the object you want to digitize.
A *Scan* represents one concrete scanning strategy applied to that object, including its own settings and camera calibration.

## The Problem

3D scanning never works with a single pass if you want to reconstruct an entire object.

Even with turntables, multi-axis rigs, or rotating camera arms, parts of an object inevitably remain occluded. A classic example is the underside of an object resting on the turntable. To capture it properly, you have to flip the object and scan it again.

But occlusion is not the only reason for multiple scans. Different areas of an object often benefit from different scanning strategies. Some regions have many fine details or holes and require many images from slightly varied angles. Other parts are comparatively simple and can be captured with fewer images.

**![Front and back views of a small 3D-printed figurine used as an OpenScan benchmark, showing fine surface details and geometry.](/assets/img/posts/2026-02-02-openscan3-firmware-projects-scans/os3-projects-and-scans-benchy.png)**

Take the OpenScan Benchy[1] as an example: From the front, the miniature contains a lot of fine details: facial features, a sharp sword, and a pointy helmet. Capturing these areas benefits from many images taken at small angular steps. The back is rather simple in comparison. Fewer images are usually sufficient here, without negatively affecting reconstruction quality.

If you were capturing images manually, you would naturally adapt your approach to be as effective as possible. You would spend more time and take more photos where it matters, and less where it does not. Not only would the picture-taking be much faster, also the reconstruction time will decrease significantly.

The same idea applies to semi-automated systems like OpenScan. When you then want to use advanced techniques like focus or exposure stacking (or bracketing) it becomes clear that in practice, scanning a single object usually means:

- different camera settings or calibration
- adapted photo density
- multiple capture passes with the flipped object

So, scanning an object usually means having more than one scan routine ideally using different scan settings and camera calibrations.

## The Solution: Projects and Scans

OpenScan3 embraces this reality by introducing a simple but flexible concept.

Think of a **Project** as everything related to one physical object.

Within that *Project*, you create one or more **Scans**. Each *Scan* represents a specific strategy for capturing part of that object. A *Scan* can e.g. differ in:

- number of images
- angles or movement patterns
- focus, exposure and/or other camera calibration

### A Concrete Example: The OpenScan Benchy

Here you can see how I scanned the OpenScan Benchy miniature on an OpenScan Mini using the alpha firmware of OpenScan3:

![OpenScan3 web interface showing a project with multiple completed scans, including scan settings, image counts, and download options.](/assets/img/posts/2026-02-02-openscan3-firmware-projects-scans/os3-projects-and-scans-screenshot.jpg)

In *Scan* #1, I did a “general” pass and captured the Benchy from all possible angles using the auto focus mode to ensure sharpness across the pictures.

To catch the finer details, I made a second pass, where I used focus stacking. The scanner took 3 photos with different focus settings from 30 positions totaling in 90 pictures for *Scan* #2. But focus stacking wasn't the only thing I did differently from the first *Scan*: I also restricted the angles of the scanning path and thus ensured, that most of the photos were in the areas with fine details and not e.g. from very high or low angles.

For the final *Scan* #3, I flipped the figurine on the turntable to get some pictures of the underside using only 20 pictures.

## A Short Technical Detour

This section deep dives in the current implementation and is suited for those interested, what's happening behind the curtains and can be safely skipped ;)

*Projects* in OpenScan3 are meant to be portable and user-owned: a *Project* is a self-contained bundle you can download, backup, share or feed into your own tooling. We decided to stick to plain files and small JSON manifests so projects remain inspectable without special software: a file browser and a text editor are enough.

A *Scan* is simply one capture run inside a *Project* living in its own folder. That’s helpful when you run multi-pass workflows (general pass, detail pass, flipped pass) or when you want to trigger different downstream steps depending on the type of *Scan*. In practice, this means you don’t just get “a pile of images”, you get images that are explicitly grouped and described in a way that other tools can act on.

Each photo within a *Scan* folder is stored as a normal image file and comes with a small “sidecar” metadata JSON next to it. That metadata is meant to be useful outside of OpenScan as well: you can filter or sort pictures, debug lighting or focus issues, map images back to capture positions, or generate your own reports without having to reverse-engineer anything. The goal of this structure isn’t to be fancy, it’s to stay approachable and scriptable, so you can use OpenScan projects as building blocks in your own workflow!

### What's happening inside the firmware?

Inside the firmware, *Projects* are handled by a dedicated project service controller that acts as the single interface for loading, updating, and persisting *Project* data.

Other parts of the system interact with projects only through this interface. A scanning routine, for example, doesn’t need to know how files are laid out on disk or how metadata is stored. It simply reports captures (images plus metadata) to the project service.

Both *Projects* and *Scans* have their own data model and in case of *Scans* an additional settings model. These models closely mirror what you see when you download a *Project*, which keeps the system consistent and makes the on-disk format easy to understand.

Overall, this keeps responsibilities clearly separated and reduces coupling between subsystems, which is important OpenScan3 continues to grow with new features.

## What this structure makes possible

This structure enables a number of useful extensions:

- scan-specific pre- and post-processing
- reusable *Scan* templates for recurring workflows
- cleaner automation and scripting
- easier experimentation with new hardware or capture strategies

While this seems a bit complex right now, we work hard on automate the settings so that especially new users are not overwhelmed and get good results.

## Summary

In OpenScan3, *Projects* are object-centric and approachable.
*Scans* encapsulate strategies, settings and technical details.

This gives newcomers a clear mental model and a straightforward workflow, while offering experienced users and developers well-defined extension points for automation, customization and future features.

*If you have thoughts, questions, suggestions, or want to contribute we would love hearing from you. You can reach out via*[*e-mail*](mailto:esto@openscan.eu)*, join the*[*Discord*](https://discord.gg/eBdqtdkXyF)*or create issues on*[*GitHub/OpenScan3*]([https://github.com/OpenScan-org/OpenScan3](https://github.com/OpenScan-org/OpenScan3))*.*

---

[1] OpenScan Benchy is a creation by [Valander](https://cults3d.com/en/users/Valandar/3d-models) and used as a 3d scanner benchmark on [GitHub](https://github.com/OpenScanEu/OpenScanBenchy)
