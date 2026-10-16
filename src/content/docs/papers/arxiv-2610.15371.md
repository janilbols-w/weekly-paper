---
title: "A Sovereign, Indic-First, Reasoning Model"
description: "Gnani-Evon-v3.3-30B-A3B is a long-context hybrid Mamba-Transformer mixture-of-experts model for reasoning, instruction following, and tool use in English and eight Indian languages."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.15371v1) · [PDF](https://arxiv.org/pdf/2610.15371v1)

## 一句话摘要

Gnani-Evon-v3.3-30B-A3B is a long-context hybrid Mamba-Transformer mixture-of-experts model for reasoning, instruction following, and tool use in English and eight Indian languages.

## 为什么值得关注

待编辑增强。

## 摘要原文

Gnani-Evon-v3.3-30B-A3B is a long-context hybrid Mamba-Transformer mixture-of-experts model for reasoning, instruction following, and tool use in English and eight Indian languages. Starting from NVIDIA's Nemotron-3-Nano-30B-A3B checkpoint, it retains the 52-layer backbone and changes the vocabulary, training data, and post-training objectives. An in-place expansion from 131,072 to 163,072 tokens reduces mean Indian-language fertility by 38.6%. The new embedding rows are initialized from their upstream decompositions and warmed before the backbone is updated. Continual pretraining then adds broad English-Indic data, high-quality annealing, and direct training at a 131,072-token sequence length. The central result appears after post-training. Reinforcement learning across four verifiable task environments improves mathematics, graduate-level science, and instruction following, but degrades Indic extractive question answering because the rewards do not require an answer in the requested language. The share of Indic extraction items answered in English rises from 8.7% to 91.7%. Accuracy conditional on answering in the target script roughly doubles, which is consistent with preserved reading ability but is measured on a self-selected subset. Two unreleased studies test repairs. A scoped Indic reward restores the language convention. A 26B-A4B generative judge outperforms a 235B-parameter model on RM-Bench, and distillation restores 81% of the capabilities displaced by optimizing against it. Relative to the architecture-identical starting checkpoint, the released model gains 5.2 points on an Indic aggregate while giving up 1.7 points of English retention. The unreleased Indic-aware branch trades further, gaining 14.6 Indic points at a cost of 5.4 in English. A planned FP8 release reduces the artifact to 32GB with near-zero mean change across 32 paired benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sutanshu Saksena Raj, Prasanjith Pasunuti, Parijat Chatterjee, Daksh Maan, Purusharth Malik, Nayanjit Sarkar, Avinash Benki
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
