---
title: "LightDenseYOLO"
collection: publications
permalink: /publication/paper2_lightDenseYOLO
excerpt: 'Use lightweight CNN architecture to detect and track marker using Kalman filter.'
date: 2018-05-24
venue: 'Sensors'
paperurl: 'https://www.mdpi.com/1424-8220/18/6/1703'
citation: 'Nguyen, P.H.; Arsalan, M.; Koo, J.H.; Naqvi, R.A.; Truong, N.Q.; Park, K.R. LightDenseYOLO: A Fast and Accurate Marker Tracker for Autonomous UAV Landing by Visible Light Camera Sensor on Drone. Sensors 2018, 18, 1703.'
---
### Abstract:
Autonomous landing of an unmanned aerial vehicle or a drone is a challenging problem for the robotics research community. Previous researchers have attempted to solve this problem by combining multiple sensors such as global positioning system (GPS) receivers, inertial measurement unit, and multiple camera systems. Although these approaches successfully estimate an unmanned aerial vehicle location during landing, many calibration processes are required to achieve good detection accuracy. In addition, cases where drones operate in heterogeneous areas with no GPS signal should be considered. To overcome these problems, we determined how to safely land a drone in a GPS-denied environment using our remote-marker-based tracking algorithm based on a single visible-light-camera sensor. Instead of using hand-crafted features, our algorithm includes a convolutional neural network named lightDenseYOLO to extract trained features from an input image to predict a marker’s location by visible light camera sensor on drone. Experimental results show that our method significantly outperforms state-of-the-art object trackers both using and not using convolutional neural network in terms of both accuracy and processing time.

### lightDenseNet: 
![](../images/lightDenseYOLO/1.png)

### Comparing with SOTA object detectors
![](../images/lightDenseYOLO/2.png)

### More qualitative results
![](../images/lightDenseYOLO/3.png)
![](../images/lightDenseYOLO/4.png)