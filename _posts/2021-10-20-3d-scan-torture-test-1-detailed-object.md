---
title: "3D Scan Torture Test (1) - Detailed object"
date: "2021-10-20T11:00:00+02:00"
author: "Thomas Megel"
categories:
  - "Research"
tags:
  - "photogrammetry"
  - "3d-model"
  - "openscan-mini"
image:
  path: "/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-osc1.jpg"
redirect_from:
  - "/blogs/news/3d-scan-torture-test-1-detailed-object"
  - "https://openscan.eu/blogs/news/3d-scan-torture-test-1-detailed-object"
---

This is the first post of an upcoming series, where I will publish challenging image sets, each containing at least an isolated challenging property. The images of this particular set are not very challenging (as described below), but the object contains a ton of tiny and very challenging features. I will try to test as many different photogrammetry programs as possible. So if you want to join testing, feel free to download and process the files which are linked at the end of this article.

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/2021-10-20-scan-torture-test1-600x600.webp)

### Object characteristics

- baseplate is roughly 75x35mm
- very complex surface
- narrow slots and holes (0.2 - 1.0mm)
- spikes (0.2 - 1.0mm)
- partially occluded areas (between body and hexagon)
- shallow features (eyes + eyebrows)
- deep and narrow holes (honeycomb structure)

If anyone with a different scanner is interested in giving this one a try: You can download and print this object from [PrusaPrinters](https://www.prusaprinters.org/prints/5375). Don't forget to print it at 150% to keep the results comparable. In case, you do not have access to a 3d printer, I would love to send some printed copies around Europe or the US, so feel free to reach out to info@openscan.eu

### Photos

- 200 photos with the pi camera v2.1 (8mp)
- even lighting
- many surface features (created with scanning spray)
- blurry foreground and background

Despite the challenging object, the image set is of good quality and thus the resulting mesh is very detailed. The surface has been covered with chalk spray and thus there are enough features/dots for the software to pick up. The images are evenly lit and there are no hard shadows. The whole surface is covered with tiny dots, and the 200 photos are enough even for such a complicated object. Note that some images have a blurry foreground and background, and thus some areas of the object might be challenging to reconstruct.

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/2021-10-20-scan-torture-test2-600x600.webp)

### Results

Images can say more than a thousand words, so here are some renders of the final scanning results, where the first image is the CAD file from printables, the second one is OpenScanCloud and the third one is Reality Capture on High Detail.

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-orig1-600x600.jpg)

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-osc1-600x600.jpg)

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-rc1-600x600.jpg)

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-orig2-600x600.jpg)

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-osc2-600x600.jpg)

![](/assets/img/posts/2021-10-20-3d-scan-torture-test-1-detailed-object/render-rc2-600x600.jpg)

[Result with OpenScanCloud on Sketchfab](https://skfb.ly/oqnxG)

[Result with RealityCapture on Sketchfab](https://skfb.ly/oq6OJ)

### Downloads and more

You can download this image set and the resulting meshes from my [Google Drive](https://drive.google.com/drive/folders/15zAvuZRO3YX1WXOl7bdb167kNNcqVpso?usp=sharing) and use it as you wish. It would be nice if you could contribute some results from a different photogrammetry software.

Please follow this [Github Page](https://github.com/OpenScanEu/OpenScan/blob/master/Photosets/README.md), where I will publish all resulting 3d Models + various free image sets in the future.

If you would like to contribute an image set, please contact me :)

Best Regards,

Thomas
