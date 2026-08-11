---
title: "OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference"
description: "Large language models (LLMs) with extended context windows enable powerful applications but impose significant memory overhead, as caching all key-value (KV) states scales linearly with sequence length and batch size."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.07651) · [PDF](https://arxiv.org/pdf/2510.07651)

## 一句话摘要

Large language models (LLMs) with extended context windows enable powerful applications but impose significant memory overhead, as caching all key-value (KV) states scales linearly with sequence length and batch size.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) with extended context windows enable powerful applications but impose significant memory overhead, as caching all key-value (KV) states scales linearly with sequence length and batch size. Existing cache eviction methods address this by exploiting attention sparsity, yet they typically rank tokens heuristically using accumulated attention weights without considering their true impact on attention outputs. We propose Optimal Brain Cache (OBCache), a principled framework that formulates cache eviction as a layer-wise structured pruning problem. Building upon the Optimal Brain Damage (OBD) theory, OBCache quantifies token saliency by measuring the perturbation in attention outputs induced by pruning tokens, with closed-form scores derived for isolated keys, isolated values, and joint key-value pairs. Our scores account not only for attention weights but also for information from value states and attention outputs, thereby enhancing existing eviction strategies with output-aware signals. Experiments on LLaMA and Qwen models demonstrate that replacing the heuristic scores in existing works, which estimate token saliency across different query positions, with OBCache's output-aware scores consistently improves long-context accuracy. Code is available at https://github.com/DreamSoul-AI/OBCache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuzhe Gu, Xiyu Liang, Jiaojiao Zhao, Enmao Diao
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/DreamSoul-AI/OBCache](https://github.com/DreamSoul-AI/OBCache)
- 阅读深度：metadata
