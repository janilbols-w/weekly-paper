---
title: "Aha-Flow Distillation: Flow Markers Matter in LLM Reasoning"
description: "We identify the Flow Moment, a reasoning pattern characterized by sustained, process-confirming verbalizations such as I'm doing, in contrast to the revision- and backtracking-oriented Aha Moment."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.07036) · [PDF](https://arxiv.org/pdf/2609.07036)

## 一句话摘要

We identify the Flow Moment, a reasoning pattern characterized by sustained, process-confirming verbalizations such as I'm doing, in contrast to the revision- and backtracking-oriented Aha Moment.

## 为什么值得关注

待编辑增强。

## 摘要原文

We identify the Flow Moment, a reasoning pattern characterized by sustained, process-confirming verbalizations such as I'm doing, in contrast to the revision- and backtracking-oriented Aha Moment. We refer to their corresponding linguistic expressions as Flow Markers and Aha Markers, respectively. Based on this observation, we construct Flow-CoT by rewriting the discourse markers of original reasoning traces while preserving their underlying reasoning content, and use it as auxiliary supervision for on-policy self-distillation (OPSD). We further propose \textbf{Aha-Flow Distillation (AFD)}, a dual-mode extension of OPSD that pairs different forms of privileged information with corresponding reasoning instructions. The Aha branch retains concise solution-based supervision, while the Flow branch introduces rewritten Flow-CoT under a direct and confident reasoning instruction. At inference time, the model uses only the standard reflective instruction, so Flow-style reasoning serves purely as a training signal. Experiments on AIME25 and HMMT25 show consistent improvements across Qwen3-8B and Qwen3-4B: AFD improves Avg@12 from 60.8 to 61.3 on Qwen3-8B and from 57.5 to 58.6 on Qwen3-4B over our reproduced OPSD baselines. Controlled ablations further show that, with the same Flow-CoT/Aha-CoT composition, dual-mode training improves Avg@12 from 59.5 to 60.1, indicating that the benefit comes not only from introducing heterogeneous reasoning supervision, but also from how it is organized during self-distillation. The code is available at https://github.com/Wang-Xiaodong1899/Aha-Flow-Distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xiaodong Wang, Peixi Peng
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Wang-Xiaodong1899/Aha-Flow-Distillation](https://github.com/Wang-Xiaodong1899/Aha-Flow-Distillation)
- 阅读深度：metadata
