---
title: "Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic Budget"
description: "Training large dense and mixture-of-experts (MoE) rerankers is constrained by GPU memory and distributed-execution efficiency, which has kept academic reranker research largely on dense models."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.00916) · [PDF](https://arxiv.org/pdf/2608.00916)

## 一句话摘要

Training large dense and mixture-of-experts (MoE) rerankers is constrained by GPU memory and distributed-execution efficiency, which has kept academic reranker research largely on dense models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large dense and mixture-of-experts (MoE) rerankers is constrained by GPU memory and distributed-execution efficiency, which has kept academic reranker research largely on dense models. Tevatron trains rerankers through the Hugging Face Trainer with DeepSpeed and PyTorch FSDP1, a stack that stalls on three fronts: DeepSpeed ZeRO-2 has a known gradient-gathering failure on this path, FSDP1 full sharding is memory-safe but throughput-bound, and neither offers the expert parallelism (EP) that MoE training needs. We present Tevatron 3.0, which integrates Megatron-Core as a reranker training backend while preserving Tevatron's data processing, evaluation pipeline, and Hugging Face checkpoint format. For full-parameter dense 8B training, Megatron matches FSDP1 on BEIR-15 NDCG@10 with approximately 4% lower epoch time and twice the peak GPU memory under matched data-parallel and recomputation settings, and approximately 22% lower epoch time in its recommended configuration; it supports both LoRA and full-parameter fine-tuning. Expert parallelism makes it possible to train a 30B-parameter MoE reranker (Qwen3-30B-A3B) on two nodes. A controlled study of architecture, LoRA, and distillation on BEIR-15, with three first-stage retrievers and Hugging Face and vLLM serving, shows that the MoE reranker matches dense-8B quality at less than half the activated parameters and at higher inference throughput. We open-source the framework and trained checkpoints.

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

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhichao Xu, Xueguang Ma, Shengyao Zhuang, Luyu Gao, Wenqian Ye, Yu Wang, Jamie Callan, Jimmy Lin
- 发布：2026-08-02；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
