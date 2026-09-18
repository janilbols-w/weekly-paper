---
title: "M2Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models"
description: "Recent advancements have successfully adapted autoregressive language models to process multimodal signals, such as images and actions."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.18259) · [PDF](https://arxiv.org/pdf/2609.18259)

## 一句话摘要

Recent advancements have successfully adapted autoregressive language models to process multimodal signals, such as images and actions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advancements have successfully adapted autoregressive language models to process multimodal signals, such as images and actions. Since raw action signals are continuous, effective tokenization is essential to map high-dimensional inputs into compact discrete tokens for autoregressive processing. However, existing discrete action tokenizers often suffer from high reconstruction loss, failing to preserve the fine-grained dynamics required for precise control. This "discretization bottleneck" significantly limits the performance ceiling of downstream Vision-Language-Action (VLA) models. To address this, we propose ${M}^2$Tok, a Multi-head Multi-codebook Action Tokenizer designed to minimize reconstruction error and enhance policy performance. Our approach introduces two key structural innovations: (1) we decompose the latent action features into multiple heads, enabling the model to implicitly align specific heads with distinct action dimensions; (2) we assign independent codebooks to each head for quantization. By leveraging the combinatorial nature of multiple codebooks, we significantly expand the representational expressivity of the tokenizer, leading to substantially lower reconstruction loss compared to previous methods. We evaluate the ${M}^2$Tok-based VLA on the RoboTwin, Simpler-Env, and 3 zero-shot real-world tasks. Experimental results demonstrate our method not only achieves superior reconstruction fidelity but also significantly boosts the success rate of VLA models. Comprehensive ablation studies further confirm the effectiveness of the multi-head and multi-codebook mechanisms. Code is available at https://github.com/cpaaax/M2Tok.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chunpu Xu, Zhixuan Liang, Yuhao Zhang, Chi-Min Chan, Jessie Wang, Yang Xiao, Mengkang Hu, Xiaokang Yang, Yao Mu
- 发布：2026-09-16；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/cpaaax/M2Tok](https://github.com/cpaaax/M2Tok)
- 阅读深度：metadata
