---
title: "Elastic KV Cache for LLM Serving:A Working Reclamation Mechanism, and Why Chunked Prefill Already Closes the Gap"
description: "An LLM serving engine sizes its key-value (KV) cache once, at startup, permanently setting aside a reserve for the worst-case prefill activation."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.23658) · [PDF](https://arxiv.org/pdf/2608.23658)

## 一句话摘要

An LLM serving engine sizes its key-value (KV) cache once, at startup, permanently setting aside a reserve for the worst-case prefill activation.

## 为什么值得关注

待编辑增强。

## 摘要原文

An LLM serving engine sizes its key-value (KV) cache once, at startup, permanently setting aside a reserve for the worst-case prefill activation. During decode-dominant phases that reserve sits idle, yet it cannot be handed to the KV pool because it is exactly the memory a large prefill needs. We ask whether this reserve is reclaimable, and build a mechanism to test it. Our elastic KV cache lends the reserve to the KV pool during decode and returns it before prefill, driven by the scheduler's one-step-ahead view of the next batch. It is pure userspace on the CUDA virtual-memory path: two physical handles mapped into one contiguous virtual range per layer, so the attention kernel is unchanged and no driver patch is required. It decommits in a few milliseconds and recommits in tens of milliseconds, works with CUDA graphs and prefix caching, and never triggers an out-of-memory event. A static commit of the same memory is unsafe, crashing on prefill bursts, which makes the dynamic toggle necessary. Having built the mechanism, we test the premise it rests on and report an honest negative result. It only pays off if a small prefill chunk size badly hurts prefill latency. In a controlled experiment injecting long prompts into a live decode load, that penalty is small (median time-to-first-token differs by about 1% between chunk sizes of 8192 and 32768 tokens), because prefill is compute bound and decode consumes only about one token per sequence per step. Simply lowering max_num_batched_tokens recovers more KV than the controller does, at nearly equal latency. The reserve also dilutes under tensor parallelism, from 16% of KV at TP1 to 2.7% at TP4. We state precisely when reclaiming the reserve could still help, and release the mechanism as a reusable userspace elastic-VMM allocator.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, kv cache, prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sathishkumar Sivashanmugam
- 发布：2026-08-24；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
