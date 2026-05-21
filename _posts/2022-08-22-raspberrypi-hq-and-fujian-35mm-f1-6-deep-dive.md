---
title: "RaspberryPi HQ and Fujian 35mm f1.6 deep dive"
date: "2022-08-22T13:30:00+02:00"
author: "Thomas Megel"
legacy: true
categories:
  - "Research"
tags:
  - "photogrammetry"
  - "depth-of-field"
image:
  path: "/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-09.webp"
redirect_from:
  - "/blogs/news/raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive"
  - "https://62f7a3-4.myshopify.com/blogs/news/raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive"
---

**by MichaelX**

In my blog article I talked about the reasons for building an [OpenScan classic](https://en.openscan.eu/openscan-classic) with an RPi HQ camera. I also showed a bit of the increase in quality and sharpness of the scans.

I sort of glossed over the whole project because I knew there was no way of including everything I want to talk about in one blog post while also keeping most of you reading until the end. That’s why, very early in writing the first blog post, I decided to make a series of articles. This is the second article, a deep dive in the pro’s and con’s of the 35 mm 1.6f Fujian lens!

### What constitutes a good photogrammetry image set?

Now, let's take a few steps back. What constitutes a good photogrammetry image set for say a miniature? Most articles many of us have read state something along these lines:

1. A dark or contrasting background
2. Enough depth of field to have the model in focus, but not too much to keep the background out of focus.
3. Use the highest resolution possible.
4. Each point of the model surface should be clearly visible in at least two high quality images. On OpenScan 150 to 200 images usually suffices! Any more just means more processing time. Anything less could mean loss of detail, but your mileage might vary.
5. Always move around the object circularly when taking photos.
6. Do not change view point more than 30 degrees.

Many of the items you’ll find online are covered by the OpenScan hardware, and software, and are not part of these blogs. The ones we care about right now are 2, 3 and 4.

Highest resolution, as I talked about in the previous post, is one of the main reasons for doing what I’m doing. Getting most of the object I want to scan onto the camera's sensor!

Item 2 and 3 however, getting two or more high quality pictures of every part of the model and getting a perfect DOF, are not as easy as they seem. There are so many variables that come into play, when using the setup I’m using, that affect image and thus mesh quality, they are worthy of their own time in the spotlight. I’m not talking about setup of the scanner (though that is very important) but things that affect image quality, for example:

1. Distance between object and camera
2. Aperture
3. Focus
4. Exposure
5. ISO (though we have no control over that within OpenScan software)
6. Use of Macro extension tubes, filters, macro lenses, …
7. Sensor size/crop factor (though honestly, I know little about this)
8. DOF

### What is DOF?

DOF, or Depth of Field, is a range of distances from your lens outward that are in focus. With a large DOF the entire picture is in focus, this is often used in landscape photography. Narrow DOF is often used in macro and portrait photography to isolate the object from the background. When using a specific lens/camera combo, you can only manipulate DOF by changing the aperture. Lowering the aperture number opens the iris in the lens. Increasing aperture numbers closes the aperture in the lens.

A picture speaks a thousand words, so here is a visual representation of DOF.

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-01-600x600.webp)

*Image credit: https://photographylife.com/what-is-depth-of-field*

> **DOF encompasses a lot more than what i'm covering, if you want to know more, [this site](https://photographylife.com/what-is-depth-of-field) explains nicely!**

Another thing that affects DOF is using macro extension tubes. Having one, or more, macro tubes means your MOD, or minimal object distance, lowers significantly. This allows you to physically move closer to an object and still be able to focus. It also means your maximum focal distance decreases from infinity to… well not infinity and your DOF will also get more and more narrow.

### The Fujian 35 mm f1.6...

When looking for proper lenses to use with the [OpenScan classic](https://en.openscan.eu/openscan-classic), I was overwhelmed with a lot of technical details. I know the basics from when I learned how to use my DSLR, but nowhere near enough to know what kind of lenses would work with photogrammetry and how macro extensions and different image sensor sizes would affect image quality. Even after reading many sites and explanations, I still found it hard to extrapolate that to photogrammetry setups, where you want to be up close and personal with the model. I chose the 35 mm Fujian pretty randomly based on some reviews online. These are the "Features" stated on the seller's website:

<div>
<pre>Mount type: C mount
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

Now, these stats should be taken with some huge grains of salt. Especially the MOD is not 30 cm but 50 cm, and the sensor format is NOT 1/2. If used on my Canon, I will definitely get vignetting at some point. However, it's still a great cheap lens.

### Testing MOD (Minimal object distance) and DOF!

With the extension tubes ready, I started experimenting. At first, I tried using the lens without any extension tubes. Well, technically I used one, but that was needed because it's a C lens on a CS mount camera.

I could not focus on the model at 24 cm distance, but the RPI HQ does have a "backplane focus ring" that acts as a variable extension tube. The BFL, or backplane focal length, is intended to overcome differences in lens designs. It can be extended to about 5mm before you don't have enough threads to keep is securely in place. I wanted to know if I could get the lens to focus at 24cm without a macro tube. The lens was able to focus when the backplane focus ring was extended about 3mm. Below is a table of all the tests I did with a superglue bottle cap.

The only variables for each set are the relation between aperture and exposure.

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-02-600x600.webp)

As you can see, as the aperture increases, the iris in the camera gets smaller and thus longer exposure times are needed.

These are the image results, top row is picture 1 and 2, bottom row is 3 and 4:

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-03-600x600.webp)

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-04-600x600.webp)

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-05-600x600.webp)

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-06-600x600.webp)

*Side note, there was a spec of dust on my sensor that has since been removed, sorry about that. Also, I don't really know what happened with D3 and D4, but they are clearly useless!*

As you can see from the image sets, increasing the aperture number results in more of the bottle cap to be in focus. They also show the effect of the macro rings to an extent. Without a macro ring, or with a 3mm macro ring to be exact, I could just about focus at 24cm distance. With only one ring, I had to set my focus ring from 0.5m to 1m to get the model in focus. I could also move the object to about 20 cm and still get it to focus. I could still get a little closer with these settings, but not to the minimal distance my setup allows, being 15cm. With two macro rings I could focus the model at 15cm, but not much more than that and at a cost of a very narrow DOF and loss of quality.

It seems like one 5mm ring is the sweet spot for this lens. With that in mind, I wanted to figure out what the actual DOF would be. Since I am still clueless to the actual science behind it, I figured another test was in order. I decided to create a tool that has 2mm increments forward and backwards and see what DOF would be like.

### How do you test DOF easlily? Create a tool of course!

This is the backwards DOF, on the back it has the positive values. The model is mounted on a pin that is in the middle of the 0mm block on both sides, ensuring distances are correct on both sides.

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-07-600x600.webp)

I printed it in resin to get the cleanest result with as little deviation as possible.

Since I got the best results with one macro ring, I figured I would only test with one ring for now. These four images were taken, same apertures as the previous set but slightly different distances and exposure settings and one macro ring.

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-08-600x600.webp)

Unfortunately, the 35mm would not allow me to get the -16mm tab fully in the frame, but there's enough of it visible to see the sharpness of it. As you can clearly see, DOF in the f1.6 image is about 6mm (-3mm to +3mm as the image only shows negative DOF). It slowly increases until at f11, where the -16mm tab becomes pretty sharp. I assume at f11 we are looking at a DOF of about 32 to 35mm. Since I got this lens to mostly scan small sub 10mm objects, I can probably get away with ~f5.6 or even f2.8!

Happy with my test item I got curious to see how they would look like as a mesh! So I ran the scans and processed them using the free [OpenScanCloud](https://github.com/OpenScan-org/OpenScanCloud). In the future, I might do an update where I process them with Agisoft Metashape, but I figured running them all through the same software would be the most important part.

As you can see in the previous image, I did not have a black backdrop, and I think that's affected at least the f1.6 scan.

These are the results, in the same order as the previous picture:

![](/assets/img/posts/2022-08-22-raspberrypi-hq-and-fujian-35mm-f1-6-deep-dive/2022-08-22-fujian-deepdive-09-600x600.webp)

I was NOT expecting these results! While using the [OpenScan Mini](https://en.openscan.eu/openscan-mini) I noticed not all the parts of the model being in focus all the time, but it still got good results. I did not expect DOF to affect the meshes to this extent. That said, while the picture of the f2.8 image clearly shows sharpness deteriorating at -6mm, the mesh is still fairly good at -8mm. This implies there is a limit to how out of focus parts of the model can become before they get fuzzy in the mesh.

Well, I knew there would be a lot of variables in this project I have started on, but there is clearly more to be tested and more to be explored!

In the next article, I will talk about two new lenses I have bought. They have MUCH lower focal length of 3.2mm and 8mm instead of the 35mm lens used in this article. I chose those lenses because the Arducam IMX519 used on the [OpenScan Mini](https://en.openscan.eu/openscan-mini) has a focal length of 4.28mm and I wanted something similar. Again, there are a lot more variables that impact focal length (like crop factor, which I still not grasp fully) but with these lenses being so cheap (about 25 euros each) it won't break the bank and I can use them as cheap fun lenses on my DLSR if nothing else. In fact, I might get some more, probably a 16mm at least.

Once again, stay tuned and see you soon!
