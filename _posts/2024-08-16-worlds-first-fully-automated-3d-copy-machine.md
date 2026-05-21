---
title: "Worlds first fully automated 3d copy machine"
date: "2024-08-16T13:30:49+02:00"
author: "Thomas Megel"
description: "It has been a long-standing dream to have a machine into which you can simply place an object, press a button, and obtain an exact copy. Through the power of open-source software and open hardware, we have been able to build the world's first fully automated copy machine for real-world objects . We achieved this by com..."
shopify_summary_html: |-
  <span data-mce-fragment="1">It has been a long-standing dream to have a machine into which you can simply place an object, press a button, and obtain an exact copy. Through the power of open-source software and open hardware, we have been able to build </span><strong data-mce-fragment="1">the world's first fully automated copy machine for real-world objects</strong><span data-mce-fragment="1">. We achieved this by combining our </span><a data-mce-fragment="1" href="https://openscan.eu/pages/openscan-mini" title="OpenScan Mini" data-mce-href="https://openscan.eu/pages/openscan-mini">OpenScan Mini</a><span data-mce-fragment="1"> with a </span><a data-mce-fragment="1" href="https://www.prusa3d.com/category/original-prusa-i3-mk3s/" title="Prusa MK3S+" data-mce-href="https://www.prusa3d.com/category/original-prusa-i3-mk3s/">Prusa MK3S+</a><span data-mce-fragment="1"> 3D printer.</span>
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
  - "Firmware"
image:
  path: "/assets/img/posts/2024-08-16-worlds-first-fully-automated-3d-copy-machine/title.jpg"
redirect_from:
  - "/blogs/news/worlds-first-fully-automated-3d-copy-machine"
  - "https://62f7a3-4.myshopify.com/blogs/news/worlds-first-fully-automated-3d-copy-machine"
---

It has been a long-standing dream to have a machine into which you can simply place an object, press a button, and obtain an exact copy. Through the power of open-source software and open hardware, we have been able to build **the world's first copy machine for real-world objects**. We achieved this by combining our [OpenScan Mini](https://openscan.eu/pages/openscan-mini) with a [Prusa MK3S+](https://www.prusa3d.com/category/original-prusa-i3-mk3s/) 3D printer.

## The Technology Behind

Our 3D copy machine combines two key technologies with a high grade of automation:

1. **3D Scanning**: The [OpenScan Mini](https://openscan.eu/pages/openscan-mini) captures a detailed 3D model of the object.
2. **3D Printing**: The Prusa MK3s+ creates a physical copy based on the scanned model.

## OpenScan Mini

The [OpenScan Mini](https://openscan.eu/pages/openscan-mini) is a compact and efficient 3D scanner. It uses photogrammetry to capture multiple images of an object from various angles. These images are then automatically processed through the [OpenScanCloud](https://openscan.eu/pages/openscancloud) to create a highly accurate 3D model.

## Prusa MK3s+

The Prusa MK3s+ is probably the most known 3D printer. The story of the development of the Prusa i3 printer has been highly encouraging and showed, that open hardware can revolutionize a whole markets.

## The Process

The copying process is largely automated, with minimal manual interaction required. The steps marked with an asterisk (*) require human intervention, while the main processes run fully automatically.

<table>
<tbody>
<tr>
<td>Step</td>
<td>Operation</td>
<td>Duration</td>
</tr>
<tr>
<td>0</td>
<td>Object preparation with scanning spray (*)</td>
<td><strong>1 min</strong></td>
</tr>
<tr>
<td>1</td>
<td>Scanning (first pass) - <a href="https://openscan.eu/pages/openscan-mini">OpenScan Mini</a> with local node-red browser interface</td>
<td> 4 mins</td>
</tr>
<tr>
<td>2</td>
<td>Reorienting the model on the scanner (*)</td>
<td><strong>0.5 min</strong></td>
</tr>
<tr>
<td>3</td>
<td>Scanning (second pass) - <a href="https://openscan.eu/pages/openscan-mini">OpenScan Mini</a> with local node-red browser interface
</td>
<td>4 mins</td>
</tr>
<tr>
<td>4</td>
<td>Processing using the <a href="https://openscan.eu/pages/openscancloud">OpenScanCloud</a> (free cloud processing through our public API)</td>
<td>18 mins</td>
</tr>
<tr>
<td>5</td>
<td>Downloading the file to and creating a printable .gcode file through PrusaSlicer console (local flask server on a windows machine handling the processes)</td>
<td>3 mins</td>
</tr>
<tr>
<td>6</td>
<td>Printing the file through PrusaConnect API (Prusa MK3S+ &amp; Raspberry Pi Zero)</td>
<td>203 mins</td>
</tr>
</tbody>
</table>

## Results

We chose the well-known 3D Benchy as our test object, as it presents challenges for both 3D printing and 3D scanning. Despite using only 188 photos (two passes of 94 each) for the 3D reconstruction, our resulting model captured almost all details of the original object.

![](/assets/img/posts/2024-08-16-worlds-first-fully-automated-3d-copy-machine/orig-result1-1024x1024.jpg)

In the left, you can see the surface preparation, which is absolutely crucial for photogrammetry. The 3D scanner was able to capture the inside of the cabin as well as the container. Some layer inconsistencies and the layer steps are clearly visible.

![](/assets/img/posts/2024-08-16-worlds-first-fully-automated-3d-copy-machine/05-1024x1024.jpg)

The underside shows the text as well as the artifacts of the textured print bed surface.

## Discussion

While this setup produces great results, it primarily serves as a proof of concept. There are several limitations:

- Size constraints based on the scanner and printer capacities
- The quality of the copy is mostly determined by the printing process. FDM comes with several necessities (e.g. support, orientation..).
- The automation software has been stitched together in an afternoon and is not ready for production ;)
- Orientation of the object is currently random, which could be addressed through software improvements.
- Only a few 3d printers offer a full API, limiting the feasibility of other printing processes (e.g. SLA).

The automation is only possible because both machines come with an API, which is unfortunately uncommon in the world of 3D printers and even rarer in the world of 3D scanners. We hope that this project can motivate other manufacturers to open up their machines to users, enabling people to create even more amazing things.
