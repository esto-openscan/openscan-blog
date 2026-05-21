---
title: "Optimizing 3D Scans: What is the right shutter speed?"
date: "2025-04-01T15:40:20+02:00"
author: "Thomas Megel"
categories:
  - "Research"
tags:
  - "exposure"
  - "photogrammetry"
  - "shutter-speed"
  - "analysis"
  - "experiment"
image:
  path: "/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/shutterspeed-compare-histo-bc2e5f75-193a-4567-b5dc-c1c70c2bdd57.jpg"
redirect_from:
  - "/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed"
  - "https://62f7a3-4.myshopify.com/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed"
---

**TL;DR: We tested the OpenScan Mini to determine how shutter speed impacts 3D reconstruction quality. We found photogrammetry is surprisingly robust to exposure variations.**

**In our test, there's a wide "sweet spot" between 15ms-150ms where mesh quality remains consistently high despite significant differences in image exposure. Even obviously under/overexposed images produced nearly identical 3D meshes. Focus on avoiding extreme exposure issues rather than perfect exposure.**

## Method

In this experiment, we took 150 photos with the OpenScan Mini with cross-polarisation using autofocus. We varied the shutter speed of the Arducam IMX519 16mpx camera starting from 10ms to 300ms. The results were automatically calculated using the OpenScan Cloud (sorry for temporarily overloading the cloud and thereby increasing the wait-times to ~8h ;)

If anyone is interested in any of the source data, feel free to reach out to [info@openscan.eu](mailto:info@openscan.eu).

## Analysis

All meshes were automatically aligned to a reference mesh from an earlier experiment (500 photos with autofocus) and we derived various mesh-comparison metrics.

### RMS - Error

![](/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/rms-error-vs-shutterspeed.png)

### Standard Deviation

![](/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/std-dev-vs-shutterspeed.png)

### Mean distance

![](/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/mean-distance-vs-shutterspeed.png)

### 16ms vs 140ms shutter speed comparison

The histogram of the 16ms photo set shows clear under-exposure, with the distribution heavily weighted toward the left side of the histogram. This indicates that a significant portion of the image data is concentrated in the shadow regions.

### ![](/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/shutterspeed-16284-1-94-histo.jpg)

Whereas the 130ms photo is clearly overexposed as visible in the histogram. The overexposure pushes the histogram distribution toward the right edge, potentially causing highlight clipping where bright areas lose detail and texture information. In photogrammetry, overexposed areas create "blank" regions where the reconstruction algorithm cannot find distinctive features to match between images.

![](/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/shutterspeed-135326-1-98-histo.jpg)

Surprisingly, both images sets create almost indistinguishable meshes:

![](/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/16vs135-meshcomparison.jpg)

### What is the right shutter speed?

Across various metrics, there is a surprisingly large stable range, where the mesh quality only changes insignificantly! The exact values are not too important here, but the main takeaway is that photogrammetry reconstruction is remarkably robust to exposure variations. Our results indicate a "sweet spot" between 15ms-150ms where reconstruction quality remains consistently high despite significant differences in image exposure.

This suggests that users can prioritize avoiding extreme under or overexposure rather than seeking perfect exposure. A good rule of thumb is to aim for a histogram with good distribution across the middle range while avoiding significant clipping at either end. When fine-tuning your exposure settings, consider applying the ETTR (Expose To The Right) technique, which involves deliberately pushing your histogram data toward the right without clipping highlights.

For this purpose, we are working hard add the histogram functionality to the upcoming rebuild-firmware :)
