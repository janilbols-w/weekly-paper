---
title: "Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation"
description: "Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.22215) · [PDF](https://arxiv.org/pdf/2608.22215)

## 一句话摘要

Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves. Existing memory systems typically treat external memory as a monotonically growing repository, inevitably leading to retrieval degradation and increasing computational costs over time. We argue that the core challenge is not retrieval alone, but managing the knowledge lifecycle: deciding what to externalize, update, or ultimately internalize. Inspired by Complementary Learning Systems (CLS) theory in neuroscience, we propose Dual-Layer Agentic Memory, a framework that shifts memory management to the write phase through cost-aware epistemic routing and periodic parametric consolidation. Incoming information is categorized as non-write, write-new, or write-update, and routed through a small-to-large model cascade that minimizes routing overhead while filtering redundant memories. A subsequent write-back phase selectively consolidates high-value external memories into model parameters via supervised fine-tuning. Experiments demonstrate the dual efficiency of our approach: a 1.7B/8B cascade prunes up to 68% of redundant external memory while escalating fewer than 50% of inputs, yet retains over 98% of the downstream QA Exact Match (EM) achieved by an exhaustive retention baseline. We further show that periodic consolidation successfully internalizes external knowledge, allowing the router to adaptively suppress redundant writes as the model's epistemic boundaries evolve. Overall, our framework presents a unified paradigm for agent memory: selective externalization followed by selective internalization. Code and dataset will be released upon acceptance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wenzhi Li, Dong Nie, Rui Lan, Tongtong Lyu, Peiyao Wang, Lingzi Hong, Weihang Pan, Boyuan Pan, Yao Hu
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
