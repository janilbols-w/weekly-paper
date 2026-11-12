---
title: "Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines"
description: "DeepSeek-V4.1's 203 GB of Engram n-gram tables sit in host DRAM today, taking 190 of the 223 GiB a 4-GPU serving process uses."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.13413) · [PDF](https://arxiv.org/pdf/2611.13413)

## 一句话摘要

DeepSeek-V4.1's 203 GB of Engram n-gram tables sit in host DRAM today, taking 190 of the 223 GiB a 4-GPU serving process uses.

## 为什么值得关注

待编辑增强。

## 摘要原文

DeepSeek-V4.1's 203 GB of Engram n-gram tables sit in host DRAM today, taking 190 of the 223 GiB a 4-GPU serving process uses. Row indices depend only on input tokens, so reads can start with each step and overlap earlier layers. V4.1's two Engram layers have windows that differ by 30x (0.3 vs. 9.3 ms). We show that this deadline, together with session reuse and contention on a shared device, decides which tier each table can use and which layers need cache, and we give a model that predicts the resulting slowdown from measured read times. Agent and chat traffic reuse rows within sessions, and static hot sets transfer poorly. We build SlackTier, a table tier for SGLang that issues all lookups at step start. It reads the short-window layer first and splits a small GPU row cache across layers. The path runs inside the decode CUDA graph and is bit-exact with the original gather. Layer 14's table can go to NVMe uncached with no measurable decode cost. With both tables on four NVMe disks, mean time per output token on agent and chat replays rises at most 1.4% over unmodified SGLang, and host memory falls from 212 to 34 GiB. Both tables need no cache when read over RDMA (remote direct memory access) from another node's memory; one copy serves two instances. On a KV-constrained agent workload, using the freed memory as host KV cache at the same memory budget raises median throughput by 36% and cuts median p90 time to first token from 38 to 24 s.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Wen Huang, Jack Liu
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
