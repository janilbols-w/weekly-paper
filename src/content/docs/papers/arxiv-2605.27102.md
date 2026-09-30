---
title: "Equivalent Flows, Unequal Learning: Clean-Latent Prediction in Transformers"
description: "Flow samplers consume velocity, but the neural network can predict the clean endpoint and convert it to velocity through a fixed affine readout."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2605.27102) · [PDF](https://arxiv.org/pdf/2605.27102)

## 一句话摘要

Flow samplers consume velocity, but the neural network can predict the clean endpoint and convert it to velocity through a fixed affine readout.

## 为什么值得关注

待编辑增强。

## 摘要原文

Flow samplers consume velocity, but the neural network can predict the clean endpoint and convert it to velocity through a fixed affine readout. We study this choice with JLT, a latent Transformer in a frozen variational autoencoder (VAE) representation. For squared error, the optimal clean and velocity predictors are algebraically equivalent; a finite Transformer assigns different computation to its learned output under the two interfaces. A local Gaussian analysis identifies a known residual response supplied by the readout and isotropic target variance added by velocity prediction. Measured FLUX.2 channel spectra support this geometric distinction: 90% of target variance occupies 83 of 128 clean directions versus 109 velocity directions. Under a matched velocity objective, clean prediction improves ImageNet FID-50K from 6.56 to 2.70 at Base scale and from 2.12 to 1.47 at Large scale, with lower FID at every measured Large checkpoint. Scaling clean prediction to 951M parameters reaches FID-50K 1.19 and IS 271.96. In addition, an objective ablation at Base scale shows that direct clean regression reaches FID-50K 2.38 without time-dependent error weighting. These results show how moving known computation outside the network changes learning under algebraically equivalent flow interfaces. Code: https://github.com/akatsuki-neo/JLT/blob/main/README.md

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Funing Fu, Tenghui Wang, Guanyu Zhou, Junyong Cen, Qichao Zhu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/akatsuki-neo/JLT/blob/main/README.md](https://github.com/akatsuki-neo/JLT/blob/main/README.md)
- 阅读深度：metadata
