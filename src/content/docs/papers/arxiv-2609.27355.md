---
title: "Quantization-Robust Unlearning through the Lens of Retain-Forget Loss Landscapes Interaction"
description: "Unlearning ensures LLM compliance by removing the influence of private or copyrighted training data."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.27355) · [PDF](https://arxiv.org/pdf/2609.27355)

## 一句话摘要

Unlearning ensures LLM compliance by removing the influence of private or copyrighted training data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unlearning ensures LLM compliance by removing the influence of private or copyrighted training data. However, since LLM models typically undergo post-training compression, like quantization, in practical deployment, it has been observed that the unlearning effect can be substantially weakened, with the forgetting behavior degrading more severely than that of model utility. This paper proposes a quantization-robust unlearning framework that makes forgetting robust to quantization while maintaining overall model utility. We analyze this gap through the lens of loss landscape. Specifically, our analysis reveals a curvature-based criteria that pinpoints sensitive weights in the unlearned model that leads to both non-robust forgetting and reduced utility. We therefore propose sensitivity-guided noisy regularization, which is applied on the sensitive parameters to steer the model convergence towards a smoother minima of uniformly low forget and retain losses. Balancing unlearning and utility, we further propose forget-critical optimization, which updates only forget-critical layers, preserving most of the network to retain useful knowledge. Extensive experiments on the MUSE and TOFU benchmarks across multiple LLM unlearning algorithms show that our approach achieves substantially more quantization-resilient forgetting while maintaining utility.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jialu Wang, Jianing Deng, Shuqing Luo, Yuanzhe Li, Dongwei Wang, Jingtong Hu, Huanrui Yang, Song Wang, Tianlong Chen
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
