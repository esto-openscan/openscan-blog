---
title: "Bambu Lab A1 Mini - InfiniMod - Endless 3d printing"
date: "2025-02-07T17:20:18+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
  - "Tutorial"
image:
  path: "/assets/img/posts/2025-02-07-bambulab-infinimod/img-8901.jpg"
redirect_from:
  - "/blogs/news/bambulab_infinimod"
  - "https://62f7a3-4.myshopify.com/blogs/news/bambulab_infinimod"
---

<h2 style="text-align: center;">TLDR</h2>
<p>How to modify existing gcode files (.gcode.3mf) for Bambulab A1 Mini for repetitive printing of the same build plate (PLA only!). Make sure to see the shortcomings/results</p>
<h3 style="text-align: center;">Motivation</h3>
<p>We run a small print station with a handful of 3d printers that produce the parts for our open-source 3D Scanner (<a href="https://openscan.eu/products/openscan-mini" rel="noopener" target="_blank">OpenScan Mini</a> &amp; <a href="https://openscan.eu/products/openscan-classic" rel="noopener" target="_blank">Classic</a>).</p>
<p>But then two of our beloved Prusa MK3s decided to retire prematurely on the exact same day (after many years and thousands of printing hours). Unfortunately, this happened at a moment, where we had a bit of backlog and thus needed to ramp up the existing and now quite limited print capacity. Under normal circumstances, we run our printers 20-30% of the time. Which means they collect dust for the majority of their time!&nbsp;</p>
<p><strong>With this mod, we managed to increase the capazity utilization to above 80 percent!</strong></p>
<h3 style="text-align: center;">Disclaimer</h3>
<p style="text-align: center;"><span style="text-decoration: underline;"><strong>Do not change your gcode files unless you are absolutely certain, what you are doing!! This is one of the few operations that can severely damage a 3D printer. </strong></span></p>
<p style="text-align: center;"><span style="text-decoration: underline;"><strong>Make sure to carefully WATCH your printer, whenever you use modified gcode.</strong></span></p>
<p style="text-align: center;"><span style="text-decoration: underline;"><strong>The provided scripts and outlines of this blog post are for educational purposes only and should be seen as a general guideline and NOT a 1:1 instruction.&nbsp;</strong></span></p>
<h3 style="text-align: center;">Setup</h3>
<ul>
<li>Bambulab A1 Mini with or without AMS lite</li>
<li>Textured PEI Sheet</li>
<li>Filament: <strong>PLA only!!</strong>
</li>
<li>tilt printer by ~20deg so that parts can slide down after cooldown (1)</li>
<li>optional printed guide (2 - see download section), so that parts are guided into a box (3)</li>
</ul>
<h3 style="text-align: center;">Understanding the gcode</h3>
<p>In order to modify the gcode, you will need to export and modify a sliced model from Bambu Studio. Using the "<strong>Export plate sliced file</strong>" in the top right corner of the slicer, you can save a ***.gcode.3mf file.</p>
<p><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/bambustudio-export-sliced-file.jpg" style="font-size: 0.875rem; display: block; margin-left: auto; margin-right: auto;"/><span style="font-size: 0.875rem;"></span></p>
<p>&nbsp;</p>
<p>The ***.gcode.3mf is a type of zip file and you can use&nbsp;<strong>7Zip</strong> to open and manually view/edit the file.</p>
<p><span style="font-size: 0.875rem;"><img/><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/7zip-1.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></span></p>
<p>&nbsp;</p>
<p>The interesting file sits inside the Metadata folder and is called <strong>plate_1.gcode.</strong></p>
<p>&nbsp;</p>
<p><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/7zip-2.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p>&nbsp;</p>
<p>You can open and modify the file with your texteditor. Again:&nbsp;<strong>Changes here can severely damage your 3D printer...</strong></p>
<p>Anyway, let's get started.</p>
<p>The overall structure of the file is somewhat like this:</p>
<p><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/gcode-standard.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<h3 style="text-align: center;"></h3>
<h3 style="text-align: center;">Adding custom gcode</h3>
<p>What we want to do is adding a custom gcode to the end of the file, which ejects the printed parts from the build plate (after giving it enough time to cool down).</p>
<p><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/gcode-custom.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p>Unfortunately, Bambulab does not use a standard Marlin/Reprap Gcode implementation and so there is no proper documentation of which codes are implemented and their details.</p>
<ul>
<li>First, you want to make sure that the build plate has enough time to cool down. In my case of roughly 20&deg;C room temperature, this takes roughly an hour. I would conservatively choose this value, as the adhesion between printed parts and build plate greatly increases at the end of the cooldown phase.</li>
</ul>
<pre style="padding-left: 80px;"><span>M140 S0      ; Set bed temperature to 0&deg;C<br/></span><span>M104 S0      ; Set hotend temperature to 0&deg;C<br/></span><span>G4 P3200000  ; pause for 1h</span><br/></pre>
<ul>
<li>After cooling down, I use the M970 command to vibrate the build plate in order to loosen the printed parts. Smaller parts will come loose and should fall of the plate into the box</li>
</ul>
<pre style="padding-left: 80px;"><span>M970.3 Q1 A7 K0 O2      ; vibrate printbed<br/></span><span>M970 Q0 A10 B50 C90 H15 K0 M20 O3   ; vibrate printbed</span><br/></pre>
<ul>
<li>The hotend moves to the top left corner of the build plate + lowering the nozzle to almost touch the plate.</li>
</ul>
<pre style="padding-left: 80px;"><span>G1 X0 Y185  ; Move to X50 Y185<br/></span><span>G1 Z0.2      ; Move Z to 0.2mm</span></pre>
<ul>
<li>Followed by the<strong> most critical and potentially damaging step</strong>: moving the plate to the back and thus pushing parts to the front:</li>
</ul>
<pre style="padding-left: 80px;"><span>G1 X0 Y-1 F1000    ; Move to Y-1 at 1000mm/min speed<br/></span><span>G1 X0 Y185  ; Move back to Y185<br/></span><span>G1 X50      ; Move to X50<br/></span></pre>
<ul>
<li>Repeating a similar motion with different position for X:</li>
</ul>
<pre style="padding-left: 80px;"><span>G1 X50 Y-1 F1000 ; Move to Y-1 at 1000mm/min speed<br/></span><span>G1 X50 Y185 ; Move back to Y185<br/></span><span>G1 X100 ; Move to X100<br/></span><span>G1 X100 Y-1 F1000 ; Move to Y-1 at 1000mm/min speed<br/></span><span>G1 X100 Y185 ; Move back to Y185<br/></span><span>G1 X150 ; Move to X150<br/></span><span>G1 X150 Y-1 F1000 ; Move to Y-1 at 1000mm/min speed</span></pre>
<h3 style="text-align: center;"></h3>
<h3 style="text-align: center;">Addition repetitions --&gt; "endless mode"<br/>
</h3>
<p>Now we have all the building blocks to create a number of repetitions, where the printer cools down and ejects the printed parts before starting the next print.</p>
<p><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/research-and-design-1.png" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p>This can be done manually by modifying the plate_1.gcode file (see above) and saving it in the original ***.gcode.3mf file.&nbsp;</p>
<p>Alternatively, it is possible to use the provided python script (see Download section below), where you only need to specify your input_file (path) and number of repetitions.</p>
<p>This could be easily modified to take a number of different input files and combine those into one long print-queue.</p>
<p>&nbsp;</p>
<h3 style="text-align: center;">Results &amp; Issues</h3>
<p>To make one thing clear, this procedure is prone to errors and has severe limitations. Nevertheless, we see quite some potential to automate small scale print "farms". After a bit of trial and error, we have:</p>
<ul>
<li>successfully printed 10+kg of material</li>
<li>100+ ejections</li>
<li>~800h of (mostly) uninterrupted printing</li>
<li>tested the procedure on various designs (small parts + larger parts)</li>
</ul>
<p><iframe height="315" src="https://www.youtube.com/embed/v4umCPKtwgc?si=VNkkvBui1Nk50gFq" title="YouTube video player" width="560"></iframe></p>
<ul></ul>
<h3 style="text-align: center;">BUT!</h3>
<p>We also had quite a few fails and close-calls:</p>
<p><iframe height="315" src="https://www.youtube.com/embed/wyuOJjMLYCo?si=BxXeEvteQmwcYIOh" title="YouTube video player" width="560"></iframe></p>
<p>The main problem is getting the prints to self-release as much as possible.</p>
<p>The detachability (? --&gt; ability of the print to self-release after cooldown) is greatly influenced by several factors:</p>
<ul>
<li>
<strong>Material - Build plate combination: </strong>PLA + textured PEI works fine. PETG + textured PEI does not work at all</li>
<li>
<strong>Cooldown time:</strong> some objects could be easily pushed of the build plate after 20 minutes, where others needed 60+mins</li>
<li>
<strong>Object geometry:</strong> round objects stick better than parts with sharp corners (--&gt; prone to warping/self-releasing). Smaller objects come of easier than larger ones</li>
<li>
<strong>Room temperature:</strong> there was a very notable difference, where at 16&deg;C room temp the prints released easily, whereas at 22&deg;C the prints stuck too well to the build plate and the print head had to do several attempts of pushing the parts of the plate (video above).<br/>
</li>
</ul>
<div style="text-align: left;"><img alt="" src="/assets/img/posts/2025-02-07-bambulab-infinimod/img-8911-600x600.jpg" style="float: none;"/></div>
<div style="text-align: left;">Depending on how much the printed parts self-release after a given time, the procedure can produce quite some stress on the print head as well as the whole cantilever. If prints stick too well, the print head is pushing against the printed parts until the motor starts skipping. This causes quite some violent vibrations, which will cause damage or at least increased wear over the mid- to long-term.&nbsp;</div>
<div style="text-align: left;"></div>
<div style="text-align: left;"><br/></div>
<h3 style="text-align: center;">Downloads</h3>
<ul>
<li><a href="https://www.dropbox.com/scl/fi/ghgkto3l6aj4utpm3miuv/2025-01-27-BambuA1MiniGuide.stl?rlkey=pi43f25xqd3bgq5w6qofsm7zf&amp;st=582g49kq&amp;dl=0" rel="noopener" target="_blank">.stl file for A1 Mini parts funnel</a></li>
<li><a href="https://www.dropbox.com/scl/fi/kos08yc70kxab5e9gqi7t/gcode_endless_print_modifier.py?rlkey=l6gnbe7a7am23qtjz65dwpjy7&amp;st=w5ytx5gu&amp;dl=0" rel="noopener" target="_blank">Python script for repetitive printing of the same file</a></li>
</ul>
<h3 style="text-align: center;"></h3>
<h3 style="text-align: center;">Future improvements</h3>
<p>There is A LOT to improve with this setup:</p>
<ul>
<li>do more tests with different prints</li>
<li>add a dedicated parts scraper so that the fan shroud and nozzle are protected</li>
<li>try different material/build plate combinations</li>
<li>improve ejection code (e.g. create a script or interface to add/combine multiple print files into one)</li>
<li>adopt this approach to other machines</li>
<li>add some fan for additional cooling to speed up the cooldown phase<br/>
</li>
</ul>
<p>...</p>
