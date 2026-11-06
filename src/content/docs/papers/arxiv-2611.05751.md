---
title: "Scheduling Data to Compute: Hierarchical Data Pipelining for LLM Training on AMD GPUs"
description: "Large language models (LLM) have been the key focus of recent machine learning breakthroughs."
---

**评分：50/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2611.05751) · [PDF](https://arxiv.org/pdf/2611.05751)

## 一句话摘要

Large language models (LLM) have been the key focus of recent machine learning breakthroughs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLM) have been the key focus of recent machine learning breakthroughs. As the model size grows exponentially, the computation needed for training is astronomical. A GPU can do a huge amount of arithmetic. However, the data its compute units need is not always available when they are ready. This data may still be in slow memory or on another GPU. While the chip waits, expensive compute sits idle, and at scale even a small drop in utilization translates into substantial cost. In this paper, we treat this waiting time as the primary bottleneck. We focus on hardware features designed for explicit data movement. These features load data from off-chip memory onto the chip, rearrange it into the layout the computation requires as it is loaded, and transfer it between GPUs. By orchestrating them, we keep a steady pipeline of data flowing to the compute units so that they remain busy. We present kernel and framework implementations that address this bottleneck using three key data-movement instructions and hardware features. The Tensor Data Mover (TDM) moves tensor data from high-bandwidth memory (HBM) into on-chip memory. Transpose-load instructions transpose tensor data into the layout that LLM computations require as it is loaded on-chip. Finally, System DMA (SDMA) and Remote DMA (RDMA) move data between GPUs over the scale-up and scale-out networks, respectively. Our results show that TDM and transpose-load provide on average 1.88x and 1.19x speedup at the kernel level, respectively. The SDMA and RDMA lead to on average 1.16x and 1.33x speedup for computation overlapped with communication. This is the first AMD LLM training system to utilize all the GPU data pipelining features. Our implementation has been integrated into open source framework and library for AMD GPUs. https://github.com/AMD-AGI/Primus-Turbo https://github.com/AMD-AGI/Primus

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: rdma
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Gengyu Rao, Ghadeer Ahmed H Alabandi, Su Ann Chong, Thomas Huber, Kailash Gogineni, Subhajit Dutta Chowdhury, Saleel Kudchadker, Suchita Pati, Zirui Zhang, Zhen Huang, Yanyuan Qin, Xiaoming Peng, Lihuan Zhang, Botao Hu, Wei Huang, Yang Bo, Wen Xie, Xiangyu Zhao, Ruibin Zhang, Xiaobo Chen, Vidushi Goyal, Anshu Raina, Claire Songhyun Lee, Jiakun Yan, Yao Fu, Nusrat Islam, Ravi Dwivedula, Jie Zhang, Maria Garzaran, Zhenyu Gu, Emad Barsoum
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AMD-AGI/Primus-Turbo](https://github.com/AMD-AGI/Primus-Turbo)
- 阅读深度：metadata
