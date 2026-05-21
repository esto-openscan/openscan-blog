---
title: "Update on the upcoming OpenScan firmware release (IMX519 + other changes)"
date: "2022-01-28T12:30:00+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Firmware"
  - "Update"
image:
  path: "/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking1.webp"
redirect_from:
  - "/blogs/news/update-on-the-upcoming-openscan-firmware-release-imx519-other-changes"
  - "https://62f7a3-4.myshopify.com/blogs/news/update-on-the-upcoming-openscan-firmware-release-imx519-other-changes"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">For almost two years, I have been working on the first version of the firmware for the OpenScan Mini + Classic. And so far, I have been able to release updates, that could be easily installed through the user interface.</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="7v9lf" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">But due to two major external factors, I decided to rewrite the whole code and create a 'new' firmware (with many of the old features + some exciting new functionality). It will be necessary to flash the micro SD-card with the new image, but this should be easily doable :)</span></p>
<h3 class="vGBkk sWzLp" data-mce-fragment="1" dir="auto" id="79agi" indentation="0" level="3" textstyle="[object Object]"><span data-mce-fragment="1">Support for many more camera models</span></h3>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="3pgld" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">The first factor is, that the Raspberry Pi foundation dropped the used camera python library in favor of the libcamera framework. Generally speaking, this is a great step, as it will allow many more camera sensors to be supported. This coincided with the release of the new Arducam IMX519 camera, which I have been testing for a few weeks now. This camera needs the libcamera functionality too, and thus I have to move forward.</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="4f5cv" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">For now, this means that the following camera will be supported:</span></p>
<ul>
<li>IMX219 (pi camera v2) with 8mp</li>
<li>IMX477 (pi camera HQ) with 12mp</li>
<li>OV5647 (pi camera 1.3) with 5mp</li>
<li>IMX378 with 11mp</li>
<li>OV9271 with 1mp and global shutter</li>
<li>IMX290 with 2mp and global shutter</li>
</ul>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="6mark" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Furthermore, using the libcamera framework will allow third parties (like Arducam) to add support for their cameras too. For now, the following Arducam cameras should work too:</span></p>
<ul>
<li>IMX519 with 16mp and autofocus (definitely working, see below :)</li>
<li>AR0234 with 2.3mp and global shutter</li>
<li>IMX230 with 21mp (!!!)</li>
<li>IMX298 with 16mp and autofocus (and microphone)</li>
<li>IMX462 with 2mp (and low-light functionality)</li>
<li>OV9281 with 1mp, monochrom</li>
<li>OV2311 with 2mp global shutter</li>
</ul>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="4maf5" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">So can you see, that the overall usability is widely improved. The only shortcoming of the new libcamera framework is, that the preview is very slow at a framerate of below 1fps (which should be improved as soon as the Raspberry Pi Foundation releases their new python camera library, which is expected somewhat soonish)</span></p>
<h3 class="vGBkk sWzLp" data-mce-fragment="1" dir="auto" id="4ckuq" indentation="0" level="3" textstyle="[object Object]"><span data-mce-fragment="1">Autofocus + Focus Stacking </span></h3>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="dqbop" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">With the adjustable focus of the Arducam IMX519 it will be possible to create stacks of photos. The position of the camera remains the same and only the focal plane is shifted. In theory, this should improve the photogrammetry output for models, where depth of field is an issue and some areas are blurry in one photo. Those areas will be crisp in the next photo, and the photogrammetry software -should- be able to only use the crisp areas for reconstruction. But there is a lot of testing needed ;)</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">For the coming update, I implemented three different modes (autofocus, MF - manual focus and ST - stacking) for the adjustable-focus IMX519 sensor:</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking1-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="68uca" indentation="0" textstyle="[object Object]"><span>- autofocus (default), where you do not need to worry about setting the focus. The focus will be calculated in every position and the algorithm seems really robust. I only had some issues, when the object only covered a small part of the photo and the camera tried to focus the background instead.</span></p>
<p class="j1LEL va-er" dir="auto" id="6e8p0" indentation="0" textstyle="[object Object]"><span>- for this reason, there is the <strong>M</strong>anual <strong>F</strong>ocus mode, where you can set the focus distance manually. This value will be kept for all photos during the routine. </span></p>
<p class="j1LEL va-er" dir="auto" id="dldpe" indentation="0" textstyle="[object Object]"><span>- And finally, Stacking, where you can set a lower and upper limit for the focus distance and a number of x photos. During the routine, the camera will stop in each position and take x instead of 1 photos with varying focus (in the given range). Note, that the overall size of the image sets will be increased accordingly by a factor of x.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="5jer3" indentation="0" level="3" textstyle="[object Object]"><span>Re-adding DSLR support (with gphoto2)</span></h3>
<p class="j1LEL va-er" dir="auto" id="2tccv" indentation="0" textstyle="[object Object]"><span>This feature has already been tested a long time ago, but I did not get around to fully implement it into the firmware. So it rested in developer mode for ages... I will try my best to implement this functionality too, so that many, many DSLR cameras can be used with the official main firmware.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="5qnri" indentation="0" level="3" textstyle="[object Object]"><span>Improvements in stability + usability</span></h3>
<p class="j1LEL va-er" dir="auto" id="6jbdc" indentation="0" textstyle="[object Object]"><span>This is seems like a tiny step, but this is a thing, that gives me at least some satisfaction ^^: The user interface + backend are now accessible directly via <em>openscan </em>and <em>openscan/editor </em>respectively. (and not through openscan:1880/ui as before)</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking2-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="8qveg" indentation="0" textstyle="[object Object]"><span>A much more important improvement is the introduction of 'advanced settings' - mode, where you can access many more settings. This should make it much easier to modify and create your own hardware version:</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1"><img alt="" src="/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking3-600x600.webp"/></span></p>
<h3 class="vGBkk sWzLp" data-pm-slice="1 1 []" dir="auto" id="beqic" indentation="0" level="3" textstyle="[object Object]"><span>Cleaning the Code + Backend</span></h3>
<p class="j1LEL va-er" dir="auto" id="cu34v" indentation="0" textstyle="[object Object]"><span>For a long time, I have just kept adding and adding new features and code-snippets. And over the time, the backend (node-red) and the underlying file-structure became a huge mess. I decided to re-organize and re-write a lot of code and clean up the overall file- and code-structure. I hope, that this will help future contributions!</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><span><img alt="" src="/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking4-600x600.webp"/></span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="du5vp" indentation="0" textstyle="[object Object]"><span>There will be a dedicated update + documentation on how to use and modify the existing code at some point.</span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="c52l5" indentation="0" level="3" textstyle="[object Object]"><span>Conclusion</span></h3>
<p class="j1LEL va-er" dir="auto" id="74miu" indentation="0" textstyle="[object Object]"><span>I started this blog post with the words 'short update', but had to realize, that there have been quite a few changes already and there is even more to talk about in future posts. Please let me know if you wish any particular functionality or usability improvement!</span></p>
<p class="j1LEL va-er" dir="auto" id="534ut" indentation="0" textstyle="[object Object]"><span>If you made it that far in the text, feel free to <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://www.buymeacoffee.com/OpenScan" target="_blank"><u>support my work through a coffee or two </u></a>;)</span></p>
