---
title: "LSVD: Loss-Aware Low-Rank Approximation for Efficient Low-Precision Vision-Language Models"
description: "Vision-language models (VLMs) deliver strong multimodal reasoning capabilities, but their large computational cost and high parameter counts make deployment challenging on resource-constrained devices."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.00573) · [PDF](https://arxiv.org/pdf/2606.00573)

## 一句话摘要

Vision-language models (VLMs) deliver strong multimodal reasoning capabilities, but their large computational cost and high parameter counts make deployment challenging on resource-constrained devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) deliver strong multimodal reasoning capabilities, but their large computational cost and high parameter counts make deployment challenging on resource-constrained devices. Low-rank decomposition has emerged as a promising compression technique, yet existing methods often optimize local matrix reconstruction error, rely on uniform or heuristic rank allocation, and focus mainly on attention projections while leaving feed-forward networks underexplored. In this paper, we propose~\textit{LASER} (\textbf{L}oss-\textbf{A}ware \textbf{S}ingular-value d\textbf{E}composition and \textbf{R}ank allocation), a low-rank compression framework for efficient low-precision VLM inference. LASER derives a curvature-weighted SVD objective from a second-order approximation of the model loss and uses Kronecker-factored Fisher information to guide decomposition toward downstream performance rather than reconstruction alone. We further introduce a loss-aware cross-layer rank allocation strategy based on calibration gradients, enabling more effective parameter budgeting across layers. Finally, we extend low-rank compression to FFN layers through a hybrid scheme that combines SVD with quantization. The evaluation results show that LASER achieves more than $2.3\times$ decoding speedup over previous work while preserving strong accuracy under low-precision inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haiyu Wang, Yutong Wang, Leshu Li, Yihui Ren, Sai Qian Zhang
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
