---
title: "Major Firmware Update - OpenScanCloud 4 All"
date: "2022-01-08T12:00:00+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "News"
  - "Tutorial"
  - "Update"
image:
  path: "/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update1.webp"
redirect_from:
  - "/blogs/news/major-firmware-update-openscancloud-4-all"
  - "https://62f7a3-4.myshopify.com/blogs/news/major-firmware-update-openscancloud-4-all"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1"><strong data-mce-fragment="1">In short: You can create 3d models like this with only your Raspberry Pi + Camera and an internet connection (5 clicks --&gt; 100 photos + 5 min of automated processing)</strong></span></p>
<div data-mce-style="text-align: center;" style="text-align: center;"><img alt="" data-mce-src="https://cdn.shopify.com/s/files/1/0810/2327/1257/files/2022-01-08_Firmware_Update1_600x600.webp?v=1710327408" data-mce-style="float: none;" src="/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update1-600x600.webp" style="float: none;"/></div>
<div data-mce-style="text-align: center;" style="text-align: center;">
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="bvh61" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>After a lot of testing, I am finally able to release the firmware with integrated cloud functionality. From now on, every OpenScan device can transfer image sets to the OpenScanCloud for processing. </span></p>
<p class="j1LEL va-er" dir="auto" id="fmpcq" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>The visible changes of the user interface seem minor, but the usability-improvement should be huge, as you won't need any processing power or additional software to get a detailed 3d model. Of course, you will always be able to do the processing locally.</span></p>
<p class="j1LEL va-er" dir="auto" id="fudcp" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>The installation is as simple as possible: You should get a notification about the available update, or you can manually check &amp; install the update in the "Update&amp;Info" tab on your device. Note, that two automated restarts are required, and therefore the installation will take roughly two minutes.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="4mv7f" indentation="0" level="3" style="text-align: left;" textstyle="[object Object]"><span><strong>File Menu</strong></span></h3>
<p><span><strong><img data-mce-src="https://cdn.shopify.com/s/files/1/0810/2327/1257/files/2022-01-08_Firmware_Update2_600x600.webp?v=1710327440" data-mce-style="float: none;" src="/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update2-600x600.webp" style="float: none;"/></strong></span></p>
<p data-mce-style="text-align: left;" style="text-align: left;"><span>In the file menu, you can select a stored image set and upload it to the OpenScanCloud Servers. </span></p>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="cgqv8" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>Refreshing will query the server for your stored image sets. This will update the status in the file table accordingly ('file approved', 'processing started', 'processing done', 'processing failed'). See the help icon for a detailed description</span>&nbsp;</p>
<h3 class="vGBkk sWzLp" data-mce-style="text-align: left;" dir="auto" id="f70vr" indentation="0" level="3" style="text-align: left;" textstyle="[object Object]"><span><strong>Settings Menu</strong></span></h3>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="65pft" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>In order to use the cloud processing, you will need to read&amp;agree to the Terms of Use.&nbsp;</span><span>Find more details using the little help icon :)</span></p>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="cv40p" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>Upon first usage, you will need to register by giving your name + email address. Note, that I currently have to approve each request manually and thus, the confirmation email might take a bit ;)</span></p>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" indentation="0" style="text-align: left;" textstyle="[object Object]"><span><img data-mce-src="https://cdn.shopify.com/s/files/1/0810/2327/1257/files/2022-01-08_Firmware_Update3_600x600.webp?v=1710327492" data-mce-style="float: none; display: block; margin-left: auto; margin-right: auto;" src="/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update3-600x600.webp" style="float: none; display: block; margin-left: auto; margin-right: auto;"/></span></p>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>Once you received the registration email, you can enter the token and use the cloud processing.</span></p>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="799nu" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>In case you run out of "credit", just send me a mail to <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="cloud@openscan.eu" href="cloud@openscan.eu" target="_blank"><u>cloud@openscan.eu</u></a>. (In the future, i might remove those limits)</span></p>
<h3 class="vGBkk sWzLp" data-mce-style="text-align: left;" dir="auto" id="7fhr" indentation="0" level="3" style="text-align: left;" textstyle="[object Object]"><span><strong>Changelog on GitHub</strong></span></h3>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="a8e3u" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>See some other minor improvements and all details on <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://github.com/OpenScanEu/OpenScan" href="https://github.com/OpenScanEu/OpenScan" target="_blank"><u>GitHub</u></a> </span></p>
<h3 class="vGBkk sWzLp" data-mce-style="text-align: left;" dir="auto" id="1a233" indentation="0" level="3" style="text-align: left;" textstyle="[object Object]"><span><strong>Support the project</strong></span></h3>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="79li2" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>I will do everything I can to keep this functionality free and open. In case you can, please consider supporting my endeavor financially through a <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://www.buymeacoffee.com/OpenScan" href="https://www.buymeacoffee.com/OpenScan" target="_blank"><u>donation on BuyMeACoffee</u></a> OR share the project, so that more people get involved. :)</span></p>
<h3 class="vGBkk sWzLp" data-mce-style="text-align: left;" dir="auto" id="2ace8" indentation="0" level="3" style="text-align: left;" textstyle="[object Object]"><span><strong>Little Promotion</strong></span></h3>
<p class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" id="4gf5b" indentation="0" style="text-align: left;" textstyle="[object Object]"><span>To start this new year, I offer free worldwide shipping with the coupon code '<strong>2022willbegreat</strong>', which is valid till 15th of January and can be applied on all orders at <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="www.openscan.eu/shop" href="www.openscan.eu/shop" target="_blank"><u>www.openscan.eu/shop</u></a> over &euro;50.</span></p>
</div>
