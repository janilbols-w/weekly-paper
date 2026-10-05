---
title: "Exploring the Trade-Off Between Structured Pruning and Fault Tolerance in Deep Neural Networks for Space Applications"
description: "Deep Neural Networks (DNNs) inherently exhibit a degree of robustness to bit-level faults due to their distributed representation of information."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.03117) · [PDF](https://arxiv.org/pdf/2610.03117)

## 一句话摘要

Deep Neural Networks (DNNs) inherently exhibit a degree of robustness to bit-level faults due to their distributed representation of information.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep Neural Networks (DNNs) inherently exhibit a degree of robustness to bit-level faults due to their distributed representation of information. As a model increases in width, this information becomes more dispersed, theoretically reducing the impact of any single bit fault. In this paper, we empirically investigate the relationship between model width and robustness to Single Event Upsets (SEUs). We conduct a comprehensive experiment in which baseline models undergo iterative structured pruning to reduce their width while preserving task performance as much as possible. At each pruning stage, we run a targeted fault-injection campaign to evaluate the model's performance under simulated bit-flip scenarios. Our results show that, although structured pruning increases per-inference sensitivity to faults by reducing redundancy, this effect is effectively counterbalanced by shorter execution time, which lowers the probability of encountering an SEU. These findings suggest that structured pruning can yield significant energy and latency savings without compromising overall reliability, providing useful guidance for designing robust AI systems for space applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Toon Vinck, Na\"in Jonckers, Jaro De Roose, Jeffrey Prinzie, Peter Karsmakers
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
