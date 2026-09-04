---
title: "When to Adapt: Conditional Memory Adapters for Retention-Preserving Domain Specialization"
description: "Large language models deployed in specialized domains must improve in-domain performance without sacrificing general capabilities."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.29327) · [PDF](https://arxiv.org/pdf/2608.29327)

## 一句话摘要

Large language models deployed in specialized domains must improve in-domain performance without sacrificing general capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models deployed in specialized domains must improve in-domain performance without sacrificing general capabilities. Existing parameter-efficient fine-tuning methods are typically always on: their learned perturbations are applied to every input, which can degrade out-of-domain (OOD) performance. We propose Engram Adapter, a framework that repurposes pretraining-time conditional memory as a post-hoc adapter for frozen LLMs. It uses multi-channel matching over local n-gram patterns with explicit occupancy tracking as a lightweight selectivity prior, making residual injection more likely on in-domain inputs while a learned scalar gate suppresses incoherent OOD retrievals. We evaluate on Qwen3-4B and Qwen3-8B with AG-News and MedMCQA as adaptation tasks and OOD benchmarks spanning reasoning, translation, code generation, and legal reasoning. Engram Adapter improves in-domain accuracy while preserving 99.4%--100.1% of average OOD performance; on LegalBench it slightly exceeds the frozen base model on average, whereas comparable always-on baselines degrade sharply. Mechanistic analyses show that although OOD activations are non-zero, gate and projection attenuation reduce residuals to approximately 0.08% of hidden-state norm, yielding small KL drift and negligible accuracy change. These results suggest conditional activation is a promising route toward modular, retention-preserving domain specialization over frozen backbones.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiayu Hou, Lei Wang
- 发布：2026-08-29；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
