---
title: "OpenScan Mini + Classic - New Firmware (Beta)"
date: "2021-11-22T11:30:00+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "News"
  - "Update"
image:
  path: "/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta.webp"
redirect_from:
  - "/blogs/news/openscan-mini-classic-new-firmware-beta"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan-mini-classic-new-firmware-beta"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 3 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Finally, there is a new Raspbian image for the OpenScan devices incorporating the latest changes:</span></p>
<ul>
<li>OpenScanCloud - one-click-processing of your 3d models</li>
<li>Access Point - whenever there is no Wifi available, the device will create an access point</li>
<li>Many minor and major bug fixes :)</li>
<li>...</li>
</ul>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="d517p" indentation="0" textstyle="[object Object]">In order to test the beta, please&nbsp;follow this <a href="https://openscan-org.github.io/OpenScan-Doc/firmware/setup/" target="_blank" title="Github">Github Link</a>.</p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="f3mti" indentation="0" textstyle="[object Object]"><span><strong>Note, that this is still a beta version and there might/will be some bugs included. So only install the image, if you know at least a bit of troubleshooting (i.e. command line/headless access to Raspbian).</strong></span></p>
<h3 class="vGBkk sWzLp" data-pm-slice="1 1 []" dir="auto" id="7iheh" indentation="0" level="3" textstyle="[object Object]"><span><strong>(1) Setup - Burning the SD card image</strong></span></h3>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta1-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="big6r" indentation="0" textstyle="[object Object]"><span>Select the downloaded image file ("2021-11-19 OpenScanPi_AP.zip"), your SD card and hit <em><u>write</u></em>.</span></p>
<p class="j1LEL va-er" dir="auto" id="2abe2" indentation="0" textstyle="[object Object]">&nbsp;</p>
<p class="j1LEL va-er" dir="auto" id="td0h" indentation="0" textstyle="[object Object]"><span><strong>Important note:</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="384dm" indentation="0" textstyle="[object Object]"><span><strong>In earlier releases, you needed to modify/add a wpa_supplicant.conf file with your wifi credentials to the boot folder of the SD card. <u>This is not the case anymore! Do not change anything on the SD card</u>! You can directly insert the card into the Raspberry Pi and start booting the device. Wifi credentials can be added in the next step.</strong></span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="370ph" indentation="0" level="3" textstyle="[object Object]"><span><strong>(2) Starting the Raspberry Pi</strong></span></h3>
<p class="j1LEL va-er" dir="auto" id="6s0vh" indentation="0" textstyle="[object Object]"><span>Connect all electronic components, insert the SD card and power your Raspberry Pi. The first boot might take several minutes. Once node-red (the browser user interface) is loaded, the ringlight LED will flash in one of the following patterns:</span></p>
<p class="j1LEL va-er" dir="auto" id="fsh77" indentation="0" textstyle="[object Object]"><span>(I) fast flashing + 1s off + 1s on + 1s off + 1s on --&gt; Access Point Mode</span></p>
<p class="j1LEL va-er" dir="auto" id="91l6e" indentation="0" textstyle="[object Object]"><span>(II) fast flashing + 1s off + 1s on --&gt; Connected to local wifi network</span></p>
<p class="j1LEL va-er" dir="auto" id="2dc4i" indentation="0" textstyle="[object Object]"><span>On first boot, there the device will enter the Access Point Mode and you should be able to see the following network <em><u>OpenScanPi</u></em> with the password <em><u>raspberry</u></em>:</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]">&nbsp;</p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta2-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="73ov6" indentation="0" textstyle="[object Object]"><span>You should be able to connect to this network with any of your devices.</span></p>
<p class="j1LEL va-er" dir="auto" id="ctp31" indentation="0" textstyle="[object Object]"><span><strong>Important note: Prior tests seemed to indicate that some devices do not like to connect to this network, but I do not know the reason yet. Please let me know if you encounter any problems!</strong></span></p>
<p class="j1LEL va-er" dir="auto" id="665sb" indentation="0" textstyle="[object Object]"><span>Once connected, you should be able to open the user interface in your browser through the following site: <a class="Y-s64 XzMaT" data-hook="WebLink" href="http://openscanpi:1880/ui" target="_blank"><u>http://openscanpi:1880/ui</u></a> (and the backend of node-red <a class="Y-s64 XzMaT" data-hook="WebLink" href="http://openscanpi:1880" target="_blank"><u>http://openscanpi:1880</u></a> for debugging)</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="9f1qc" indentation="0" level="3" textstyle="[object Object]"><span><strong>(3) Settings Menu</strong></span></h3>
<p class="j1LEL va-er" dir="auto" id="bk3vl" indentation="0" textstyle="[object Object]"><span>Your first step should be opening the settings menu, where you will find two new &amp; refined columns (<em>Network </em>and <em>OpenScancloud</em>).</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta3-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="abu40" indentation="0" textstyle="[object Object]"><span>First, choose your <em><u>OpenScan model</u></em> (left column). If you intend to use the OpenScanCloud service, please read and agree to the <em><u>Terms of Use</u></em>.</span></p>
<p class="j1LEL va-er" dir="auto" id="9ao19" indentation="0" textstyle="[object Object]"><span>In order to connect to a Wifi network, first hit <em><u>search wifi</u></em> and after a short moment a dropdown with all available networks should be visible. Choose one of the networks and enter your wifi password and two-digit country code (see <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank"><u>Wikipedia</u></a>). Once added, the pi will remember this network. You can reset ALL saved networks by hitting <em><u>reset wifi</u></em>. This will restore the access point mode with the given access point name, which can be set freely.</span></p>
<p class="j1LEL va-er" dir="auto" id="6q1gf" indentation="0" textstyle="[object Object]"><span>OpenScanCloud allows you to easily process your images and create highly detailed 3d models. In order to activate the cloud-functionality, you need to enter your token. If you do not have a token yet, you can use the register button and enter your details (name + email). I will create your personal token and send you a mail to the given address, which currently might take a few days, but I try my best :)</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="7te04" indentation="0" level="3" textstyle="[object Object]"><span><strong>(4) OpenScanCloud - Fileupload</strong></span></h3>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta4-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="ajqvb" indentation="0" textstyle="[object Object]"><span>Once you have created an image set, you can download the locally stored files by clicking on <em><u>zip</u></em>. Alternatively, you can select an image set and press <em><u>upload </u></em>in order to transfer the files to my servers for processing. Note, that this might take some time, first the image set will be prepared (split into chunks of 200mb) and then uploaded to my servers. You will receive an email with the result as soon as the processing is done.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="cl3re" indentation="0" level="3" textstyle="[object Object]"><span><strong>(5) Help texts</strong></span></h3>
<p class="j1LEL va-er" dir="auto" id="vm2s" indentation="0" textstyle="[object Object]"><span>I have started adding little help icons (" ? ") with additional information. Please let me know if you find it helpful or if you wish more or less details.</span>&nbsp;</p>
<h3 class="vGBkk sWzLp" dir="auto" id="ddpbb" indentation="0" level="3" textstyle="[object Object]"><span><strong>(6) IMPORTANT</strong></span></h3>
<p class="j1LEL va-er" dir="auto" id="9psgd" indentation="0" textstyle="[object Object]"><span>Please let me know if you encounter any problems! There will be future beta-updates, which can be installed by clicking on the <em><u>install latest beta version</u></em> on the start screen (see first image)! Do not use the regular update-routine in the <em><u>Update&amp;Info</u></em> tab as this will install the latest stable version (without OpenScanCloud + Access Point mode).</span></p>
<p class="j1LEL va-er" dir="auto" id="7mfer" indentation="0" textstyle="[object Object]"><span>I am really looking forward to pushing this release, but i definitely need your help and feedback!</span></p>
<p class="j1LEL va-er" dir="auto" id="957jg" indentation="0" textstyle="[object Object]"><span>Thank you so much for your time,</span></p>
<p class="j1LEL va-er" dir="auto" id="4ql3b" indentation="0" textstyle="[object Object]"><span>best regards,</span></p>
<p class="j1LEL va-er" dir="auto" id="d5pkk" indentation="0" textstyle="[object Object]"><span>Thomas</span></p>
