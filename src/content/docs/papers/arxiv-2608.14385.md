---
title: "DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding"
description: "Mixture-of-Experts (MoE) models have been widely adopted in real-time interactive applications such as coding assistants, real-time audio-video interaction systems."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2608.14385) · [PDF](https://arxiv.org/pdf/2608.14385)

## 一句话摘要

Mixture-of-Experts (MoE) models have been widely adopted in real-time interactive applications such as coding assistants, real-time audio-video interaction systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models have been widely adopted in real-time interactive applications such as coding assistants, real-time audio-video interaction systems. To meet the extremely low response latency requirements of these scenarios, practitioners commonly employ small-batch decoding, under which MoE inference becomes memory-bound and is severely bottlenecked by expert weight loading. However, this bottleneck has received limited attention, and existing solutions such as post-training weight compression or fine-grained expert design during pre-training either degrade model accuracy or introduce additional computation and communication overhead. To tackle this issue, we propose DeaMoE, a decoding-efficient MoE architecture, in which the experts are grouped into several departments, and the experts belonging to the same department share most parameters since they come from the same professional field, and additionally each expert contains a few private parameters to reflect its uniqueness. Moreover, we design customized two-stage routing strategy for DeaMoE to avoid redundant loading, under which DeaMoE greatly improves the efficiency during LLM decoding. Compared with vanilla MoE, DeaMoE reduces per-step loaded weights by up to 50.9% and achieves up to 1.33 end-to-end TPOT speedup for the pre-trained 7B model on A40, and up to 2.00x and 1.97x peak speedup for DeepSeek-V3 on A40 and H100 in microbenchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zewen Jin, Shen Fu, Zeping Duan, Shannon Wang, Weihao Wu, Chengjie Tang, Congkun Ai, Ping Gong, Zijian Dai, Youhui Bai, Cheng Li
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
