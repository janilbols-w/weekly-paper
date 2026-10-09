---
title: "KDFP: A first-principles approach to knowledge distillation in large language models"
description: "Knowledge distillation is an established technique for improving the capabilities of small, efficient student models by training them with the representations of larger, more capable teacher models."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.10854) · [PDF](https://arxiv.org/pdf/2610.10854)

## 一句话摘要

Knowledge distillation is an established technique for improving the capabilities of small, efficient student models by training them with the representations of larger, more capable teacher models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation is an established technique for improving the capabilities of small, efficient student models by training them with the representations of larger, more capable teacher models. Much of the recent work in the distillation of large language models (LLMs) has focused on distilling abilities learned during post-training, such as instruction following, chain-of-thought reasoning, and tool usage. This has left a large research gap in general knowledge distillation for LLMs, which is essential for developing efficient and private systems suitable for deployment on edge devices. We take a first-principles approach, evaluating previous lessons from prior works and conducting new explorations to develop a distillation methodology suitable for modern LLMs. We present KDFP, a novel methodology for white-box general knowledge distillation in LLMs. We demonstrate that KDFP outperforms existing methods by 1.6% $-$ 4.9% across 9 benchmarks while increasing training efficiency by up to 99.1% through ephemeral parameter reduction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ryan Swift, Konstantinos Psounis
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
