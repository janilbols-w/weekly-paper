---
title: "FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference by Algorithm-Kernel Synergy"
description: "While binary quantization theoretically promises extreme compression and acceleration for Large Language Models (LLMs), existing research often overlooks the necessity of specialized hardware kernels, thus failing to unleash the full acceleration potential due to persistent reliance on expensive floating-point arithmetic or runtime dequantization overheads."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.15602) · [PDF](https://arxiv.org/pdf/2608.15602)

## 一句话摘要

While binary quantization theoretically promises extreme compression and acceleration for Large Language Models (LLMs), existing research often overlooks the necessity of specialized hardware kernels, thus failing to unleash the full acceleration potential due to persistent reliance on expensive floating-point arithmetic or runtime dequantization overheads.

## 为什么值得关注

待编辑增强。

## 摘要原文

While binary quantization theoretically promises extreme compression and acceleration for Large Language Models (LLMs), existing research often overlooks the necessity of specialized hardware kernels, thus failing to unleash the full acceleration potential due to persistent reliance on expensive floating-point arithmetic or runtime dequantization overheads. To bridge this gap, we propose FluxBin (\textbf{F}lexible \textbf{L}UT-based \textbf{U}ltra-low-bit e\textbf{X}ecution with \textbf{Bin}ary bases), an algorithm-kernel co-design that synergizes post-training quantization with a highly optimized CUDA kernel. Algorithmically, we introduce Decoupled Row-Column Binary Decomposition to enhance representational capacity while maintaining hardware efficiency, complemented by a Hessian-guided saliency-aware hybrid bases that preserve critical information. At the kernel level, we implement a Lookup Table Building Approach with Scale Fusion to reduce floating-point arithmetic, featuring a Virtual Columnar Mapping that transforms irregular, sparse, and salient matrices into dense execution. Extensive evaluations demonstrate FluxBin achieves up to $5.92\times$ speedup and $10.19\times$ energy savings across diverse model architectures, delivering comparable accuracy to heavily fine-tuned methods. This effectively enables the deployment of 70B-scale models on one single A100 GPU with a $4\times$ memory reduction. Code is available at https://github.com/nicyyyy/FluxBin.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cuda kernel
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Qingyao Yang, Runming Yang, He Xiao, Wendong Xu, Junyu Chen, Haobo Liu, Chenchen Ding, Ruihan Hu, Yik-Chung Wu, Ngai Wong
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/nicyyyy/FluxBin](https://github.com/nicyyyy/FluxBin)
- 阅读深度：metadata
