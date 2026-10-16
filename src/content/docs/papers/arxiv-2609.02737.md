---
title: "Language Models Can Control Their Own Attention"
description: "Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.02737) · [PDF](https://arxiv.org/pdf/2609.02737)

## 一句话摘要

Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language models spend most of their attention on a small fraction of context, yet they read the entire KV cache to find the few tokens that matter. If the user asks about a previous detail in a 1M-token conversation, global attention layers must scan the full context to generate each token of the reply. A prominent approach pre-selects relevant tokens via lightweight proxy scores, but this extrinsic scoring still incurs O(N) per step. We take an intrinsic approach motivated by the simple question: wouldn't the model already know which parts of the context are relevant? We introduce Declarative Attention (DA), a protocol that elicits the model to declare where it needs to attend within its chain-of-thought, partitioning generation into three modes: (full context), (a specific region), and (recent output only). The inference engine parses these declarations like tool calls and skips most of the KV cache read. Under zero-shot evaluation across 15 long-context tasks, DA on off-the-shelf models (Gemma-4-31B, Qwen-3.6-27B) reduces total attended tokens per response (45.8%, 19.6%), despite extra decoding steps, with modest accuracy drops (1.40pp, 2.10pp) that shrink with model scale. DA unlocks a new axis of sparse attention, with further potential under training-based methods. Code is available at https://github.com/itsnamgyu/declarative-attention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Namgyu Ho, Huzama Ahmad, Woosung Koh, Se-Young Yun, Tal Schuster, Cicero Nogueira dos Santos
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/itsnamgyu/declarative-attention](https://github.com/itsnamgyu/declarative-attention)
- 阅读深度：metadata
