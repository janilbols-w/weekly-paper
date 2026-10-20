---
title: "MOSAIC: More LLMs, Less Cost through Collaborative Reasoning for Compiler Optimizations"
description: "LLM-guided compiler optimization has recently shown promise."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.01935) · [PDF](https://arxiv.org/pdf/2602.01935)

## 一句话摘要

LLM-guided compiler optimization has recently shown promise.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-guided compiler optimization has recently shown promise. However, current LLM-guided optimizers query a single LLM at every search step, so their cost grows with both that model's price and the search budget. A smaller model is cheaper but degrades the search: in our experiments, a recent single-LLM optimizer reaches 10.2% (6.0%) lower speedup on GPU (CPU) with gpt-5-mini than with GPT-5.2. Agentic multi-LLM frameworks add controllers, concurrent calls, and shared memory, whose overhead can offset the savings of cheaper models. This paper shows that the optimization search tree itself can coordinate heterogeneous LLMs: the tree already records which proposals improved the program, and we can augment the tree to record which model made them. That evidence can then be used to decide which model should propose next. To this end, we introduce MOSAIC, in which each Monte Carlo tree search (MCTS) node records a program and the LLM that expands it, and the active LLM proposes both a compiler transformation and the LLM for the next step. We also contribute an LLM-aware UCT that favors smaller models and a course-alteration rule that invokes the largest model only after repeated small-model regressions. Against that single-LLM optimizer run with GPT-5.2 alone and the same number of search iterations and tree parameters, on an NVIDIA GPU (Intel CPU), MOSAIC with eight LLMs improves the geometric-mean speedup on five kernels by 7.2% (14.4%) and the end-to-end Llama-3-8B speedup by 1.61x (1.41x), while reducing kernel compilation time by 1.95x (1.74x) and API cost by 4.47x (4.32x), with GPT-5.2 making only 23.1% (23.9%) of LLM calls. With the same eight models, random or round-robin model choice improves over the single-LLM baseline by only 2.5% on CPU, showing that the gains come from letting the LLMs choose the next model rather than from mixing the pool at random.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compiler optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Annabelle Sujun Tang, Christopher Priebe, Lianhui Qin, Hadi Esmaeilzadeh
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
