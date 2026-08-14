---
title: "High-Layer Attention Pruning with Rescaling"
description: "提出免训练的高层注意力头剪枝方法 HARP，优先移除网络高层的注意力头，并用自适应缩放校正剪枝后 token 表征幅度；实验覆盖 4 个 LLM 和 27 个生成、判别数据集。"
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2507.01900) · [PDF](https://arxiv.org/pdf/2507.01900)

## 一句话摘要

提出免训练的高层注意力头剪枝方法 HARP，优先移除网络高层的注意力头，并用自适应缩放校正剪枝后 token 表征幅度；实验覆盖 4 个 LLM 和 27 个生成、判别数据集。

## 为什么值得关注

相比跨层统一按启发式分数剪枝，该方法显式利用层位置并补偿表征尺度，提供了一条无需再训练的结构化压缩路径；若执行栈能利用剪枝结构，可降低推理计算开销。

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
- 限制：摘要未给出剪枝比例、硬件、端到端延迟或吞吐数字，只报告任务质量优于既有方法；实际加速仍取决于模型结构及运行时对裁剪后注意力形状的支持。

## 元数据

- 作者：Songtao Liu, Peng Liu
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SongtaoLiu0823/HARP](https://github.com/SongtaoLiu0823/HARP)
- 阅读深度：abstract
