---
title: "Update on the upcoming OpenScan firmware release (IMX519 + other changes)"
date: "2022-01-28T12:30:00+01:00"
author: "Thomas Megel"
legacy: true
categories:
  - "Firmware"
tags:
  - "openscan2"
image:
  path: "/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking1.webp"
redirect_from:
  - "/blogs/news/update-on-the-upcoming-openscan-firmware-release-imx519-other-changes"
  - "https://openscan.eu/blogs/news/update-on-the-upcoming-openscan-firmware-release-imx519-other-changes"
---

For almost two years, I have been working on the first version of the firmware for the OpenScan Mini + Classic. And so far, I have been able to release updates, that could be easily installed through the user interface.

But due to two major external factors, I decided to rewrite the whole code and create a 'new' firmware (with many of the old features + some exciting new functionality). It will be necessary to flash the micro SD-card with the new image, but this should be easily doable :)

### Support for many more camera models

The first factor is, that the Raspberry Pi foundation dropped the used camera python library in favor of the libcamera framework. Generally speaking, this is a great step, as it will allow many more camera sensors to be supported. This coincided with the release of the new Arducam IMX519 camera, which I have been testing for a few weeks now. This camera needs the libcamera functionality too, and thus I have to move forward.

For now, this means that the following camera will be supported:

- IMX219 (pi camera v2) with 8mp
- IMX477 (pi camera HQ) with 12mp
- OV5647 (pi camera 1.3) with 5mp
- IMX378 with 11mp
- OV9271 with 1mp and global shutter
- IMX290 with 2mp and global shutter

Furthermore, using the libcamera framework will allow third parties (like Arducam) to add support for their cameras too. For now, the following Arducam cameras should work too:

- IMX519 with 16mp and autofocus (definitely working, see below :)
- AR0234 with 2.3mp and global shutter
- IMX230 with 21mp (!!!)
- IMX298 with 16mp and autofocus (and microphone)
- IMX462 with 2mp (and low-light functionality)
- OV9281 with 1mp, monochrom
- OV2311 with 2mp global shutter

So can you see, that the overall usability is widely improved. The only shortcoming of the new libcamera framework is, that the preview is very slow at a framerate of below 1fps (which should be improved as soon as the Raspberry Pi Foundation releases their new python camera library, which is expected somewhat soonish)

### Autofocus + Focus Stacking

With the adjustable focus of the Arducam IMX519 it will be possible to create stacks of photos. The position of the camera remains the same and only the focal plane is shifted. In theory, this should improve the photogrammetry output for models, where depth of field is an issue and some areas are blurry in one photo. Those areas will be crisp in the next photo, and the photogrammetry software -should- be able to only use the crisp areas for reconstruction. But there is a lot of testing needed ;)

For the coming update, I implemented three different modes (autofocus, MF - manual focus and ST - stacking) for the adjustable-focus IMX519 sensor:

![](/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking1-600x600.webp)

- autofocus (default), where you do not need to worry about setting the focus. The focus will be calculated in every position and the algorithm seems really robust. I only had some issues, when the object only covered a small part of the photo and the camera tried to focus the background instead.

- for this reason, there is the **M**anual **F**ocus mode, where you can set the focus distance manually. This value will be kept for all photos during the routine.

- And finally, Stacking, where you can set a lower and upper limit for the focus distance and a number of x photos. During the routine, the camera will stop in each position and take x instead of 1 photos with varying focus (in the given range). Note, that the overall size of the image sets will be increased accordingly by a factor of x.

### Re-adding DSLR support (with gphoto2)

This feature has already been tested a long time ago, but I did not get around to fully implement it into the firmware. So it rested in developer mode for ages... I will try my best to implement this functionality too, so that many, many DSLR cameras can be used with the official main firmware.

### Improvements in stability + usability

This is seems like a tiny step, but this is a thing, that gives me at least some satisfaction ^^: The user interface + backend are now accessible directly via *openscan*and *openscan/editor*respectively. (and not through openscan:1880/ui as before)

![](/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking2-600x600.webp)

A much more important improvement is the introduction of 'advanced settings' - mode, where you can access many more settings. This should make it much easier to modify and create your own hardware version:

![](/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking3-600x600.webp)

### Cleaning the Code + Backend

For a long time, I have just kept adding and adding new features and code-snippets. And over the time, the backend (node-red) and the underlying file-structure became a huge mess. I decided to re-organize and re-write a lot of code and clean up the overall file- and code-structure. I hope, that this will help future contributions!

![](/assets/img/posts/2022-01-28-update-on-the-upcoming-openscan-firmware-release-imx519-other-changes/2022-01-28-firmware-stacking4-600x600.webp)

There will be a dedicated update + documentation on how to use and modify the existing code at some point.

### Conclusion

I started this blog post with the words 'short update', but had to realize, that there have been quite a few changes already and there is even more to talk about in future posts. Please let me know if you wish any particular functionality or usability improvement!

If you made it that far in the text, feel free to [support my work through a coffee or two](https://www.buymeacoffee.com/OpenScan);)
