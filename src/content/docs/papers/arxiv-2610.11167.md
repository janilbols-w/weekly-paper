---
title: "PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation"
description: "Vertical-domain few-shot classification remains challenging for small language models, as limited supervision makes it difficult to acquire domain-specific decision knowledge."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.11167) · [PDF](https://arxiv.org/pdf/2610.11167)

## 一句话摘要

Vertical-domain few-shot classification remains challenging for small language models, as limited supervision makes it difficult to acquire domain-specific decision knowledge.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vertical-domain few-shot classification remains challenging for small language models, as limited supervision makes it difficult to acquire domain-specific decision knowledge. On-Policy Distillation (OPD) can improve teacher-guided adaptation by supervising student-generated rollouts, while GRPO-based reinforcement learning can further refine downstream predictions. However, existing KD-to-RL pipelines typically rely on globally fixed transition schedules, ignoring that different samples may require different amounts of teacher-guided acquisition before reward-driven refinement. We propose PIVOT (Perplexity-Informed Transition Optimization), a dynamic transition framework that routes samples between OPD and GRPO according to teacher-evaluated sequence perplexity. PIVOT moves low-perplexity samples to GRPO for reward-driven refinement while keeping high-perplexity samples under OPD for continued domain knowledge acquisition. Experiments on Banking77 and HWU64 show that PIVOT consistently outperforms continued OPD and globally synchronized OPD$\rightarrow$GRPO baselines under the same number of post-warm-up student optimization steps, achieving stronger downstream performance and more stable training dynamics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Heng Li, Yong Zhang, Ning Cheng, Zhigen Li, Yun Zhu, Yanmeng Wang, Shaojun Wang, Jing Xiao
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
