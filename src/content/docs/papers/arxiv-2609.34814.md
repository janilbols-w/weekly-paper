---
title: "WaveAlign: Cache-Aware Query-Row Scheduling for Sparse Attention in Long-Video Generation"
description: "Long-video generation with diffusion transformers (DiTs) produces extremely long token sequences, making attention a dominant inference bottleneck."
---

**评分：38/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](http://arxiv.org/abs/2609.34814v1) · [PDF](https://arxiv.org/pdf/2609.34814v1)

## 一句话摘要

Long-video generation with diffusion transformers (DiTs) produces extremely long token sequences, making attention a dominant inference bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-video generation with diffusion transformers (DiTs) produces extremely long token sequences, making attention a dominant inference bottleneck. Dynamic sparse attention reduces computation, but its realized speedup remains limited because irregular query-row execution degrades L2 cache locality and increases HBM traffic. We present WaveAlign, a lightweight, cache-aware query-row reordering framework for dynamic sparse attention. WaveAlign formulates row ordering as an optimization problem and approximates it with two stages. The first stage derives a low-rank SVD representation of sparse-mask rows and groups query rows with similar K/V access patterns, increasing K/V overlap among concurrently scheduled rows. The second stage exploits streaming GPU scheduling by sorting rows within each wave in descending order of their K/V-block counts, so that short rows from the current wave are followed by long rows from the next. This aligns K/V accesses across wave boundaries and enables shared blocks to be reused before eviction. An adaptive skip module avoids unprofitable reordering. By only permuting query and mask rows, WaveAlign preserves sparse-attention semantics and requires no changes to existing methods or backend kernels. Across two GPU architectures, two video DiTs, and four sparse-attention methods, WaveAlign raises the L2 cache hit ratio from 28.48%--36.35% to 79.38%--89.06%, reduces HBM read traffic by up to 92.11%, and achieves up to 1.25x kernel and 1.17x end-to-end generation speedup without quality loss.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu scheduling
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zijian Dai, Sen Han, Youhui Bai, Shannon Wang, Kan Wu, Jingkai Huang, Yuhang Wang, Jing Li, Cheng Li
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
