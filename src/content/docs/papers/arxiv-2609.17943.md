---
title: "ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference"
description: "Long-context LLM inference is bottlenecked by attention, whose repeated KV-cache reads make decoding memory-bound."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.17943) · [PDF](https://arxiv.org/pdf/2609.17943)

## 一句话摘要

Long-context LLM inference is bottlenecked by attention, whose repeated KV-cache reads make decoding memory-bound.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM inference is bottlenecked by attention, whose repeated KV-cache reads make decoding memory-bound. Self-speculative decoding alleviates this by drafting tokens with sparse attention and verifying them with full attention, but existing batched methods remain synchronized: all requests in a batch share a single draft-verify schedule, even though the optimal draft length varies widely across requests and changes dynamically within each request. We propose ASPIRE, a non-synchronized batched self-speculative decoding framework built on three components. First, a unified mixed forward allows drafting and verifying requests to coexist in the same batched forward pass, removing the need for global draft-verify phases. Second, a lightweight online speculation scheduler uses per-request acceptance-rate estimates and a batch-aware cost model to let each request independently choose when to verify. Third, an intra-draft refresh layer performs full attention at a single designated layer during drafting, updating the sparse context at every draft step to reduce staleness during drafting. Across three models and five reasoning and long-context benchmarks, ASPIRE achieves $1.70$-$4.58\times$ speedup in decoding throughput over autoregressive baselines and improves average speedup by approximately $27\%$ over the strongest prior self-speculative baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Amir Ziashahabi, Hossein Entezari Zarch, Lei Gao, Murali Annavaram, Salman Avestimehr
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
