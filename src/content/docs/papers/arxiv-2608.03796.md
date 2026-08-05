---
title: "Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chunked KL Loss"
description: "Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD)."
---

**评分：57/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03796) · [PDF](https://arxiv.org/pdf/2608.03796)

## 一句话摘要

Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD).

## 为什么值得关注

待编辑增强。

## 摘要原文

Small language models are often the only option for deployment under tight latency, cost, and on-premises constraints, but they are rarely trained from scratch: a compressed model is usually recovered through knowledge distillation (KD). This recovery step largely decides the final quality, yet it is expensive. We present a practitioner's study of how to make distillation training efficient, organised around two systems contributions. First, we show that offline KD (caching the teacher's top-$K$ logits once and training the student against the cache) matches online distillation at near-identical training loss while removing the teacher from memory, running about 29\% faster per iteration, and reaching up to 41\% higher throughput on a single H200 GPU. Second, we introduce a \emph{fused, chunked KL loss} that never materialises the full vocabulary-sized logit tensor, making peak memory linear in the sequence length. This removes the memory spike that otherwise caps context length and lets us train at four times the context (32{,}768 tokens) on a single GPU. A separate output-head-only toy benchmark isolates the loss kernel and confirms its memory and iteration-rate scaling from 4K to 256K tokens. Together these make large-scale healing and hundreds of ablations affordable. We also report supporting ablations on loss design and sequence packing. We release our chunked-loss implementation: https://github.com/CompactifAI/Full-Chunked-KL-Loss.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model, distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Bakbergen Ryskulov, Iker Garc\'ia-Ferrero, David Montero, David Jansen, Ali Hashemi, Jezabel R. Garcia, Antonio Tiene, Rom\'an Or\'us
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CompactifAI/Full-Chunked-KL-Loss](https://github.com/CompactifAI/Full-Chunked-KL-Loss)
- 阅读深度：metadata
