---
title: "OdysSim: Building Foundation Models for Human Behavior Simulation"
description: "Large language models are increasingly deployed as human simulators for interactive evaluation and social simulation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.14199) · [PDF](https://arxiv.org/pdf/2606.14199)

## 一句话摘要

Large language models are increasingly deployed as human simulators for interactive evaluation and social simulation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly deployed as human simulators for interactive evaluation and social simulation. Yet helpfulness-driven post-training pulls them toward a homogeneous, overly agreeable assistant register, creating a behavioral Sim2Real gap. We present OdysSim, the largest open systematic investigation of behavioral foundation models, i.e., models trained to simulate human behavior at scale. We propose SOUL, a taxonomy of five capability axes (CONV, SS, COG, ROLE, EVAL) that unifies 62 datasets and 23 benchmark tasks under one framework. Specifically, we curate the OdysSim corpus (21.4M interactions, 10B tokens, retrofitted with back-generated social contexts), construct the SOUL-Index benchmark, and develop an end-to-end training recipe combining midtraining, task-specific RL, and expert distillation. The resulting open 8B OSim model ranks first or tied-first on 8 of 23 tasks, outperforming any individual frontier model by this count, with the strongest gains on conversational and social tasks. Its outputs are also more human-like in length, formatting, and word choice, and it transfers zero-shot to out-of-distribution user simulation on $\tau$-bench, nearly matching real users on reaction alignment (93.2 vs. 93.5). We further show that LLM-as-judge RL induces reward-hacking patterns, and that our detectors can mitigate them during post-training. Together, our findings suggest that behavioral foundation models require rethinking the LLM training paradigm. We release all artifacts to support future research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuhui Zhou, Weiwei Sun, Weihua Du, Jiarui Liu, Haojia Sun, Qianou Ma, Tongshuang Wu, Yiming Yang, Maarten Sap
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
