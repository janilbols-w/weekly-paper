---
title: "Q-First: Attention and Feed-Forward Concurrency at the Smallest Change to the Block"
description: "Disaggregated LLM serving puts the KV-cache sweep on memory-optimised hardware and the projections and feed-forward on compute-optimised hardware, then inherits from the decoder block a dependency neither device wants: attention runs first and the feed-forward consumes its output, so within one sequence each side idles while the other works."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.15473) · [PDF](https://arxiv.org/pdf/2608.15473)

## 一句话摘要

Disaggregated LLM serving puts the KV-cache sweep on memory-optimised hardware and the projections and feed-forward on compute-optimised hardware, then inherits from the decoder block a dependency neither device wants: attention runs first and the feed-forward consumes its output, so within one sequence each side idles while the other works.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregated LLM serving puts the KV-cache sweep on memory-optimised hardware and the projections and feed-forward on compute-optimised hardware, then inherits from the decoder block a dependency neither device wants: attention runs first and the feed-forward consumes its output, so within one sequence each side idles while the other works. The usual repair costs one resident KV cache per extra sequence in flight, which is what motivated separating the devices at all. We remove the dependency instead. The sweep needs only the query, and exchanging the two sub-layers makes that query available while the compute side still has work to do; the current key and value follow as a cache write nothing waits on. We state the resulting decode as a protocol, show that it runs on stock kernels, and verify it end to end on a trained checkpoint to a relative error of 3.2x10^-3 -- with no new operator, no changed shape and no new hardware. We then train the block 8 ways at two seeds each, varying only where the attention reads and holding everything else fixed. At three per cent of compute-optimal a lead in bits per byte measures how much a change disturbed training rather than what it reaches, so we read magnitudes and not rankings. Among the 5 blocks whose feed-forward does not consume their own attention, no read point differs from the one that moves nothing by more than 0.0026 bits per byte -- smaller than the gap between an arm and itself at a second seed, 0.0066 -- while the same runs resolve a sub-layer exchange 25 times as large. Moving the query early is a change the measurement cannot find, which is what the protocol needs. The reach is bounded: projecting every layer's query from the network's input costs +0.0974, refuting a pre-registered threshold at both seeds, so a query may be read one feed-forward early and no further back.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：WenJie Fan
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
