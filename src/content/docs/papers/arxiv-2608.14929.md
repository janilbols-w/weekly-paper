---
title: "Training Leaves Traces: Centered Residual Signatures for Language Model Lineage Verification"
description: "Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.14929) · [PDF](https://arxiv.org/pdf/2608.14929)

## 一句话摘要

Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented.

## 为什么值得关注

待编辑增强。

## 摘要原文

Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented. We study data-free white-box lineage verification: can weights alone reveal whether two compatible model checkpoints share ancestry? Residual training produces a shared identity-aligned component in branch products, so this structure alone cannot establish ancestry. We remove it and compare checkpoint-specific structure across residual blocks, yielding a symmetric lineage score calibrated against independent checkpoints. On residual-MLP and GPT-2 benchmarks, the score separates fine-tuned, LoRA-merged, pruned, and quantized descendants from independent and distilled models (AUROC=1.0), distinguishing weight ancestry from behavioral similarity. Under function-preserving checkpoint laundering experiments, weight-space baselines lose margin or fail; our score remains unchanged and runs 76x faster than the nearest robust baseline on GPT-2. The projection-pairing signal appears across six language-model families and beyond, and a case study correctly identifies 3 related and 7 unrelated LLaMA-2 public checkpoints. Collectively, these results establish a passive, data-free provenance signal for compatible open-weight language-model checkpoints

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aman Singh Thakur, Rayan Khoury
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
