---
title: "State Space Attention: Learning Context-Dependent Memory Retention"
description: "Standard attention's key-value cache grows linearly with context length."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.33625) · [PDF](https://arxiv.org/pdf/2611.33625)

## 一句话摘要

Standard attention's key-value cache grows linearly with context length.

## 为什么值得关注

待编辑增强。

## 摘要原文

Standard attention's key-value cache grows linearly with context length. Bounding it raises the question of what a sequence model should retain for long-context reasoning. We argue this choice should be learned, and introduce State Space Attention (SSA), which learns to keep a bounded set of past representations and reads them with standard attention. A learned scorer rescores every chunk against newly arriving context and the rest of memory. A fixed-context Transformer is then the special case that always keeps the most recent tokens. We train the scorer and reader jointly, either moving gradually from a differentiable soft weighting of memories to hard retention, or with hard retention from the start. To produce signal for the scorer, we generate supervised samples during training, a technique we call recovery. We compare SSA with recurrent models, bounded-memory attention methods, and full-attention Transformers across retrieval, variable tracking, multi-hop reasoning, and language modeling. On our retrieval and reasoning benchmarks, SSA matches or comes within a few points of full attention on most tasks, far outperforms a Transformer with the same readable budget on every long-context retrieval task we evaluate, and matches or outperforms one with about 4 times that budget, while using constant inference memory. The largest remaining gap to full attention at small language model scale is on RULER. SSA makes a fixed number of tokens useful over a longer context, and since it reads memory with standard attention, we propose that it can be stacked with KV cache eviction methods. We also pretrain and post-train 400M-parameter models and measure how SSA's training and inference costs scale with context length and model size. Together, these experiments examine the capabilities and limitations of learned memory retention for long-context sequence modeling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ege Çakar, Cengiz Pehlevan
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Ege-Cakar/State-Space-Attention](https://github.com/Ege-Cakar/State-Space-Attention)
- 阅读深度：metadata
