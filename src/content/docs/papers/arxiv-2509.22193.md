---
title: "Scale or Reason? A Compute-Equivalent Analysis of Reasoning Distillation"
description: "Distilling reasoning traces from strong teacher models has become the standard recipe for building capable small language models."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2509.22193) · [PDF](https://arxiv.org/pdf/2509.22193)

## 一句话摘要

Distilling reasoning traces from strong teacher models has become the standard recipe for building capable small language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distilling reasoning traces from strong teacher models has become the standard recipe for building capable small language models. Yet reasoning traces are 5-20$\times$ longer than standard instruction fine-tuning (IFT) outputs, meaning every practitioner who chooses reasoning distillation implicitly forgoes training a larger IFT model on the same compute budget. Whether this trade-off is worthwhile remains unaddressed. We study it with a controlled experiment: a single teacher generates paired IFT and reasoning outputs for identical prompts by toggling only its reasoning mode, isolating supervision format as the sole variable. Training students at five scales (0.5B to 14B) and evaluating on 18 benchmarks, we find that at matched FLOPs, IFT lies on or near the Pareto frontier across the majority of configurations. Reasoning reaches the Pareto frontier only on open-ended tasks at 7B and above. Even there, a sequential curriculum mixing just 25-50\% reasoning data with IFT captures most of the accuracy benefit at far lower compute cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nicolas Boizard, Hippolyte Gisserot-Boukhlef, Kevin El Haddad, C\'eline Hudelot, Pierre Colombo
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
