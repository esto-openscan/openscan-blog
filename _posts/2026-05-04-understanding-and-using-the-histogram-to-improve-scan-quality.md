---
title: "Reading the Histogram: Getting Exposure Right for Your 3D Scans"
date: "2026-05-04T11:19:48+02:00"
author: "Thomas Megel"
categories:
  - "Tutorials"
tags:
  - "histogram"
  - "photogrammetry"
  - "shutter-speed"
  - "how-to"
  - "exposure"
  - "openscan3"
image:
  path: "/assets/img/posts/2026-05-04-understanding-and-using-the-histogram-to-improve-scan-quality/histogram-titel-b9cf756f-7dc4-48fc-a592-519892a09f70.png"
redirect_from:
  - "/blogs/news/understanding-and-using-the-histogram-to-improve-scan-quality"
  - "https://openscan.eu/blogs/news/understanding-and-using-the-histogram-to-improve-scan-quality"
---

Choosing the right exposure/shutter speed is important for successful 3D scans with photogrammetry. The histogram is a simple tool that helps you find the right settings for your scan object and environment.

In short: what you are aiming for is an image that is not over- or underexposed, which can be easily seen in the histogram. **Increase the shutter speed until the graph is barely reaching the right side.**

If you want to get a little deeper understanding just follow the rest of this blog post :)

### What is a histogram, really?

A histogram is just a bar chart showing how bright the pixels in your image are. The horizontal axis runs from pure black on the left to pure white on the right, and the height of the curve at any point tells you how many pixels in your image have that particuliar brightness.

In the new [OpenScan3 firmware](https://openscan.eu/blogs/news/openscan3-beta-whats-new) we show three curves on top of each other - one for the red, green, and blue channel. If one channel is clipping (slammed against the right edge) while the others aren't, you're losing color detail even though the image might look fine to your eye.

### Underexposed, well-exposed, overexposed

Here is the same scan area at three different shutter speeds:

![](/assets/img/posts/2026-05-04-understanding-and-using-the-histogram-to-improve-scan-quality/histogram-comparison2.png)

**Left - underexposed.** The histogram is squashed to the left. Everything looks muddy and dark, the texture detail is buried in noise, and there's nothing on the right side of the graph at all.

**Middle - well exposed.** The curves spread nicely across most of the available range and just barely touch the right side without piling up against it. Shadows have detail, highlights have detail, and the texture of the miniature is clearly visible. This is what you want.

**Right - overexposed.** The histogram is shoved against the right edge - this is called *clipping*. Once a group of pixels is pure white, you lose valuable features that are crucial for photogrammetry. No amount of post-processing can recover what was never recorded. Bright surfaces like the highlights on this miniature lose all texture detail, and again, your photogrammetry pipeline struggles to match features.

### Real world example - it is always a bit messier than the theory ;)

![](/assets/img/posts/2026-05-04-understanding-and-using-the-histogram-to-improve-scan-quality/histogram-comparison.png)

Comparing the full image to the section shown earlier, you can see, that the histogram looks a lot more noisy and contains some peaks. Don't worry about those peaks and noise, the take-away from above is still valid --> set the exposure so that the histogram is barely touching the right side as shown in the middle image.

### Why "barely touching the right side" is the sweet spot

You might wonder why we don't aim for a perfectly centered histogram. Two reasons:

The first is signal-to-noise ratio. Camera sensors are noisier in the dark parts of the image than in the bright parts. By pushing your exposure as far right as you can without clipping, you maximize the useful signal in every pixel. This is sometimes called "expose to the right" (ETTR) and it's a well-established technique in landscape and product photography too.

The second is that photogrammetry feature matching loves contrast and detail across the whole tonal range. A bright, well-exposed image with rich shadow detail simply gives the algorithms more to work with than a dim one.

### Using the histogram in OpenScan

In the OpenScan3 firmware the live histogram sits right below your camera preview. The workflow is simple:

1. Place your object on the scanner with your usual lighting setup.
2. Open the scan tab and look at the histogram.
3. Adjust shutter speed until the curves stretch across most of the range and *just* approach the right edge without piling up against it.
4. Don't worry too much about finding the perfect shutter speed. We did some experiments in the past and found that the acceptable shutter speed range is surprisingly high ([see this blog post](https://openscan.eu/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed)) **when the objects surface is properly prepared**.
5. optional: move the turntable + rotor and check the histogram for a different perspective of the camera. Aim for a shutter speed that avoids overexposure in all those positions (generally speaking, lower shutter speed).

That's it. Exposure matters, but it is only one factor for a good scan. Proper surface preparation of your object remains the single most important factor for a great scan and is usually the most common point of failure!
