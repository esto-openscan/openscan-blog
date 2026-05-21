---
title: "Short Review - New Arducam TOF sensor (Kickstarter)"
date: "2022-09-26T13:30:00+02:00"
author: "Thomas Megel"
legacy: true
categories:
  - "News"
tags:
  - "makerfaire"
  - "arducam"
  - "time-of-flight"
image:
  path: "/assets/img/posts/2022-09-26-short-review-new-arducam-tof-sensor-kickstarter/2022-09-26-arducam-tof2.webp"
redirect_from:
  - "/blogs/news/short-review-new-arducam-tof-sensor-kickstarter"
  - "https://62f7a3-4.myshopify.com/blogs/news/short-review-new-arducam-tof-sensor-kickstarter"
---

tldr; Till the end of September, you can get the [new Arducam TOF camera on Kickstarter*](https://www.kickstarter.com/projects/arducam/time-of-flight-tof-camera-for-raspberry-pi?ref=4apsz7), where you can now get the device for ~US$30 instead of US$50. What looks like a normal camera, is a depth sensor with a resolution of 240x180 pixel. This sensor is capable of capturing depth (3D) information with 30fps on a Raspberry Pi 4.

![](/assets/img/posts/2022-09-26-short-review-new-arducam-tof-sensor-kickstarter/2022-09-26-arducam-tof1-600x600.webp)

Disclaimer: I got this sensor free of charge from Arducam. No money changed hands, and I am just doing some independent testing and evaluation. This post reflects my findings and opinion.

An important note on Kickstarter and other Crowdfunding platforms: Before taking part in any campaign as a backer, please read T&Cs. Rewards aren’t guaranteed! Always do your own research on the project and companies involved!

### What is time of flight (ToF)

The [Arducam ToF module](https://www.kickstarter.com/projects/arducam/time-of-flight-tof-camera-for-raspberry-pi?ref=4apsz7) emits 940 nm invisible infrared light, which bounces off the object's surface. The 240x180-resolution image sensor detects that light and calculates the distance to the objects.

A similar module can be found in modern smartphones, which some companies falsely call "LIDAR". Smartphones use this module to either detect the shape of the person's face, scan rooms or even full environments. For instance, the Apple iPad Pro 2020 seems to have a 0.03MP ToF sensor[**¹**](http://image-sensors-world.blogspot.com/2020/03/techinsights-finds-sony-tof-sensor.html#:~:text=Saturday%2C%20March%2028%2C%202020&text=%22TechInsights%20has%20begun%20the%20teardown,%2Ddepth%20reports%20to%20follow.%22), which is even lower than this 0.04MP Arducam module. Another well-known ToF sensor sits in the Kinect, which has a 0.3MP sensor. But remember that resolution is just one part of the equation.

What stands out is that the [Arducam ToF](https://www.kickstarter.com/projects/arducam/time-of-flight-tof-camera-for-raspberry-pi?ref=4apsz7) comes open-source, as a bare module of only 38x38mm, which can be easily integrated into existing projects. Furthermore, it comes with easily customizable python, C and C++ scripts, that can be found on this [Arducams GitHub Repository](https://github.com/ArduCAM/Arducam_tof_camera).

### Using the Arducam ToF module

It only took me a couple of minutes to set up the module with a Raspberry Pi 4 by following [the official documentation](https://github.com/ArduCAM/Arducam_tof_camera). The camera can be connected through the known CSI camera ribbon cable and after installing the drivers, the provided example scripts can be used to easily generate depth maps or even point clouds.

![](/assets/img/posts/2022-09-26-short-review-new-arducam-tof-sensor-kickstarter/2022-09-26-arducam-tof2-600x600.webp)

[*OpenScan Classic*](https://www.openscan.eu/openscan-classic)*through the eyes of the Arducam ToF module*

The color of the depth map indicates the distance of the surface to the camera. The more red, the closer the object. Blue indicates larger distances (see below). I was absolutely surprised, that the camera was able to capture even the smaller details like the 5 mm wide stepper motor cable. Another interesting observation is the reflection on the underside of the turntable. The yellowish color indicates, that it measured the signal coming from the wall (behind the OpenScan Classic.)

Note, that there are two operational modes available: 2 m and 4 m, where the increased range of the latter one comes at the cost of more noise.

Since I have been on a very tight schedule for several weeks, I just modeled a quick 3d printed enclosure for the ToF module, set up the Raspberry Pi and added the module to the stand on the last Maker Faire in Prague.

![](/assets/img/posts/2022-09-26-short-review-new-arducam-tof-sensor-kickstarter/2022-09-26-arducam-tof3-600x600.webp)

*OpenScan&Arducam @ MakerFaire Prague 2022 (sorry for the wrong price tag on the display)*

Since I didn't have any prior practical experience with ToF modules, I was very interested to hear the feedback of the visitors of the Maker Faire. I love this kind of event, as you always meet people with way more experience and knowledge, so there is the chance to learn plenty of new stuff. Several people were stunned by the output and told me that the noise (even using the 4 m range) was much better compared to other low-cost devices.

### Summary

In contrast to Photogrammetry, ToF is a non-contact active 3d scanning method with its own pros and cons. It is very important to understand the limitations of each method, so that one can choose the right scanning procedure for the given needs. ToF definitely has its place in robotics, object detection, detecting people, night 3d vision and many others. Note, that transparent and reflective surfaces might not be detected well (as with almost all 3d scanning methods). And another important note: due to an immense lack of time, I barely touched the surface of this little device, so there is much more to test and to explore.

I am really looking forward to seeing more projects being realized with the help of this low-cost and ingenious module. I see a huge potential and want to say thanks to Arducam for another great contribution to the open-source world.

PS.: There will be another blog post about the Maker Faire and some more updates soon.
