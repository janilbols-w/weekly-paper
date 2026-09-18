---
title: "Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation"
description: "Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.20744) · [PDF](https://arxiv.org/pdf/2609.20744)

## 一句话摘要

Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Video diffusion models repeatedly process long spatiotemporal token sequences during denoising, making attention a major computational bottleneck. Linear attention offers an appealing alternative and has been widely adopted in recent large language models, but directly applying it to video models often fails to preserve the fine-grained interactions required for high-quality generation. We present Video DeltaNet (VDN), which combines local Softmax attention with bidirectional linear memory for long-range video context. Its linear branch introduces Video Delta Attention (VDA), which updates memory once per frame by jointly incorporating its spatial tokens. Separate output projections and learnable gates calibrate the two branches, while a staged teacher-alignment recipe progressively introduces the new pathway into pretrained models. We instantiate VDN on MiniMax H3, applying the hybrid to video-to-video interactions while retaining Softmax for interactions involving text or audio. With eight-step distillation and an optimized SGLang serving stack, VDN-H3 completes DiT denoising for a 14.3-second, 768p video in 6.70 seconds on eight NVIDIA B200 GPUs, corresponding to a 14.5x speedup over the 50-step dense H3 baseline on the same GPU count.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haocheng Xi, Yiming Xie, Hexu Zhao, Yiwen Zhang, Michael Liu, Thomas Creavin, Kurt Keutzer, Xiuyu Li, Zhaoyang Lv, Chenfeng Xu, Haiwen Feng
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
