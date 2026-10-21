---
title: "TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning"
description: "Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.26754) · [PDF](https://arxiv.org/pdf/2610.26754)

## 一句话摘要

Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To enable end-to-end learning despite the non-differentiable top-K operator for token pruning, we introduce token-gated attention, a mechanism inspired by Mixture-of-Experts that re-weights attention logits using token importance scores. Across diverse tasks, TokenGate achieves $1.4$-$11.3\times$ faster time-to-first token (TTFT) and $1.5$-$3.4\times$ lower peak memory at no accuracy degradation for prefill in transformers. Compared to the best-performing prior methods for token-pruning, TokenGate gives up to $6.4\times$ faster prefill and $2\times$ lower peak memory. TokenGate natively extends both standard transformers (e.g., Qwen3) and hybrid-attention models (e.g., Qwen3.5) with simple lightweight adaptation comparable to standard parameter-efficient fine-tuning. We make our code available at: https://github.com/tokengate-models/TokenGate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Liana Patel, Rishabh Ranjan, Ion Stoica, Matei Zaharia, Carlos Guestrin
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/tokengate-models/TokenGate](https://github.com/tokengate-models/TokenGate)
- 阅读深度：metadata
