---
title: "OpenScan3 Firmware: Quick Start & Troubleshooting"
date: "2026-04-16T13:31:29+02:00"
author: "Elias Stognienko"
description: "Getting started with OpenScan3 is straightforward once the image is flashed and the device is on the network. This post explains the basic setup process and covers the most common issues during installation and first boot."
categories:
  - "Tutorials"
tags:
  - "openscan3"
  - "firmware"
  - "how-to"
image:
  path: "/assets/img/posts/2026-04-16-openscan3-firmware-quick-start/os3-quickstart-9ceb2653-685c-4333-8bfa-89509fc6266c.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-quick-start"
  - "https://openscan.eu/blogs/news/openscan3-firmware-quick-start"
---

This post explains how to get started with OpenScan3 and covers the most common setup issues during installation and first boot.

## Install OpenScan3 with Raspberry Pi Imager

The easiest way to install OpenScan3 is with Raspberry Pi Imager using the OpenScan image repository.

**Note:** Advanced customization such as hostname, username, password, and Wi-Fi is confirmed to work with Raspberry Pi Imager version 2.x. Older versions may not apply these settings correctly.

1. Open **Raspberry Pi Imager**.
2. Click **ADD OPTIONS**.
3. Select **EDIT Content Repository**.
4. Choose **Use custom URL** and enter:
   <code>https://openscan.eu/rpi-repo.json</code>
5. Click **Apply and restart**.
6. Select your Raspberry Pi model.
7. Choose the image matching your camera variant.

**Important:** Make sure to select the image that matches your camera model. Using the wrong image may prevent the camera from working properly and can potentially damage hardware.

8. Select the storage device you want to flash.
9. Adjust settings such as hostname, username, password, and Wi-Fi if needed.
10. Write the image to the card.
11. Insert the card into the Raspberry Pi and power it on.

## Open the web interface

If you did not change the default hostname during flashing, you should be able to access the OpenScan3 web interface from another device in the same network at:

- <code>http://openscan/</code>
- <code>http://openscan.local/</code> if mDNS is available on your network

The API documentation is available at:

- <code>http://openscan/api/latest/docs</code>
- or <code>http://openscan.local/api/latest/docs</code>

## Run the setup wizard

After connecting to the web interface for the first time, you will see the dashboard with a notice that the device still needs to be configured.

Follow the setup wizard to complete the initial setup of your scanner.

## No Wi-Fi configured? Use Wi-Fi QR setup

If you did not configure Wi-Fi during flashing and do not want to connect the device via Ethernet, you can provide Wi-Fi credentials using a QR code shown to the camera.

1. Create a Wi-Fi QR code on your Android or iOS device.
2. Hold the phone in front of the camera.
3. The device will read the Wi-Fi credentials and try to connect to your network.
4. Once connected, you should be able to open the web interface using the hostnames above.

## Troubleshooting

### I cannot reach the device

Make sure the Raspberry Pi has finished booting and is connected to the same network as your computer or phone.

If you configured a custom hostname during flashing, use that hostname instead of <code>openscan</code>.

If <code>http://openscan/</code> does not work, try:

- <code>http://openscan.local/</code>
- the device IP address from your router or network scanner

If you did not configure Wi-Fi and are not connected via Ethernet, use the Wi-Fi QR setup described above.

### The device does not detect the camera

First, check that the camera cable is connected correctly and inserted in the proper orientation.

Also make sure that you flashed the image matching your camera model.

For more detailed diagnostics, you can check the camera report here:

<code>http://openscan.local/api/latest/develop/camera-report?format=text</code>

You may also want to inspect the system logs for additional clues.

If the issue persists, feel free to open an issue on GitHub or ask for help on Discord.

### I cannot SSH into the device

Most likely, no user account was created during the flashing process.

By default, the standard OpenScan3 images do not include a default login. The exception is the develop image, which is intended for development and testing.

Also note that if you used an older Raspberry Pi Imager version, customization settings such as user creation may not have been applied correctly.

In that case, reflash the card with a current Raspberry Pi Imager version and make sure to configure a user during setup.

## Need help?

If you get stuck, you can always:

- open an [issue on GitHub](https://github.com/OpenScan-org/OpenScan3)
- ask for help on our [Discord Server](https://discord.com/invite/eBdqtdkXyF)
