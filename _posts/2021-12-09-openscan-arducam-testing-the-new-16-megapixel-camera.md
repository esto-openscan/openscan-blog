---
title: "OpenScan + Arducam - testing the new 16 Megapixel camera"
date: "2021-12-09T11:30:00+01:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "News"
  - "Update"
image:
  path: "/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam04.webp"
redirect_from:
  - "/blogs/news/openscan-arducam-testing-the-new-16-megapixel-camera"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan-arducam-testing-the-new-16-megapixel-camera"
---

After sticking to the Pi Camera for a long time, finally, there seems to be a very promising alternative featuring twice the resolution and built-in autofocus capabilities: The Arducam 16MP camera. I got lucky being able to test this new camera...

[Arducam](https://www.arducam.com/)is a well-established open-source hardware specialist from China, who is currently running a [Kickstarter campaign](https://www.kickstarter.com/projects/arducam/high-resolution-autofocus-camera-module-for-raspberry-pi) featuring a new 16 megapixel camera. The camera does not only exceed both the Pi Camera v2.1 and even the HQ camera in resolution, but also has built-in autofocus and comes at an amazing price of ~14€, during the Kickstarter and ~22€ after the campaign. The camera is fully compatible with the Raspberry Pi, so I got super excited...

See the following comparison (source image in [Kickstarter campaign](https://www.kickstarter.com/projects/arducam/high-resolution-autofocus-camera-module-for-raspberry-pi))

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam01-600x600.webp)

A note on Crowdfunding campaigns - before taking part in any campaign as a backer, please read T&Cs. Rewards aren’t guaranteed! And it is very important to do your own research on the project and companies involved!

Anyway, as Arducam is a well-established company, I reached out and Lee immediately responded and shipped a sample. It took only three days between first mail and having the product in my hand, which is remarkable!

After I got the package, I immediately had to mount the camera to the [OpenScan Mini](https://en.openscan.eu/openscan-mini) and everything fits perfectly as the footprint of the pcb is the same as the Pi Camera v2.1! Note, that the camera module is slightly thicker due to the autofocus mechanism.

It became time to start coding, which I was a little afraid of... But following [Arducams clear instructions](https://www.arducam.com/docs/cameras-for-raspberry-pi/raspberry-pi-libcamera-guide/#how-to-install-libcamera-d9f38d46-8576-43e2-9375-e225c272095f), it took only 10 minutes to create the first image! I continued playing around with the autofocus feature and testing some individual settings (like fixing exposure) and I became more and more excited as the overall image quality seemed superb.

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam02-600x600.webp)

left: pi camera v2.1 - right: Arducam 16mp IMX519 (note that I had to re-coat the model as the Aesub scanning spray vanished in the meantime)

I used [this 3d printed rook](https://www.thingiverse.com/thing:3962430) scaled to 50mm height. This thing has so many tiny features! The difference in resolution is much more obvious when you look at some of those details, like the stairs:

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam03-600x600.webp)

In order to use the camera with the OpenScan Mini, I quickly modified the firmware. It did not even take an hour to get the camera to run as part of the scan routine and show a preview in the browser interface. So, 3d scanning should reveal the full potential of this camera.

I took a total of 150 images and uploaded those to the [OpenScanCloud](https://github.com/OpenScanEu/OpenScanCloud) for processing. I will let the results speak for themselves (left pi camera v2.1 and right Arducam 16mp):

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam04-600x600.webp)

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam05-600x600.webp)

And some close-ups of the Arducam-result:

The original .stl file (left) has some mesh artifacts (large facets), which are visible in the scan result (area right of the letter 's'):

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam06-600x600.webp)

You can even see the individual pixels from the resin printer's LCD screen (most visible under the stairs and next to the letter 'E'):

![](/assets/img/posts/2021-12-09-openscan-arducam-testing-the-new-16-megapixel-camera/2021-12-01-arducam07-600x600.webp)

Note, that the 3d printer Photon Mono has a pixel size of only 50 micron...

As always, you can inspect the 3d model on [Sketchfab](https://skfb.ly/orHKG).

Conclusion:

I will definitely incorporate the camera into the OpenScan Firmware. Both, the increased resolution and thus accuracy, and the autofocus of the camera, are two major improvements to the machine. Especially the OpenScan Classic could hugely benefit from the autofocus, as setting the focus of the pi camera v2.1 manually can be quite a pain ...

I will try to get my hands on more of these cameras, so that I can add it to the [OpenScan Shop](https://openscan.eu/shop) as soon as possible.

If you agree with me about the potential of this camera, you might consider [supporting Arducam on Kickstarter](https://www.kickstarter.com/projects/arducam/high-resolution-autofocus-camera-module-for-raspberry-pi/description)!

And finally, Thank you Lee and the whole Arducam team for making such a great product! Good luck with the campaign and any future work.

Best Regards,

Thomas
