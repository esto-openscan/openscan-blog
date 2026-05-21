---
title: "New Firmware with cloud functionality for OpenScan Classic & Mini (Beta)"
date: "2021-10-11T11:00:00+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Update"
image:
  path: "/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware.webp"
redirect_from:
  - "/blogs/news/new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta"
  - "https://62f7a3-4.myshopify.com/blogs/news/new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">After publishing a Windows Desktop GUI and the Python scripts to upload files to the OpenScanCloud, I finally managed to implement the new features into the OpenScan Firmware.</span></p>
<h3 class="vGBkk sWzLp" data-pm-slice="1 1 []" dir="auto" id="894d2" indentation="0" level="3" textstyle="[object Object]"><span>Overview</span></h3>
<p class="j1LEL va-er" dir="auto" id="f8ndc" indentation="0" textstyle="[object Object]"><span>Basically, this makes the</span> OpenScan Classic and Mini<span> smart devices able to create highly detailed 3D scans without any additional hardware or software!</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="9dki1" indentation="0" textstyle="[object Object]"><span>The firmware hasn't been changed a lot, and I only added two new panels to the right side of the Files&amp;Cloud tab. You will always be able to transfer the zip-files to your local computer and do the processing manually. </span></p>
<p class="j1LEL va-er" dir="auto" id="ad73a" indentation="0" textstyle="[object Object]">&nbsp;</p>
<p class="j1LEL va-er" dir="auto" id="faak0" indentation="0" textstyle="[object Object]"><span>But I have seen an increasing number of people struggling with either the software and/or hardware requirements that come with photogrammetry... Therefore, it is now possible to select and upload an image set to my servers, where I will do the processing and send you the result by email.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="15qk9" indentation="0" level="3" textstyle="[object Object]"><span>Install the latest Beta-Firmware</span></h3>
<p class="j1LEL va-er" dir="auto" id="d9rfc" indentation="0" textstyle="[object Object]"><span>In order to use this beta functionality, you will need to log in to your Raspberry Pi and run the following single-line-command in the terminal:</span></p>
<p class="j1LEL va-er" dir="auto" id="a57vs" indentation="0" textstyle="[object Object]"><span><em>sudo wget -O /home/pi/.node-red/flows_raspberrypi.json https://raw.githubusercontent.com/OpenScanEu/OpenScanCloud/main/uploader/firmware_beta.json &amp;&amp; node-red-restart</em></span></p>
<p class="j1LEL va-er" dir="auto" id="d094f" indentation="0" textstyle="[object Object]"><span>which will download and install the latest beta firmware.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="akksd" indentation="0" level="3" textstyle="[object Object]"><span>OpenScanCloud Settings </span></h3>
<p class="j1LEL va-er" dir="auto" id="4hoic" indentation="0" textstyle="[object Object]"><span>The only thing needed is a personal token, which you can easily apply for by sending an email to <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="cloud@openscan.eu" href="cloud@openscan.eu" target="_blank"><u>cloud@openscan.eu</u></a>. You will then need to enter the token in the OpenScanCloud Settings Tab (in this example: <em>4x1c1128e </em>...):</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware1-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="6iqaa" indentation="0" textstyle="[object Object]"><span>After hitting refresh, some associated data will be loaded from the server:</span></p>
<ul>
<li>
<strong><em>Credit </em></strong>- A number showing how much gigabyte you are currently allowed to upload and process. This value is currently limited to prevent abuse. Anyway, if you run out of "credit", just email me.</li>
<li>
<strong><em>Max. Number of Photos</em></strong>: Is the maximum number of photos that are allowed in ONE set.</li>
<li>
<strong><em>Max Filesize: </em></strong>in gigabyte is the limit for the file size for ONE image set/zip.</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="8rb3a" indentation="0" textstyle="[object Object]"><span> There will be some updates in the near future, and after installing this version, you will be able to get those updates by simply clicking the update button below. I will write blog posts about any major updates of the firmware, but you can also follow the project on <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://github.com/OpenScanEu/OpenScanCloud/blob/main/README.md" href="https://github.com/OpenScanEu/OpenScanCloud/blob/main/README.md" target="_blank"><u>GitHub</u></a><u>.</u></span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="6h31e" indentation="0" level="3" textstyle="[object Object]"><span>Upload &amp; Process image sets with OpenScanCloud</span></h3>
<p class="j1LEL va-er" dir="auto" id="35s9e" indentation="0" textstyle="[object Object]"><span>In order to start processing, you will only need to select an image set from the list and press <em>upload</em>. In order to upload the set, the file might need to be split into 200MB chunks. This step is fully automated and can take up to a minute, so please be patient. Those chunks will be uploaded and processing will be started as soon as possible. </span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware2-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="8mud6" indentation="0" textstyle="[object Object]"><span>You can always press <em>refresh </em>to query the current status of your projects, which should be one of the following:</span></p>
<ul>
<li>
<strong>created</strong>: The project has been successfully created on the server</li>
<li>
<strong>initialized</strong>: All files have been uploaded and processing will start soon</li>
<li>
<strong>processing started/failed/done</strong>: self-explanatory</li>
</ul>
<div class="vGBkk sWzLp" dir="auto" id="d4es3" indentation="0" level="3" style="text-align: left;" textstyle="[object Object]"><strong>OpenScanCloud - Example - Miniature</strong></div>
<div class="j1LEL va-er" dir="auto" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="560" src="https://www.youtube.com/embed/zTf4UN-JXps" title="YouTube video player" width="315"></iframe></span></div>
<div class="j1LEL va-er" dir="auto" indentation="0" style="text-align: left;" textstyle="[object Object]">
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="2rugt" indentation="0" textstyle="[object Object]"><span>I have scanned this 9 cm tall figurine with the OpenScanMini and took a total of 70 photos. In order to get such a clean result, I needed to cover the surface with a fine layer of scanning spray. Besides the uploading time, processing took not even three full minutes :)</span></p>
<p class="j1LEL va-er" dir="auto" id="4t18r" indentation="0" textstyle="[object Object]"><span>So far, I have tested the engine with over 50.000 images in 700 photo sets and the robustness and speed are quite impressive.</span></p>
<p class="j1LEL va-er" dir="auto" id="6objh" indentation="0" textstyle="[object Object]"><span>Feel free to join the testing by sending me a mail to <a class="Y-s64 XzMaT" data-hook="WebLink" href="cloud@openscan.eu" target="_blank"><u>cloud@openscan.eu</u></a> and let me know what you think.</span></p>
<p class="j1LEL va-er" dir="auto" id="abml1" indentation="0" textstyle="[object Object]"><span>Best regards,</span></p>
<p class="j1LEL va-er" dir="auto" id="4d7t1" indentation="0" textstyle="[object Object]"><span>Thomas</span></p>
</div>
