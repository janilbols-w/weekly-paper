---
title: "Tevatron Meets Megatron: Expert-Parallel LLM Reranker Training on an Academic Budget"
description: "Modern reranking recipes---billion-scale cross-encoders, mixture-of-experts (MoE) backbones, and distillation against strong teachers---have outpaced the training infrastructure available to most academic groups."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.00916) · [PDF](https://arxiv.org/pdf/2608.00916)

## 一句话摘要

Modern reranking recipes---billion-scale cross-encoders, mixture-of-experts (MoE) backbones, and distillation against strong teachers---have outpaced the training infrastructure available to most academic groups.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern reranking recipes---billion-scale cross-encoders, mixture-of-experts (MoE) backbones, and distillation against strong teachers---have outpaced the training infrastructure available to most academic groups. Existing Tevatron reranker training relies on the Hugging Face Trainer with DeepSpeed or PyTorch FSDP1, but these backends lack efficient support for large-scale MoE training. We present Tevatron 3.0, which integrates a Megatron-Core training backend into Tevatron while preserving its data pipeline, evaluation workflow, and Hugging Face-compatible checkpoints. We benchmark existing distributed training configurations against the new backend, showing that Megatron matches FSDP reranker quality and training efficiency under comparable data-parallel settings, is up to 22% faster in the recommended single-node configuration, and supports both LoRA and full-parameter fine-tuning. Crucially, expert parallelism enables training a 30B-parameter Qwen3-30B-A3B MoE reranker, which is infeasible with PyTorch FSDP1. Using this framework, we conduct a controlled comparison of MoE versus dense models, LoRA versus full-parameter tuning, and distillation versus contrastive training on BEIR-15 with three first-stage retrievers, and report serving throughput for Hugging Face and vLLM. We find that the MoE reranker matches dense 8B quality while activating less than half as many parameters and achieving substantially higher inference throughput. We will release the framework and trained checkpoints.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhichao Xu, Xueguang Ma, Shengyao Zhuang, Luyu Gao, Wenqian Ye, Yu Wang, Jamie Callan, Jimmy Lin
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
