---
title: "HiLo-RD: Cross-Budget Self-Distillation for Masked Diffusion Language Models"
description: "We propose HiLo-RD (High-to-Low Budget Representation Distillation) to improve masked diffusion language models (MDLMs) under a limited generation budget."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.36901) · [PDF](https://arxiv.org/pdf/2610.36901)

## 一句话摘要

We propose HiLo-RD (High-to-Low Budget Representation Distillation) to improve masked diffusion language models (MDLMs) under a limited generation budget.

## 为什么值得关注

待编辑增强。

## 摘要原文

We propose HiLo-RD (High-to-Low Budget Representation Distillation) to improve masked diffusion language models (MDLMs) under a limited generation budget. Unlike autoregressive models, MDLMs choose both what to generate and where to commit it. This creates two coupled challenges: predicting useful content before reasoning is complete, and deciding when to fix answer tokens that shape later predictions. We identify budget-induced premature commitment: even when a correct solution fits, the model can fix answer fragments near the window boundary before resolving intermediate steps. These fragments become context for later predictions and redirect subsequent reasoning. Existing post-training methods do not directly transfer the stronger trajectories that the same model follows with a larger window. HiLo-RD addresses this gap by (1) pairing large-window teacher states with cropped small-window views and (2) matching their hidden representations at committed positions. This supervision guides both token prediction and commitment order without an external teacher. Across mathematics benchmarks, HiLo-RD improves low-budget accuracy and shortens responses; these gains extend to code generation without code-domain training. On GSM8K, accuracy rises by 9.4 percentage points as mean readable length falls by about 25%. Attention diagnostics and fixed-budget order interventions support the proposed mechanism. Together, these results show that large-window reasoning can improve small-window decoding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiang Li, Chengting Yu, Jungang Li, Yilun Zheng, Junzhuo Li, Xingyao Zhang, Wenbo Su, Xuming Hu
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
