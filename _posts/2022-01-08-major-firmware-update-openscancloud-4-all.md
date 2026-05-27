---
title: "Major Firmware Update - OpenScanCloud 4 All"
date: "2022-01-08T12:00:00+01:00"
author: "Thomas Megel"
legacy: true
categories:
  - "Firmware"
tags:
  - "openscan2"
image:
  path: "/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update1.webp"
redirect_from:
  - "/blogs/news/major-firmware-update-openscancloud-4-all"
  - "https://openscan.eu/blogs/news/major-firmware-update-openscancloud-4-all"
---

**In short: You can create 3d models like this with only your Raspberry Pi + Camera and an internet connection (5 clicks --> 100 photos + 5 min of automated processing)**

![](/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update1-600x600.webp)

After a lot of testing, I am finally able to release the firmware with integrated cloud functionality. From now on, every OpenScan device can transfer image sets to the OpenScanCloud for processing.

The visible changes of the user interface seem minor, but the usability-improvement should be huge, as you won't need any processing power or additional software to get a detailed 3d model. Of course, you will always be able to do the processing locally.

The installation is as simple as possible: You should get a notification about the available update, or you can manually check & install the update in the "Update&Info" tab on your device. Note, that two automated restarts are required, and therefore the installation will take roughly two minutes.

### **File Menu**

**![](/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update2-600x600.webp)**

In the file menu, you can select a stored image set and upload it to the OpenScanCloud Servers.

Refreshing will query the server for your stored image sets. This will update the status in the file table accordingly ('file approved', 'processing started', 'processing done', 'processing failed'). See the help icon for a detailed description

### **Settings Menu**

In order to use the cloud processing, you will need to read&agree to the Terms of Use. Find more details using the little help icon :)

Upon first usage, you will need to register by giving your name + email address. Note, that I currently have to approve each request manually and thus, the confirmation email might take a bit ;)

![](/assets/img/posts/2022-01-08-major-firmware-update-openscancloud-4-all/2022-01-08-firmware-update3-600x600.webp)

Once you received the registration email, you can enter the token and use the cloud processing.

In case you run out of "credit", just send me a mail to [cloud@openscan.eu](mailto:cloud@openscan.eu). (In the future, i might remove those limits)

### **Changelog on GitHub**

See some other minor improvements and all details on [GitHub](https://github.com/OpenScanEu/OpenScan)

### **Support the project**

I will do everything I can to keep this functionality free and open. In case you can, please consider supporting my endeavor financially through a [donation on BuyMeACoffee](https://www.buymeacoffee.com/OpenScan) OR share the project, so that more people get involved. :)

### **Little Promotion**

To start this new year, I offer free worldwide shipping with the coupon code '**2022willbegreat**', which is valid till 15th of January and can be applied on all orders at [www.openscan.eu/shop](https://www.openscan.eu/shop) over €50.
