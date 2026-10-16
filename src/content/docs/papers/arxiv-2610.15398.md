---
title: "GA-SVD: Generation-aware Singular Value Decomposition for LLM Compression"
description: "Large language models (LLMs) demonstrate strong generalization across a broad range of reasoning and generation tasks, but their large parameter counts impose substantial memory and computation costs, hindering deployment in practical resource-constrained settings."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.15398v1) · [PDF](https://arxiv.org/pdf/2610.15398v1)

## 一句话摘要

Large language models (LLMs) demonstrate strong generalization across a broad range of reasoning and generation tasks, but their large parameter counts impose substantial memory and computation costs, hindering deployment in practical resource-constrained settings.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) demonstrate strong generalization across a broad range of reasoning and generation tasks, but their large parameter counts impose substantial memory and computation costs, hindering deployment in practical resource-constrained settings. One-shot low-rank compression is a promising solution since it reduces model size and inference cost effectively. However, existing SVD-based methods primarily target multiple-choice benchmarks and often fail to preserve performance on generation tasks. Moreover, their rank allocation strategies are typically heuristic. We propose GA-SVD, a generation-aware low-rank compression framework for LLMs. First, we introduce Generation-Aware Weight Whitening (GAWW), which leverages gradients from on-policy knowledge distillation to construct whitening transformations aligned with generative behavior. Second, we develop an evolutionary global rank allocation method that searches for effective layer-wise rank allocation under a given global compression ratio. Across extensive experiments on Mistral-7B, Qwen3 series, and Llama-3.3 models, evaluated on both multiple-choice and generative benchmarks, GA-SVD consistently outperforms existing SVD-based baselines and achieves state-of-the-art (SoTA) results. We further demonstrate scalability by applying our method to models with up to 70B parameters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shengkun Tang, Cong Zeng, Zongfang Liu, Dan Alistarh, Zhiqiang Shen
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
