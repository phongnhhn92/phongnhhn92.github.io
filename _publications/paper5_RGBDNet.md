---
title: "RGBD-Net: Predicting color and depth images for novel views synthesis"
collection: publications
permalink: /publication/paper5_RGBDNet
excerpt: 'A new method called RGBD-Net is proposed to predict the depth map and the color images at the target pose. RGBD-Net produces high-quality novel views and depth maps. We also shows better 3D reconstruction than MVS methods.'
date: 2020-11-29
venue: 'arXiv'
---
### Abstract:
<div style="text-align: justify"> We address the problem of novel view synthesis from an unstructured set of reference images. A new method called RGBD-Net is proposed to predict the depth map and the color images at the target pose in a multi-scale manner. The reference views are warped to the target pose to obtain multi-scale plane sweep volumes, which are then passed to our first module, a hierarchical depth regression network which predicts the depth map of the novel view. Second, a depth-aware generator network refines the warped novel views and renders the final target image. These two networks can be trained with or without depth supervision. In experimental evaluation, RGBD-Net not only produces novel views with higher quality than the previous state-of-the-art methods, but also the obtained depth maps enable reconstruction of more accurate 3D point clouds than the existing multi-view stereo methods. The results indicate that RGBD-Net generalizes well to previously unseen data. </div>


[[Download]](https://arxiv.org/abs/2011.14398)

### Overview of RGBD-Net: 
![](../images/RGBDNet/1.png)

### NovelDepth network:
![](../images/RGBDNet/2.png)

### Depth-aware refinement network 
![](../images/RGBDNet/3.png)

### Quantiative and Qualitative results on view synthesis 
![](../images/RGBDNet/4.png)

### Qualitative results on 3D reconstruction
![](../images/RGBDNet/5.png)

### More qualitative results on view synthesis 
![](../images/RGBDNet/6.png)
![](../images/RGBDNet/7.png)
![](../images/RGBDNet/8.png)

### More qualitative results on 3D pointcloud reconstruction
![](../images/RGBDNet/9.png)
![](../images/RGBDNet/10.png)
![](../images/RGBDNet/11.png)
