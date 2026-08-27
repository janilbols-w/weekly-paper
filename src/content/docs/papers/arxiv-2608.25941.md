---
title: "When Pruning Meets Interpretability: Preserving Sparse Autoencoder Robustness in LLMs"
description: "Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.25941) · [PDF](https://arxiv.org/pdf/2608.25941)

## 一句话摘要

Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse autoencoders (SAEs) are widely used to interpret the internal representations of large language models (LLMs), yet their reliability under post-hoc model compression remains poorly understood. We present a systematic study of how pruning affects SAE behavior and theoretically show that, for a fixed SAE, its impact is governed by perturbation energy, a covariance-weighted norm. This perspective exposes a key limitation of magnitude pruning: by ignoring activation geometry, it distorts the learned representation space and degrades SAE functionality. Activation-aware methods such as Wanda and SparseGPT, in contrast, implicitly control perturbation energy and are therefore substantially more robust at preserving SAE behavior. We further reveal a consistent structural vulnerability across all pruning methods: middle layers are significantly more sensitive to pruning than early or late layers. Guided by this insight, we propose a layer-wise sparsity allocation strategy, achieving lower perplexity under the same average pruning sparsity. Experiments across four model architectures validate our theoretical findings. Code is publicly available at https://github.com/osu-srml/sae-robustness-under-pruning/tree/main.

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

- 作者：Suchit Gupte, Xueru Zhang, Mohammad Mahdi Khalili
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/osu-srml/sae-robustness-under-pruning/tree/main](https://github.com/osu-srml/sae-robustness-under-pruning/tree/main)
- 阅读深度：metadata
