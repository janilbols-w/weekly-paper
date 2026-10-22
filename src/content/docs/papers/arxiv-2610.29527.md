---
title: "RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding"
description: "Speculative decoding accelerates large language model inference by employing a compact draft model to propose candidate tokens that are verified in parallel by a target model."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.29527) · [PDF](https://arxiv.org/pdf/2610.29527)

## 一句话摘要

Speculative decoding accelerates large language model inference by employing a compact draft model to propose candidate tokens that are verified in parallel by a target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by employing a compact draft model to propose candidate tokens that are verified in parallel by a target model. Conventional training relies on soft-label distillation, which forces the draft model to mimic the target's full output distribution, including high-entropy regions that degrade acceptance rates and increase early rejection risk. We propose RCSD (Reinforcement and Continual Learning for Speculative Decoding), a training framework that aligns draft model optimization with the system-level objective of maximizing acceptance length. RCSD leverages naturally occurring accepted and rejected sequences during speculative inference to construct implicit preference pairs, with masked loss to avoid penalizing target-aligned tokens. Evaluated across multiple benchmarks, RCSD improves average acceptance length by 35% over HASS and achieves 1.35x faster end-to-end inference than HASS on practical workloads, without compromising generation quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mingkang Liu, Weiming Meng, Peipei Jiao, Jiawei Zhang, Tianyuan Liu, Junyan Li, Lichen Pang
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
