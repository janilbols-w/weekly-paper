---
title: "SLICE-CiM: Selective Layer-wise Inference Control Engine with Confidence-Based Early Exit for SRAM based Digital Compute-in-Memory"
description: "Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.37601) · [PDF](https://arxiv.org/pdf/2610.37601)

## 一句话摘要

Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3).

## 为什么值得关注

待编辑增强。

## 摘要原文

Digital SRAM compute-in-memory (CIM) macros enable energy-efficient CNN inference by eliminating off-chip weight transfers; however, peripheral control logic introduces three inefficiencies: bit- slice over-activation at reduced precision (L1), unnecessary accumula- tion depth (L2), and idle precision-transition stalls (L3). To address these, we present four synthesizable peripheral blocks: a Flush-Merge Enable (FME) controller, a Confidence-Based Early-Exit (EE) module, a Precision Register with Decoder (PR/PD), and a Bit-Serial Cycle Controller (CC), co-designed to minimize switching activity, wordline overhead, and leakage. Implemented in TSMC 65-nm CMOS at 335 MHz, the peripheral framework occupies 1769.760 {\mu}m2 post-synthesis and 1982.131 {\mu}m2 post-PnR. Gate-level VCD analysis reports 6.0706 {\mu}W leakage and 288.2902 {\mu}W (post-synthesis) / 322.8850 {\mu}W (post-PnR) dynamic power, totaling 328.9556 {\mu}W (0.2402% of system power). The EE module dominates dynamic power (58.2%), while WLG dominates area (58.1%). System evaluation on MobileNetV2 (CIFAR-100) shows efficiency scaling from 31.35 TOPS/W (8b/8b, 1.2 V) to 454.91 TOPS/W (2b/8b, 0.8 V), achieving 13.33x improvement without bitcell modification or retraining. The framework targets CNN workloads exploiting sparsity, with Transformer extension as future work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Pratham Sharma, Mohd Faisal Khan, Santosh Kumar Vishvakarma
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
