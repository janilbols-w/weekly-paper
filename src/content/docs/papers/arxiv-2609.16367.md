---
title: "FINNAS: FINN-Guided Hardware-Aware NAS and Pruning for FPGA Jet Substructure Classification"
description: "FPGAs are well suited to deploying quantised neural networks (QNNs) under strict accuracy, latency, and resource constraints; however, identifying efficient model-accelerator combinations commonly requires extensive manual design-space exploration and repeated hardware synthesis."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.16367) · [PDF](https://arxiv.org/pdf/2609.16367)

## 一句话摘要

FPGAs are well suited to deploying quantised neural networks (QNNs) under strict accuracy, latency, and resource constraints; however, identifying efficient model-accelerator combinations commonly requires extensive manual design-space exploration and repeated hardware synthesis.

## 为什么值得关注

待编辑增强。

## 摘要原文

FPGAs are well suited to deploying quantised neural networks (QNNs) under strict accuracy, latency, and resource constraints; however, identifying efficient model-accelerator combinations commonly requires extensive manual design-space exploration and repeated hardware synthesis. This paper presents FINNAS, a FINN-guided hardware-aware evolutionary neural architecture search framework. FINNAS jointly searches quantised MLP depth, width, and global precision settings, and ranks candidates using proxy validation accuracy together with FINN-estimated LUT usage and latency under a fully parallel mapping. Selected finalists are fully retrained, subjected to post-search unstructured pruning, and validated using RTL simulation and Vivado out-of-context synthesis. On the CERNBox jet substructure classification task, the searched implementations expose competitive accuracy-resource trade-offs. Compared with a manually optimised dense FINN accelerator, a compact FINNAS design improves accuracy from 73.78\% to 74.36\%, while reducing LUT usage by \(8.5\times\) and RTL-simulation latency by \(1.77\times\). Unstructured pruning further provides consistent LUT and FF reductions across the fully parallel finalists.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eva Chauffour, Changhong Li, Georgios Floros, Shreejith Shanker
- 发布：2026-09-14；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
