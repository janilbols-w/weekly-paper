---
title: "One-Cycle Fault Classification and Faulted-Line Identification on the PROTECT-90 Dataset: An Initial Application Benchmark"
description: "Open electromagnetic-transient datasets are beginning to make reproducible learning-based protection studies possible, but the practical use of these datasets still requires application-level benchmarks that define timing, sensing, and validation assumptions."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2610.04155) · [PDF](https://arxiv.org/pdf/2610.04155)

## 一句话摘要

Open electromagnetic-transient datasets are beginning to make reproducible learning-based protection studies possible, but the practical use of these datasets still requires application-level benchmarks that define timing, sensing, and validation assumptions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Open electromagnetic-transient datasets are beginning to make reproducible learning-based protection studies possible, but the practical use of these datasets still requires application-level benchmarks that define timing, sensing, and validation assumptions. This paper presents an initial application benchmark on the recently released PROTECT-90 dataset for two protection-oriented tasks: fault-type classification and discrete faulted-line identification. A compact one-dimensional convolutional neural network (CNN) is evaluated using post-inception windows of 0.25, 0.5, 1, and 2 cycles under strict episode-wise splitting. A non-convolutional multilayer perceptron (MLP) is also trained as an architecture-control baseline. The results show that both tasks are nearly saturated under full observability, with one-cycle test accuracies of 99.84% for fault type and 100.00% for line identification. The main performance variation appears under reduced observability: current-only inputs preserve line identification accuracy at 100.00%, whereas voltage-only inputs reduce line identification accuracy to 53.09% with the CNN and 50.57% with the MLP. This indicates that the limiting factor is measurement information rather than neural architecture. Additional stratified checks show stable performance across topology states and fault-resistance bins, while CPU inference contributes only 0.528 ms to the one-cycle total decision time of 20.53 ms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Emad Abukhousa, Abdulaziz Qwbaiban, Saman Zonouz, A. P. Sakis Meliopoulos
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
