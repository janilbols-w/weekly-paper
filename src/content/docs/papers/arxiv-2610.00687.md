---
title: "Leto: Fast In-Place Recovery for LLM Training on Surviving Hardware"
description: "Hardware-operable failures (HOFs) interrupt large language model (LLM) training but permit recovery on the same hardware without reset, repair, or replacement."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.00687) · [PDF](https://arxiv.org/pdf/2610.00687)

## 一句话摘要

Hardware-operable failures (HOFs) interrupt large language model (LLM) training but permit recovery on the same hardware without reset, repair, or replacement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hardware-operable failures (HOFs) interrupt large language model (LLM) training but permit recovery on the same hardware without reset, repair, or replacement. Existing recovery systems nevertheless reload checkpoints, recompute lost progress, and rebuild process state, idling GPUs that could otherwise continue training. We present Leto, a fault-tolerant training system that leverages surviving hardware to enable efficient in-place recovery. Our key insight is that the state needed to resume training can be retained or prepared outside the active training process while remaining on the same hardware. Leto retains the working model state and the reusable process state, and preinitializes the remaining state in a shadow trainer. We devise two-tier erasure protection and chunk-level transactional updates to keep the retained model state recoverable and consistent, and reclaim the shadow state when active training needs its GPU memory. Evaluation on 6- and 72-GPU NVIDIA A100 clusters shows that Leto recovers 3.6--6.5$\times$ faster than the best-performing checkpointing baselines and improves productive training time by up to 13.7 percentage points. Large-scale simulation shows over 95% productive training time on a 131,072-GPU cluster.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Geon-Woo Kim, Joon Ha Kim, Daehyeok Kim
- 发布：2026-09-30；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
