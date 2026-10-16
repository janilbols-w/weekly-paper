---
title: "ProTok: Unified Protein Tokenization via Modular Multi-Codebook Quantization"
description: "Protein sequence, structure, and functional annotations each capture complementary aspects of protein biology, yet existing tokenizers encode each modality independently, limiting the expressiveness of discrete protein representations."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.18481v1) · [PDF](https://arxiv.org/pdf/2610.18481v1)

## 一句话摘要

Protein sequence, structure, and functional annotations each capture complementary aspects of protein biology, yet existing tokenizers encode each modality independently, limiting the expressiveness of discrete protein representations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Protein sequence, structure, and functional annotations each capture complementary aspects of protein biology, yet existing tokenizers encode each modality independently, limiting the expressiveness of discrete protein representations. We present ProTok, a unified protein tokenizer that maps all three modalities into a modular discrete vocabulary via product quantization with per-modality codebook groups and modality dropout. A single ProTok checkpoint supports flexible inference from any modality subset without retraining. On seven StructTokenBench benchmarks spanning 14 tasks and 28 test splits, ProTok achieves an average rank of 1.4 across all structure-only tokenizers, placing first on 21 splits and among the top two on 27 of the 28. These gains come without sacrificing reconstruction: ProTok's tokens reach 0.939 lDDT on CATH 4.2, showing that multi-codebook quantization and multi-modal training yield tokens that are both reconstructable and informative. ProTok's structure tokens further lead all baseline structure tokenizers on zero-shot functional retrieval across CATH, Enzyme Commission, and Gene Ontology label hierarchies. The vocabulary also supports generation: a compact language model trained from scratch over ProTok tokens jointly generates backbone and sequence, with 52% of sampled backbones designable versus 21% for a parameter-matched GeoBPE baseline. ProTok shows that structure, sequence, and function can share one discrete vocabulary, motivating protein language models that reason over a unified token stream.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Romain Hardy, Xiaoman Zhang, Pranav Rajpurkar
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
