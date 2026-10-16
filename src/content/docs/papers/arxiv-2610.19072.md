---
title: "Tracing Knowledge Lineage for Federated Unlearning under Mutual Distillation"
description: "An edge server and nearby devices can train language models of different sizes together by mutual distillation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.19072) · [PDF](https://arxiv.org/pdf/2610.19072)

## 一句话摘要

An edge server and nearby devices can train language models of different sizes together by mutual distillation.

## 为什么值得关注

待编辑增强。

## 摘要原文

An edge server and nearby devices can train language models of different sizes together by mutual distillation. Federated unlearning (FU) and unlearning for large language models (LLMs) execute a removal request on one model. Under mutual distillation, however, the effect of the removed data has been copied into many students, and their uploads teach it back to the corrected teacher. We propose Holder-level Erasure via Replication-weighted Delta-closure (HERD), which decides which holders must be corrected. HERD records a knowledge lineage graph from the transfers that the server already performs and weights each edge by its transfer type. It computes how many times the residual at each holder will be copied and selects the cheapest set of holders whose correction bounds the cumulative residual after the request. A transfer guard and a rejoin rule cover the holders left uncorrected or offline. We prove that partial correction suffices only when the copy number of the lineage graph is below one, that averaging alone never reaches one, and that the correction set remains valid under link outages. On TOFU, HERD leaves 18% to 52% less cumulative residual than the strongest baseline at 6% to 12% of its correction cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zihao Ding, Jun Huang, Guodong Wang
- 发布：2026-10-13；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
