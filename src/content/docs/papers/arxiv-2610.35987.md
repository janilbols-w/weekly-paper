---
title: "PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix"
description: "Proactive bug discovery is an important software-engineering problem."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.35987) · [PDF](https://arxiv.org/pdf/2610.35987)

## 一句话摘要

Proactive bug discovery is an important software-engineering problem.

## 为什么值得关注

待编辑增强。

## 摘要原文

Proactive bug discovery is an important software-engineering problem. Even though coding agents are already widely deployed in this domain, their capabilities remain understudied. In particular, the challenging task of finding all bugs that human maintainers would repair across an entire repository has not been studied yet. To close this gap, we introduce PROBE, a benchmark consisting of all 2,457 bugs fixed over the course of 18 months across 20 diverse GitHub repositories, together with a method for matching candidate findings to this partial reference set. We evaluate coding agents across frontier models and find they all achieve a recall of below $21\%$ and a precision of less than $9\%$ with respect to the reference set. While stronger models increase recall substantially from $8\%$ to $17\%$, they do not improve precision. Surprisingly, despite the low precision, LLM and human evaluators still judge $85\%$ of findings valid. Crucially, we find that found bug distributions are similar across agents but differ substantially from those of bugs fixed by maintainers. The practical relevance of bug discovery and the low recall of frontier models make this benchmark a valuable resource for both model users and developers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Marco Paina, Mark Niklas M\"uller, Niels M\"undler-Sasahara, Martin Vechev
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
