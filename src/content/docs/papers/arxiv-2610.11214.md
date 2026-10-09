---
title: "Bridging KV-Cache Quantization and Linear Attention: From Theory to Pretrained Weight Migration"
description: "KV-cache quantization and linear attention are two representative approaches to tackling the storage and computational costs of Transformers."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.11214) · [PDF](https://arxiv.org/pdf/2610.11214)

## 一句话摘要

KV-cache quantization and linear attention are two representative approaches to tackling the storage and computational costs of Transformers.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV-cache quantization and linear attention are two representative approaches to tackling the storage and computational costs of Transformers. KV-cache quantization compresses individual KV entries into discrete codes but retains all entries, whereas linear attention recurrently aggregates multiple historical KV contributions into a fixed-size continuous state but can introduce interference. This contrast raises the question of whether per-KV compression and multi-KV aggregation can be bridged within a single mechanism for efficient attention. We identify RAM-Net as such a bridge through soft assignments over a discrete address space. These assignments determine recurrent updates to the continuous slot state associated with each address. Under a restricted RAM-Net construction, we prove that soft address assignments extend hard quantized matching to a separable read-write overlap that locally approximates full-attention similarity and supports recurrent aggregation. These connections further enable Transformer-to-RAM-Net weight migration through a new path based on a soft-quantized intermediate construction. Across nine pretrained Transformer models from 0.3B to 7B parameters, RAM-Net recovers an average of 87.1% of the teachers' accuracy gains over random guessing across six commonsense and knowledge tasks using only a 500M-token budget per model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaicheng Xiao, Liran Dong, Haotian Li, Guoliang Xing
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
