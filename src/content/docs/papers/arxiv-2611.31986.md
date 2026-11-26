---
title: "Network-Guided Automated Synthesis of MAC Units for Neural Network Inference"
description: "In neural inference accelerators, multiply-accumulate (MAC) datapaths account for the majority of circuit area and critical-path delay, where operator-level numerical formats simultaneously dictate hardware overhead and quantization error."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.31986) · [PDF](https://arxiv.org/pdf/2611.31986)

## 一句话摘要

In neural inference accelerators, multiply-accumulate (MAC) datapaths account for the majority of circuit area and critical-path delay, where operator-level numerical formats simultaneously dictate hardware overhead and quantization error.

## 为什么值得关注

待编辑增强。

## 摘要原文

In neural inference accelerators, multiply-accumulate (MAC) datapaths account for the majority of circuit area and critical-path delay, where operator-level numerical formats simultaneously dictate hardware overhead and quantization error. Yet no straightforward mapping exists between hardware cost and end-to-end network accuracy: logic synthesis transforms datapaths in a highly nonlinear manner, while numerical errors propagate and couple across layers. To address this disconnect, we present NAMSI, an automated network-aware MAC synthesis framework tailored for neural inference. NAMSI characterizes heterogeneous data formats using a format-distribution representation (FD) and leverages topology-aware accuracy and hardware-cost modeling (TaH), calibrated with actual post-synthesis Area-Delay Product (ADP) measurements, to jointly estimate coupled full-network accuracy and circuit cost. Furthermore, reversible lattice search (RLS) is introduced to tractably navigate the exponentially scaling design space. Evaluations across five neural networks on ImageNet-1K demonstrate that under post-training quantization (PTQ), NAMSI achieves 54.2%-60.4% reductions in post-synthesis MAC ADP compared with FP32 while retaining at least 99% of full-precision Top-1 accuracy, surpassing baseline approaches in both hardware efficiency and accuracy preservation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhouyang Wu, Hongyang Pan, Chuyu Wang, Ji Zhuang, Keren Zhu, Xin Zhao, Xuan Zeng
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
