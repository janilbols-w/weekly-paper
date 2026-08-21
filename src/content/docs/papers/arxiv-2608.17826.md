---
title: "Bounded-State Restoration: Decoupling Local Restore Capacity from External LLM State"
description: "Hierarchical KV-cache systems can retain long-context LLM execution state beyond GPU memory, but retention capacity does not determine the local memory required to make that state executable again."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.17826) · [PDF](https://arxiv.org/pdf/2608.17826)

## 一句话摘要

Hierarchical KV-cache systems can retain long-context LLM execution state beyond GPU memory, but retention capacity does not determine the local memory required to make that state executable again.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hierarchical KV-cache systems can retain long-context LLM execution state beyond GPU memory, but retention capacity does not determine the local memory required to make that state executable again. We isolate this second resource as the restoration working set (RWS): the peak local staging state whose lifetimes overlap during restoration. In the pinned upstream LMCache whole-plan path, measured full-reuse points for 1.956, 7.823, and 15.646 GiB/rank states first succeed at 2, 8, and 16 GiB L1 rungs, with successful L1 peaks of 1.956, 7.824, and 15.648 GiB/rank. We introduce Bounded-State Restoration (BSR), which separates complete discovery from local residency. BSR probes the complete reusable prefix without materializing the whole hit in L1, then installs confirmed state through a reusable window of at most $W$ chunks. Under bounded auxiliary state, peak restoration capacity is $O(W)$ while total transfer and installation work remains $\Theta(|S|)$. Because reusable state spans heterogeneous allocator groups and tensor-parallel ranks, BSR uses a request-level commit rule: partial installation is never exposed as a valid reusable prefix; failures invalidate the advertised prefix and fall back to a lower valid tier or deterministic recomputation. On DeepSeek-V4-Flash with TP=2 across two DGX Spark nodes, a clean no-resume sweep grows external state from 1.956 to 31.277 GiB/rank while measured L1 RWS remains exactly 500.75 MiB/rank at $W=32$, a 63.959x largest-state external-to-live-staging ratio. A second fresh 524K-token run repeats the largest-state acceptance result. Evaluated tier and rank-asymmetric failures expose either complete reuse or zero external reuse before fallback. A matched SSD optimization reduces 512K restore TTFT from 43.1 to 17.6 seconds without changing RWS.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zixuan Li
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
