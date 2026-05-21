---
title: "OpenScan3 Firmware: The Coordinate System"
date: "2026-02-10T18:27:23+01:00"
author: "Elias Stognienko"
description: "This post explains how OpenScan3 represents camera viewpoints using two angles (φ and θ) instead of (x, y, z), and how those angles map directly to the OpenScan Mini and OpenScan Classic."
shopify_summary_html: |-
  <div class="flex flex-col text-sm pb-25">
  <article class="text-token-text-primary w-full focus:outline-none [--shadow-height:45px] has-data-writing-block:pointer-events-none has-data-writing-block:-mt-(--shadow-height) has-data-writing-block:pt-(--shadow-height) [&amp;:has([data-writing-block])&gt;*]:pointer-events-auto scroll-mt-[calc(var(--header-height)+min(200px,max(70px,20svh)))]" dir="auto" data-turn-id="6ea01284-57a7-4030-aff4-a3bc6a939bcf" data-testid="conversation-turn-14" data-scroll-anchor="true" data-turn="assistant" tabindex="-1">
  <div class="text-base my-auto mx-auto pb-10 [--thread-content-margin:--spacing(4)] @w-sm/main:[--thread-content-margin:--spacing(6)] @w-lg/main:[--thread-content-margin:--spacing(16)] px-(--thread-content-margin)">
  <div class="[--thread-content-max-width:40rem] @w-lg/main:[--thread-content-max-width:48rem] mx-auto max-w-(--thread-content-max-width) flex-1 group/turn-messages focus-visible:outline-hidden relative flex w-full min-w-0 flex-col agent-turn" tabindex="-1">
  <div class="flex max-w-full flex-col grow">
  <div data-message-author-role="assistant" data-message-id="eae2faf7-8d20-478b-b417-87846408e71e" dir="auto" class="min-h-8 text-message relative flex w-full flex-col items-end gap-2 text-start break-words whitespace-normal [.text-message+&amp;]:mt-1" data-message-model-slug="gpt-5-2-thinking">
  <div class="flex w-full flex-col gap-1 empty:hidden first:pt-[1px]">
  <div class="markdown prose dark:prose-invert w-full wrap-break-word light markdown-new-styling">
  <p data-start="0" data-end="199" data-is-last-node="" data-is-only-node="">This post explains how OpenScan3 represents camera viewpoints using two angles (φ and θ) instead of (x, y, z), and how those angles map directly to the OpenScan Mini and OpenScan Classic.</p>
  </div>
  </div>
  </div>
  </div>
  <div class="z-0 flex min-h-[46px] justify-start"><br></div>
  <div class="mt-3 w-full empty:hidden">
  <div class="text-center"><br></div>
  </div>
  </div>
  </div>
  </article>
  </div>
categories:
  - "OpenScan Blog"
tags:
  - "Firmware"
image:
  path: "/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-coordinate-system-ad175c30-74f9-4c84-b1a1-184b77f69f7a.jpg"
redirect_from:
  - "/blogs/news/openscan3-coordinate-system-why-%CF%86-%CE%B8-instead-of-x-y-z"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-coordinate-system-why-%CF%86-%CE%B8-instead-of-x-y-z"
---

*This is the third blog post of a series on the OpenScan3 firmware. Read the [previous post here](https://openscan.eu/blogs/news/openscan3-firmware-projects-scans). Comments, questions, or suggestions are always very welcome and a great help for future work on the firmware!*

tl;dr: OpenScan3 uses a spherical coordinate system and expresses positions using two angles. **φ** (phi) is the azimuth (="the turntable") and **θ** (theta) is like the vertical height angle (="the rotor" of an OpenScan Mini.)

## The Theory: Why (φ, θ) instead of (x,y,z)?

Instead of describing camera positions using Cartesian coordinates (x, y, z), OpenScan3 represents viewpoints using two angles: **φ (phi)** and **θ (theta)**. The reason is simple: most scanners don’t “fly freely” in 3D space. They rotate their view around an object and tilt it up and down.

You can think of these viewpoints as lying on a sphere. Figure 1 shows the idea:

![](/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-1.jpg)*Source: [“Kugelkoord-def.svg”](https://de.wikipedia.org/wiki/Datei:Kugelkoord-def.svg) by Ag2gaeh (Wikimedia Commons), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Image version includes edits by Geek3.*

Figure 1 shows the standard spherical coordinate system. The object sits at the center of a sphere **O**, and each camera position corresponds to a viewing **direction** from a point **P** on that sphere. This direction can be sufficiently described by two angles: the azimuth **φ** and the polar angle **θ**. The radius *r* describes the distance from the center, but in OpenScan setups this distance is usually fixed by the hardware.

Note: Different fields swap φ/θ or choose different zero directions. In OpenScan3, we define θ = 0° as top-down (camera pointing straight down to the object) and increase θ towards a horizontal side view.

As you can see in Figure 1, the sphere we described with **φ**, **θ** and *r* sits in a Cartesian coordinate system and it is trivial to transform the (**φ**, **θ**, *r*) coordinates to (x, y, z). This transformation is built in OpenScan3 and used for example for the photo metadata, because photogrammetry reconstruction tools like Colmap use this format.

So why use spherical coordinates at all? The answer is less technical and more human: it is much easier to reason about “a turntable angle” and “a height angle” than juggling three variables with possibly different signs.

Here is a small concrete example of what I mean. Assume the camera moves on a sphere with a fixed distance r = 100 mm. We keep the azimuth constant at **φ = 30°** and only “move down” by increasing **θ**:

- **Point A** (spherical)**:** (φ = 30°, θ = 30°, r = 100)
- **Point B** (spherical)**:** (φ = 30°, θ = 60°, r = 100)

In spherical coordinates this motion is obvious: **only θ changes**.

If we convert both points to Cartesian coordinates (x, y, z), we get:

- **Point A** (Cartesian)**:** (x, y, z) ≈ (43.3, 25.0, 86.6)
- **Point B** (Cartesian)**:** (x, y, z) ≈ (75.0, 43.3, 50.0)

Here, all three values change at the same time: **x and y increase, z decreases**. That is correct, but it does not directly communicate the simple idea of “same turntable angle, just move down”.

### OpenScan Mini

For OpenScan Mini devices, this spherical interpretation is particularly intuitive. The camera is mounted on a curved rotor arm that allows it to tilt up and down, directly sweeping through different values of θ. At the same time, the object itself is rotated on a turntable, which corresponds to changing φ. Together, these two motions allow the system to sample viewpoints distributed over a spherical surface around the object.

To make this more tangible, **Figure 2** breaks the spherical model down into the two views. The left diagram shows the turntable view (top-down), which defines the azimuth angle φ. The right diagram shows the rotor view (side), which defines the polar angle θ.

![](/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-2.jpg)

In the turntable view (Figure 2, left), φ is the rotation around the object in the horizontal plane: it runs from **0° to 360°**, measured **counterclockwise**when viewed from above.

In the**rotor view**(Figure 2, right), θ is the vertical tilt away from the top-down direction: **θ = 0°** is straight down, **θ = 90°** is a horizontal side view, and **θ = 180°** would be bottom-up. The shaded region indicates the mechanically reachable window on a typical OpenScan Mini. In OpenScan3, these limits are configurable in the settings.

A simple way to remember it:

- **θ** moves your view **up and down**
- **φ** moves your view **around the object**

While φ can rotate freely without a fixed reference,θ depends on a known physical starting position, especially on OpenScan Mini devices. (More on this in a follow up blog post)

### OpenScan Classic

The situation for OpenScan Classic is conceptually the same, even though the camera is fixed in space. Instead of moving the camera, OpenScan Classic achieves equivalent viewpoints by rotating and tilting the object. From the perspective of the coordinate system, the relative viewing direction between camera and object still traces points on a sphere. Those directions are again described by **φ** and **θ**.

**![](/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-3.jpg)****Figure 3** shows how **θ** maps to the Classic rotor angle: **θ = 0°** is a top-down view, **θ = 45°** is slightly from above, and **θ = 90°** is a horizontal view.

One big difference to the Mini: the Classic is not limited to a small “reachable window” of θ by the rotor geometry. In theory, you can drive almost any angle.

In practice though, not every angle is useful.
![](/assets/img/posts/2026-02-10-openscan3-coordinate-system-why-instead-of-x-y-z/os3-03-coordinates-4.jpg)
**Figure 4:***“Just because you can, doesn’t mean you should.”*
Left: at extreme angles you mostly capture the stepper motor.
Right: at *very* extreme angles you might experience catastrophic failure (also known as gravity).

## The Reality

In our theoretical model shown in Figure 1, we described the view from *P* as pointing straight to the center of the sphere where the object sits. This is an ideal case. In reality, there are small deviations.

Take the OpenScan Mini: due to material tolerances, the camera is not always perfectly centered to the turntable. For the OpenScan Classic, it’s also obvious: rotating the object around two axes with a fixed camera means the object “jitters” a bit around the theoretical center of the sphere.

These deviations are negligible in practice. But if you made it this far in the blog post, you are most likely interested in these details.
