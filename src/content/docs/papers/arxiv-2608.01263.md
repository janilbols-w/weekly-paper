---
title: "Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models"
description: "On-policy distillation (OPD) samples trajectories from the current student policy and minimizes token-level divergence between student and teacher next-token distributions at prefixes along those trajectories."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.01263) · [PDF](https://arxiv.org/pdf/2608.01263)

## 一句话摘要

On-policy distillation (OPD) samples trajectories from the current student policy and minimizes token-level divergence between student and teacher next-token distributions at prefixes along those trajectories.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) samples trajectories from the current student policy and minimizes token-level divergence between student and teacher next-token distributions at prefixes along those trajectories. This aligns the distillation states with the student's own generation distribution. However, it still assumes that the complete teacher distribution is an appropriate target across student capacities. In vision--language reasoning, teacher corrections can depend on visual distinctions that a compact student cannot represent. Our target-scaling study shows that, as the target approaches the complete teacher distribution, the student realizes less of the prescribed shift and obtains worse downstream performance. We therefore propose \emph{Fisher-Projected On-Policy Distillation} (FP-OPD), which distills only locally realizable teacher corrections. FP-OPD uses continuous visual perturbations to estimate the student's local visual tangent space and projects the centered teacher--student log-probability gap onto this space under the student's Fisher metric. The resulting capacity-aware target is optimized with full-vocabulary reverse KL on student trajectories, retaining the standard OPD framework. In 8B-to-2B distillation, FP-OPD improves all seven evaluated multimodal benchmarks. It raises the average score by 2.77 points over the pretrained student and by 1.60 points over standard OPD. These results demonstrate that locally realizable teacher corrections provide a more effective target for distilling compact vision--language models.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leyan Xue, Feng Xiong, Mingjun Ma, Changqing Zhang
- 发布：2026-08-04；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
