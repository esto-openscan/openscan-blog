---
title: "360 degree 3D Scan without any post-processing"
date: "2022-03-02T12:30:00+01:00"
author: "Thomas Megel"
legacy: true
categories:
  - "Tutorials"
tags:
  - "openscan2"
  - "openscancloud"
  - "how-to"
  - "surface-prep"
image:
  path: "/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning1.webp"
redirect_from:
  - "/blogs/news/360-degree-3d-scan-without-any-post-processing"
  - "https://openscan.eu/blogs/news/360-degree-3d-scan-without-any-post-processing"
---

This post will guide you through the process of creating a complete 3d model using the OpenScanCloud and the newly introduced "combine" function in the latest beta firmware

First, take a look at some raw scans, which were automatically created by the OpenScanCloud using two image sets each:

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/_zIUczRJFK4?si=V84AmRLLowLvRuLV" title="YouTube video player" width="560"></iframe>

See the 3d models on my [Sketchfab page](https://sketchfab.com/openscan/models).

Normally, created 3d models will not be complete, as at least part of the model is occluded by the object holder. There will either be a hole in the created model, or you will be able to see the object holder, which would have to be removed manually.

Fortunately, there is a relative easy fix for this issue: re-orient the object and take a second (and third) set of photos. But be aware, that there are certain requirements and sources of error.

## Best Practice

### (1) clean and feature-less object holder

It is absolutely crucial, that the object holder is totally clean and contains only large uniform areas without a lot of features. A feature-less object holder will be ignored by the software.

On the right, you can see a failed attempt, where the object holder got partly reconstructed:

![](/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning1-600x600.webp)

The red arrow shows the putty, which got reconstructed from the second set of photos, where the object had a different orientation. You can see in the photo on the left, that the putty and object holder are covered in chalk spray and thus contribute a lot of features. The software tries to reconstruct those (unwanted) areas too, and thus you will get some artifacts.

There is actually a second issue visible too:

### (2) Limit the rotor movement to only cover the upper part of the object

Go to the settings menu and limit the rotor angle to angle_min = +10° and angle_max = +45-90°

The second visible artifact shown is the bright texture at the bottom. In this area, the software managed to ignore the putty when constructing the mesh. But it falsely used the white and pink color to texture the created mesh in that area. This can be easily avoided by limiting the perspectives of the camera as described above. The idea is, that the camera only looks from the top and thus there should not be a perspective contributing bad texture information.

![](/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning2-600x600.webp)

### (3) When using scanning spray or powder:

- **do not cover the object holder/putty**
- **try to coat the whole object in one go**

If possible, try to cover the whole object in one go. Touch the object as little as possible in order to not remove the applied features. Handling small objects can be done with the help of a pair of tweezers.

When you change the object's orientation, there might be areas with only little or no features. It is possible to apply more powder/spray, but remember: less is more (as almost always)

## How to use the firmware

Combining two or more image sets has been introduced in the latest [beta release](https://en.openscan.eu/post/beta-firmware-imx519-16mpx-autofocus-dslr-finally-1) and can be done via the Files&Cloud tab. Select the first image set by clicking into the table. The name of the selected set is visible on the right side.

Click the combine button and ...

![](/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning3-600x600.webp)

... click the second set in the files list. A popup will appear. Please make sure, that you selected the right files. Confirming your choice will combine the two sets into one. Note that the original will be deleted (but all photos are still available through the combined set)

![](/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning4-600x600.webp)

You will have a new set, that can be either downloaded and processed locally or uploaded to the OpenScanCloud.

If you want to know more about a particular topic or practice, please let me know in the comments.

PS: is the title of this blog post technically right? I mean, is it 360° ? or 360° by 180°? or ... ?
