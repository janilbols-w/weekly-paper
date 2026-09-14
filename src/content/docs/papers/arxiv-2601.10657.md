---
title: "PACEvolve: Enabling Progress-Aware Consistent Evolution"
description: "Self-evolving agents powered by Large Language Models (LLMs) have emerged as a promising direction across diverse domains, including code optimization and scientific discovery, yet their core failure modes remain underexplored."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.10657) · [PDF](https://arxiv.org/pdf/2601.10657)

## 一句话摘要

Self-evolving agents powered by Large Language Models (LLMs) have emerged as a promising direction across diverse domains, including code optimization and scientific discovery, yet their core failure modes remain underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-evolving agents powered by Large Language Models (LLMs) have emerged as a promising direction across diverse domains, including code optimization and scientific discovery, yet their core failure modes remain underexplored. Through a comprehensive empirical study, we identify that the model's reasoning becomes anchored to the local context of current hypotheses, overemphasizing low-level details while neglecting the broader search landscape. As a result, such agents become prone to context pollution and mode collapse, repeatedly revisiting flawed hypotheses and converging on suboptimal solutions. To address this challenge, we propose Progress-Aware Consistent Evolution (PACEvolve), a systematic framework for governing agent memory and search dynamics. PACEvolve overcomes these limitations through three key techniques: (1) Hierarchical Context Management (HCM), which structures historical trajectories while dynamically pruning branches to preserve a high-signal memory state; (2) Momentum-Based Backtracking (MBB), which monitors optimization progress to escape local minima; and (3) a self-adaptive Collaborative Evolution policy (CE) that balances intra-trajectory refinement with inter-trajectory knowledge transfer. By decoupling high-level idea generation from low-level code evaluation, PACEvolve maintains a global view of search momentum and achieves state-of-the-art results across complex evolutionary benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minghao Yan, Bo Peng, Benjamin Coleman, Ziqi Chen, Zhouhang Xie, Shuo Chen, Zhankui He, Noveen Sachdeva, Isabella Ye, Weili Wang, Chi Wang, Ed H. Chi, Fernando Pereira, Wang-Cheng Kang, Derek Zhiyuan Cheng, Beidou Wang
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
