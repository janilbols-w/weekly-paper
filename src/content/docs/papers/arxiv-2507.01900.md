---
title: "High-Layer Attention Pruning with Rescaling"
description: "Pruning is a highly effective approach for compressing large language models (LLMs), significantly reducing inference latency."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2507.01900) · [PDF](https://arxiv.org/pdf/2507.01900)

## 一句话摘要

Pruning is a highly effective approach for compressing large language models (LLMs), significantly reducing inference latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pruning is a highly effective approach for compressing large language models (LLMs), significantly reducing inference latency. However, conventional training-free structured pruning methods often employ a heuristic metric that indiscriminately removes some attention heads across all pruning layers, without considering their positions within the network architecture. In this work, we propose a novel pruning algorithm that strategically prunes attention heads in the model's higher layers. Since the removal of attention heads can alter the magnitude of token representations, we introduce an adaptive rescaling parameter that calibrates the representation scale post-pruning to counteract this effect. We conduct comprehensive experiments on a wide range of LLMs, including LLaMA3.1-8B, Mistral-7B-v0.3, Qwen2-7B, and Gemma2-9B. Our evaluation includes both generation and discriminative tasks across 27 datasets. The results consistently demonstrate that our method outperforms existing structured pruning methods. This improvement is particularly notable in generation tasks, where our approach significantly outperforms existing baselines. Code is available at https://github.com/SongtaoLiu0823/HARP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Songtao Liu, Peng Liu
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SongtaoLiu0823/HARP](https://github.com/SongtaoLiu0823/HARP)
- 阅读深度：metadata
