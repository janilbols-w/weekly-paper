---
title: "Model Compression and Hardware-Aware Acceleration for Deep Learning on FPGAs: A Co-Design Taxonomy and Comparative Analysis"
description: "Deploying deep neural networks on Field-Programmable Gate Arrays (FPGAs) requires joint reasoning about model compression and hardware acceleration, however the most comprehensive existing cross-platform treatment of this space, Deng et al.~\\cite{deng2020model}, compared compression techniques against CPU, GPU, FPGA, and ASIC targets at the level of broad, q"
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.21657) · [PDF](https://arxiv.org/pdf/2608.21657)

## 一句话摘要

Deploying deep neural networks on Field-Programmable Gate Arrays (FPGAs) requires joint reasoning about model compression and hardware acceleration, however the most comprehensive existing cross-platform treatment of this space, Deng et al.~\cite{deng2020model}, compared compression techniques against CPU, GPU, FPGA, and ASIC targets at the level of broad, q

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying deep neural networks on Field-Programmable Gate Arrays (FPGAs) requires joint reasoning about model compression and hardware acceleration, however the most comprehensive existing cross-platform treatment of this space, Deng et al.~\cite{deng2020model}, compared compression techniques against CPU, GPU, FPGA, and ASIC targets at the level of broad, qualitative trade-offs, and not specific FPGA resource consequences. This survey instead restricted the scope to FPGAs alone and organized 25 compression-hardware co-design case studies (2015--2026) into a five-category taxonomy defined by which FPGA resources each strategy primarily reshapes: DSP-eliminating, DSP-repurposing/mixed-precision, sparsity-exploiting, memory-hierarchy-driven, and toolchain/deployment-level. Normalizing these case studies along a common set of dimensions (compression ratio, accuracy change, throughput, energy efficiency, and DSP/LUT/BRAM utilization) surfaces a central, quantitative finding; of the 25 reviewed works, only \emph{one} reported a compression ratio and accuracy change measured against a single common baseline, and only \emph{two} reported energy efficiency normalized against a common GPU baseline, exposing a field-wide characterization gap that no individual toolchain (FINN, HLS4ML, Vitis AI, or DNNWeaver) resolves on its own. Building on this taxonomy and meta-analysis, we formalize six open challenges: toolchain fragmentation, accuracy--efficiency characterization, automated mixed-precision optimization, sparse computation reliability, persistent memory bottlenecks, and FPGA-based training. Each is paired with a concrete next step grounded in extending an existing, cited technique, not a general call for future work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peter Forcha, H. Kajekusumadhar, Mbua Peter, Muhammed Kawser, Audrey Cyriell Mo, Christophe Bobda
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
