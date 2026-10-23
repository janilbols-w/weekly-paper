---
title: "SARIA: Persistence-Aware KV Caching with Coordinated DRAM--SSD Reload for LLM Agents"
description: "Multi-turn LLM agents usually reuse long context prefixes, making key value (KV) caching crucial for reducing prefill latency."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.31169) · [PDF](https://arxiv.org/pdf/2610.31169)

## 一句话摘要

Multi-turn LLM agents usually reuse long context prefixes, making key value (KV) caching crucial for reducing prefill latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-turn LLM agents usually reuse long context prefixes, making key value (KV) caching crucial for reducing prefill latency. SSDs provide a low-cost extension to limited DRAM capacity but introduce two key challenges. Eagerly persisting all KV cache blocks incurs substantial write traffic and rapidly consumes finite SSD endurance. Meanwhile, the small number of SSDs provisioned in typical GPU servers limits aggregate reload bandwidth, making SSD-resident KV cache much slower to retrieve than that in DRAM and inflating prefill latency. We present \textsc{Saria} (Selective Admission and Reload for Inference Acceleration), a KV caching system that jointly manages DRAM and SSD by exploiting the session-level temporal locality of LLM agents to reduce SSD writes and accelerate cache reload. On the write path, \textsc{Saria} uses eviction and reuse history to selectively persist KV cache blocks that exhibit reuse opportunities beyond their DRAM residency, avoiding unnecessary writes for KV cache already hosted in DRAM. On the read path, \textsc{Saria} promotes selected SSD-hit KV cache blocks from GPU memory into DRAM after prefill, allowing subsequent reuse within the same session to reduce SSD read traffic while limiting DRAM contention. A transfer coordinator paces DRAM reads while SSD transfers are active, allowing both paths to make progress and efficiently share GPU ingress bandwidth. We implement \textsc{Saria} on LMCache MP and evaluate it using workloads from TraceLab and WEKA, covering both full-attention and hybrid-attention models. The results show that \textsc{Saria} reduces SSD writes by 57.1--58.9\% compared with popular full duplicate caching and the mean time to first token (TTFT) by 42.3--79.7\% over DRAM-only caching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hui Li, Qihui Zhou, Xiao Yan, Shumeng Zhang, Zijie Dai, Zequn Gong, Mingcong Song, Guoping Long, Hongjie Si, James Cheng
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
