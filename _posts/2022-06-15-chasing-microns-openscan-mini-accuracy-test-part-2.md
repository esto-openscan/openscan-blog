---
title: "Chasing microns - OpenScan Mini accuracy test part 2"
date: "2022-06-15T13:00:00+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
  - "News"
  - "Tutorial"
image:
  path: "/assets/img/posts/2022-06-15-chasing-microns-openscan-mini-accuracy-test-part-2/2022-06-15-accuracy04.webp"
redirect_from:
  - "/blogs/news/chasing-microns-openscan-mini-accuracy-test-part-2"
  - "https://62f7a3-4.myshopify.com/blogs/news/chasing-microns-openscan-mini-accuracy-test-part-2"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1"><strong data-mce-fragment="1">TLDR: I improved the setup and got myself some highly accurate steel spheres with nominal diameter of 20 and 25 mm &plusmn; 0.0025mm. I used the </strong><a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://en.openscan.eu/openscan-mini" href="https://en.openscan.eu/openscan-mini" target="_blank"><strong data-mce-fragment="1"><u data-mce-fragment="1">OpenScan Mini</u></strong></a><strong data-mce-fragment="1"> to scan a scene with both spheres, scaled it using a reference measurement from one sphere, and analyzed the diameter and surface deviation of the second one. I reliably get a diameter of ~20&plusmn;0.03mm as well as a surface deviation within 2&sigma; = 0.03mm</strong></span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="c8bss" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">I knew that <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://en.openscan.eu/post/0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare-1" href="https://en.openscan.eu/post/0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare-1" target="_blank">my latest post claiming a bold 0.008mm accuracy</a> made a very click-baity claim, but it triggered enough professionals, so that I got a lot of feedback and valuable input. Thanks to all those people, sharing their knowledge. This is a great help to improve this project!</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="b90eb" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">And even more thanks goes to those people supporting the project with donations through <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://www.patreon.com/OpenScan" href="https://www.patreon.com/OpenScan" target="_blank"><u data-mce-fragment="1">Patreon</u></a>. I probably couldn't face my wife, after spending &gt;100&euro; on some steel balls, so thank you for making this kind of experiments possible! :)</span></p>
<h3 class="vGBkk sWzLp" data-mce-fragment="1" dir="auto" id="6j9pf" indentation="0" level="3" textstyle="[object Object]"><span data-mce-fragment="1">The setup: Chrome Alloy Steel spheres</span></h3>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-15-chasing-microns-openscan-mini-accuracy-test-part-2/2022-06-15-accuracy01-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="9gq1t" indentation="0" textstyle="[object Object]"><span>Sample image showing the illumination and surface preparation</span></p>
<ul>
<li>two spheres of 20 and 25mm diameter (claimed accuracy within 0.0025mm)</li>
<li>using the <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://en.openscan.eu/openscan-mini" href="https://en.openscan.eu/openscan-mini" target="_blank"><u>OpenScan Mini</u></a> with Polarizer module (cross polarization setup)</li>
<li>covered the scene in a thin layer of Aesub Orange self-vanishing 3D Scanning spray</li>
<li>took 150 photos per set (--&gt; 230-250MB total data) and a total</li>
<li>capture process takes 11 mins per set</li>
<li>a total of 8 sets within two days (temperature within 20&deg;C &plusmn; 2K)</li>
<li>processing was done using the <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://en.openscan.eu/openscan-cloud" href="https://en.openscan.eu/openscan-cloud" target="_blank"><u>OpenScanCloud</u></a> and took 6-8 mins per set</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="8r7g6" indentation="0" textstyle="[object Object]"><span>Just let me know if you want to check the raw image data or resulting raw/scaled 3d models, and I will happily share all files.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="en8e2" indentation="0" level="3" textstyle="[object Object]"><span>The scaling procedure (using free Autodesk Meshmixer)</span></h3>
<p><span><img alt="" src="/assets/img/posts/2022-06-15-chasing-microns-openscan-mini-accuracy-test-part-2/2022-06-15-accuracy02-600x600.webp"/></span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="b5krs" indentation="0" textstyle="[object Object]"><span><em>Measuring the diameter of the sphere to calculate the scaling factor in </em><a class="Y-s64 XzMaT" data-hook="WebLink" href="https://www.meshmixer.com/" target="_blank"><em><u>Meshmixer</u></em></a> </span></p>
<p class="j1LEL va-er" dir="auto" id="44uds" indentation="0" textstyle="[object Object]"><span>I can not repeat this point enough: Photogrammetry models naturally come without any information about scale. But it is absolutely possible to scale the model accurately with various methods:</span></p>
<ul>
<li>include markers in the scene with known distance</li>
<li>know the camera positions and parameters</li>
<li>include an object with known dimensions</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="cgdmj" indentation="0" textstyle="[object Object]"><span>Unfortunately, the first two options are not implemented in the <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://en.openscan.eu/openscan-cloud" target="_blank"><u>OpenScanCloud</u></a> yet (but would work with different software packages).</span></p>
<p class="j1LEL va-er" dir="auto" id="6av9h" indentation="0" textstyle="[object Object]"><span>For this reason, I used the 25 mm sphere to take 5 measurements and calculate the mean. See the image above, where the raw scan shows a diameter of ~ 0.3128mm (--&gt; scaling factor: 79.923). I used the measuring tool in "Analyse --&gt; Measure" (select the type and direct as shown in the image). I scribble over the surface of the sphere and collect several values and calculate the scaling factor. </span></p>
<p class="j1LEL va-er" dir="auto" id="f5dv9" indentation="0" textstyle="[object Object]"><span>Scaling was done in Meshmixer too ("Edit --&gt; Transform --&gt; Scale XYZ"). </span></p>
<p class="j1LEL va-er" dir="auto" id="bgn9q" indentation="0" textstyle="[object Object]"><span>I understand, that this method is not perfect and introduces quite a bit of uncertainty, but from a practical point of view, it just works fine. And we shall see in the results of this post, if scaling can be done reliably...</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-15-chasing-microns-openscan-mini-accuracy-test-part-2/2022-06-15-accuracy03-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="8tjl1" indentation="0" textstyle="[object Object]"><span><em>Getting the scaling factor for each dataset using five measurements</em></span></p>
<p class="j1LEL va-er" dir="auto" id="554tf" indentation="0" textstyle="[object Object]"><span>Unfortunately, this blog just lets me post images and videos (no tables), so let me know if you are interested in the raw Excel sheet containing all the measured and derived values ;)</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="fdqdn" indentation="0" level="3" textstyle="[object Object]"><span>Mesh analysis using GOM inspect</span></h3>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-15-chasing-microns-openscan-mini-accuracy-test-part-2/2022-06-15-accuracy04-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="3v6nt" indentation="0" textstyle="[object Object]"><span><em>Selecting an area in </em><a class="Y-s64 XzMaT" data-hook="WebLink" href="https://www.gom.com/en/products/gom-suite/gom-inspect-pro" target="_blank"><em><u>GOM inspect</u></em></a><em> and auto-fitting a sphere</em></span></p>
<p class="j1LEL va-er" dir="auto" id="369ja" indentation="0" textstyle="[object Object]"><span>I selected ~ 60-80% of the scanned sphere's surface and used "construct --&gt; sphere --&gt; auto-sphere" to create the best fitting sphere. I repeated this procedure for both spheres and all eight datasets.</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-15-chasing-microns-openscan-mini-accuracy-test-part-2/2022-06-15-accuracy05-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="60go2" indentation="0" textstyle="[object Object]"><span><em>Measured Radius and surface deviation (sigma) from ideal sphere</em></span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="3mlcf" indentation="0" level="3" textstyle="[object Object]"><span>Results and Discussion</span></h3>
<p class="j1LEL va-er" dir="auto" id="as437" indentation="0" textstyle="[object Object]"><span>For the radius, I measured:</span></p>
<div class="j1LEL va-er" dir="auto" id="duloo" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>r_1 = 12.493 mm (should be 12.500 mm)</strong></span></div>
<div class="j1LEL va-er" dir="auto" id="a8eh5" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>r_2 = 9.985 mm (should be 10.000 mm)</strong></span></div>
<div class="j1LEL va-er" dir="auto" id="rl2m" indentation="0" style="text-align: center;" textstyle="[object Object]"></div>
<p class="j1LEL va-er" dir="auto" id="50v7q" indentation="0" textstyle="[object Object]"><span>The surface deviation of the sphere lie within:</span></p>
<div class="j1LEL va-er" dir="auto" id="9abe3" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong> 2&sigma;_1 = 0.024 mm</strong></span></div>
<div class="j1LEL va-er" dir="auto" id="cqa9i" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>2&sigma;_1 = 0.028 mm</strong></span></div>
<p class="j1LEL va-er" dir="auto" id="qhj9" indentation="0" textstyle="[object Object]"><span>I know, that one could do much more with those numbers, but I am fine with that result.</span></p>
<p class="j1LEL va-er" dir="auto" id="73nlt" indentation="0" textstyle="[object Object]"><span>Note, that there are definitely some shortcomings in my methods:</span></p>
<ul>
<li>The scaling seems to be slightly off, since all measured values are below the expected values. This is probably caused in my tool choice in Meshmixer.</li>
<li>I just realized how my former math "skills" got really rusty over the years of non-use, so please excuse my mistakes and let me know what to improve!</li>
<li>I did not get the spheres calibrated in a certified lab due to the high cost for a piece of paper</li>
<li>...</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="adavt" indentation="0" textstyle="[object Object]"><span>Hmmm, I am still not really able to make a valid accuracy-statement for the scanner. Maybe someone can help me with a good and not so click-baity formulation!</span></p>
<p class="j1LEL va-er" dir="auto" id="brdgp" indentation="0" textstyle="[object Object]"><span>And let me know what else I could try with this (or other 3d scanners)</span></p>
