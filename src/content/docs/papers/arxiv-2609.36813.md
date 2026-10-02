---
title: "RESCUE: Repairing Language Model Errors to Sparse Circuits via Reinforcement Learning"
description: "Large language models (LLMs) exhibit strong general capabilities that mechanistic interpretability has attributed to sparse computational circuits."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2609.36813v1) · [PDF](https://arxiv.org/pdf/2609.36813v1)

## 一句话摘要

Large language models (LLMs) exhibit strong general capabilities that mechanistic interpretability has attributed to sparse computational circuits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) exhibit strong general capabilities that mechanistic interpretability has attributed to sparse computational circuits. However, existing circuit studies emphasize preserving functionality or explaining safety, leaving the mechanisms underlying failures across a broader range of tasks largely unexplored. Extending circuit analysis from abilities to errors, we explore the perspective that such failures may likewise arise from erroneous internal computations and that targeted tuning of the corresponding parameters can correct such errors while largely preserving other capabilities. Motivated by this insight, we introduce RESCUE (Reasoning-Error Sparse-Circuit Uncovering and Editing), a framework that localizes error-associated circuits and surgically repairs them for performance enhancement. General tasks typically involve multi-step reasoning and long-form generation, where early deviations can cause prefixes to drift from supervised references, leading SFT-based mask optimization to overlook circuits involved in generation-time errors. RESCUE therefore refines these masks through reinforcement learning with multiple masked-model rollouts, improving their relevance to observed task failures. Finally, RESCUE introduces a pruning technique and precisely fine-tunes error circuits to correct task failures, thereby translating error localization into a sparse and targeted model update. We validate RESCUE on heterogeneous repair sets across two domains: (1) mathematical reasoning, identifying a math error circuit of 1.40% density whose repair raises accuracy from 6.0% to 75.5%; and (2) medical QA, where a similarly compact 1.44% circuit improves repair-set accuracy from 0% to 81%. Our code is available at: https://github.com/chuanpupig/RESCUE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chuanpu Liu, Miao Yu, Yikai Cai, Yuanhe Zhang, Zhenhong Zhou, Li Sun, Zuming Jiang, Yufei Guo
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/chuanpupig/RESCUE](https://github.com/chuanpupig/RESCUE)
- 阅读深度：metadata
