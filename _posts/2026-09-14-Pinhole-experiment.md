---
title: "Pinhole Experiment: Better DOF"
date: "2026-09-14T00:00:00+02:00"
author: "Thomas Megel"
description: "Adding a pinhole in front of the camera to improve depth of field for close-range photogrammetry, plus a 3D-printable aperture add-on for OpenScan Mini and Classic."
categories:
  - "News"
tags:
  - "hardware"
  - "add-on"
  - "developing"
image:
  path: "/assets/img/posts/2026-09-14-Pinhole-setup-for-better-DOF/grid.jpg"
---



## TL;DR

- the limited DOF creates blurry areas --> focus stacking can solve this, but needs many more images and thus time
- New alternative approach: easy 3d printable add-on for Mini & Classic that greatly enhances DOF
- Bonus: no more stupid M2 nylon screws :)
## Motivation

When doing close-range photography, you will always encounter some amount of bluryness for areas that are farther away from the focal plane. This can be a nice effect for photographs. With photogrammetry you'd want as much of the object in focus as possible. 

In the past, we solved this issue with focus stacking (which can now be run [directly on the Raspberry Pi with the new OpenScan3 firmware](https://github.com/OpenScan-org/OpenScan3/)). This greatly enhances the effective DOF but also needs many more photos (in each position, the scanner takes photos with varying focus).

## The solution: Adding a pinhole in front of the camera

![Comparing Stock vs. Aperture Add-on](/assets/img/posts/2026-09-14-Pinhole-setup-for-better-DOF/grid.jpg)

**LEFT COLUMN: stock setup OpenScan Mini + IMX519**
- Shutterspeed: 80ms
- When zooming in you can see that the front arm and the sword are visibily blurry. This will create noise in the scan result. 
- The sharpness heatmap shows the areas which are well in focus (right leg, head). 

**RIGHT COLUMN: additional pinhole with r=0.8mm**
- Shutterspeed 250ms (!)
- The sharpness heatmap indicates a wider area that is in focus
- the sift feature density (those are the features the photogrammetry pipeline is looking for) improved greatly

## 3D printable pinhole in front of the camera

![3d printable aperture for OpenScan Mini and Classic](/assets/img/posts/2026-09-14-Pinhole-setup-for-better-DOF/Aperture.jpg)

As a nice side-effect of the [macro add-on](https://openscan.eu/products/macro-add-on-for-mini-classic), I have just published a stand-alone printable add-on for the stock OpenScan Mini & Classic. 
This part also gets rid of the tiny Nylon screws that used to hold the camera and replaces those with two M3x8 screws (third image). The printed part can be easily added to the backside of the ring light PCB and works with the stock OpenScan Mini + Classic.

Print settings:
- black Filament (optimally matte)
- 0.08mm for the first three layers (set initial layer height ot 0.08mm and add a layer modifier for 0-0.24mm with the 0.08mm layer height)
- alternatively print the whole part at 0.08mm

There are three different sizes available on printables. You can either print the different size versions or just drill/enlarge the hole with a small drill bit or needle.

[Download the files](https://www.printables.com/model/1842234-dof-add-on-for-openscan-mini-classic-experimental) from Printables.

## A few words on Optics ([find in-depth info (^^) on Wikipedia](https://en.wikipedia.org/wiki/Depth_of_field))

DOF basically comes down to one number: the aperture. The smaller the aperture (=the bigger the f-number), the more of your scene is acceptably sharp, front to back. That's why a stopped-down DSLR lens gives you a larger focus area, while wide open at f/1.4 only a thin slice is sharp.

Problem is, that the cheap camera modules we use don't have an adjustable aperture at all. You get whatever the stock lens ships with. In the case of the Arducam IMX this is a fixed f/1.75. Fast lens, small DOF, great for smartphone-style photos, bad for scanning.

### So why don't we use infinitely small apertures?

**(1) Exposure time `t ∝ 1/r²`** 
A smaller aperture allows less light to pass through and thus exposure times increase quadric. This is not a primary concern for the scanners since the ring light usually provides enough light (though we already lose 75% of intensity to the cross-polarizer).

**(2) Diffraction `blur ∝ 1/r`**
Shrink the aperture far enough and light starts bending around the edges instead of travelling straight through, and it gets worse the smaller you go. The blur spot it creates (the Airy disk) scales with wavelength and f-number: `w ≈ 2.44 · λ · f/d`. So while a smaller aperture buys you sharpness by reducing defocus blur, it simultaneously _adds_ a different kind of blur that has nothing to do with focus at all. This is a hard physical limit , not something better optics can fix. (--> stupid physics ;)

**(3) Depth of Field `blur ∝ r`**
This is the flip side and tthe place for possible gains. Any point away from the focal plane gets smeared into a small blur circle on the sensor, and the size of that circle scales linearly with aperture diameter. Halve the aperture, halve the blur for the same amount of defocus, meaning you can tolerate twice the depth before it looks unacceptably soft. 

## Limitations and Outlook
Using the additional pinhole, there is a clear improvement visible in both the image quality as well as the scan outputs. The decreased number of necessary photos (for focus stacking) marks a great improvement in regards of speed without losing quality.

At this point, I am still looking for the optimal pinhole size. The goal is to balance the trade-offs introduced by diffraction and increased exposure times needed with the benefits of the increased DOF.

Since 3d printing is not the best option for producing such tiny features, I ordered a batch of flex-PCB with varying hole sizes. Anyway, the printable files published on printables are definitely worth a try and it would be a great help if you could give it a try and report your findings.
