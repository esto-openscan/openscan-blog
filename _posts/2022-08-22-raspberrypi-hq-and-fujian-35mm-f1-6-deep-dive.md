---
title: "RaspberryPi HQ and Fujian 35mm f1.6 deep dive"
date: "2022-08-22T13:30:00+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "Experiment"
  - "News"
image:
  path: "/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-09.webp"
redirect_from:
  - "/blogs/news/raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive"
  - "https://62f7a3-4.myshopify.com/blogs/news/raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive"
---

<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" id="foo" indentation="0" textstyle="[object Object]"><strong>by MichaelX</strong></p>
<p class="j1LEL va-er" data-mce-fragment="1" data-pm-slice="1 1 []" dir="auto" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">In my&nbsp;blog article&nbsp;I talked about the reasons for building an <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-fragment="1" data-mce-href="https://en.openscan.eu/openscan-classic" href="https://en.openscan.eu/openscan-classic" target="_blank"><u data-mce-fragment="1">OpenScan classic</u></a> with an RPi HQ camera. I also showed a bit of the increase in quality and sharpness of the scans. </span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="317dc" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">I sort of glossed over the whole project because I knew there was no way of including everything I want to talk about in one blog post while also keeping most of you reading until the end. That&rsquo;s why, very early in writing the first blog post, I decided to make a series of articles. This is the second article, a deep dive in the pro&rsquo;s and con&rsquo;s of the 35&nbsp;mm 1.6f Fujian lens!</span></p>
<h3 class="vGBkk sWzLp" data-mce-fragment="1" dir="auto" id="foih4" indentation="0" level="3" textstyle="[object Object]"><span data-mce-fragment="1">What constitutes a good photogrammetry image set?</span></h3>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="6305b" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Now, let's take a few steps back. What constitutes a good photogrammetry image set for say a miniature? Most articles many of us have read state something along these lines:</span></p>
<ol>
<li>A dark or contrasting background</li>
<li>Enough depth of field to have the model in focus, but not too much to keep the background out of focus.</li>
<li>Use the highest resolution possible.</li>
<li>Each point of the model surface should be clearly visible in at least two high quality images. On OpenScan 150 to 200 images usually suffices! Any more just means more processing time. Anything less could mean loss of detail, but your mileage might vary.</li>
<li>Always move around the object circularly when taking photos.</li>
<li>Do not change view point more than 30 degrees.</li>
</ol>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="fmgre" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Many of the items you&rsquo;ll find online are covered by the OpenScan hardware, and software, and are not part of these blogs. The ones we care about right now are 2, 3 and 4. </span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="2g6ka" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Highest resolution, as I talked about in the previous post, is one of the main reasons for doing what I&rsquo;m doing. Getting most of the object I want to scan onto the camera's sensor! </span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="6hk3t" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">Item 2 and 3 however, getting two or more high quality pictures of every part of the model and getting a perfect DOF, are not as easy as they seem. There are so many variables that come into play, when using the setup I&rsquo;m using, that affect image and thus mesh quality, they are worthy of their own time in the spotlight. I&rsquo;m not talking about setup of the scanner (though that is very important) but things that affect image quality, for example:</span></p>
<ol>
<li>Distance between object and camera</li>
<li>Aperture</li>
<li>Focus</li>
<li>Exposure</li>
<li>ISO (though we have no control over that within OpenScan software)</li>
<li>Use of Macro extension tubes, filters, macro lenses, &hellip;</li>
<li>Sensor size/crop factor (though honestly, I know little about this)</li>
<li>DOF</li>
</ol>
<h3 class="vGBkk sWzLp" data-mce-fragment="1" dir="auto" id="94et" indentation="0" level="3" textstyle="[object Object]"><span data-mce-fragment="1">What is DOF?</span></h3>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="afl53" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">DOF, or Depth of Field, is a range of distances from your lens outward that are in focus. With a large DOF the entire picture is in focus, this is often used in landscape photography. Narrow DOF is often used in macro and portrait photography to isolate the object from the background. When using a specific lens/camera combo, you can only manipulate DOF by changing the aperture. Lowering the aperture number opens the iris in the lens. Increasing aperture numbers closes the aperture in the lens. </span></p>
<p class="j1LEL va-er" data-mce-fragment="1" dir="auto" id="100j6" indentation="0" textstyle="[object Object]"><span data-mce-fragment="1">A picture speaks a thousand words, so here is a visual representation of DOF.</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-01-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="rtl" id="5jal2" indentation="0" textstyle="[object Object]"><span dir="auto"><span data-font-size="14"><em>Image credit: https://photographylife.com/what-is-depth-of-field</em></span></span></p>
<div dir="ltr">
<blockquote class="_-2S60" id="d6b5l" indentation="0" paragraphid="2sguc275" textstyle="[object Object]"><strong><span dir="auto">DOF encompasses a lot more than what i'm covering, if you want to know more, <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://photographylife.com/what-is-depth-of-field" href="https://photographylife.com/what-is-depth-of-field" target="_blank"><u>this site</u></a> explains nicely!<br id=""/></span></strong></blockquote>
</div>
<p class="j1LEL va-er" dir="auto" id="clutt" indentation="0" textstyle="[object Object]"><span>Another thing that affects DOF is using macro extension tubes. Having one, or more, macro tubes means your MOD, or minimal object distance, lowers significantly. This allows you to physically move closer to an object and still be able to focus. It also means your maximum focal distance decreases from infinity to&hellip; well not infinity and your DOF will also get more and more narrow. </span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="9lv2" indentation="0" level="3" textstyle="[object Object]"><span>The Fujian 35&nbsp;mm f1.6...</span></h3>
<p class="j1LEL va-er" dir="auto" id="a5j2e" indentation="0" textstyle="[object Object]"><span>When looking for proper lenses to use with the <a class="Y-s64 XzMaT" data-hook="WebLink" data-mce-href="https://en.openscan.eu/openscan-classic" href="https://en.openscan.eu/openscan-classic" target="_blank"><u>OpenScan classic</u></a>, I was overwhelmed with a lot of technical details. I know the basics from when I learned how to use my DSLR, but nowhere near enough to know what kind of lenses would work with photogrammetry and how macro extensions and different image sensor sizes would affect image quality. Even after reading many sites and explanations, I still found it hard to extrapolate that to photogrammetry setups, where you want to be up close and personal with the model. I chose the 35&nbsp;mm Fujian pretty randomly based on some reviews online. These are the "Features" stated on the seller's website:</span></p>
<div dir="auto">
<pre class="CRU7E Q8Dcg" id="aq39k" style="padding-left: 30px;" textstyle="[object Object]">Mount type: C mount
Focal Length: 35mm
Aperture: F1.6-C
Angle of view: 18
Aperture blades: Four groups Four Blades
Frame:APS-C
lens Coating:MC Multilevel
Lens Size:37mm
Iris &amp; Focus Operation: Manual
Minimum Object Distance (M.O.D.): 30cm
Focus: focus to infinity
Image plane size (Format): 1 / 2 inch</pre>
</div>
<p class="j1LEL va-er" dir="auto" id="8735l" indentation="0" textstyle="[object Object]"><span>Now, these stats should be taken with some huge grains of salt. Especially the MOD is not 30&nbsp;cm but 50&nbsp;cm, and the sensor format is NOT 1/2. If used on my Canon, I will definitely get vignetting at some point. However, it's still a great cheap lens.</span></p>
<h3 class="vGBkk sWzLp" data-pm-slice="1 1 []" dir="auto" id="bqsu9" indentation="0" level="3" textstyle="[object Object]"><span>Testing MOD (Minimal object distance) and DOF!</span></h3>
<p class="j1LEL va-er" dir="auto" id="94hi1" indentation="0" textstyle="[object Object]"><span>With the extension tubes ready, I started experimenting. At first, I tried using the lens without any extension tubes. Well, technically I used one, but that was needed because it's a C lens on a CS mount camera. </span></p>
<p class="j1LEL va-er" dir="auto" id="fl4nr" indentation="0" textstyle="[object Object]"><span>I could not focus on the model at 24&nbsp;cm distance, but the RPI HQ does have a "backplane focus ring" that acts as a variable extension tube. The BFL, or backplane focal length, is intended to overcome differences in lens designs. It can be extended to about 5mm before you don't have enough threads to keep is securely in place. I wanted to know if I could get the lens to focus at 24cm without a macro tube. The lens was able to focus when the backplane focus ring was extended about 3mm. Below is a table of all the tests I did with a superglue bottle cap. </span></p>
<p class="j1LEL va-er" dir="auto" id="epdmv" indentation="0" textstyle="[object Object]"><span>The only variables for each set are the relation between aperture and exposure.</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><span><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-02-600x600.webp" style="display: block; margin-left: auto; margin-right: auto;"/></span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="d1f9g" indentation="0" textstyle="[object Object]"><span>As you can see, as the aperture increases, the iris in the camera gets smaller and thus longer exposure times are needed. </span></p>
<p class="j1LEL va-er" dir="auto" id="4h9k2" indentation="0" textstyle="[object Object]"><span>These are the image results, top row is picture 1 and 2, bottom row is 3 and 4:</span></p>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-03-600x600.webp" style="float: none;"/></div>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-04-600x600.webp" style="float: none;"/></div>
<div style="text-align: center;"><img src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-05-600x600.webp" style="float: none;"/></div>
<div style="text-align: center;"><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-06-600x600.webp" style="float: none;"/></div>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="7pct7" indentation="0" textstyle="[object Object]"><span><em>Side note, there was a spec of dust on my sensor that has since been removed, sorry about that. Also, I don't really know what happened with D3 and D4, but they are clearly useless! </em></span></p>
<p class="j1LEL va-er" dir="auto" id="2o8sq" indentation="0" textstyle="[object Object]"><span>As you can see from the image sets, increasing the aperture number results in more of the bottle cap to be in focus. They also show the effect of the macro rings to an extent. Without a macro ring, or with a 3mm macro ring to be exact, I could just about focus at 24cm distance. With only one ring, I had to set my focus ring from 0.5m to 1m to get the model in focus. I could also move the object to about 20 cm and still get it to focus. I could still get a little closer with these settings, but not to the minimal distance my setup allows, being 15cm. With two macro rings I could focus the model at 15cm, but not much more than that and at a cost of a very narrow DOF and loss of quality. </span></p>
<p class="j1LEL va-er" dir="auto" id="fomeu" indentation="0" textstyle="[object Object]"><span>It seems like one 5mm ring is the sweet spot for this lens. With that in mind, I wanted to figure out what the actual DOF would be. Since I am still clueless to the actual science behind it, I figured another test was in order. I decided to create a tool that has 2mm increments forward and backwards and see what DOF would be like. </span></p>
<h3 class="vGBkk sWzLp" dir="auto" id="3b5rf" indentation="0" level="3" textstyle="[object Object]"><span>How do you test DOF easlily? Create a tool of course! </span></h3>
<p class="j1LEL va-er" dir="auto" id="6i07b" indentation="0" textstyle="[object Object]"><span>This is the backwards DOF, on the back it has the positive values. The model is mounted on a pin that is in the middle of the 0mm block on both sides, ensuring distances are correct on both sides.</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><span><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-07-600x600.webp" style="display: block; margin-left: auto; margin-right: auto;"/></span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="7vda0" indentation="0" textstyle="[object Object]"><span>I printed it in resin to get the cleanest result with as little deviation as possible. </span></p>
<p class="j1LEL va-er" dir="auto" id="5t0kd" indentation="0" textstyle="[object Object]"><span>Since I got the best results with one macro ring, I figured I would only test with one ring for now. These four images were taken, same apertures as the previous set but slightly different distances and exposure settings and one macro ring.</span></p>
<p class="j1LEL va-er" dir="auto" id="fmfin" indentation="0" textstyle="[object Object]">&nbsp;<img alt="" data-mce-fragment="1" data-mce-src="https://cdn.shopify.com/s/files/1/0810/2327/1257/files/2022-08-22_Fujian_Deepdive_08_600x600.webp?v=1710332410" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-08-600x600.webp" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="em170" indentation="0" textstyle="[object Object]"><span>Unfortunately, the 35mm would not allow me to get the -16mm tab fully in the frame, but there's enough of it visible to see the sharpness of it. As you can clearly see, DOF in the f1.6 image is about 6mm (-3mm to +3mm as the image only shows negative DOF). It slowly increases until at f11, where the -16mm tab becomes pretty sharp. I assume at f11 we are looking at a DOF of about 32 to 35mm. Since I got this lens to mostly scan small sub 10mm objects, I can probably get away with ~f5.6 or even f2.8!</span></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" indentation="0" textstyle="[object Object]"><span>Happy with my test item I got curious to see how they would look like as a mesh! So I ran the scans and processed them using the free <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://github.com/OpenScan-org/OpenScanCloud" target="_blank"><u>OpenScanCloud</u></a>. In the future, I might do an update where I process them with Agisoft Metashape, but I figured running them all through the same software would be the most important part. </span></p>
<p class="j1LEL va-er" dir="auto" id="9o7lj" indentation="0" textstyle="[object Object]"><span>As you can see in the previous image, I did not have a black backdrop, and I think that's affected at least the f1.6 scan.</span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><span>These are the results, in the same order as the previous picture: </span></p>
<p class="j1LEL va-er" dir="auto" indentation="0" textstyle="[object Object]"><img alt="" src="/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-09-600x600.webp" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p class="j1LEL va-er" data-pm-slice="1 1 []" dir="auto" id="fonr" indentation="0" textstyle="[object Object]"><span>I was NOT expecting these results! While using the <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://en.openscan.eu/openscan-mini" target="_blank"><u>OpenScan Mini</u></a> I noticed not all the parts of the model being in focus all the time, but it still got good results. I did not expect DOF to affect the meshes to this extent. That said, while the picture of the f2.8 image clearly shows sharpness deteriorating at -6mm, the mesh is still fairly good at -8mm. This implies there is a limit to how out of focus parts of the model can become before they get fuzzy in the mesh. </span></p>
<p class="j1LEL va-er" dir="auto" id="93vmf" indentation="0" textstyle="[object Object]"><span>Well, I knew there would be a lot of variables in this project I have started on, but there is clearly more to be tested and more to be explored! </span></p>
<p class="j1LEL va-er" dir="auto" id="4141s" indentation="0" textstyle="[object Object]"><span>In the next article, I will talk about two new lenses I have bought. They have MUCH lower focal length of 3.2mm and 8mm instead of the 35mm lens used in this article. I chose those lenses because the Arducam IMX519 used on the <a class="Y-s64 XzMaT" data-hook="WebLink" href="https://en.openscan.eu/openscan-mini" target="_blank"><u>OpenScan Mini</u></a> has a focal length of 4.28mm and I wanted something similar. Again, there are a lot more variables that impact focal length (like crop factor, which I still not grasp fully) but with these lenses being so cheap (about 25 euros each) it won't break the bank and I can use them as cheap fun lenses on my DLSR if nothing else. In fact, I might get some more, probably a 16mm at least. </span></p>
<p class="j1LEL va-er" dir="auto" id="4kdga" indentation="0" textstyle="[object Object]">&nbsp;<span>Once again, stay tuned and see you soon! </span></p>
<p class="j1LEL va-er" dir="auto" id="5dm07" indentation="0" textstyle="[object Object]">&nbsp;</p>
