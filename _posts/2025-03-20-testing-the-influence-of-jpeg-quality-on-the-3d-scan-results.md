---
title: "Testing the influence of JPEG quality on the 3D scan results"
date: "2025-03-20T11:52:34+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
image:
  path: "/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/10vs100-d32c27ee-7617-44a5-a35b-a940b99b3aad.gif"
redirect_from:
  - "/blogs/news/testing-the-influence-of-jpeg-quality-on-the-3d-scan-results"
  - "https://62f7a3-4.myshopify.com/blogs/news/testing-the-influence-of-jpeg-quality-on-the-3d-scan-results"
---

<p><strong>TLDR: With high contrast surface preparation of the object, JPEG quality can be reduced to under 20% without any noticeable influence on the 3D mesh. Furthermore, the experiment indicates that the size of an image after JPEG compression seems to be a great indicator of existing features (SIFT or similar).</strong></p>
<h2><strong>Method</strong></h2>
<p>We are currently running experiments to determine the influence of various parameters on the photogrammetry pipeline and resulting 3D mesh files.</p>
<p>In this first test, we used a sample dataset of 100 images (which were the result of using HDR with 5 levels and stacking with 5 levels, so a total of 2500 photos). This image set gives great mesh quality on default settings.</p>
<p>We used the OpenScanCloud to upload and process the sets automatically. Using 10 sets per jpg quality value (as it only allows integer values) gives a better understanding of the noise level.</p>
<p>After obtaining the results, we faced the challenge of alignment, as photogrammetry without markers will orient the object somewhat randomly. Therefore, we used the following approach:</p>
<ul>
<li>brute-force sampling for various random rotations of the mesh and initial ICP alignment with only 50 iterations --&gt; derived promising rotations</li>
<li>fine-alignment with ICP using 500 iterations</li>
</ul>
<p>This way, we created almost 1000 fine-aligned meshes for further analysis.<br/><br/></p>
<p><img alt="" src="/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/100to3qualitylq.gif"/></p>
<h2>Analysis</h2>
<p>We compared the 3d mesh from the lower quality sample to the 100% quality mesh as reference and got the following results. We grouped the 10 results per quality level for better results and removed some outliers, which happened due to some failures in the pipeline.</p>
<p>As my time is limited, I just drop the various graphs here, but if someone is interested in having a detailed look at the data, feel free to reach out to&nbsp;<a href="mailto:info@openscan.eu">info@openscan.eu</a></p>
<h3>RMS - Error</h3>
<p>The RMS (Root Mean Square) error measures the average deviation between each point in the lower-quality JPEG-compressed pointclouds and the corresponding surfaces of the 100% quality reference mesh. The values stabilize above ~ 15% quality.</p>
<p><img alt="" src="/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/rms-error-vs-quality.png"/></p>
<h3>Standard deviation</h3>
<p>The standard deviation indicates the variation or spread in the measurement errors between points in the lower-quality JPEG-compressed pointclouds and the corresponding surfaces of the 100% quality reference mesh. Again the values stabilize above ~ 15-20% quality.</p>
<p><img alt="" src="/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/std-dev-vs-quality.png"/></p>
<h3>Maximum distance</h3>
<p>The maximum distance represents the largest measured deviation between any point in the lower-quality JPEG-compressed pointcloud and the corresponding surface. This metric is very sensitive to variations in the mesh and shows a higher fluctuation and uncertainty.</p>
<p><img alt="" src="/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/max-distance-vs-quality.png"/></p>
<h3>Processing times</h3>
<p>This metric has some major outliers due to some failures with the OpenScanCloud processing pipeline. Ignoring those outliers gives very consistent values which only decrease below quality level of 20%.</p>
<p><img alt="" src="/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/duration-seconds-vs-quality.png"/></p>
<h2>Limitation</h2>
<p>We only used one reference set with very distinct and high-contrast surface features. This is the best-case scenario for photogrammetry, but can not always be achieved. Results will definitely differ when using another image set. I assume, that the stabilization points will be higher when the contrast of the surface-features is lower (e.g. white spray on grey material).</p>
<h2>Conclusion and Implications</h2>
<p class="whitespace-pre-wrap break-words">It is surprising to see how well high-contrast features are preserved under JPEG compression even though the overall filesize is decreased significantly (300MB at 100% --&gt; 50MB at 70%&nbsp; and 24MB at 20% Quality). The processing times indicate that mostly irrelevant areas of the images are compressed.</p>
<p class="whitespace-pre-wrap break-words">Thus suggests that for photogrammetry with high-contrast surface preparation, you can safely drop JPEG quality to about 70% without hurting mesh quality. This is a meaningful optimization - file sizes shrink by over 80% while maintaining virtually identical results.</p>
<p class="whitespace-pre-wrap break-words">What's more, the size of an image after JPEG compression seems to be a great indicator of feature preservation. This makes sense given how JPEG works - it keeps high-contrast edges while compressing uniform areas, which is exactly what photogrammetry algorithms like SIFT need for reconstruction.</p>
<p class="whitespace-pre-wrap break-words">These results have practical implications for photogrammetry workflows, especially when storage or bandwidth is limited.</p>
<p class="whitespace-pre-wrap break-words">Furthermore, we will use these findings to create a compute-cheap feature-density-preview algorithm which is roughly 20 times faster than SIFT in a coming blog post.</p>
<p class="whitespace-pre-wrap break-words"><img alt="" src="/assets/img/posts/2025-03-20-testing-the-influence-of-jpeg-quality-on-the-3d-scan-results/feature-density.jpg"/></p>
<p>Red overlay indicates high feature density.</p>
<ol>
<li>Sprayed Benchy - Camera Focus on legs (further away)</li>
<li>Sprayed Benchy - Camera Focus on Body</li>
<li>untreated Benchy --&gt; no features</li>
</ol>
<p>&nbsp;</p>
