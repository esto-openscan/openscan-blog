---
title: "Mobile Scanning - Preparing a major update"
date: "2021-10-28T11:00:00+02:00"
author: "Thomas Megel"
categories:
  - "OpenScan Blog"
tags:
  - "News"
  - "Update"
image:
  path: "/assets/img/posts/2021-10-28-mobile-scanning-preparing-a-major-update/2021-10-28-firmware-improvements.webp"
redirect_from:
  - "/blogs/news/mobile-scanning-preparing-a-major-update"
  - "https://62f7a3-4.myshopify.com/blogs/news/mobile-scanning-preparing-a-major-update"
---

Everyone who has set up an OpenScan device will know the following nuisance: You have spent quite some time assembling the 3D-printed parts, connected all the wires and finally want to boot the Raspberry Pi for the first time. But before that, you will have to take the Micro-SD-Card to your PC, create and open the WPA-Supplicant.conf file and add your Wi-Fi settings... And of course, this has to be repeated every time you want to connect to a new network.

(Alternatively, I had implemented a settings submenu, where you could add a single Wi-Fi connection via the User Interface when directly connected to the router by Ethernet).

*Long story short: This is the opposite of usability, and I finally found a promising way to fix this (and several other) issues. If you know any issues or see ways to improve the overall experience, please see the list of future improvements below and definitely add your thoughts!*

![](/assets/img/posts/2021-10-28-mobile-scanning-preparing-a-major-update/2021-10-28-firmware-improvements-600x600.webp)

### Access Point - Use the device anywhere

With the upcoming update, you will be able to access the OpenScan devices anywhere. The device will scan for known networks and if none is found, it will create an Access Point with the obvious name *OpenScanPi*. Thus, it becomes a stand-alone device and can be easily used in classroom, MakerFaire or on a scanning-field-trip ;)

You can simply access the scanner from any device and start the scanning and save the image sets on your computer. You can optionally connect Ethernet and use the OpenScanCloud to process the image sets.

![](/assets/img/posts/2021-10-28-mobile-scanning-preparing-a-major-update/2021-10-28-firmware-improvements2-600x600.webp)

### OpenScanCloud - Processing without the need for additional software

I am currently testing the cloud processing feature, where you can simply send your image sets to my servers for processing. With every incoming image set my confidence rises :) So far, there have been only very minor issues (on the processing side) and the overall performance is great. You can already use the beta version of the firmware (see [GitHub](https://github.com/OpenScanEu/OpenScanCloud)for more details). So feel free to try it out!

### Documentation - FINALLY (!!)

This is by far my largest weakness. I love tinkering, but writing down, what I have done is just plain annoying. I totally understand, that a good documentation is key for a good user experience. And I have finally decided to migrate all documentation to GitHub, where it is much easier to implement changes, track issues and so on... My plan is to release the above-mentioned update, fix some final issues with the OpenScanCloud and then rewrite and migrate the documentation. If somebody would like to contribute, see you on [GitHub](https://github.com/OpenScanEu/OpenScan/blob/master/Documentation/readme.md)

### Other Improvements

- Better booting routine - there will be some kind of feedback (blinking of ringlight LED) so indicate the state of the device. This should improve any troubleshooting
- new and updated raspbian image
- remove dev mode (as there haven't been any changes in a long time)
- ... PLEASE ADD YOUR WISHES IN THE COMMENTS :)

I am looking forward to publishing this great update soon(ish) :)

Best regards,

Thomas
