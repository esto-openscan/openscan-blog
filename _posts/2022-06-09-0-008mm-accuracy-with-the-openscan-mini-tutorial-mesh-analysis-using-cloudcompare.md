---
title: "0.008mm accuracy with the OpenScan Mini - Tutorial - Mesh analysis using CloudCompare"
date: "2022-06-09T13:00:00+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
  - "Tutorial"
image:
  path: "/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy03.webp"
redirect_from:
  - "/blogs/news/0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare"
  - "https://62f7a3-4.myshopify.com/blogs/news/0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1"><strong data-mce-fragment="1">TLDR: </strong></span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="doabn" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1"><strong data-mce-fragment="1">I scanned a feeler gauge with the</strong><a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://en.openscan.eu/openscan-mini" href="https://en.openscan.eu/openscan-mini" target="_blank"><strong data-mce-fragment="1"><u data-mce-fragment="1"> OpenScan Mini</u></strong></a><strong data-mce-fragment="1">, processed the data in the </strong><a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://en.openscan.eu/openscan-cloud" href="https://en.openscan.eu/openscan-cloud" target="_blank"><strong data-mce-fragment="1"><u data-mce-fragment="1">OpenScan Cloud</u></strong></a><strong data-mce-fragment="1"> and scaled the object with the help of the known dimension. Next, I digitally measured the thickness of each feeler and got a deviation of 0.008&nbsp;mm from the claimed/real thicknesses (0.05 mm - 0.55 mm). There are several points that will be discussed in this article. But just to give you a perspective, that 0.008 mm is somewhat around a fifth of the thickness of the human hair. </strong></span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="8detm" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Since the beginning of the OpenScan project, the question of how accurate the device can be had been haunting. I have been very hesitant to even try to answer this question, since I am no metrology expert and my methods might be a bit funky. But I finally convinced myself, that the following measurements and discussion seem at least worth sharing. And hopefully, this could even start a discussion with some more experienced users. Maybe even some other scanner users or developers could do a similar scan with their devices and share the (raw) results. I would even do the analysis :)</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="d8qfc" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">I will use this case to show my standard procedure of analyzing the mesh in <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://www.danielgm.net/cc/" href="https://www.danielgm.net/cc/" target="_blank"><u data-mce-fragment="1">CloudCompare </u></a>(which are both free-to-use programs).</span></p>
<h2 class="RwFIZ sWzLp" data-mce-fragment="1" dir="auto" id="8mltl" indentation="0" level="2" textstyle="[object Object]"><span data-mce-fragment="1"><strong data-mce-fragment="1">The scan object and procedure: Feeler gauge</strong></span></h2>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy01-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="7f4p6" indentation="0" textstyle="[object Object]"><span>Source: https://www.amazon.de/-/en/3083-Precision-Feeler-Sheets-Metric/dp/B001ILD9HQ/ref=sxin_14_b2b_sx_ibs_v4_desktop</span></p>
<p class="j1LEL va-er" dir="auto" id="4mjtp" indentation="0" textstyle="[object Object]"><span>The feeler gauge is normally used to measure gap widths. I got mine for around 10&euro; and this should be at least an indicator for the quality and accuracy. The feeler's thickness range from 0.05 mm to 1 mm in steps of 0.05 mm. But I only used those in the range of 0.05-0.55 mm plus the 1 mm piece.</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy02-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 3 []" dir="auto" id="81lfu" indentation="0" textstyle="[object Object]"><span>This is probably the ugliest scan object arrangement I ever did, but it is highly functional:</span></p>
<ul>
<li>I used some putty to give the object some depth, because the alignment of front and back seemed to be tricky/fail otherwise in earlier attempts</li>
<li>
<span data-font-size="18">added the gauge block of known dimensions. The width along the blue line (see below) is 50.000(5) mm and accurate to 0.5 microns according to </span>DIN EN ISO 3650</li>
<li>sprayed the whole arrangement with a light sprinkle of Aesub Orange to create enough surface features</li>
<li>
<span data-font-size="18">used the polarizer module of the </span><a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://en.openscan.eu/openscan-mini" href="https://en.openscan.eu/openscan-mini" target="_blank"><span data-font-size="18"><u>OpenScan Mini</u></span></a><span data-font-size="18"> to filter reflective highlights</span>
</li>
<li>took a total of 150 photos with the Arducam IMX519</li>
</ul>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy03-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="fk9kj" indentation="0" textstyle="[object Object]"><span>Raw scan result using the OpenScan Cloud, see and download the 3d model on <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://skfb.ly/ouQxR" href="https://skfb.ly/ouQxR" target="_blank"><u>Sketchfab</u></a> </span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" indentation="0" textstyle="[object Object]"><span><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy04-600x600.webp"/></span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="aj6s" indentation="0" textstyle="[object Object]"><span>Cross-section along the red line (0.005 to 0.055 mm thickness)</span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="mo1g" indentation="0" textstyle="[object Object]"><span><strong>Some observations:</strong></span></p>
<ul>
<li>the noise in the bottom area of the scan is caused by the photos being mostly blurry in that area (since the object exceeds the 8x8x8cm scanning volume of the <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://en.openscan.eu/openscan-mini" href="https://en.openscan.eu/openscan-mini" target="_blank"><u>OpenScan Mini</u></a>)</li>
<li>in the area of interest (the feeler tips and the gauge block) have very low noise</li>
<li>you can even see my fingerprints in the putty ;)</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="6du4j" indentation="0" textstyle="[object Object]"><span>Scaling was done in <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://www.meshmixer.com/" href="https://www.meshmixer.com/" target="_blank"><u>Autodesk Meshmixer</u></a> and the procedure will be covered in an upcoming tutorial. But basically I took three measurements along the blue line and scaled the object accordingly.</span></p>
<h2 class="RwFIZ sWzLp" dir="auto" id="2k9f7" indentation="0" level="2" textstyle="[object Object]"><span><strong>Analysis in CloudCompare</strong></span></h2>
<p class="j1LEL va-er" dir="auto" id="cdaqj" indentation="0" textstyle="[object Object]">&nbsp;<span><strong>Feel free to skip this chapter by jumping to the results</strong><strong>&nbsp;;)</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="8qlpg" indentation="0" textstyle="[object Object]">&nbsp;<span><strong>(1) Drag and Drop the .stl/.obj file into CloudCompare</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy05-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="7arvd" indentation="0" textstyle="[object Object]"><span>If the object appears fully white, you should activate "Display --&gt; Shaders &amp; Filters --&gt; EDL shader"</span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="922ob" indentation="0" textstyle="[object Object]"><span><strong>(2) Segment the object into smaller pieces</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy06-600x600.webp" style="float: none;"/></div>
<ul>
<li>Zoom into the area of interest and use "Edit --&gt; Segment".</li>
<li>Click into the 3d view to create a contour (green lines).</li>
<li>Press "I" or "O" to keep the inner/outer segment. (Don't worry, the other part will be kept as well). This will create two new objects to work with.</li>
</ul>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="eomcs" indentation="0" textstyle="[object Object]"><span><strong>(3) Rename the created objects and save everything</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy07-600x600.webp" style="float: none;"/></div>
<ul>
<li>Use the DB Tree window on the left to manage the individual parts. I like to rename each segment to keep it somewhat organized.</li>
<li>Note, that CloudCompare has no undo-operation (!!) and thus you should save your progress from time to time.</li>
<li>Therefore, select all objects in the DB Tree and "File --&gt; Save". This will create .bin file, which you can reload at any time.</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="ag4is" indentation="0" textstyle="[object Object]">&nbsp;<span><strong>(4) Sample Points (Mesh --&gt; PointCloud)</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy08-600x600.webp" style="float: none;"/></div>
<ul>
<li>Hide all unneeded object by unticking the boxes in the DB Tree window.</li>
<li>Select one of the segments (in my case, the "100" mesh, which is the left most feeler with a thickness of 1.00mm).</li>
<li>Convert the Mesh to a point cloud with 1 Mio. Points with "Edit --&gt; Mesh --&gt; Sample Points"</li>
<li>And hide the 100 mesh (since a 100.sampled object appears, which contains the samples point cloud)</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="c67sc" indentation="0" textstyle="[object Object]"><span><strong>(5) Segment into the upper and lower part</strong></span></p>
<div style="text-align: center;"><img src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy09-600x600.webp" style="float: none;"/></div>
<ul>
<li>Select the point cloud in the DB Tree (100.sampled)</li>
<li>Use "Edit --&gt; Segment" Tool and create a contour around the upper or lower part</li>
<li>two point clouds 100.sampled.remaining and 100.sampled.segmented will be created</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="3jrda" indentation="0" textstyle="[object Object]"><span><strong>(6) Calculate the mean distance between the two objects</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy10-600x600.webp" style="float: none;"/></div>
<ul>
<li>"Tools --&gt; Distances --&gt; Cloud/Cloud Dist."</li>
<li>Choose the role, when you are using for instance a CAD model as reference (doesn't matter here)</li>
<li>Ok --&gt; Compute --&gt; Ok to create a colorful histogram ;)</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="8lt0h" indentation="0" textstyle="[object Object]"><span><strong>(7) Showing the results (pt. 1)</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy11-600x600.webp" style="float: none;"/></div>
<ul>
<li>Select each point cloud in the DB Tree and deactivate the "Normals" in the Properties window (left side)</li>
<li>Now, one of the point clouds appears in wonderful colors</li>
<li>Note, that the mean distance and std. deviation between the two entities is displayed on the bottom of the main window (MEAN = 1.007713 and STD = 0.007364)</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="ftt77" indentation="0" textstyle="[object Object]"><span><strong>(8) Showing the results (pt. 2)</strong></span></p>
<div style="text-align: center;"><img src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy12-600x600.webp" style="float: none;"/></div>
<ul>
<li>Select the colored point cloud in the DB Tree</li>
<li>"Edit --&gt; Scalar fields --&gt; Show Histogram"</li>
<li>A new window will appear showing the histogram</li>
<li>You can export the histogram as .png or the raw values as .csv on the top right of the window.</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="14h41" indentation="0" textstyle="[object Object]"><span><strong>(9) Repeat for the other 11 feelers ;)</strong></span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy13-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="4cfgg" indentation="0" textstyle="[object Object]"><span>(Note, that I changed the scalar-field's x-axis a bit to get comparable color-coding. This doesn't have any influence on the mean and STD values shown below. If anyone is interested in the raw data, feel free to reach out ;)</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-06-09-0-008mm-accuracy-with-the-openscan-mini-tutorial-mesh-analysis-using-cloudcompare/2022-06-09-accuracy14-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="2fg1k" indentation="0" textstyle="[object Object]"><span>I am really not sure, what to think about these results, so let's continue with some discussion:</span></p>
<h2 class="RwFIZ sWzLp" data-pm-slice="1 1 []" dir="auto" id="1d6t4" indentation="0" level="2" textstyle="[object Object]"><span><strong>Results and Discussion</strong></span></h2>
<h2 class="j1LEL va-er" dir="auto" id="8s11d" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>&Delta;d = </strong><strong>0,0077&plusmn;0,0059 mm</strong></span></h2>
<p class="j1LEL va-er" dir="auto" id="dt1jk" indentation="0" textstyle="[object Object]"><span><strong>(the mean difference between digitally measured and real/claimed thickness is roughly 0.007 micron)</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="e4c5p" indentation="0" textstyle="[object Object]"><span><strong>Some thoughts and partly open questions:</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="feudr" indentation="0" textstyle="[object Object]"><span><strong>What are the real dimensions of the individual feelers?</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="em589" indentation="0" textstyle="[object Object]"><span> This is hard to tell, but I would say, that due to the low variance, they seemed to be surprisingly accurate.</span></p>
<p class="j1LEL va-er" dir="auto" id="8avgn" indentation="0" textstyle="[object Object]"><span><strong>How accurate and reliable is the scaling?</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="1ekcd" indentation="0" textstyle="[object Object]"><span> I repeated this scan and scanned some other objects too and seem to get consistent results.</span></p>
<p class="j1LEL va-er" dir="auto" id="69ds7" indentation="0" textstyle="[object Object]"><span><strong>What is the influence of the scanning spray?</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="d8psh" indentation="0" textstyle="[object Object]"><span> As far as I know, the thickness of carefully applied Aesub Orange lies within the low single digit micron range (but maybe someone can verify/correct)</span></p>
<p class="j1LEL va-er" dir="auto" id="ar69q" indentation="0" textstyle="[object Object]"><span><strong>Did I do any other methodical mistakes??</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="2h5u9" indentation="0" textstyle="[object Object]"><span> I do not know, please point me into the right direction and share your thoughts!</span></p>
<p class="j1LEL va-er" dir="auto" id="pvae" indentation="0" textstyle="[object Object]"><span><strong>Can I claim, that the OpenScan Mini can be accurate to 0.008mm (or 0.02mm to be a bit more conservative)??</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="7agqj" indentation="0" textstyle="[object Object]"><span> I am still hesitant to claim this or any accuracy and would love to hear some professional opinions on that!</span></p>
<p class="j1LEL va-er" dir="auto" id="1ad39" indentation="0" textstyle="[object Object]"><span>Thanks for your interest! </span></p>
<p class="j1LEL va-er" dir="auto" id="6hc1n" indentation="0" textstyle="[object Object]"><span>Best regards,</span></p>
<p class="j1LEL va-er" dir="auto" id="47tpq" indentation="0" textstyle="[object Object]"><span>Thomas</span></p>
<p class="j1LEL va-er" dir="auto" id="5i5ft" indentation="0" textstyle="[object Object]"><span>PS: If you made it that far and like what I do, feel free to support the project through <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://www.patreon.com/OpenScan" target="_blank"><u>Patreon</u></a><u>.</u> </span></p>
