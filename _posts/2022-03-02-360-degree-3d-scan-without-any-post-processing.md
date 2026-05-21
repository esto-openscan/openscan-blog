---
title: "360 degree 3D Scan without any post-processing"
date: "2022-03-02T12:30:00+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
  - "Firmware"
  - "Tutorial"
image:
  path: "/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning1.webp"
redirect_from:
  - "/blogs/news/360-degree-3d-scan-without-any-post-processing"
  - "https://62f7a3-4.myshopify.com/blogs/news/360-degree-3d-scan-without-any-post-processing"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">This post will guide you through the process of creating a complete 3d model using the OpenScanCloud and the newly introduced "combine" function in the latest beta firmware</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="cd1kv" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">First, take a look at some raw scans, which were automatically created by the OpenScanCloud using two image sets each:</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1"><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/_zIUczRJFK4?si=V84AmRLLowLvRuLV" title="YouTube video player" width="560"></iframe></span></p>
<div data-breakout="normal">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-ahq6"><span class="_1N6tE"><span>See the 3d models on my </span><a class="_37YHL hO7NK" data-hook="WebLink" href="https://sketchfab.com/openscan/models" target="_blank"><span>Sketchfab page</span></a><span>.</span></span></p>
</div>
<div data-hook="rcv-block5" type="paragraph">Normally, created 3d models will not be complete, as at least part of the model is occluded by the object holder. There will either be a hole in the created model, or you will be able to see the object holder, which would have to be removed manually.</div>
<div data-hook="rcv-block5" type="paragraph"></div>
<div data-breakout="normal">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-9478q"><span class="_1N6tE"><span>Fortunately, there is a relative easy fix for this issue: re-orient the object and take a second (and third) set of photos. But be aware, that there are certain requirements and sources of error.</span></span></p>
</div>
<div data-breakout="normal">
<h2 class="Y6Mj6 XtK1R KNByY iPC6I TI-xX" id="viewer-5fefb"><span class="hQoyd"><span>Best Practice</span></span></h2>
</div>
<h3 data-hook="rcv-block11" type="heading">(1) clean and feature-less object holder</h3>
<div data-hook="rcv-block13" type="heading">It is absolutely crucial, that the object holder is totally clean and contains only large uniform areas without a lot of features. A feature-less object holder will be ignored by the software.</div>
<div data-hook="rcv-block15" type="paragraph"></div>
<div data-breakout="normal" style="text-align: center;">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-8tf5p" style="text-align: left;"><span class="_1N6tE"><span>On the right, you can see a failed attempt, where the object holder got partly reconstructed:</span></span></p>
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX"><img src="/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning1-600x600.webp" style="float: none;"/></p>
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" style="text-align: left;">The red arrow shows the putty, which got reconstructed from the second set of photos, where the object had a different orientation. You can see in the photo on the left, that the putty and object holder are covered in chalk spray and thus contribute a lot of features. The software tries to reconstruct those (unwanted) areas too, and thus you will get some artifacts.</p>
<div data-breakout="normal">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-fhvi7" style="text-align: left;"><span class="_1N6tE"><span>There is actually a second issue visible too:</span></span></p>
</div>
<div data-hook="rcv-block22" style="text-align: left;" type="empty-line"></div>
<div data-breakout="normal" style="text-align: left;">
<h3 class="IQ7kr XtK1R KNByY iPC6I TI-xX" id="viewer-eu363"><span class="hQoyd"><span>(2) Limit the rotor movement to only cover the upper part of the object</span></span></h3>
</div>
<p data-hook="rcv-block23" style="text-align: left;" type="heading">Go to the settings menu and limit the rotor angle to angle_min = +10&deg; and angle_max = +45-90&deg;</p>
<p data-hook="rcv-block26" style="text-align: left;" type="empty-line">The second visible artifact shown is the bright texture at the bottom. In this area, the software managed to ignore the putty when constructing the mesh. But it falsely used the white and pink color to texture the created mesh in that area. This can be easily avoided by limiting the perspectives of the camera as described above. The idea is, that the camera only looks from the top and thus there should not be a perspective contributing bad texture information.</p>
<p data-hook="rcv-block26" style="text-align: left;" type="empty-line"><img src="/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning2-600x600.webp" style="float: none;"/></p>
<div data-breakout="normal">
<h3 class="IQ7kr XtK1R KNByY iPC6I TI-xX" id="viewer-8k3ph" style="text-align: left;"><span class="hQoyd"><span>(3) When using scanning spray or powder: </span></span></h3>
</div>
<div data-hook="rcv-block30" style="text-align: left;" type="heading">
<ul>
<li><strong>do not cover the object holder/putty</strong></li>
<li><strong>try to coat the whole object in one go</strong></li>
</ul>
</div>
<div data-hook="rcv-block34" style="text-align: left;" type="empty-line"></div>
<div data-breakout="normal" style="text-align: left;">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-549q9"><span class="_1N6tE"><span>If possible, try to cover the whole object in one go. Touch the object as little as possible in order to not remove the applied features. Handling small objects can be done with the help of a pair of tweezers.</span></span></p>
</div>
<div data-breakout="normal" style="text-align: left;">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-bci3u"><span class="_1N6tE"><span>When you change the object's orientation, there might be areas with only little or no features. It is possible to apply more powder/spray, but remember: less is more (as almost always)</span></span></p>
</div>
<div data-breakout="normal" style="text-align: left;">
<h2 class="Y6Mj6 XtK1R KNByY iPC6I TI-xX" id="viewer-6k96l"><span class="hQoyd"><span>How to use the firmware</span></span></h2>
</div>
<div data-hook="rcv-block39" style="text-align: left;" type="heading">
<span>Combining two or more image sets has been introduced in the latest </span><a class="_37YHL hO7NK" data-hook="WebLink" href="https://en.openscan.eu/post/beta-firmware-imx519-16mpx-autofocus-dslr-finally-1" target="_blank"><span>beta release</span></a><span> and can be done via the </span><span>Files&amp;Cloud</span><span> tab. </span><span>Select the first image set by clicking into the table.</span><span> The name of the selected set is visible on the right side.</span>
</div>
<div data-hook="rcv-block41" style="text-align: left;" type="paragraph"></div>
<div data-breakout="normal" style="text-align: center;">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-1ggok" style="text-align: left;"><span class="_1N6tE"><span>Click the combine button and ...</span></span></p>
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" style="text-align: left;"><span class="_1N6tE"><span><img src="/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning3-600x600.webp" style="float: none;"/></span></span></p>
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" style="text-align: left;"><span class="_1N6tE"><span>... click the second set in the files list. A popup will appear. Please make sure, that you selected the right files. Confirming your choice will combine the two sets into one. Note that the original will be deleted (but all photos are still available through the combined set)</span></span></p>
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" style="text-align: left;"><img src="/assets/img/posts/2022-03-02-360-degree-3d-scan-without-any-post-processing/2022-03-02-360degree-scanning4-600x600.webp" style="float: none;"/></p>
<div data-breakout="normal">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-1jpo2" style="text-align: left;"><span class="_1N6tE"><span>You will have a new set, that can be either downloaded and processed locally or uploaded to the OpenScanCloud.</span></span></p>
</div>
<div data-breakout="normal" style="text-align: left;">
<p class="_9-O5y h4vUg KNByY iPC6I TI-xX" id="viewer-764nd"><span class="_1N6tE"><span>If you want to know more about a particular topic or practice, please let me know in the comments.</span></span></p>
</div>
<div data-hook="rcv-block49" style="text-align: left;" type="paragraph">PS: is the title of this blog post technically right? I mean, is it 360&deg; ? or 360&deg; by 180&deg;? or ... ?</div>
</div>
</div>
