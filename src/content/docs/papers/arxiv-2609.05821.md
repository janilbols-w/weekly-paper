---
title: "CONDUIT: A Unified Residual-Stream Restoration Framework for KV Cache Reuse in Vision-Language Models"
description: "Vision-language models (VLMs) often answer new questions about recurring visual content, where reusing the key-value (KV) cache can avoid re-encoding expensive visual prefixes."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.05821) · [PDF](https://arxiv.org/pdf/2609.05821)

## 一句话摘要

Vision-language models (VLMs) often answer new questions about recurring visual content, where reusing the key-value (KV) cache can avoid re-encoding expensive visual prefixes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) often answer new questions about recurring visual content, where reusing the key-value (KV) cache can avoid re-encoding expensive visual prefixes. Exact-prefix reuse, however, fails when the same visual content appears under a changed prefix. Selective recomputation can recover quality under a small visual-token budget, but only when the right stale tokens are refreshed. Raw-attention selection can waste budget on high-attention tokens with small value-norm proxy scores and on query-irrelevant images. To address these failure modes, we propose CONDUIT, a training-free refresh policy that unifies single- and multi-image reuse as residual-stream restoration. Building on norm-weighted attention, CONDUIT ranks cached visual tokens using cached-key query attention and an accessible pre-output cached-value-norm proxy, then applies empirical image-level relevance amplification before one global selection. With one image, the coefficient is one and the rule reduces to intra-image token selection. The method preserves model architecture and weights, adding only a single query-conditioned scoring pass at inference. At a 10% refresh budget, CONDUIT achieves 97.0-99.5% of the corresponding full-prefill five-dataset average across three VLM backbones and leads budgeted methods on average; on the MMLongBench-Doc latency subset, it uses 13.5% of full-prefill FLOPs and achieves a 2.99x time-to-first-token speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Pengan Chen, Kaisheng Zheng, Liang Hong, Lixia Yi, Jiyue Jiang, Jiayang Chen, Yixuan Wang, Yimin Fan, Xinyuan Liu, Jiayi Li, Zhanqiu Zhang, Yiwen Guo, Yu Li
- 发布：2026-09-05；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
