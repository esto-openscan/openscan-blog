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

<p class="whitespace-pre-wrap break-words">It has been a long-standing dream to have a machine into which you can simply place an object, press a button, and obtain an exact copy. Through the power of open-source software and open hardware, we have been able to build <strong>the world's first copy machine for real-world objects</strong>. We achieved this by combining our <a data-mce-href="https://openscan.eu/pages/openscan-mini" href="https://openscan.eu/pages/openscan-mini" title="OpenScan Mini">OpenScan Mini</a> with a <a data-mce-href="https://www.prusa3d.com/category/original-prusa-i3-mk3s/" href="https://www.prusa3d.com/category/original-prusa-i3-mk3s/" title="Prusa MK3S+">Prusa MK3S+</a> 3D printer.</p>
<h2 class="whitespace-pre-wrap break-words">The Technology Behind</h2>
<p class="whitespace-pre-wrap break-words">Our 3D copy machine combines two key technologies with a high grade of automation:</p>
<ol class="-mt-1 list-decimal space-y-2 pl-8" depth="0">
<li class="whitespace-normal break-words" index="0">
<strong>3D Scanning</strong>: The <a href="https://openscan.eu/pages/openscan-mini" title="OpenScan Mini">OpenScan Mini</a> captures a detailed 3D model of the object.</li>
<li class="whitespace-normal break-words" index="1">
<strong>3D Printing</strong>: The Prusa MK3s+ creates a physical copy based on the scanned model.</li>
</ol>
<div data-mce-style="text-align: center;" style="text-align: center;"></div>
<h2>OpenScan Mini</h2>
<p class="whitespace-pre-wrap break-words">The <a href="https://openscan.eu/pages/openscan-mini" title="OpenScan Mini">OpenScan Mini</a> is a compact and efficient 3D scanner. It uses photogrammetry to capture multiple images of an object from various angles. These images are then automatically processed through the <a href="https://openscan.eu/pages/openscancloud">OpenScanCloud</a> to create a highly accurate 3D model.</p>
<h2 class="font-600 text-lg font-bold" level="3">Prusa MK3s+</h2>
<p class="whitespace-pre-wrap break-words">The Prusa MK3s+ is&nbsp;probably the most known 3D printer. The story of the development of the Prusa i3 printer has been highly encouraging and showed, that open hardware can revolutionize a whole markets.&nbsp;</p>
<h2>The Process</h2>
<p>The copying process is largely automated, with minimal manual interaction required. The steps marked with an asterisk (*) require human intervention, while the main processes run fully automatically.</p>
<table width="100%">
<tbody>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">Step</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Operation</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;">Duration</td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">0</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Object preparation with scanning spray (*)</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;"><strong>1 min</strong></td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">1</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Scanning (first pass) - <a href="https://openscan.eu/pages/openscan-mini" title="OpenScan Mini">OpenScan Mini</a> with local node-red browser interface</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;">&nbsp;4 mins</td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">2</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Reorienting the model on the scanner (*)</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;"><strong>0.5 min</strong></td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">3</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Scanning (second pass) -&nbsp;<span data-mce-fragment="1"><a href="https://openscan.eu/pages/openscan-mini" title="OpenScan Mini">OpenScan Mini</a> with local node-red browser interface</span>
</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;">4 mins</td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">4</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Processing using the <a href="https://openscan.eu/pages/openscancloud" title="OpenScanCloud">OpenScanCloud</a> (free cloud processing through our public API)</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;">18 mins</td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">5</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Downloading the file to and creating a printable .gcode file through PrusaSlicer console (local flask server on a windows machine handling the processes)</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;">3 mins</td>
</tr>
<tr>
<td data-mce-style="width: 30.8594px;" style="width: 30.8594px;">6</td>
<td data-mce-style="width: 435.438px;" style="width: 435.438px;">Printing the file through PrusaConnect API (Prusa MK3S+ &amp; Raspberry Pi Zero)</td>
<td data-mce-style="width: 56.7031px;" style="width: 56.7031px;">203 mins</td>
</tr>
</tbody>
</table>
<p class="whitespace-pre-wrap break-words">&nbsp;</p>
<h2 class="whitespace-pre-wrap break-words">Results</h2>
<p class="whitespace-pre-wrap break-words">We chose the well-known 3D Benchy as our test object, as it presents challenges for both 3D printing and 3D scanning. Despite using only 188 photos (two passes of 94 each) for the 3D reconstruction, our resulting model captured almost all details of the original object.</p>
<p class="whitespace-pre-wrap break-words">&nbsp;</p>
<div data-mce-style="text-align: left;" style="text-align: left;"><img data-mce-style="float: none;" src="/assets/img/posts/2024-08-16-worlds-first-fully-automated-3d-copy-machine/orig-result1-1024x1024.jpg" style="float: none;"/></div>
<p class="whitespace-pre-wrap break-words">In the left, you can see the surface preparation, which is absolutely crucial for photogrammetry. The 3D scanner was able to capture the inside of the cabin as well as the container. Some layer inconsistencies and the layer steps are clearly visible.</p>
<div data-mce-style="text-align: center;" style="text-align: center;"><img data-mce-style="float: none;" src="/assets/img/posts/2024-08-16-worlds-first-fully-automated-3d-copy-machine/05-1024x1024.jpg" style="float: none;"/></div>
<p class="whitespace-pre-wrap break-words">The underside shows the text as well as the artifacts of the textured print bed surface.</p>
<h2 class="whitespace-pre-wrap break-words">Discussion</h2>
<p class="whitespace-pre-wrap break-words">While this setup produces great results, it primarily serves as a proof of concept. There are several limitations:</p>
<ul class="-mt-1 list-disc space-y-2 pl-8" depth="0">
<li class="whitespace-normal break-words" index="0">Size constraints based on the scanner and printer capacities</li>
<li class="whitespace-normal break-words" index="0">The quality of the copy is mostly determined by the printing process. FDM comes with several necessities (e.g. support, orientation..).</li>
<li class="whitespace-normal break-words" index="0">The automation software has been stitched together in an afternoon and is not ready for production ;)</li>
<li class="whitespace-normal break-words" index="1">Orientation of the object is currently random, which could be addressed through software improvements.</li>
<li class="whitespace-normal break-words" index="2">Only a few 3d printers offer a full API, limiting the feasibility of other printing processes (e.g. SLA).</li>
</ul>
<p class="whitespace-pre-wrap break-words">The automation is only possible because both machines come with an API, which is unfortunately uncommon in the world of 3D printers and even rarer in the world of 3D scanners. We hope that this project can motivate other manufacturers to open up their machines to users, enabling people to create even more amazing things.</p>
