---
title: "SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference"
description: "SharQ 以在线稀疏—稠密分解处理激活：将离群值为主的 N:M 稀疏骨干量化为 FP4，再用稠密 FP4 残差同时补偿掩码损失与稀疏路径量化误差，并融合准备阶段算子。"
---

**评分：59/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.26587) · [PDF](https://arxiv.org/pdf/2606.26587)

## 一句话摘要

SharQ 以在线稀疏—稠密分解处理激活：将离群值为主的 N:M 稀疏骨干量化为 FP4，再用稠密 FP4 残差同时补偿掩码损失与稀疏路径量化误差，并融合准备阶段算子。

## 为什么值得关注

该方法无需校准数据、重训练或模型专用调参，尝试把现代加速器已有的半结构化稀疏与 FP4 能力组合起来，直接改善推理延迟和吞吐。

## 摘要原文

Low-bit floating-point formats and semi-structured sparsity are increasingly supported by modern accelerators, yet combining them for LLM activation compression remains challenging: activations contain input-dependent outliers that dominate block scales in FP4 quantization, and directly applying N:M sparsity masks discards moderate values, coupling sparsification loss with quantization error. We introduce SharQ, a training-free inference method that bridges activation sparsity and FP4 quantization through an online sparse--dense decomposition. For each activation tensor, SharQ generates an input-adaptive N:M mask to extract an outlier-dominated sparse backbone, quantizes it to FP4, and defines a dense residual relative to the quantized sparse backbone rather than the unquantized sparse values. A sparse FP4 GEMM processes the backbone while a dense FP4 GEMM compensates for both mask-induced activation loss and sparse-path quantization error. The two paths share a single FP4 weight payload with path-specific scale views, and a fused preparation kernel absorbs mask generation, residual construction, and layer normalization into one operator. SharQ requires no calibration data, retraining, or model-specific tuning. Evaluated on Llama-3.1-8B, Qwen2.5-7B, Qwen3-30B-A3B, and Qwen3-VL-8B, SharQ recovers 43--63% of the NVFP4-to-FP16 accuracy gap across language and vision-language tasks, and generalizes across NVFP4, HiF4, and MXFP4 formats. On an RTX 5090, SharQ delivers 2.2--2.4$\times$ latency reduction over FP16 and 1.2--1.4$\times$ throughput improvement over FP8 in language model serving, and up to 1.58$\times$ speedup on Wan2.2-T2V-A14B video generation when combined with SageAttention. Our code is available at https://github.com/actypedef/SharQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 25 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected
- 限制：性能结果主要来自 RTX 5090 与文中选定的模型和低精度格式；双路径 GEMM、融合算子及稀疏 FP4 支持对硬件和运行时有明确依赖，跨平台收益仍待验证。

## 元数据

- 作者：Haoqian Meng, Yilun Luo, Yafei Zhao, Wenyuan Liu, Huaqing Zheng, Xindian Ma, Peng Zhang
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/actypedef/SharQ](https://github.com/actypedef/SharQ)
- 阅读深度：abstract
