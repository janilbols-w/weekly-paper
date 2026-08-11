---
title: "From Interface to Inference: Eliciting Any-Order Inference from Any-Order Models"
description: "Many discrete reasoning tasks, such as code generation, are inherently non-causal: programmers move between high-level structure and local details, a process we call any-order inference."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2607.26504) · [PDF](https://arxiv.org/pdf/2607.26504)

## 一句话摘要

Many discrete reasoning tasks, such as code generation, are inherently non-causal: programmers move between high-level structure and local details, a process we call any-order inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many discrete reasoning tasks, such as code generation, are inherently non-causal: programmers move between high-level structure and local details, a process we call any-order inference. For autoregressive language models, which lack a native any-order interface, non-causal abilities such as infilling and next-edit prediction require hand-designed mechanisms. Can we instead design models that natively support any-order inference? Masked diffusion models have recently emerged as compelling candidates, as their any-order training objective naturally offers an any-order prediction interface. This interface, however, does not automatically yield any-order inference. We demonstrate that this interface-inference gap stems from positional uncertainty: fixed-canvas, token-level models may know what semantic component should appear without knowing where to place it. In light of this, we propose two complementary approaches: (1) Insertion-based masked diffusion, building on FlexMDM (Kim et al, 2025), relaxes fixed-position commitments via insertions, enabling generation across non-contiguous regions. (2) Latent-space masked diffusion shifts prediction to coarser semantic segments, enabling search over latent generation orders. Empirically, we train a 7B FlexMDM for Python coding and a 125M LatentMDM for GSM8K and show that both approaches induce distinct any-order inference behaviors and improve downstream performance. We release our codebase at https://github.com/SeunggeunKimkr/genuine-any-order.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Seunggeun Kim, Jaeyeon Kim, Taekyun Lee, Yuyuan Chen, Yilun Du, Sham Kakade, Sitan Chen
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SeunggeunKimkr/genuine-any-order](https://github.com/SeunggeunKimkr/genuine-any-order)
- 阅读深度：metadata
