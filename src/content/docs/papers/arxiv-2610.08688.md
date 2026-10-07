---
title: "A Framework for Accelerating Transformer Inference on RISC-V for Edge AI"
description: "This work presents a framework for accelerating transformer-based language models (LMs) on resource-constrained IoT devices."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.08688) · [PDF](https://arxiv.org/pdf/2610.08688)

## 一句话摘要

This work presents a framework for accelerating transformer-based language models (LMs) on resource-constrained IoT devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

This work presents a framework for accelerating transformer-based language models (LMs) on resource-constrained IoT devices. The framework targets compact LMs: BERT-Tiny (B-Ty), MobileBERT (M-Bt), MiniLM (M-Lm), Electra (E-Lt) and DeBERTa (D-Bt) -- selected for their architectural diversity and use in edge inference scenarios. The proposed flow derives lightweight instruction set extensions tailored to the non-obvious computational patterns of these models. In addition, a custom instruction is introduced to accelerate the address generation stage of batch matrix multiplication, achieving a performance improvement of 15.39--21.74% with modest ASIC overheads of 6.79% in area and 2.33% in power. To further enhance performance without incurring additional processor core hardware cost, an optional compiler-directed loop unrolling strategy is employed, trading increased code size for overall reduced execution time. Evaluation on the Synopsys trv32p3f RISC-V core demonstrates inference speedups of up to 2.19x, and FPGA implementation on the AMD Zynq UltraScale+ ZCU102 shows a 32.94% area overhead at 75 MHz, whereas the ASIC implementation using the TSMC 28 nm library incurs a 21.08% area overhead while operating at 250 MHz.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ajay Kumar M, Vishnu PS, Yike Li, Shreejith Shanker, Dimitrios S. Nikolopoulos, Bo Ji, Hans Vandierendonck, Deepu John
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
