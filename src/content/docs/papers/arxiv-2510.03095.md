---
title: "SPID: Distilled Protein Backbone Generation"
description: "Diffusion- and flow-based generative models have recently demonstrated strong performance in protein backbone generation tasks, offering unprecedented capabilities for de novo protein design."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.03095) · [PDF](https://arxiv.org/pdf/2510.03095)

## 一句话摘要

Diffusion- and flow-based generative models have recently demonstrated strong performance in protein backbone generation tasks, offering unprecedented capabilities for de novo protein design.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion- and flow-based generative models have recently demonstrated strong performance in protein backbone generation tasks, offering unprecedented capabilities for de novo protein design. However, despite their generation quality, these models are constrained by slow sampling, often requiring hundreds of iterative steps. This computational bottleneck limits their practical utility in large-scale protein discovery, where thousands to millions of candidate structures are needed. To address this challenge, we explore the techniques of score distillation, which has shown great success in reducing the number of sampling steps in the vision domain while maintaining high generation quality. However, a straightforward adaptation of these methods results in unacceptably low designability. We introduce Score Protein identity Distillation (SPID), which resolves this incompatibility by combining few-step generation with inference-time noise scaling. SPID adapts the Score identity Distillation (SiD) framework to both diffusion- and flow-based models without requiring access to pretraining data. Applied to the Proteina flow-matching model, our 16-step generator achieves 94.4% designability, matching the 400-step teacher, while delivering more than a 20-fold reduction in effective backbone-generation time and maintaining comparable diversity and novelty. SPID generalizes across unconditional generation, fold-class conditional generation, and motif scaffolding, and extends to equivariant diffusion architectures, achieving significant reduction in generation time with comparable generation quality to the teacher in all tasks. The resulting reduction in inference cost could facilitate large-scale in silico protein design, thereby advancing diffusion-based models toward real-world protein engineering applications. The PyTorch implementation is available at https://github.com/LY-Xie/SiD_Protein

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Liyang Xie, Haoran Zhang, Zhendong Wang, Wesley Tansey, Mingyuan Zhou
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LY-Xie/SiD_Protein](https://github.com/LY-Xie/SiD_Protein)
- 阅读深度：metadata
