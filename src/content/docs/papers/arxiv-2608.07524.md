---
title: "Training Variable Long Sequences with Data-Centric Parallel"
description: "Training deep learning models on variable long sequences poses significant computational challenges."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.07524) · [PDF](https://arxiv.org/pdf/2608.07524)

## 一句话摘要

Training deep learning models on variable long sequences poses significant computational challenges.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training deep learning models on variable long sequences poses significant computational challenges. Existing methods force a difficult trade-off between efficiency and ease-of-use. Simple approaches use static configurations that cause workload imbalance low efficiency, while complex methods introduces significant complexity and code change for new models. To break this trade-off, we introduce Data-Centric Parallel (DCP). Its core principle is to let the data itself drive the runtime. It achieves this by dynamically adjusting direct runtime settings (e.g., parallel size, gradient accumulation, recomputation) based on each batch's sequence length. Empirical results demonstrate that our method achieves up to a 2.88$\times$ speedup on 32 H200 GPUs. Designed for generalization, it can be integrated into any model with 10 lines of code. We anticipate this simple yet effective approach will serve as a robust baseline and facilitate future advancements in distributed training for variable long sequences.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Geng Zhang, Xuanlei Zhao, Kai Wang, Yang You
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
