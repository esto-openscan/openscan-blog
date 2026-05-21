---
title: "New Firmware with cloud functionality for OpenScan Classic & Mini (Beta)"
date: "2021-10-11T11:00:00+02:00"
author: "Thomas Megel"
legacy: true
categories:
  - "Firmware"
tags:
  - "openscancloud"
  - "openscan2"
image:
  path: "/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware.webp"
redirect_from:
  - "/blogs/news/new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta"
  - "https://62f7a3-4.myshopify.com/blogs/news/new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta"
---

After publishing a Windows Desktop GUI and the Python scripts to upload files to the OpenScanCloud, I finally managed to implement the new features into the OpenScan Firmware.

### Overview

Basically, this makes the OpenScan Classic and Mini smart devices able to create highly detailed 3D scans without any additional hardware or software!

![](/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware-600x600.webp)

The firmware hasn't been changed a lot, and I only added two new panels to the right side of the Files&Cloud tab. You will always be able to transfer the zip-files to your local computer and do the processing manually.

But I have seen an increasing number of people struggling with either the software and/or hardware requirements that come with photogrammetry... Therefore, it is now possible to select and upload an image set to my servers, where I will do the processing and send you the result by email.

### Install the latest Beta-Firmware

In order to use this beta functionality, you will need to log in to your Raspberry Pi and run the following single-line-command in the terminal:

*sudo wget -O /home/pi/.node-red/flows_raspberrypi.json https://raw.githubusercontent.com/OpenScanEu/OpenScanCloud/main/uploader/firmware_beta.json && node-red-restart*

which will download and install the latest beta firmware.

### OpenScanCloud Settings

The only thing needed is a personal token, which you can easily apply for by sending an email to [cloud@openscan.eu](cloud@openscan.eu). You will then need to enter the token in the OpenScanCloud Settings Tab (in this example: *4x1c1128e*...):

![](/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware1-600x600.webp)

After hitting refresh, some associated data will be loaded from the server:

- ***Credit***- A number showing how much gigabyte you are currently allowed to upload and process. This value is currently limited to prevent abuse. Anyway, if you run out of "credit", just email me.
- ***Max. Number of Photos***: Is the maximum number of photos that are allowed in ONE set.
- ***Max Filesize:***in gigabyte is the limit for the file size for ONE image set/zip.

There will be some updates in the near future, and after installing this version, you will be able to get those updates by simply clicking the update button below. I will write blog posts about any major updates of the firmware, but you can also follow the project on [GitHub](https://github.com/OpenScanEu/OpenScanCloud/blob/main/README.md).

### Upload & Process image sets with OpenScanCloud

In order to start processing, you will only need to select an image set from the list and press *upload*. In order to upload the set, the file might need to be split into 200MB chunks. This step is fully automated and can take up to a minute, so please be patient. Those chunks will be uploaded and processing will be started as soon as possible.

![](/assets/img/posts/2021-10-11-new-firmware-with-cloud-functionality-for-openscan-classic-mini-beta/2021-10-12-osc-firmware2-600x600.webp)

You can always press *refresh*to query the current status of your projects, which should be one of the following:

- **created**: The project has been successfully created on the server
- **initialized**: All files have been uploaded and processing will start soon
- **processing started/failed/done**: self-explanatory

**OpenScanCloud - Example - Miniature**

<div><iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="560" src="https://www.youtube.com/embed/zTf4UN-JXps" title="YouTube video player" width="315"></iframe></div>

I have scanned this 9 cm tall figurine with the OpenScanMini and took a total of 70 photos. In order to get such a clean result, I needed to cover the surface with a fine layer of scanning spray. Besides the uploading time, processing took not even three full minutes :)

So far, I have tested the engine with over 50.000 images in 700 photo sets and the robustness and speed are quite impressive.

Feel free to join the testing by sending me a mail to [cloud@openscan.eu](cloud@openscan.eu) and let me know what you think.

Best regards,

Thomas
