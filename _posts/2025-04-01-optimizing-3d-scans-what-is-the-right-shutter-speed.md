---
title: "Optimizing 3D Scans: What is the right shutter speed?"
date: "2025-04-01T15:40:20+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
image:
  path: "/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/shutterspeed-compare-histo-bc2e5f75-193a-4567-b5dc-c1c70c2bdd57.jpg"
redirect_from:
  - "/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed"
  - "https://62f7a3-4.myshopify.com/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed"
---

<p class="whitespace-pre-wrap break-words"><strong>TL;DR:<span>&nbsp;</span>We tested the OpenScan Mini to determine how shutter speed impacts 3D reconstruction quality. We found photogrammetry is surprisingly robust to exposure variations.&nbsp;</strong></p>
<p class="whitespace-pre-wrap break-words"><strong>In our test, there's a wide "sweet spot" between 15ms-150ms where mesh quality remains consistently high despite significant differences in image exposure. Even obviously under/overexposed images produced nearly identical 3D meshes. Focus on avoiding extreme exposure issues rather than perfect exposure.&nbsp;</strong></p>
<h2>Method</h2>
<p>In this experiment, we took 150 photos with the OpenScan Mini with cross-polarisation using autofocus. We varied the shutter speed of the Arducam IMX519 16mpx camera starting from 10ms to 300ms. The results were automatically calculated using the OpenScan Cloud (sorry for temporarily overloading the cloud and thereby increasing the wait-times to ~8h ;)</p>
<p>If anyone is interested in any of the source data, feel free to reach out to<span>&nbsp;</span><a href="mailto:info@openscan.eu">info@openscan.eu</a>.<br/></p>
<h2>Analysis</h2>
<p>All meshes were automatically aligned to a reference mesh from an earlier experiment (500 photos with autofocus) and we derived various mesh-comparison metrics.</p>
<h3 class="text-xl font-bold text-text-200 mt-1 -mb-0.5">RMS - Error</h3>
<p><img alt="" src="/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/rms-error-vs-shutterspeed.png"/></p>
<h3 class="whitespace-pre-wrap break-words">Standard Deviation</h3>
<p><img alt="" src="/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/std-dev-vs-shutterspeed.png"/></p>
<h3 class="whitespace-pre-wrap break-words">Mean distance</h3>
<p><img alt="" src="/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/mean-distance-vs-shutterspeed.png"/></p>
<h3>16ms vs 140ms shutter speed comparison</h3>
<p class="whitespace-pre-wrap break-words">The histogram of the 16ms photo set shows clear under-exposure, with the distribution heavily weighted toward the left side of the histogram. This indicates that a significant portion of the image data is concentrated in the shadow regions.</p>
<h3><img alt="" src="/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/shutterspeed-16284-1-94-histo.jpg"/></h3>
<p class="whitespace-pre-wrap break-words">Whereas the 130ms photo is clearly overexposed as visible in the histogram. The overexposure pushes the histogram distribution toward the right edge, potentially causing highlight clipping where bright areas lose detail and texture information. In photogrammetry, overexposed areas create "blank" regions where the reconstruction algorithm cannot find distinctive features to match between images.&nbsp;</p>
<p><img alt="" src="/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/shutterspeed-135326-1-98-histo.jpg"/></p>
<p>Surprisingly, both images sets create almost indistinguishable meshes:</p>
<p><img alt="" src="/assets/img/posts/2025-04-01-optimizing-3d-scans-what-is-the-right-shutter-speed/16vs135-meshcomparison.jpg"/></p>
<h3>What is the right shutter speed?</h3>
<p class="whitespace-pre-wrap break-words">Across various metrics, there is a surprisingly large stable range, where the mesh quality only changes insignificantly! The exact values are not too important here, but the main takeaway is that photogrammetry reconstruction is remarkably robust to exposure variations. Our results indicate a "sweet spot" between 15ms-150ms where reconstruction quality remains consistently high despite significant differences in image exposure.</p>
<p class="whitespace-pre-wrap break-words">This suggests that users can prioritize avoiding extreme under or overexposure rather than seeking perfect exposure. A good rule of thumb is to aim for a histogram with good distribution across the middle range while avoiding significant clipping at either end. When fine-tuning your exposure settings, consider applying the ETTR (Expose To The Right) technique, which involves deliberately pushing your histogram data toward the right without clipping highlights.</p>
<p class="whitespace-pre-wrap break-words">For this purpose, we are working hard add the histogram functionality to the upcoming rebuild-firmware :)</p>
