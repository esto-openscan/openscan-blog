---
title: "Optimizing 3D Scans: How Many Photos Do You Really Need?"
date: "2025-03-26T19:14:43+01:00"
author: "Thomas Megel"
categories:
  - "Research"
tags:
  - "experiment"
  - "research"
  - "analysis"
  - "photo-count"
image:
  path: "/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/photocount-photogrammetry-5d3b6b89-b153-4885-83fa-1019c633f20a.gif"
redirect_from:
  - "/blogs/news/optimizing-3d-scans-how-many-photos-do-you-really-need"
  - "https://openscan.eu/blogs/news/optimizing-3d-scans-how-many-photos-do-you-really-need"
---

**TL;DR: Is more always better? When it comes to photogrammetry, the clear answer is no! We performed tests, which align with our experience, showing that there is an optimal number of images for turntable photogrammetry—around 200 photos. Increasing beyond 300 photos does not improve mesh quality and only increases processing times.**

**As a little side effect, we also found a bug in our current positioning algorithm (above ~500 photos), which will be fixed in the next firmware update! :)**

## Method

In this experiment, we methodically evaluated the influence of the number of images onto the results from the photogrammetry pipeline. Therefore, we use the 45mm OpenScan Benchy model. The OpenScan Mini created various image sets ranging from 10 photos up to 1000 photos. The results were automatically calculated using the OpenScan Cloud. We created a total of 367 image sets and resulting meshes. If anyone is interested in any of the source data, feel free to reach out to [info@openscan.eu](mailto:info@openscan.eu).

The goal is to evaluate, whether there is some optimal number of images or whether the mesh quality increases steadily (at the cost of increased processing time).

## Pre-Analysis

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/duration-seconds-vs-photocount.png)As in our last experiment, the outliers can be easily explained by the OpenScan Cloud struggling occasionally, which will be fixed at some point. Ignoring those outliers, there is a clear linear trend for low photocount values (under 500). Surprisingly, there is a sudden plateau beyond that.

Looking closer at the scan data, we found that **there is an error with the path creation of the scanner**, where the *create_coordinates(angle_min, angle_max,point_count)* function did not produce coordinates with certain rotor angles (<0 ?).

The following image shows a comparison between the 502 and 1000 photos mesh result. You can see that areas that are only visible from below are not reproduced well due to a lack of photos. For this reason, the overall quality metrics drastically decreased.

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/500vs1000photos.jpg)

As expected, the quality of the meshes reaches a certain limit way before 500 photos. In the following plot, we used the 1000 photocount set as reference:

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/std-dev-vs-photocount.png)

Therefore, we decided that for the following evaluation, we remove the data for the results above 502 photos.

## Analysis

We compared the 3D meshes with the 502 photocount mesh as reference. We used ICP to reorient the meshes and cut the base in order to remove some scan artifacts.

### RMS - Error

The RMS (Root Mean Square) error measures the average deviation between each point in the pointclouds and the corresponding surfaces of the 502 photocount reference mesh.

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/rms-error-vs-photocount.png)

### Standard Deviation

Between points in the lower-photocount generated pointclouds and the corresponding surfaces of the 502 photocount reference mesh, the standard deviation reveals the spread or variation in measurement errors.

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/std-dev-vs-photocount-507.png)

### Maximum Distance

Representing the largest measured deviation between any point in the lower-photocount generated pointcloud and the corresponding surface, the maximum distance metric exhibits higher fluctuation and uncertainty. This particular measurement demonstrates significant sensitivity to variations in the mesh structure due to differences in photo quantity.

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/max-distance-vs-photocount-507.png)

### Normal Consistency

The normal consistency quantifies the alignment of surface normals between the lower-photocount generated meshes and the 502 photocount reference mesh. Higher values indicate better preservation of surface orientation details. This metric provides insight into how well meshes created with fewer photos maintain the directional properties of the high-photocount surface, with consistency improving as photocount increases.

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/normal-consistency-vs-photocount-507.png)

## Stabilizing points - or - what is the right amount of photos?

![](/assets/img/posts/2025-03-26-optimizing-3d-scans-how-many-photos-do-you-really-need/summary.jpg)

- **Stabilization Points**:

  - RMS Error stabilizes at 292 photos
  - Standard Deviation stabilizes at 292 photos
  - Normal Consistency stabilizes at 333 photos
  - Maximum Distance does not show clear stabilization within the dataset
- **Confidence Intervals** (calculated from data with photocount > 400):

  - RMS Error: 0.0108 - 0.0130
  - Standard Deviation: 0.0097 - 0.0118
  - Maximum Distance: 0.3976 - 0.5069
  - Normal Consistency: 0.9904 - 0.9918

**Above 300 photos, the metrics clearly reach their plateau and there is no gain in quality with increased photo count above that threshold! So in general it is save to say that 150 photos should give you great results, whereas 300 photos should be considered the maximum for very detailed models.**

## Limitation

We only used one reference set with very distinct and high-contrast surface features. The results might vary slightly with other objects and setups, but we are quite confident, that this number should be valid for a wide range of objects in a turntable setup.

## Conclusion and Implications

The most important thing with photogrammetry is understanding what a good surface looks like (i.e. having a lot of features). The amount of photos in a set plays only a minor role and when 150 photos do not give a good result, increasing the amount of photos will not improve the results significantly. Our testing clearly shows that there's an optimal range of around 150-300 images for turntable photogrammetry, with diminishing returns beyond this point.

**Based on the analysis:**

- **For most objects, 150-200 photos will yield excellent results**
- **Going up to 300 photos may provide marginal improvements for highly detailed models**
- **Exceeding 300 photos only increases processing time without quality benefits**
- **Image quality, lighting, and surface features remain more important factors than raw photo count**

This finding has important practical implications for workflow efficiency. By limiting capture sessions to the optimal range, users can significantly reduce processing times while maintaining high-quality results. The time saved can be better invested in proper lighting setup, surface preparation, or post-processing refinements.

For OpenScan users, we recommend starting with 150-200 photos for most objects and only increasing to 300 for exceptionally detailed models where every surface feature is critical. The results will be implemented in the future firmware revisions, giving some more standardized presets for beginners (while keeping full control in expert mode)
