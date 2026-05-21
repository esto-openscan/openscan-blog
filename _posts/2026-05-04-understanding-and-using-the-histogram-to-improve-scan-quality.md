---
title: "Reading the Histogram: Getting Exposure Right for Your 3D Scans"
date: "2026-05-04T11:19:48+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags: []
image:
  path: "/assets/img/posts/2026-05-04-understanding-and-using-the-histogram-to-improve-scan-quality/histogram-titel-b9cf756f-7dc4-48fc-a592-519892a09f70.png"
redirect_from:
  - "/blogs/news/understanding-and-using-the-histogram-to-improve-scan-quality"
  - "https://62f7a3-4.myshopify.com/blogs/news/understanding-and-using-the-histogram-to-improve-scan-quality"
---

<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">Choosing the right exposure/shutter speed is important for successful 3D scans with photogrammetry. The histogram is a simple tool that helps you find the right settings for your scan object and environment.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">In short: what you are aiming for is an image that is not over- or underexposed, which can be easily seen in the histogram. <strong>Increase the shutter speed until the graph is barely reaching the right side.</strong></p>
<p>If you want to get a little deeper understanding just follow the rest of this blog post :)</p>
<p>&nbsp;</p>
<h3 class="text-text-100 mt-3 -mb-1 text-[1.125rem] font-bold">What is a histogram, really?</h3>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">A histogram is just a bar chart showing how bright the pixels in your image are. The horizontal axis runs from pure black on the left to pure white on the right, and the height of the curve at any point tells you how many pixels in your image have that particuliar brightness.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">In the new <a href="https://openscan.eu/blogs/news/openscan3-beta-whats-new" target="_blank">OpenScan3 firmware</a> we show three curves on top of each other - one for the red, green, and blue channel. If one channel is clipping (slammed against the right edge) while the others aren't, you're losing color detail even&nbsp;though the image might look fine to your eye.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">&nbsp;</p>
<h3 class="text-text-100 mt-3 -mb-1 text-[1.125rem] font-bold">Underexposed, well-exposed, overexposed</h3>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">Here is the same scan area at three different shutter speeds:</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]"><img alt="" src="/assets/img/posts/2026-05-04-understanding-and-using-the-histogram-to-improve-scan-quality/histogram-comparison2.png"/></p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]"><strong>Left - underexposed.</strong> The histogram is squashed to the left. Everything looks muddy and dark, the texture detail is buried in noise, and there's nothing on the right side of the graph at all.&nbsp;</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]"><strong>Middle - well exposed.</strong> The curves spread nicely across most of the available range and just barely touch the right side without piling up against it. Shadows have detail, highlights have detail, and the texture of the miniature is clearly visible. This is what you want.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]"><strong>Right - overexposed.</strong> The histogram is shoved against the right edge - this is called <em>clipping</em>. Once a group of pixels is pure white, you lose valuable features that are crucial for photogrammetry. No amount of post-processing can recover what was never recorded. Bright surfaces like the highlights on this miniature lose all texture detail, and again, your photogrammetry pipeline struggles to match features.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">&nbsp;</p>
<h3 class="font-claude-response-body break-words whitespace-normal leading-[1.7]">Real world example - it is always a bit messier than the theory ;)</h3>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]"><img alt="" src="/assets/img/posts/2026-05-04-understanding-and-using-the-histogram-to-improve-scan-quality/histogram-comparison.png"/></p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">Comparing the full image to the section shown earlier, you can see, that the histogram looks a lot more noisy and contains some peaks. Don't worry about those peaks and noise, the take-away from above is still valid --&gt; set the exposure so that the histogram is barely touching the right side as shown in the middle image.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">&nbsp;</p>
<h3 class="text-text-100 mt-3 -mb-1 text-[1.125rem] font-bold">Why "barely touching the right side" is the sweet spot</h3>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">You might wonder why we don't aim for a perfectly centered histogram. Two reasons:</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">The first is signal-to-noise ratio. Camera sensors are noisier in the dark parts of the image than in the bright parts. By pushing your exposure as far right as you can without clipping, you maximize the useful signal in every pixel. This is sometimes called "expose to the right" (ETTR) and it's a well-established technique in landscape and product photography too.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">The second is that photogrammetry feature matching loves contrast and detail across the whole tonal range. A bright, well-exposed image with rich shadow detail simply gives the algorithms more to work with than a dim one.</p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]"><br/></p>
<h3 class="text-text-100 mt-3 -mb-1 text-[1.125rem] font-bold">Using the histogram in OpenScan</h3>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">In the OpenScan3 firmware the live histogram sits right below your camera preview. The workflow is simple:</p>
<ol class="[li_&amp;]:mb-0 [li_&amp;]:mt-1 [li_&amp;]:gap-1 [&amp;:not(:last-child)_ul]:pb-1 [&amp;:not(:last-child)_ol]:pb-1 list-decimal flex flex-col gap-1 pl-8 mb-3">
<li class="whitespace-normal break-words pl-2">Place your object on the scanner with your usual lighting setup.</li>
<li class="whitespace-normal break-words pl-2">Open the scan tab and look at the histogram.</li>
<li class="whitespace-normal break-words pl-2">Adjust shutter speed until the curves stretch across most of the range and&nbsp;<em>just</em> approach the right edge without piling up against it.</li>
<li class="whitespace-normal break-words pl-2">Don't worry too much about finding the perfect shutter speed. We did some experiments in the past and found that the acceptable shutter speed range is surprisingly high (<a href="https://openscan.eu/blogs/news/optimizing-3d-scans-what-is-the-right-shutter-speed" rel="noopener" target="_blank">see this blog post</a>) <strong>when the objects surface is properly prepared</strong>.</li>
<li class="whitespace-normal break-words pl-2">optional: move the turntable + rotor and check the histogram for a different perspective of the camera. Aim for a shutter speed that avoids overexposure in all those positions (generally speaking, lower shutter speed).</li>
</ol>
<p><br/>That's it. Exposure matters, but it is only one factor for a good scan. Proper surface preparation of your object remains the single most important factor for a great scan and is usually the most common point of failure!<br/></p>
<p class="font-claude-response-body break-words whitespace-normal leading-[1.7]">&nbsp;</p>
