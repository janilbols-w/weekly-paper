---
title: "OmniTide: Co-Designing Algorithms and Systems for Efficient On-Device Omni-LLM Streaming"
description: "On-device streaming omni-modal inference safeguards user privacy and eliminates prohibitive per-token API costs, but faces a critical bottleneck: the continuous influx of multimodal data rapidly exhausts constrained memory and compute budgets via monotonic KV cache growth."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.34653) · [PDF](https://arxiv.org/pdf/2609.34653)

## 一句话摘要

On-device streaming omni-modal inference safeguards user privacy and eliminates prohibitive per-token API costs, but faces a critical bottleneck: the continuous influx of multimodal data rapidly exhausts constrained memory and compute budgets via monotonic KV cache growth.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device streaming omni-modal inference safeguards user privacy and eliminates prohibitive per-token API costs, but faces a critical bottleneck: the continuous influx of multimodal data rapidly exhausts constrained memory and compute budgets via monotonic KV cache growth. Existing sparse attention methods fall short, either incurring prohibitive online estimation latency or destroying interleaved cross-modal context, while failing to resolve physical memory fragmentation. We present OmniTide, the first algorithm-system co-design tailored for efficient on-device streaming omni-modal inference. Driven by the observation of modality-aware structural sparsity, OmniTide adopts a unit-based abstraction with two components: (1) At the algorithm level, OmniPick logically retains critical multimodal context based on unit boundaries and modality importance to preserve task accuracy; (2) At the system level, OmniPage physically partitions the cache by retention likelihood and dynamically compacts surviving sparse tokens, minimizing both memory fragmentation and data-movement overhead. Extensive evaluations across three streaming benchmarks and two consumer-device architectures show that OmniTide achieves up to $12.72\times$ kernel speedups and $2.40\times$ lower stream-loop latency. On StreamingBench, it improves accuracy by up to 18.0 percentage points over sliding-window baselines at comparable session cost. OmniPage further reduces the physical KV span by up to 26.7% relative to native logical eviction, unlocking real-time, infinite-context streaming on edge devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zongshang Shen, Wangsong Yin, Daliang Xu, Mengwei Xu, Xuanzhe Liu
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
