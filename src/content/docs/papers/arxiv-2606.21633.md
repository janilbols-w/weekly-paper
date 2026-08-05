---
title: "HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval"
description: "The KV cache dominates GPU memory in long-context LLM serving, crowding out batch capacity and leaving GPU compute idle."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.21633) · [PDF](https://arxiv.org/pdf/2606.21633)

## 一句话摘要

The KV cache dominates GPU memory in long-context LLM serving, crowding out batch capacity and leaving GPU compute idle.

## 为什么值得关注

待编辑增强。

## 摘要原文

The KV cache dominates GPU memory in long-context LLM serving, crowding out batch capacity and leaving GPU compute idle. Offloading the cache to CPU DRAM restores capacity, but the limited PCIe bandwidth forces state-of-the-art offloading systems to pair it with sparse attention, fetching only a small critical subset of the cache to the GPU. These systems, however, follow the KV access pattern of autoregressive decoding, in which the critical set changes at every token: selection and fetching recur at every decoding step, and throughput remains capped by PCIe bandwidth rather than by either processor. Block diffusion LLMs(block dLLMs), which decode a block of B tokens over T denoising steps, exhibit a different KV access pattern that opens a new opportunity for offloading. Recent sparse block dLLM methods have shown that sparse inference separates into a selection phase that scans the full KV cache once per block and a denoising phase that reuses the selected small subset T times. This asymmetry aligns with the compute and memory asymmetry of a CPU-GPU system, making it advantageous to run selection on the CPU and denoising on the GPU: the critical KV cache then crosses PCIe only once per block, removing the interconnect as the bottleneck. We present HERALD, to our knowledge the first KV offloading system designed for block dLLMs. HERALD resolves the two obstacles of this mapping, the serialized dependency between the phases and the compute-bound B-query selection on the CPU, by overlapping the phases with a draft block, reducing the selection cost with a single [MASK] query, and executing both as a dual-stream pipeline over double-buffered sparse KV pools. On two production block dLLMs, HERALD sustains near-lossless accuracy at a 5% KV budget and reaches up to 2.28x the decode throughput of GPU-only serving, with gains that widen with context length.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Omin Kwon, Doyeon Kim, Jongseok Park, Seung Yul Lee, Ion Stoica, Jae W. Lee
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
