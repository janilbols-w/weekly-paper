---
title: "SpecReuse: Spectral Graph Reuse for Efficient Vision GNN Inference on FPGAs"
description: "Dynamic Image Graph Construction (DIGC) is the primary performance bottleneck in FPGA acceleration of Vision Graph Neural Networks (ViGs), reconstructing graph connectivity at every layer through irregular, memory-intensive computation."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.17718) · [PDF](https://arxiv.org/pdf/2609.17718)

## 一句话摘要

Dynamic Image Graph Construction (DIGC) is the primary performance bottleneck in FPGA acceleration of Vision Graph Neural Networks (ViGs), reconstructing graph connectivity at every layer through irregular, memory-intensive computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic Image Graph Construction (DIGC) is the primary performance bottleneck in FPGA acceleration of Vision Graph Neural Networks (ViGs), reconstructing graph connectivity at every layer through irregular, memory-intensive computation. Existing FPGA accelerators optimize DIGC but still execute it unconditionally, making repeated graph reconstruction a persistent source of latency and energy consumption. We propose the SpecReuse algorithm, which computes compact spectral descriptors of intermediate features and reuses previously constructed graphs when descriptor drift remains below a calibrated threshold. We further present the SpecReuse accelerator, an FPGA architecture that realizes graph reuse through lightweight hardware for spectral descriptor extraction and reuse control while remaining compatible with existing graph-construction accelerators. Experimental results demonstrate up to a $2.69\times$ speedup in end-to-end inference and approximately 58--65\% lower energy per inference with negligible FPGA resource overhead and minimal loss in classification accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Isabella Bernhardt Eiliya, Anvitha Ramachandran, Dhruv Parikh, Viktor Prasanna
- 发布：2026-09-15；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
