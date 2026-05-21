---
title: "OpenScan3 Firmware: Quick Start & Troubleshooting"
date: "2026-04-16T13:31:29+02:00"
author: "Elias Stognienko"
description: "Getting started with OpenScan3 is straightforward once the image is flashed and the device is on the network. This post explains the basic setup process and covers the most common issues during installation and first boot."
shopify_summary_html: |-
  <p data-start="5017" data-end="5253">Getting started with OpenScan3 is straightforward once the image is flashed and the device is on the network. This post explains the basic setup process and covers the most common issues during installation and first boot.</p>
categories:
  - "OpenScan Blog"
tags: []
image:
  path: "/assets/img/posts/2026-04-16-openscan3-firmware-quick-start/os3-quickstart-9ceb2653-685c-4333-8bfa-89509fc6266c.jpg"
redirect_from:
  - "/blogs/news/openscan3-firmware-quick-start"
  - "https://62f7a3-4.myshopify.com/blogs/news/openscan3-firmware-quick-start"
---

<p>This post explains how to get started with OpenScan3 and covers the most common setup issues during installation and first boot.</p>
<h2>Install OpenScan3 with Raspberry Pi Imager</h2>
<p>The easiest way to install OpenScan3 is with Raspberry Pi Imager using the OpenScan image repository.</p>
<p><strong>Note:</strong> Advanced customization such as hostname, username, password, and Wi-Fi is confirmed to work with Raspberry Pi Imager version 2.x. Older versions may not apply these settings correctly.</p>
<ol>
<li>Open <strong>Raspberry Pi Imager</strong>.</li>
<li>Click <strong>ADD OPTIONS</strong>.</li>
<li>Select <strong>EDIT Content Repository</strong>.</li>
<li>Choose <strong>Use custom URL</strong> and enter:<br/><code>https://openscan.eu/rpi-repo.json</code>
</li>
<li>Click <strong>Apply and restart</strong>.</li>
<li>Select your Raspberry Pi model.</li>
<li>Choose the image matching your camera variant.</li>
</ol>
<p><strong>Important:</strong> Make sure to select the image that matches your camera model. Using the wrong image may prevent the camera from working properly and can potentially damage hardware.</p>
<ol start="8">
<li>Select the storage device you want to flash.</li>
<li>Adjust settings such as hostname, username, password, and Wi-Fi if needed.</li>
<li>Write the image to the card.</li>
<li>Insert the card into the Raspberry Pi and power it on.</li>
</ol>
<h2>Open the web interface</h2>
<p>If you did not change the default hostname during flashing, you should be able to access the OpenScan3 web interface from another device in the same network at:</p>
<ul>
<li><code>http://openscan/</code></li>
<li>
<code>http://openscan.local/</code> if mDNS is available on your network</li>
</ul>
<p>The API documentation is available at:</p>
<ul>
<li><code>http://openscan/api/latest/docs</code></li>
<li>or <code>http://openscan.local/api/latest/docs</code>
</li>
</ul>
<h2>Run the setup wizard</h2>
<p>After connecting to the web interface for the first time, you will see the dashboard with a notice that the device still needs to be configured.</p>
<p>Follow the setup wizard to complete the initial setup of your scanner.</p>
<h2>No Wi-Fi configured? Use Wi-Fi QR setup</h2>
<p>If you did not configure Wi-Fi during flashing and do not want to connect the device via Ethernet, you can provide Wi-Fi credentials using a QR code shown to the camera.</p>
<ol>
<li>Create a Wi-Fi QR code on your Android or iOS device.</li>
<li>Hold the phone in front of the camera.</li>
<li>The device will read the Wi-Fi credentials and try to connect to your network.</li>
<li>Once connected, you should be able to open the web interface using the hostnames above.</li>
</ol>
<h2>Troubleshooting</h2>
<h3>I cannot reach the device</h3>
<p>Make sure the Raspberry Pi has finished booting and is connected to the same network as your computer or phone.</p>
<p>If you configured a custom hostname during flashing, use that hostname instead of <code>openscan</code>.</p>
<p>If <code>http://openscan/</code> does not work, try:</p>
<ul>
<li><code>http://openscan.local/</code></li>
<li>the device IP address from your router or network scanner</li>
</ul>
<p>If you did not configure Wi-Fi and are not connected via Ethernet, use the Wi-Fi QR setup described above.</p>
<h3>The device does not detect the camera</h3>
<p>First, check that the camera cable is connected correctly and inserted in the proper orientation.</p>
<p>Also make sure that you flashed the image matching your camera model.</p>
<p>For more detailed diagnostics, you can check the camera report here:</p>
<p><code>http://openscan.local/api/latest/develop/camera-report?format=text</code></p>
<p>You may also want to inspect the system logs for additional clues.</p>
<p>If the issue persists, feel free to open an issue on GitHub or ask for help on Discord.</p>
<h3>I cannot SSH into the device</h3>
<p>Most likely, no user account was created during the flashing process.</p>
<p>By default, the standard OpenScan3 images do not include a default login. The exception is the develop image, which is intended for development and testing.</p>
<p>Also note that if you used an older Raspberry Pi Imager version, customization settings such as user creation may not have been applied correctly.</p>
<p>In that case, reflash the card with a current Raspberry Pi Imager version and make sure to configure a user during setup.</p>
<h2>Need help?</h2>
<p>If you get stuck, you can always:</p>
<ul>
<li>open an <a href="https://github.com/OpenScan-org/OpenScan3">issue on GitHub</a>
</li>
<li>ask for help on our <a href="https://discord.com/invite/eBdqtdkXyF">Discord Server</a>
</li>
</ul>
