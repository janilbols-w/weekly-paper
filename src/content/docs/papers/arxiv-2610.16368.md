---
title: "LoopQuant: Accurate and Efficient Post-Training Quantization for Looped Transformers"
description: "Looped Language Models (LoopLMs) improve parameter efficiency by recursively reusing shared Transformer modules, yet their repeated computation over evolving recurrent states poses new challenges for low-bit deployment."
---

**评分：59/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.16368v1) · [PDF](https://arxiv.org/pdf/2610.16368v1)

## 一句话摘要

Looped Language Models (LoopLMs) improve parameter efficiency by recursively reusing shared Transformer modules, yet their repeated computation over evolving recurrent states poses new challenges for low-bit deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped Language Models (LoopLMs) improve parameter efficiency by recursively reusing shared Transformer modules, yet their repeated computation over evolving recurrent states poses new challenges for low-bit deployment. Existing post-training quantization (PTQ) methods, largely designed for feed-forward Transformers, fail to account for cross-loop activation dynamics, heterogeneous loop sensitivity, and recursive error propagation, leading to substantial performance degradation at low precision. To address these challenges, we propose LoopQuant, a loop-aware PTQ framework for accurate and efficient low-bit quantization of LoopLMs. LoopQuant is built on three core components: 1) Cross-Loop Distribution Canonicalization (CLDC) learns a shared quantization-friendly representation across recurrent states while preserving parameter sharing; 2) Interaction-Aware Loop-wise Precision Allocation (ILPA) allocates activation precision under a fixed bit budget by modeling task-level loop sensitivity and cross-loop interactions; and 3) Loop-Conditioned Task Calibration (LCTC) further aligns quantized inference with the low-bit recursive trajectory through lightweight task-space calibration. Extensive experiments across LoopLM architectures demonstrate that LoopQuant consistently outperforms existing low-bit PTQ methods. On Ouro-2.6B, LoopQuant under W4A4 surpasses all W4A8 baselines in performance, while reducing model memory by 65.3% with only 3.4% additional storage overhead over naive INT4 and achieving a 1.7 times decoding speedup over BF16. These results demonstrate a strong balance among accuracy, compression, and inference efficiency, providing a practical and deployment-friendly solution for low-bit LoopLM inference. The code is available at [https://github.com/Kishon-zzx/LoopQuant].

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, low precision, quantization, quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zhixiong Zhao, Zukang Xu, Xing Hu, Lifeng Liu, Guangyu Sun, Dawei Yang
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/Kishon-zzx/LoopQuant](https://github.com/Kishon-zzx/LoopQuant)
- 阅读深度：metadata
