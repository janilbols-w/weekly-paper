---
title: "GRAFT: Adaptive DLM-Based Draft Tree Construction with Target-Distilled Edge Scoring"
description: "Tree-based speculative decoding raises the mean accepted tokens of standard speculative decoding by verifying multiple draft paths, and existing tree builders typically construct these paths through parent-conditioned expansion, where each child token is generated conditioned on its parent path."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.20375) · [PDF](https://arxiv.org/pdf/2608.20375)

## 一句话摘要

Tree-based speculative decoding raises the mean accepted tokens of standard speculative decoding by verifying multiple draft paths, and existing tree builders typically construct these paths through parent-conditioned expansion, where each child token is generated conditioned on its parent path.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tree-based speculative decoding raises the mean accepted tokens of standard speculative decoding by verifying multiple draft paths, and existing tree builders typically construct these paths through parent-conditioned expansion, where each child token is generated conditioned on its parent path. This construction is incompatible with diffusion language model (DLM) drafters such as DFlash, which produces all future-position distributions in a single forward pass. DDTree bridges this gap by treating high-probability tokens from each future-position distribution as candidate nodes and selecting edges between consecutive positions under a fixed node budget. However, its edge selection relies on token probability alone without modeling parent--child compatibility, so target-compatible tokens can be attached to wrong parents; moreover, its fixed budget ignores that the throughput-optimal tree size varies with the decoding state. We propose GRAFT, a draft-tree construction framework for DLM-based speculative decoding. GRAFT introduces Target-Distilled Edge Scoring (TDES), which distills parent--child preferences from target-model traces to select target-compatible edges, and State-Aware Budget Allocation (SABA), which sets the per-round tree budget by balancing expected draft gain against verification cost. Across multiple models and tasks, GRAFT achieves $2.13\times$--$6.36\times$ end-to-end speedup over autoregressive decoding while adding less than $0.5$\,ms of overhead per round, approximately $1.4\%$ of the target-model verification latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuming Ye, Zeming Ma, Runjie Yu, Yuan Liu, Tianle Li, Shuhan Bai, Jian Zhou, Fei Wu
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
