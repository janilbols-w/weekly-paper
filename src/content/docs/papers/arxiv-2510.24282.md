---
title: "TsetlinKWS: A 65nm 16.58uW, 0.63mm2 State-Driven Convolutional Tsetlin Machine-Based Accelerator For Keyword Spotting"
description: "The Tsetlin Machine (TM) has recently attracted attention as a low-power alternative to neural networks due to its simple and interpretable inference mechanisms."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2510.24282) · [PDF](https://arxiv.org/pdf/2510.24282)

## 一句话摘要

The Tsetlin Machine (TM) has recently attracted attention as a low-power alternative to neural networks due to its simple and interpretable inference mechanisms.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Tsetlin Machine (TM) has recently attracted attention as a low-power alternative to neural networks due to its simple and interpretable inference mechanisms. However, its performance on speech-related tasks remains limited. This paper proposes TsetlinKWS, the first algorithm-hardware co-design framework for the Convolutional Tsetlin Machine (CTM) on the 12-keyword spotting task. Firstly, we introduce a novel Mel-Frequency Spectral Coefficient and Spectral Flux (MFSC-SF) feature extraction scheme together with spectral convolution, achieving a record-high accuracy of 87.35% for TM-based models on the 12-keyword spotting task. Secondly, we develop an Optimized Grouped Block-Compressed Sparse Row (OG-BCSR) algorithm that delivers a remarkable 9.84$\times$ reduction in model size, significantly improving the storage efficiency of CTMs. Finally, we propose a state-driven architecture tailored for CTMs, which simultaneously exploits data reuse and sparsity to attain high energy efficiency. The full system is evaluated in 65 nm process technology, consuming 16.58 $\mu$W at 0.7 V with a compact 0.63 mm$^2$ core area. TsetlinKWS demonstrates a Power-Performance-Area (PPA) product of 60.2 and requires only 907k logic operations per inference, corresponding to 1.4$\times$ and 10$\times$ reductions, respectively, compared with state-of-the-art KWS accelerators. These results position the CTM as a highly efficient candidate for ultra-low-power speech applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 9 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Baizhou Lin, Yuetong Fang, Renjing Xu, Rishad Shafik, Jagmohan Chauhan
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
