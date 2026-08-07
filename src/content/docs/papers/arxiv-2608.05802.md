---
title: "On-Policy Delta Distillation for Multilingual Math Reasoning"
description: "On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.05802) · [PDF](https://arxiv.org/pdf/2608.05802)

## 一句话摘要

On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD$^2$), for mathematical reasoning in English, Korean, and Japanese. OPD$^2$ improves OPD by using the probability gap between a post-trained teacher and its base model as the learning signal. Experiments with Qwen3 show that OPD$^2$ consistently outperforms the original OPD, with particularly strong improvements in Korean and Japanese, and generally narrows the English-Korean performance gap. We further find that English-only OPD can also increase performance for Korean and Japanese, but often shifts the responses toward English, highlighting the importance of multilingual data to preserving target-language responses.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
