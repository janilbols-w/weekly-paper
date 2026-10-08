---
title: "MIRROR: From Imitation to Internalization in LLM Personalization"
description: "The demand for personalized LLMs is shifting from style imitation toward content quality."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.09795) · [PDF](https://arxiv.org/pdf/2610.09795)

## 一句话摘要

The demand for personalized LLMs is shifting from style imitation toward content quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

The demand for personalized LLMs is shifting from style imitation toward content quality. We investigate whether self-distillation can bridge this gap in existing fine-tuning paradigm. To address this limitation, we introduce MIRROR(Meta- personalization by Internalizing Reference-Revealed On-policy Reflections), a novel self-distillation framework that shifts LLM personalization from imitation toward preference internalization. First, we replace reference-token imitation with reference-revealed on-policy self-distillation, aligning the model's next-token distributions along its own generation trajectories with those of its reference-conditioned self, thereby internalizing user preferences rather than reproducing reference wording.Second, we introduce MIRROR-F, a focal plug-in that augments on-policy distributional alignment with selective supervision over informative reference tokens, thereby strengthening content generation while preserving user-specific expression. Across three personalized generation benchmarks, two model scales, and complementary reference-based and LLM-based evaluations, MIRROR and MIRROR-F achieve leading overall personalization performance and superior text quality, while exhibiting less catastrophic forgetting than SFT-based baselines on three unseen personalized generation tasks. The gains are consistent across model scales and application scenarios, translating to improved performance in LLM personalization tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Huayi Lai, Jicheng Yang, Min Yi, Chong Meng
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
