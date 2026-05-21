---
title: "Optimizing 3D Scans: How Many Photos Do You Really Need?"
date: "2025-03-26T19:14:43+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
image:
  path: "/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/photocount-photogrammetry-5d3b6b89-b153-4885-83fa-1019c633f20a.gif"
redirect_from:
  - "/blogs/news/optimizing-3d-scans-how-many-photos-do-you-really-need"
  - "https://62f7a3-4.myshopify.com/blogs/news/optimizing-3d-scans-how-many-photos-do-you-really-need"
---

<p class="" data-end="436" data-start="97"><strong>TL;DR: Is more always better? When it comes to photogrammetry, the clear answer is no! We performed tests, which align with our experience, showing that there is an optimal number of images for turntable photogrammetry&mdash;around 200 photos. Increasing beyond 300 photos does not improve mesh quality and only increases processing times.</strong></p>
<p class="" data-end="574" data-start="438"><strong>As a little side effect, we also found a bug in our current positioning algorithm (above ~500 photos), which will be fixed in the next firmware update! :)</strong></p>
<h2>Method</h2>
<p>In this experiment, we methodically evaluated the influence of the number of images onto the results from the photogrammetry pipeline. Therefore, we use the 45mm OpenScan Benchy model. The OpenScan Mini created various image sets ranging from 10 photos up to 1000 photos. The results were automatically calculated using the OpenScan Cloud. We created a total of 367 image sets and resulting meshes. If anyone is interested in any of the source data, feel free to reach out to <a href="mailto:info@openscan.eu">info@openscan.eu</a>.<br/></p>
<p>The goal is to evaluate, whether there is some optimal number of images or whether the mesh quality increases steadily (at the cost of increased processing time).</p>
<h2>Pre-Analysis</h2>
<p><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/duration-seconds-vs-photocount.png"/>As in our last experiment, the outliers can be easily explained by the OpenScan Cloud struggling occasionally, which will be fixed at some point. Ignoring those outliers, there is a clear linear trend for low photocount values (under 500). Surprisingly, there is a sudden plateau beyond that.</p>
<p>Looking closer at the scan data, we found that <strong>there is an error with the path creation of the scanner</strong>, where the <em>create_coordinates(angle_min, angle_max,point_count)</em> function did not produce coordinates with certain rotor angles (&lt;0 ?).&nbsp;</p>
<p>The following image shows a comparison between the 502 and 1000 photos mesh result. You can see that areas that are only visible from below are not reproduced well due to a lack of photos. For this reason, the overall quality metrics drastically decreased.</p>
<p><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/500vs1000photos.jpg"/><br/></p>
<p>As expected, the quality of the meshes reaches a certain limit way before 500 photos. In the following plot, we used the 1000 photocount set as reference:</p>
<div style="text-align: start;"><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/std-dev-vs-photocount.png" style="float: none;"/></div>
<p>Therefore, we decided that for the following evaluation, we remove the data for the results above 502 photos.<br/></p>
<h2>Analysis</h2>
<p>We compared the 3D meshes with the 502 photocount mesh as reference. We used ICP to reorient the meshes and cut the base in order to remove some scan artifacts.</p>
<div class="font-claude-message relative leading-[1.65rem] [&amp;_pre&gt;div]:bg-bg-300 [&amp;_.ignore-pre-bg&gt;div]:bg-transparent [&amp;&gt;div&gt;div&gt;:is(p,ul,ol)]:pr-4 md:[&amp;&gt;div&gt;div&gt;:is(p,ul,ol)]:pr-8" style="box-sizing: border-box; border-image: initial; --tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-scroll-snap-strictness: proximity; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: hsl(var(--accent-secondary-100)/1); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; outline-color: hsl(var(--accent-main-100)); scrollbar-color: hsl(var(--border-300)/.8) transparent; position: relative; line-height: 1.65rem; font-family: var(--font-claude-message); border: 0px solid hsl(var(--border-100));">
<div class="grid-cols-1 grid gap-2.5 [&amp;_&gt;_*]:min-w-0" style="box-sizing: border-box; border-image: initial; --tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-scroll-snap-strictness: proximity; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: hsl(var(--accent-secondary-100)/1); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; outline-color: hsl(var(--accent-main-100)); scrollbar-color: hsl(var(--border-300)/.8) transparent; display: grid; grid-template-columns: repeat(1, minmax(0px, 1fr)); gap: 0.625rem; border: 0px solid hsl(var(--border-100));">
<h3 class="text-xl font-bold text-text-200 mt-1 -mb-0.5">RMS - Error</h3>
<p class="whitespace-pre-wrap break-words">The RMS (Root Mean Square) error measures the average deviation between each point in the pointclouds and the corresponding surfaces of the 502 photocount reference mesh.&nbsp;</p>
<p class="whitespace-pre-wrap break-words"><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/rms-error-vs-photocount.png"/></p>
<h3 class="whitespace-pre-wrap break-words">Standard Deviation</h3>
<p class="whitespace-pre-wrap break-words">Between points in the lower-photocount generated pointclouds and the corresponding surfaces of the 502 photocount reference mesh, the standard deviation reveals the spread or variation in measurement errors.</p>
<p class="whitespace-pre-wrap break-words"><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/std-dev-vs-photocount-507.png"/></p>
<h3 class="text-xl font-bold text-text-200 mt-1 -mb-0.5">Maximum Distance</h3>
<p class="whitespace-pre-wrap break-words">Representing the largest measured deviation between any point in the lower-photocount generated pointcloud and the corresponding surface, the maximum distance metric exhibits higher fluctuation and uncertainty. This particular measurement demonstrates significant sensitivity to variations in the mesh structure due to differences in photo quantity.</p>
<p class="whitespace-pre-wrap break-words"><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/max-distance-vs-photocount-507.png"/></p>
<h3 class="text-xl font-bold text-text-200 mt-1 -mb-0.5">Normal Consistency</h3>
<p class="whitespace-pre-wrap break-words">The normal consistency quantifies the alignment of surface normals between the lower-photocount generated meshes and the 502 photocount reference mesh. Higher values indicate better preservation of surface orientation details. This metric provides insight into how well meshes created with fewer photos maintain the directional properties of the high-photocount surface, with consistency improving as photocount increases.</p>
<p class="whitespace-pre-wrap break-words"><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/normal-consistency-vs-photocount-507.png"/></p>
<h2 class="whitespace-pre-wrap break-words">Stabilizing points - or - what is the right amount of photos?<br/>
</h2>
<p><img alt="" src="/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/summary.jpg"/></p>
<ul>
<li>
<strong style="font-family: var(--font-claude-message); font-size: 0.875rem;">Stabilization Points</strong><span style="font-family: var(--font-claude-message); font-size: 0.875rem;">:</span>
<ul class="[&amp;:not(:last-child)_ul]:pb-1 [&amp;:not(:last-child)_ol]:pb-1 list-disc space-y-1.5 pl-7">
<li>RMS Error stabilizes at 292 photos</li>
<li class="whitespace-normal break-words">Standard Deviation stabilizes at 292 photos</li>
<li class="whitespace-normal break-words">Normal Consistency stabilizes at 333 photos</li>
<li class="whitespace-normal break-words">Maximum Distance does not show clear stabilization within the dataset</li>
</ul>
</li>
<li class="whitespace-normal break-words">
<strong>Confidence Intervals</strong> (calculated from data with photocount &gt; 400):
<ul class="[&amp;:not(:last-child)_ul]:pb-1 [&amp;:not(:last-child)_ol]:pb-1 list-disc space-y-1.5 pl-7">
<li class="whitespace-normal break-words">RMS Error: 0.0108 - 0.0130</li>
<li class="whitespace-normal break-words">Standard Deviation: 0.0097 - 0.0118</li>
<li class="whitespace-normal break-words">Maximum Distance: 0.3976 - 0.5069</li>
<li class="whitespace-normal break-words">Normal Consistency: 0.9904 - 0.9918</li>
</ul>
</li>
</ul>
<p><strong>Above 300 photos, the metrics clearly reach their plateau and there is no gain in quality with increased photo count above that threshold! So in general it is save to say that 150 photos should give you great results, whereas 300 photos should be considered the maximum for very detailed models.</strong><strong style="font-family: var(--font-claude-message); font-size: 0.875rem;"></strong></p>
<h2>Limitation</h2>
<p>We only used one reference set with very distinct and high-contrast surface features. The results might vary slightly with other objects and setups, but we are quite confident, that this number should be valid for a wide range of objects in a turntable setup.</p>
<h2 class="text-xl font-bold text-text-200 mt-1 -mb-0.5">Conclusion and Implications</h2>
<p class="whitespace-pre-wrap break-words">The most important thing with photogrammetry is understanding what a good surface looks like (i.e. having a lot of features). The amount of photos in a set plays only a minor role and when 150 photos do not give a good result, increasing the amount of photos will not improve the results significantly. Our testing clearly shows that there's an optimal range of around 150-300 images for turntable photogrammetry, with diminishing returns beyond this point.</p>
<p class="whitespace-pre-wrap break-words"><strong>Based on the analysis:</strong></p>
<ul class="[&amp;:not(:last-child)_ul]:pb-1 [&amp;:not(:last-child)_ol]:pb-1 list-disc space-y-1.5 pl-7">
<li class="whitespace-normal break-words" style="font-weight: bold;"><strong>For most objects, 150-200 photos will yield excellent results</strong></li>
<li class="whitespace-normal break-words" style="font-weight: bold;"><strong>Going up to 300 photos may provide marginal improvements for highly detailed models</strong></li>
<li class="whitespace-normal break-words" style="font-weight: bold;"><strong>Exceeding 300 photos only increases processing time without quality benefits</strong></li>
<li class="whitespace-normal break-words" style="font-weight: bold;"><strong>Image quality, lighting, and surface features remain more important factors than raw photo count</strong></li>
</ul>
<p class="whitespace-pre-wrap break-words">This finding has important practical implications for workflow efficiency. By limiting capture sessions to the optimal range, users can significantly reduce processing times while maintaining high-quality results. The time saved can be better invested in proper lighting setup, surface preparation, or post-processing refinements.</p>
<p class="whitespace-pre-wrap break-words">For OpenScan users, we recommend starting with 150-200 photos for most objects and only increasing to 300 for exceptionally detailed models where every surface feature is critical. The results will be implemented in the future firmware revisions, giving some more standardized presets for beginners (while keeping full control in expert mode)</p>
</div>
</div>
