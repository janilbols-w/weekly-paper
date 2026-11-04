---
title: "OmniCast: Interaction-Aware Serving for Real-Time Omni-Modal LLMs"
description: "Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2606.22983) · [PDF](https://arxiv.org/pdf/2606.22983)

## 一句话摘要

Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely.

## 为什么值得关注

待编辑增强。

## 摘要原文

Realtime omni-modal LMs support speech-centric conversations where users stream inputs, hear generated audio, and interrupt freely. Existing Omni-LM serving systems still rely on throughput-oriented LLM scheduling and LRU KV offloading. These policies ignore audio playback and multi-turn reuse: they may generate tokens far beyond what users hear, wasting work after barge-in, and evict KV state needed in the next turn. OmniCast is an interaction-aware serving system for realtime Omni-LM interaction. It exposes playback progress, speech activity, and barge-in events to the serving pipeline. The scheduler prioritizes first-audio and near-underrun sessions while limiting generation beyond the playback frontier. The KV manager uses next-use-aware eviction and preloads likely-needed KV during user speech to hide reload latency. On vLLM-Omni, OmniCast improves realtime serving across two Omni-LMs and mixed workloads. It lowers P90 audio TTFP by $1.55\times$ on average and up to $2.21\times$, while improving completed-request throughput by $1.15\times$ on average and up to $1.56\times$, and moves most KV reload work off the next-turn critical path.

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

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiangyu Zhi, Peiqi Yin, Sheng Guan, Chenguang Zheng, James Cheng, Xiao Yan
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
