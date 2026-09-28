---
title: "Deduplication-while-Training: A Resilient Paradigm for Privacy-Preserving Cross-Client Deduplication in Federated Learning"
description: "Cross-client duplicate data in large language model training corpora degrades the efficiency of federated learning (FL) while exacerbating model memorization and privacy risks."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.31262) · [PDF](https://arxiv.org/pdf/2609.31262)

## 一句话摘要

Cross-client duplicate data in large language model training corpora degrades the efficiency of federated learning (FL) while exacerbating model memorization and privacy risks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Cross-client duplicate data in large language model training corpora degrades the efficiency of federated learning (FL) while exacerbating model memorization and privacy risks. Privacy-preserving cross-client deduplication effectively mitigates this issue by eliminating duplicate training data. However, existing schemes all follow a "Deduplication-before-Training" paradigm. This serially coupled paradigm incurs high fault-tolerance costs and lacks support for dynamic client joining. To this end, we propose an unexplored paradigm called "Deduplication-while-Training (DwT)", which enables concurrent deduplication and training. DwT transforms cross-client deduplication from a one-time, globally synchronous preprocessing operation into a continuous online service with state management, concurrent claiming, and failure recovery. By enabling state synchronization and task takeover, it minimizes the impact of client disconnections on the overall training progress while supporting the dynamic joining of clients. We design DwT-FL, a privacy-preserving deduplication system, to support DwT. By designing a concurrent state-claim mechanism and a hot-cold dual-queue scheduling strategy, DwT-FL enables the parallel execution of secure deduplication and model training, while effectively handling client disconnections and dynamic joins. Experimental evaluations demonstrate that, compared to the state-of-the-art scheme, DwT-FL significantly reduces the time overhead of failure recovery and dynamic joining by up to 93.04% and 94.18%, respectively. This provides an efficient and elastic concurrent deduplication scheme for dynamic and unstable FL environments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: failure recovery
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rongxi Wang, Guanxiong Ha, Chunfu Jia, Yongsheng Lin, Minfen Gao, Hanmiaomiao Wang
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
