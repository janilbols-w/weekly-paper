---
title: "QVal: Evaluating Dense Supervision Signals for Long-Horizon LLM Agents"
description: "LLM agents increasingly act over long horizons, where outcome-only rewards say little about which intermediate actions were good."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.32034) · [PDF](https://arxiv.org/pdf/2606.32034)

## 一句话摘要

LLM agents increasingly act over long horizons, where outcome-only rewards say little about which intermediate actions were good.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents increasingly act over long horizons, where outcome-only rewards say little about which intermediate actions were good. Dense supervision methods address this by scoring intermediate steps, but they are usually evaluated through the downstream performance of a full training pipeline. This is expensive, confounds signal quality with other training choices, and means that methods are rarely compared on common ground. We introduce QVal, a training-free testbed that measures the $Q$-alignment of a dense signal: whether it orders the candidate actions in each state the same way as their returns under a reference policy do. We benchmark 21 methods from seven families with six open-weight backbones in four environments. Simple prompting baselines are the most $Q$-aligned on average, and performance clusters strongly by family. Code-generated signals do well only in small state and action spaces; embedding-based signals are weak; self-distillation signals are anti-aligned; and no method is $Q$-aligned in open-ended environments. When five of these signals guide an actor at test time by choosing among four proposed actions, $Q$-alignment strongly correlates with the gain in task success. QVal is designed to be easily extensible to new environments and methods, enabling researchers to compare new signals cheaply before committing to a training run.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Sergio Hern\'andez-Guti\'errez, Matteo Merler, Ilze Amanda Auzina, Joschka Str\"uber, Ameya Prabhu, Matthias Bethge
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
