---
title: "Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility"
description: "Whether a stored memory helps answer a user's question often depends on world knowledge rather than surface similarity."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.21478) · [PDF](https://arxiv.org/pdf/2611.21478)

## 一句话摘要

Whether a stored memory helps answer a user's question often depends on world knowledge rather than surface similarity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Whether a stored memory helps answer a user's question often depends on world knowledge rather than surface similarity. Jetriever replaces similarity search with full-pool utility scoring: given a query, it uses Jev, an LLM-derived System One decision model, to score every stored memory for the probability that it is useful to the answer, ranking the memory pool directly by those probabilities. On InMind's 125 indirect-query tasks, Jetriever places the gold exchange first in 84.8% of cases (versus 1.6% for BM25 and 0.0% for MiniLM with user-turn indexing) and reaches 76.0% end-to-end Application, compared with at most 16.0% across published retrieval and memory systems. A controlled 20-question comparison disentangles recognizing implicit evidence from ranking it properly: Jev and Qwen3.5-9B both recover 90% of gold exchanges within the top 50 (versus 30% for the BERT-based decision model Laya), yet at rank 1 Jev reaches 85% while Qwen3.5-9B drops to 40%. On a dimension-proportional random sample of 60 MemoryAgentBench questions, Jetriever raises the four-dimension average from 44.3% (ReFind) to 55.4%, at a mean retrieval cost of USD 0.00834 per InMind query and USD 0.03103 per MAB query. Together, these results show that effective utility retrieval hinges on combining broad world knowledge, calibrated ranking probabilities, and affordable full-pool evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory pool
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruizhe Li, Licheng Zhang, Mingxuan Du, Zhendong Mao
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
