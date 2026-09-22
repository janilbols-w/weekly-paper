---
title: "Pairwise Ranking Outperforms Single-Action RL for Offline Explanation Selection: A Practical Lesson"
description: "Industrial explainable-recommendation systems built on LLMs incur a substantial serving cost: each request triggers an LLM generation, with latency in the hundreds of milliseconds and cost that scales linearly with traffic."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.18531) · [PDF](https://arxiv.org/pdf/2608.18531)

## 一句话摘要

Industrial explainable-recommendation systems built on LLMs incur a substantial serving cost: each request triggers an LLM generation, with latency in the hundreds of milliseconds and cost that scales linearly with traffic.

## 为什么值得关注

待编辑增强。

## 摘要原文

Industrial explainable-recommendation systems built on LLMs incur a substantial serving cost: each request triggers an LLM generation, with latency in the hundreds of milliseconds and cost that scales linearly with traffic. We separate generation from selection: explanations are produced ahead of time as a frozen candidate pool (six prompt styles, two commodity LLMs), and a small CPU-resident selector picks one at request time. The stack needs no GPU and returns in under 100 ms. Our primary benchmark is a 2,958-pair XRec Google Local subset, evaluating six offline-pool selectors (LambdaRank, PPO, GRPO, DPO, teacher-student distillation) and three KG-path selectors (random walks, edge-disjoint enumeration, MMR-reranked paths). A 300-pair MovieLens-1M split with Claude-Sonnet-4.5 references serves as an internal cross-dataset check, since no public benchmark exists for this setting. All variants use the same BERTScore-F1 protocol as XRec and G-Refer, averaged across five seeds. LambdaRank reaches F1 = 0.500 on Google Local, exceeding both G-Refer and XRec, and F1 = 0.329 on the MovieLens-1M check. With seed variance below 0.003 F1, the ordering is reliable: pairwise learning-to-rank outperforms single-action RL (PPO, GRPO, DPO), which use only one labelled candidate per rollout, leaving K-1 labels unused. The KG-path family targets a different objective: all three variants reach USR = 1.000 on Google Local and 0.997-1.000 on MovieLens-1M, since per-request path grounding yields a unique output per query, avoiding template-collapse failures affecting cached-LLM outputs. A generator-pool study comparing Claude 3 Haiku and Claude Haiku 4.5 shows small F1 shifts (0.001-0.006) while preserving selector ranking: selector and generator can be evaluated independently, though absolute F1 depends on the generator. End-to-end build cost is near $15 on commodity hardware.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tanay Chowdhury, Saeideh Shahrokh Esfahani
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
