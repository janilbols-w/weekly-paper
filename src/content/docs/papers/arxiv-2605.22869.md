---
title: "FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning"
description: "Both full fine-tuning (Full FT) and parameter-efficient fine-tuning methods such as LoRA introduce weight updates without accounting for the spectral structure established during pretraining."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.22869) · [PDF](https://arxiv.org/pdf/2605.22869)

## 一句话摘要

Both full fine-tuning (Full FT) and parameter-efficient fine-tuning methods such as LoRA introduce weight updates without accounting for the spectral structure established during pretraining.

## 为什么值得关注

待编辑增强。

## 摘要原文

Both full fine-tuning (Full FT) and parameter-efficient fine-tuning methods such as LoRA introduce weight updates without accounting for the spectral structure established during pretraining. As a result, noisy gradients from limited fine-tuning data can perturb robust pretrained features. We identify spectral preconditioning as the missing ingredient: reparameterizing each weight matrix through its full-rank singular value decomposition (SVD) and freezing one singular basis constrains updates to the pretrained column space, yielding a preconditioned optimization scheme that outperforms unconstrained Full FT at the same trainable parameter count. Building on this insight, we propose FuRA (Full-Rank Adaptation), an efficient full-rank adaptation framework based on a block tensor-train factorization W = LSR, where the large core L is fixed to the pretrained block-wise SVD basis, while only the compact core R and the block-wise singular values S are optimized. This design simultaneously provides full-rank spectral preconditioning, preserves full-rank update expressivity, and achieves parameter, memory, and step-time efficiency comparable to LoRA. FuRA consistently outperforms Full FT across multiple settings, including LLM fine-tuning (+1.37 on LLaMA-3-8B commonsense reasoning), LLM reinforcement learning for mathematical reasoning, and visual instruction tuning for VLMs. Furthermore, the 4-bit quantized variant, QFuRA, also surpasses QLoRA. Code is available at https://github.com/yequanzhao/FuRA

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yequan Zhao, Ruijie Zhang, Liyan Tan, Niall Moran, Tong Qin, Zheng Zhang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/yequanzhao/FuRA](https://github.com/yequanzhao/FuRA)
- 阅读深度：metadata
