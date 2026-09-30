---
title: "Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation"
description: "Specializing large language models to vertical domains improves domain-specific behavior but often degrades general capabilities."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.26735) · [PDF](https://arxiv.org/pdf/2608.26735)

## 一句话摘要

Specializing large language models to vertical domains improves domain-specific behavior but often degrades general capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Specializing large language models to vertical domains improves domain-specific behavior but often degrades general capabilities. We study this trade-off in Multi-Teacher On-Policy Distillation (MOPD), where a specialized model learns from domain and general teachers on its own sampled trajectories. Standard MOPD faces two limitations: ordinary on-policy sampling rarely exposes tokens with large positive teacher--student advantages, and advantage sign alone does not establish whether the proposed update direction is reliable. We propose Uncertainty-Calibrated MOPD (UCMOPD), which addresses these limitations through two complementary mechanisms. Golden-Gain Enhancement combines higher-temperature exploration with a standard-temperature anchor and retains trajectories whose positive learning signal matches or exceeds the prompt-specific anchor. Teacher-Endorsement Filtering then uses centered log-likelihood (CLL) to estimate each retained token's plausibility relative to the teacher's uncertainty and probabilistically preserves updates whose directions are supported by that endorsement. Across role-playing and medical-domain specialization, UCMOPD improves the general-capability average over standard MOPD by $4.48\%$ and $7.86\%$, respectively, while maintaining vertical-domain performance. Component ablations and diagnostic analyses support the intended roles of the two mechanisms: exposing and selecting stronger positive signals at the trajectory level and validating update directions through teacher endorsement at the token level.

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

- 作者：Ziyuan Liu, Jiao Ou, Jian Liang, Ruiming Tang, Cheng Luo
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
