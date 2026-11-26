---
title: "HuluOPD: Unifying Heterogeneous Medical Specialists into One Lightweight Model with Unlabeled Prompts"
description: "Specialist medical vision-language models (VLMs) are strong within their specialties but hard to unify: their training data are often private, and independently developed specialists cannot be assumed to share an architecture."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.32021) · [PDF](https://arxiv.org/pdf/2611.32021)

## 一句话摘要

Specialist medical vision-language models (VLMs) are strong within their specialties but hard to unify: their training data are often private, and independently developed specialists cannot be assumed to share an architecture.

## 为什么值得关注

待编辑增强。

## 摘要原文

Specialist medical vision-language models (VLMs) are strong within their specialties but hard to unify: their training data are often private, and independently developed specialists cannot be assumed to share an architecture. Deploying these large models separately is costly. We present HuluOPD, an on-policy distillation recipe that unifies heterogeneous specialists into one lightweight VLM using only unlabeled prompts, without requiring reference answers or the specialists' training data. The lightweight model answers each prompt, and the specialist of the prompt's modality supervises its response; a continuation-aligned cross-tokenizer loss makes this possible even when they differ in architecture and tokenizer. We apply HuluOPD to five specialists, for ultrasound, pathology, optical coherence tomography, fundus photography, and dental imaging. To distill and evaluate them, we build HuluOPDCorpus, 914k unlabeled prompts, and HuluOPDBench, 47k held-out test items, from over 90 public datasets, and score all models under one protocol on 132k test items, including third-party benchmarks. A single model with 10% of the five specialists' combined parameters retains 94% of their question-answering performance, and one with 2% retains 89%. To our knowledge, this is the first demonstration of unifying heterogeneous medical specialist VLMs without requiring their training data or a shared architecture.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuncheng Zhang, Songtao Jiang, Yitian Tang, Zijie Meng, Zihan Xu, Xuxiang Ren, Jian Wu, Hualiang Wang, Zuozhu Liu
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
