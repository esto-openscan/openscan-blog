---
title: "OpenScan Mini + Classic - New Firmware (Beta)"
date: "2021-11-22T11:30:00+01:00"
author: "Thomas Megel"
legacy: true
categories:
  - "News"
tags:
  - "openscan2"
image:
  path: "/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta.webp"
redirect_from:
  - "/blogs/news/openscan-mini-classic-new-firmware-beta"
  - "https://openscan.eu/blogs/news/openscan-mini-classic-new-firmware-beta"
---

Finally, there is a new Raspbian image for the OpenScan devices incorporating the latest changes:

- OpenScanCloud - one-click-processing of your 3d models
- Access Point - whenever there is no Wifi available, the device will create an access point
- Many minor and major bug fixes :)
- ...

![](/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta-600x600.webp)

In order to test the beta, please follow this [Github Link](https://openscan-org.github.io/OpenScan-Doc/firmware/setup/).

**Note, that this is still a beta version and there might/will be some bugs included. So only install the image, if you know at least a bit of troubleshooting (i.e. command line/headless access to Raspbian).**

### **(1) Setup - Burning the SD card image**

![](/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta1-600x600.webp)

Select the downloaded image file ("2021-11-19 OpenScanPi_AP.zip"), your SD card and hit *write*.

**Important note:**

**In earlier releases, you needed to modify/add a wpa_supplicant.conf file with your wifi credentials to the boot folder of the SD card. This is not the case anymore! Do not change anything on the SD card! You can directly insert the card into the Raspberry Pi and start booting the device. Wifi credentials can be added in the next step.**

### **(2) Starting the Raspberry Pi**

Connect all electronic components, insert the SD card and power your Raspberry Pi. The first boot might take several minutes. Once node-red (the browser user interface) is loaded, the ringlight LED will flash in one of the following patterns:

(I) fast flashing + 1s off + 1s on + 1s off + 1s on --> Access Point Mode

(II) fast flashing + 1s off + 1s on --> Connected to local wifi network

On first boot, there the device will enter the Access Point Mode and you should be able to see the following network *OpenScanPi* with the password *raspberry*:

![](/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta2-600x600.webp)

You should be able to connect to this network with any of your devices.

**Important note: Prior tests seemed to indicate that some devices do not like to connect to this network, but I do not know the reason yet. Please let me know if you encounter any problems!**

Once connected, you should be able to open the user interface in your browser through the following site: [http://openscanpi:1880/ui](http://openscanpi:1880/ui) (and the backend of node-red [http://openscanpi:1880](http://openscanpi:1880) for debugging)

### **(3) Settings Menu**

Your first step should be opening the settings menu, where you will find two new & refined columns (*Network*and *OpenScancloud*).

![](/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta3-600x600.webp)

First, choose your *OpenScan model* (left column). If you intend to use the OpenScanCloud service, please read and agree to the *Terms of Use*.

In order to connect to a Wifi network, first hit *search wifi* and after a short moment a dropdown with all available networks should be visible. Choose one of the networks and enter your wifi password and two-digit country code (see [Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). Once added, the pi will remember this network. You can reset ALL saved networks by hitting *reset wifi*. This will restore the access point mode with the given access point name, which can be set freely.

OpenScanCloud allows you to easily process your images and create highly detailed 3d models. In order to activate the cloud-functionality, you need to enter your token. If you do not have a token yet, you can use the register button and enter your details (name + email). I will create your personal token and send you a mail to the given address, which currently might take a few days, but I try my best :)

### **(4) OpenScanCloud - Fileupload**

![](/assets/img/posts/2021-11-22-openscan-mini-classic-new-firmware-beta/2021-11-21-firmware-beta4-600x600.webp)

Once you have created an image set, you can download the locally stored files by clicking on *zip*. Alternatively, you can select an image set and press *upload*in order to transfer the files to my servers for processing. Note, that this might take some time, first the image set will be prepared (split into chunks of 200mb) and then uploaded to my servers. You will receive an email with the result as soon as the processing is done.

### **(5) Help texts**

I have started adding little help icons (" ? ") with additional information. Please let me know if you find it helpful or if you wish more or less details.

### **(6) IMPORTANT**

Please let me know if you encounter any problems! There will be future beta-updates, which can be installed by clicking on the *install latest beta version* on the start screen (see first image)! Do not use the regular update-routine in the *Update&Info* tab as this will install the latest stable version (without OpenScanCloud + Access Point mode).

I am really looking forward to pushing this release, but i definitely need your help and feedback!

Thank you so much for your time,

best regards,

Thomas
