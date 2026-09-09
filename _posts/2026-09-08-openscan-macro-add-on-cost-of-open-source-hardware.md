---
title: "OpenScan Macro Add-on: Launch & The Cost of Open-Source Hardware"
date: "2026-09-08T10:00:00+02:00"
author: "Thomas Megel"
description: "A transparent breakdown of what it actually costs to develop, produce and sell the OpenScan Macro Add-on and why it launches with a 'choose your price' experiment."
categories:
  - "News"
tags:
  - "openscan"
  - "macro"
  - "add-on"
  - "pricing"
  - "open-source-hardware"
image:
  path: "/assets/img/posts/2026-09-08-openscan-macro-add-on-cost-of-open-source-hardware/OSMacro_Mini_Classic_Compatibility.jpg"
  alt: "OpenScan Macro Add-on compatibility with Mini and Classic"
---

## Limited sale & some thoughts on open-source business

![OpenScan Macro Add-on compatibility with Mini and Classic](/assets/img/posts/2026-09-08-openscan-macro-add-on-cost-of-open-source-hardware/OSMacro_Mini_Classic_Compatibility.jpg)

## Now available at openscan.eu

Pricing has always been hard for me, and I think that the open-source approach not only applies to hardware and code, but to the business aspect too. So consider this an experiment: for now, the first version of the Macro Add-on comes with a choose-your-price option — you select what seems fair to you (within reason).

[**Get the Macro Add-on →**](https://openscan.eu/products/macro-add-on-for-mini-classic)

We'll do a regular launch by early October.

## TL;DR
- pricing is hard
- limited time first batch with experimental "Choose your price" approach above 108€
- Is open-source limited to software and hardware or could it include the business aspects too?
- There will be a low-cost kit version soon too, including only the pre-cut polarizer foil and the ringlight PCB

## Cost of open-source Hardware - A case study using the OpenScan Macro Add-on

Running an open-source project as a business has always been a challenge. Finding the balance between making parts accessible while running a small business comes with a lot of difficult decisions.

In order to create more transparency, I want to give some insights into the pricing decisions for the OpenScan Macro Add-on. People often underestimate the time and investment that goes into a new development as well as the distribution of a product. A product is much more than the sum of all the parts and therefore I want to give you a run-down of the numbers. Running a project as a business creates a lot of regulatory requirements and costs that are invisible from a maker's perspective.

It has always been the goal of OpenScan to offer low-cost hardware to as many people as possible. What is defined as low-cost varies immensely depending on your background and geographic location. Since we are based in Germany, which is one of the most expensive countries in the world, some of our costs are significantly higher than in other countries.

OpenScan is more than a passion project for me, it has been paying my bills since 2019 and by now I'm in the very fortunate situation that I'm able to pay other people to help with the development. Over the years, I had to learn (and still have to learn) what decisions are worthwhile pursuing. Doing something in your free-time is a totally different thing compared to doing the same as a business. For me personally, this line between hobby and work has always been blurry and thus decision-making has sometimes not been optimal. With this blog post I want to give you (and myself) an insight into the thought-process:

## Development (one-time investment)

| Position                                   | Description                                                                                                                                                                                                                                                           | Cost  |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Buying various lenses                      | Members at the OpenScan discord have been playing around with alternative optics for years. I bought several dozens of various lenses over the time, which all needed to be researched, ordered and tested. I can only track the recent development times, see below. | 1500€ |
| Research & Sourcing                        | 20h, finding and communicating with the various sources of the parts                                                                                                                                                                                                  | 2000€ |
| CAD Design                                 | Creating a usable design that can be reproduced widely takes multiple iterations --> 60h                                                                                                                                                                              | 6000€ |
| 3D Printer Setup                           | optimizing printer and material settings for small/medium-scale production --> 20h                                                                                                                                                                                    | 2000€ |
| Filament and printer depreciation          | Over the development time, I ran through ~ 5kg of material and 300h of printing time. A typical number is 3-4€/h of printing time                                                                                                                                     | 900€  |
| Ringlight PCB                              | 2h                                                                                                                                                                                                                                                                    | 200€  |
| Polarizer                                  | Cut with a CNC Drag knife --> Design + finding the right tolerances --> 8h                                                                                                                                                                                            | 800€  |
| Documentation                              | Taking nice images and writing tutorials --> 10h                                                                                                                                                                                                                      | 1000€ |
| Packaging                                  | Figuring out the right shipping rates/packaging --> 2h                                                                                                                                                                                                                | 200€  |
| Shop + Invoicing                           | Setting up a new product in Shopify + integration into our internal invoicing/shipping pipeline --> 8h                                                                                                                                                                | 800€  |
| Community Engagement/Marketing             | Making short videos and sharing the development (80h)                                                                                                                                                                                                                 | 8000€ |
| Re-arranging internal production/logistics | Adding even just a single screw to a shop requires adjustments in storage space, invoicing, packaging workflow, sourcing --> 20h                                                                                                                                      | 2000€ |
| others                                     | There are many indirect and un-measurable pieces, that are not covered above: research into regulatory environment, market analysis, internal discussions about pricing/strategy ...                                                                                  | ???   |

Which comes to a **minimum estimate of 25400€**.

One note about the hourly rate: I assumed 100€ per hour, which sounds like a lot, but in fact is a somewhat low guesstimate. The current minimum hourly rate for unskilled labor in Germany is ~20€ (employer-side cost). Taking this number as the absolute baseline, I, as an employer, have to add a standard factor of 3x for overhead, which accounts for non-billable time, administration, facilities, and a reasonable profit margin, resulting in a **minimum** viable hourly rate of around 60€ for unskilled labor. The tasks mentioned above are far from unskilled.

Another data point: specialized self-employed engineers in Germany regularly charge 90-140€. For these reasons, I have settled on the 100€/h figure.

## Production (recurring unit cost)

| Position                 | Description                                                                          | Cost |
| ------------------------ | ------------------------------------------------------------------------------------ | ---- |
| 3D printing              | 3 printer hours (4€/h covering printer setup, filament, depreciation, failed prints) | 12€  |
| 3D printing harvest + QC | 2min                                                                                 | 2€   |
| polarizer sheet          | raw material 1€ + CNC cutting 2min, QC 1min                                          | 4€   |
| lens                     | material cost 25€, order/import/QC/assembly (3min)                                   | 28€  |
| Assembly + Packaging     | 8min                                                                                 | 8€   |

Resulting in **54€ net per unit**.

Here I assumed the lower 60€/h figure mentioned above.

## Cost of Sale

This is probably the most-overlooked part and the amount of those costs were not clear to me in the beginning of this project. Note, that these are all deductions from the end-consumer price.

| Position               | Description                                                   | Cost  |
| ---------------------- | ------------------------------------------------------------- | ----- |
| Payment Processing     | PayPal/Stripe/Shopify all take their cut from the sales price | ~6.5% |
| Shipping Cost          | as percentage of the total sales volume                       | ~7%   |
| VAT                    |                                                                | ~16%  |
| Accountants            |                                                                | ~1%   |
| Website/Infrastructure |                                                                | ~0.5% |
| refunds/disputes       |                                                                | ~1%   |

--> 32% of each and every sale. (**!! This does not include any overhead of having to rent an office, or any other business expenses !!**)

## Pay-day or Where does this leave us:

### Profit margins & Reselling

In the past, I made the huge mistake to ignore one pricing factor as I didn't consider using any reseller structure. **This "small" decision/ignorance on my side almost crashed the whole OpenScan business.** Over the years, the project grew to an international audience, but with the sudden introduction of the US tariffs in 2025, our sales to the US dropped from ~50% to below 10%. This resulted in a still ongoing financial struggle, as the US used to be our main market. During that time, I talked to several people & companies in the US about some kind of reselling arrangement, but time and time again, we realized that the prices were too low and there wouldn't be enough margin to make this viable for both sides.

There are various numbers floating around and for me it is hard to compare our products with other businesses. First of all the development costs are far from well-defined as many things are happening "by themselves" (in the community, in my free-time...).

I found the "golden industry standard" talking about 50/50 for both producer and reseller. In simple terms, this means that both markups increase the raw price by a factor of 2 **each, so quadrupling the unit price**. Those margins are needed to support all the costs running a business, marketing, logistics, after-sales, returns (...) for both parties. Ah and there still should be some profit left after all of that.

## Different scenarios:

### (0) Bare minimum - 79.4€

Material cost + cost of sale, with zero margin: `54 / (1 − 0.32) = 79.4€`. At this price, every sale is effectively a net loss once you account for the time invested in development and other invisible costs of running a business. There's no path to ever recovering the 25,400€ sunk into getting the Macro Add-on to market. This number exists purely as a floor, not as a price that we could actually charge.

### (1) "Golden" standard (without reseller) - 108€

A 50/50 split between recovering unit cost and profit, doubling the unit costs. This is the price point that industry norms would call somewhat "healthy". This is the reference point for what "sustainable, direct-to-consumer open-source hardware" actually costs when you're not subsidizing it with goodwill and unpaid hours. **This still doesn't factor in any possible reseller, which is problematic.** Furthermore, since we are still a small business, our somewhat fixed 32% cost of sale would eat up most of this margin and it is unrealistic that the remaining 18% could ever cover marketing, logistics, support, after-sales (...) and leave some profit (not to mention any amortization or future R&D costs).

### (2) "Golden" standard (with reseller) - 216€

The reseller applies their own 50% margin on top, doubling the initial unit cost again. Keep this as a reminder of how much retail markup gets added once a product moves through a traditional distribution channel, and part of why we've mostly stuck to direct sales for all parts and kits.

### Where does this leave us?

To be honest, for me personally and as a maker, some of those figures *feel* outrageous and I am still sceptical about publishing those calculations and insights, especially with the international audience in mind. None of these three numbers feel right to charge everyone. €79 loses money on every sale. €108 would be somewhat sustainable but strictly limit the development and growth of the project as resellers would never be an option. €216 prices out exactly the hobbyists and makers this project exists for.

So instead of picking and fixing one number, I want to try something different: **let you pick.** For a limited time, the Macro Add-on will be available as "choose your price" (above 108€).
1. If you're a student, a hobbyist, or just getting into photogrammetry, pay what you can.
2. If OpenScan has been useful to you, if you believe in keeping hardware open and documentation public, or if you simply have the means, you can opt to pay more.
3. If you are a business or institution, take a look at other scanning solutions, which easily exceed 10k€. I don't claim that OpenScan (yet) plays in the same league, but we've come a very long way.

You can [get your pre-assembled macro add-on](https://openscan.eu/products/macro-add-on-for-mini-classic) at openscan.eu. Choose a price (in €) that seems fair to you.

## Final thoughts (a bit more emotional after the number crunching)

Talking publicly about money/finances is a big no-go (at least in Germany). But I have some hope that this kind of exposure opens up the discussions and the mutual understanding of both sides.

In the current hyper-capitalistic world, you don't really get to opt out of playing the game, not if you want a project to survive and grow beyond what evenings and weekends can sustain. And to be absolutely clear, playing along is not only a compromise. It does come with some major benefits and advantages (that I'll discuss in an upcoming, already long-cooking blog post about *Open Hardware as a business*).

The maker and open-source movement takes knowledge that used to be guarded and proprietary, and gives it back to the world. People building hard- and software together already created some amazing achievements. But isn't the movement all about looking behind the fancy, polished facade of a thing/product? Shouldn't opening up the business side be part of that too?

When I started looking into 3D Scanning in 2017, I had very little to no knowledge about CAD, electronics, programming, scanning, printing and all those beautiful technologies. By now, I am still no expert at any of those, but thanks to many great people that contributed along the way, we've built an amazing scanning platform. The business side has always been an unwanted necessity. We share CAD files and firmware freely, shouldn't we be just as willing to open up the spreadsheets? What the last years told me is that there is always someone out there, who is much more skilled and knowledgeable, and going into an open exchange no side loses anything.

I thank all the people out there supporting the project and participating in the long way we've already gone (and which is by far not over ;). I'd really like to hear your thoughts about this particular post. Feel free to [reach out privately by mail](mailto:info@openscan.eu) or [publicly on our Discord](https://discord.com/invite/gpaKWPpWtG).
