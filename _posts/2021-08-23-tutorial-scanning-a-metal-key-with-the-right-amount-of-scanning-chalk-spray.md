---
title: "Tutorial - Scanning a metal key with the right amount of scanning/chalk spray"
date: "2021-08-23T09:30:00+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Tutorial"
image:
  path: "/assets/img/posts/2021-08-23-tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray/2021-08-23-scanned-keys.webp"
redirect_from:
  - "/blogs/news/tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray"
  - "https://62f7a3-4.myshopify.com/blogs/news/tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">As soon as you get into photogrammetry, you will encounter certain surface types and materials that are not as easy to scan as others. Very often, people blame their photogrammetry software, but I have found that most programs are able to deliver similar outputs (as soon as the input is fine).</span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="em5op" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">A metal key is a prime example of a difficult-to-scan object, as it is both glossy and unicolor.&nbsp;</span><span data-mce-fragment="1">Anyway, it is possible to get quite decent results with photogrammetry, when you follow some basic rules...</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-08-23-tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray/2021-08-23-scanned-keys1-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="cp5ac" indentation="0" textstyle="[object Object]"><span>This one is an allegedly 3d-printing-proof security key and as shown in some recent postings on Instagram and YouTube, it is easily possible to print a working copy on sub 200&euro; 3d printer. Unfortunately, this possibility is widely ignored by manufacturers and so far I only encountered one key, that I haven't been able to copy.</span></p>
<h2 class="RwFIZ sWzLp" data-pm-slice="1 1 []" dir="auto" id="18lub" indentation="0" level="2" textstyle="[object Object]"><span>Scanning Metal and Plastic (unicolor + glossiness)</span></h2>
<p class="j1LEL va-er" dir="auto" id="8l71k" indentation="0" textstyle="[object Object]"><span>Metal and plastic are two very prominent examples of hard to scan materials, as the surface has two challenging properties:</span></p>
<ul>
<li>unicolor - Most plastic and metal parts have very unicolor surfaces/areas. Even if the object seems to have surface texture like for instance the layers of a 3d printed part, the truth is that it is all just one color. The perceived texture comes from varying reflections, which will confuse any photogrammetry software!</li>
<li>glossiness - glossy/reflective surfaces create highlights that change position when the camera/object/light is moved. These highlights will be recognized by any photogrammetry software and will make the reconstruction quite difficult.</li>
</ul>
<div class="j1LEL va-er" data-mce-style="text-align: center;" dir="auto" id="21pk1" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>Generally speaking, the software tries to find tiny recognizable dots in each image, which are usually not present on plastic and metal.</strong></span></div>
<p class="j1LEL va-er" dir="ltr" indentation="0" textstyle="[object Object]">&nbsp;</p>
<p class="j1LEL va-er" dir="ltr" id="d7pi5" indentation="0" textstyle="[object Object]"><span dir="auto">Note, that even if a plastic object consists of several different colored areas, those areas themselves are still unicolor and thus will not be picked up be the software.</span></p>
<h2 class="RwFIZ sWzLp" data-pm-slice="1 1 []" dir="auto" id="145iq" indentation="0" level="2" textstyle="[object Object]"><span>The Solutions - Chalk Spray + Cross-polarization</span></h2>
<p class="j1LEL va-er" dir="auto" id="4bpp2" indentation="0" textstyle="[object Object]"><span>So we need some kind of artificial features/dots. I have seen many people and even several tutorials using a pen to create such distinct features. The principal idea is okay, but consider the following: </span></p>
<div class="j1LEL va-er" data-mce-style="text-align: center;" dir="auto" id="3taho" indentation="0" style="text-align: center;" textstyle="[object Object]">&nbsp;<span><strong>photogrammetry software needs 10.000+ distinct features in each photo</strong></span>
</div>
<p class="j1LEL va-er" dir="ltr" indentation="0" textstyle="[object Object]">&nbsp;</p>
<p class="j1LEL va-er" dir="ltr" id="r8cg" indentation="0" textstyle="[object Object]"><span dir="auto">The best way of creating such number of random features is the use of chalk or dedicated scanning spray. Try to spray the object from all sides. Most importantly try to avoid covering areas 100% as this would be a new unicolor surface with the same problem, we try to solve. Just to make one thing clear:</span></p>
<div class="j1LEL va-er" data-mce-style="text-align: center;" dir="ltr" id="dshks" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>It takes quite some time and practice to get the surface of the object right. Take your time as this step is crucial for the outcome of the reconstruction.</strong></span></div>
<p class="j1LEL va-er" dir="ltr" indentation="0" textstyle="[object Object]">&nbsp;</p>
<p class="j1LEL va-er" dir="ltr" id="7l8gf" indentation="0" textstyle="[object Object]"><span dir="auto">Here you can see one of the photos from the above-mentioned photo set. See how I evenly coated the surface. Therefore, I hold the spray can 50-70cm away from the object which I hold in my other hand and apply the coating in short bursts.</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2021-08-23-tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray/2021-08-23-scanned-keys2-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="372sg" indentation="0" textstyle="[object Object]"><span>The photos were taken with the <a data-mce-href="www.openscan.eu/openscan-mini" href="www.openscan.eu/openscan-mini" title="OpenScan Mini"><u>OpenScan Mini</u></a>. You can see the structure of the scanner in the background. </span></p>
<p class="j1LEL va-er" dir="auto" id="6s4bb" indentation="0" textstyle="[object Object]"><span>Note, that there are no distinct spots or dots in the background, which was achieved by the use of a cross-polarization setup as included in the kit.</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><img alt="" src="/assets/img/posts/2021-08-23-tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray/2021-08-23-scanned-keys3-600x600.webp"/></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="8jdvj" indentation="0" textstyle="[object Object]"><span>There are two noteworthy issues:</span></p>
<ul>
<li>the reflections on the surface of the key lead to unwanted "features", which will either throw off the software completely or at least will create some kind of noise in the resulting model</li>
<li>the reflections in the background might get interpreted as well, lowering the reconstruction quality.</li>
</ul>
<p class="j1LEL va-er" dir="auto" id="44ibo" indentation="0" textstyle="[object Object]"><span>It is still possible to get a decent model, but the overall quality will be significantly less and/or you will need much more photos. I was able to get a decent result with cross-polarization and only 40 photos. In order to get a similar result without polarizer, I needed at least 150 photos...</span>&nbsp;</p>
<div class="j1LEL va-er" data-mce-style="text-align: center;" dir="auto" id="sjl8" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>In Short: Chalk spray or similar is an absolute must for unicolor materials</strong></span></div>
<div class="j1LEL va-er" data-mce-style="text-align: center;" dir="auto" id="7o15i" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong>cross-polarization is optional but helps a lot</strong></span></div>
<div class="j1LEL va-er" data-mce-style="text-align: center;" dir="auto" indentation="0" style="text-align: center;" textstyle="[object Object]"><span><strong></strong></span></div>
<div class="j1LEL va-er" data-mce-style="text-align: left;" dir="auto" indentation="0" style="text-align: center;" textstyle="[object Object]">
<h2 class="RwFIZ sWzLp" data-pm-slice="1 1 []" dir="auto" indentation="0" level="2" textstyle="[object Object]">
<span></span><span>Bonus</span>
</h2>
<p class="j1LEL va-er" dir="auto" id="60lcc" indentation="0" textstyle="[object Object]"><span>See how different programs did a similar job and produced usable outputs from only 50 photos (with chalk spray + cross-polarizer setup):</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><span><img src="/assets/img/posts/2021-08-23-tutorial-scanning-a-metal-key-with-the-right-amount-of-scanning-chalk-spray/2021-08-23-scanned-keys-600x600.webp" style="float: none;"/></span></p>
<p class="j1LEL va-er" data-mce-style="text-align: center;" data-pm-slice="1 1 []" dir="auto" id="dnf7a" indentation="0" style="text-align: center;" textstyle="[object Object]"><span>Meshroom - Reality Capture - ObjectCapture API</span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="4ppld" indentation="0" textstyle="[object Object]"><span>I hope you like this kind of short tutorial, please feel free to share your thoughts and if you want me to cover any particular topic, reach out :)</span></p>
<p class="j1LEL va-er" dir="auto" id="c49qd" indentation="0" textstyle="[object Object]">&nbsp;And if you made it that far through the text, feel free to share it and/or support the OpenScan project&nbsp;by <a href="https://www.patreon.com/OpenScan" target="_blank" title="Support OpenScan on Patreon">becoming a Patreon</a></p>
<p class="j1LEL va-er" dir="auto" id="61bsq" indentation="0" textstyle="[object Object]"><span>Best,</span></p>
<p class="j1LEL va-er" dir="auto" id="faksb" indentation="0" textstyle="[object Object]"><span>Thomas</span></p>
</div>
