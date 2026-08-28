---
title: "Activation Outliers Matter: Robust Recovery for Quantized Multimodal LLMs"
description: "Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs)."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.26581) · [PDF](https://arxiv.org/pdf/2608.26581)

## 一句话摘要

Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit quantization offers a promising avenue for reducing the computational and memory demands of Multimodal Large Language Models (MLLMs). Recent hardware support for low-precision formats, ranging from MXFP8 to ultra-low-bit formats such as MXFP4 and HiF4, has accelerated research into efficient MLLM training and deployment. In this work, we present a systematic study of these quantization schemes in representative MLLMs that span both video generation and reasoning tasks. Our analysis shows that MXFP8 achieves near-lossless performance, whereas aggressive 4-bit quantization leads to significant degradation. Through extensive ablations, we identify activation quantization as the primary source of this performance loss, contributing substantially more than weight quantization. Motivated by this observation, we propose Residual Fallback Quantization (RFQ), a lightweight activation reconstruction framework that supplements the primary ulta-low-bit activation representation with an auxiliary quantized residual pathway. By explicitly modeling and compensating for quantization errors, RFQ improves activation fidelity while preserving the efficiency advantages of ultra-low-bit computation. RFQ requires no architectural modifications and incurs negligible computational overhead. Extensive experiments on Wan2.2 and Qwen3-VL demonstrate that RFQ consistently recovers a substantial portion of the performance lost under the quantization of MXFP4 and HiF4, significantly narrowing the gap to BF16 baselines across both generation and 4 reasoning benchmarks. Our findings establish activation quantization as the dominant bottleneck in ultra-low-bit MLLMs and highlight residual-based activation reconstruction as an effective and practical strategy for robust 4-bit deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tanzila Rahman, Mehran Taghian Jazi, Yunke Peng, Zhuang Ma, Anandharaju Durai Raju, Yao Wang, Xing Huang, Hei Yi Mak, Shadan Golestan, Hoang Le, Yonghan Dong, Wei Guo, Yaoyuan Wang
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
