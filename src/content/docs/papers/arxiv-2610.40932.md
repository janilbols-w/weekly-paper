---
title: "HippocamFLEX: FPGA Prototyping of Hippocampus-Inspired Architecture for Context-Aware Sequence Prediction"
description: "Unlike conventional architectures that treat memory as static pattern storage, the hippocampus organizes experience as ordered sequences and retrieves them through temporally compressed replay spanning prior, current, and anticipated states."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.40932) · [PDF](https://arxiv.org/pdf/2610.40932)

## 一句话摘要

Unlike conventional architectures that treat memory as static pattern storage, the hippocampus organizes experience as ordered sequences and retrieves them through temporally compressed replay spanning prior, current, and anticipated states.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unlike conventional architectures that treat memory as static pattern storage, the hippocampus organizes experience as ordered sequences and retrieves them through temporally compressed replay spanning prior, current, and anticipated states. This capacity of context-appropriate sequence prediction remains absent from conventional deep learning accelerators and existing neuromorphic fabrics. We present HippocamFLEX, a fully synthesizable digital implementation of these hippocampal computational principles, realized with SystemVerilog RTL on the AMD Zynq UltraScale+,XCZU9EG. The design maps the hippocampal trisynaptic pathway onto three pipeline stages: a Dentate Gyrus / Entorhinal Cortex (DG/EC) stage for hypervector proximity matching, a CA3 stage for context-gated recurrent sequence prediction with multi-phase temporal tagging, and a CA1 stage that integrates past, present, and predicted future events into a theta-sequence inspired output. While much brain-inspired hardware relies on analog mixed-signal design for energy efficiency, this work targets FPGA prototyping as a deliberate architectural choice: FPGAs offer rapid design-space exploration without tape-out cost, bit-exact determinism that simplifies verification. The design supports 64 events across 16 contexts and is verified on physical silicon across context-isolation, temporal-ordering, and mid-sequence sliding-window test cases and is inherently scalable to larger event and context sets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bhuvanesh S. Kayarabettu, Hamed Poursiami, Keiland Cooper, Babak Shahbaba, Norbert Fortin, Maryam Parsa, Akhilesh Jaiswal
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
