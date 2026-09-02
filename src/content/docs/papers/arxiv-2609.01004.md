---
title: "SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models"
description: "Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.01004) · [PDF](https://arxiv.org/pdf/2609.01004)

## 一句话摘要

Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences. To reduce inference costs, recent studies have explored visual token pruning through vision-centric or text-guided strategies. However, these methods often overlook high-norm outlier tokens, i.e., tokens with abnormally large feature norms, leading to suboptimal pruning decisions. In this work, we show that such high-norm outlier tokens are highly redundant in both feature and spatial dimensions, yet are often mistakenly preserved as informative cues by existing methods. Motivated by this observation, we propose SinkPruner, a training-free visual token pruning framework for efficient MLLM inference. SinkPruner follows a coarse-to-fine design with two key modules: a visual sanitizer that filters high-norm redundancies and alleviates attention sink and attention dispersion, and a text-guided pruner that further retains tokens semantically aligned with the text query. Extensive experiments on twelve image-language and four video-language benchmarks demonstrate the effectiveness, efficiency, and generalizability of our framework. Notably, SinkPruner preserves 96.5% (91.8%) of the original performance of LLaVA-1.5 (Qwen2.5-VL) under an 89% token reduction. Experiments further indicate that our visual sanitizer exhibits promising transferability in enhancing the performance of existing pruning methods. Our code is available at https://github.com/LaVi-Lab/SinkPruner.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shiyu Li, Zi-Yuan Hu, Shijia Huang, Yanyang Li, Yiwu Zhong, Liwei Wang
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LaVi-Lab/SinkPruner](https://github.com/LaVi-Lab/SinkPruner)
- 阅读深度：metadata
