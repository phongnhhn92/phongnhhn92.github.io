---
title: "Generative Adversarial Query Network"
collection: publications
permalink: /publication/paper3_GAQN
excerpt: 'Combining Generative Query Network and Generative Adversarial Network for view synthesis.'
date: 2019-05-12
venue: 'SCIA'
---
### Abstract:
<div style="text-align: justify"> The problem of predicting a novel view of the scene using an arbitrary number of observations is a challenging problem for computers as well as for humans. This paper introduces the Generative Adversarial Query Network (GAQN), a general learning framework for novel view synthesis that combines Generative Query Network (GQN) and Generative Adversarial Networks (GANs). The conventional GQN encodes input views into a latent representation that is used to generate a new view through a recurrent variational decoder. The proposed GAQN builds on this work by adding two novel aspects: First, we extend the current GQN architecture with an adversarial loss function for improving the visual quality and convergence speed. Second, we introduce a feature-matching loss function for stabilizing the training procedure. The experiments demonstrate that GAQN is able to produce high-quality results and faster convergence compared to the conventional approach. </div>

[[Download]](https://link.springer.com/chapter/10.1007/978-3-030-20205-7_2)

### Overview of GAQN: 
![](../images/GAQN/1.png)

### More qualitative results
![](../images/GAQN/2.png)
![](../images/GAQN/3.png)

### Comparision of generator and discriminator training loss between our proposed GAQN and GQN+GAN: 
![](../images/GAQN/4.png)