---
title: "CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM"
description: "Attention-FC Disaggregated (AFD) LLM inference systems offload memory-bound Attention operations to memory-rich accelerators (e.g., CPUs, HBM-PIM) while retaining compute-bound Fully-Connected (FC) operations on GPUs."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2504.17584) · [PDF](https://arxiv.org/pdf/2504.17584)

## 一句话摘要

Attention-FC Disaggregated (AFD) LLM inference systems offload memory-bound Attention operations to memory-rich accelerators (e.g., CPUs, HBM-PIM) while retaining compute-bound Fully-Connected (FC) operations on GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention-FC Disaggregated (AFD) LLM inference systems offload memory-bound Attention operations to memory-rich accelerators (e.g., CPUs, HBM-PIM) while retaining compute-bound Fully-Connected (FC) operations on GPUs. In this paper, we first design a Disaggregated Roofline Model (DRM) to characterize AFD performance, revealing that system throughput is constrained by the accelerator's limiting factor: either memory bandwidth or capacity. We observe that prior AFD systems often overlook these constraints and fail to balance them, leading to resource underutilization or constrained throughput. Therefore, we propose CHIME, the first AFD system integrating DIMM-PIM, which is a case of the new accelerator that strikes the balance with scalable capacity and bandwidth. To address the synchronization challenges inherent to the distributed cooperating DRAM chips in DIMM-PIM, CHIME employs bubble-free pipelining and hybrid-grained re-layout for efficient attention computation. Furthermore, it maximizes cross-device resource utilization via rankset-granular communication-computation overlapping and alignment-predicting scheduling. Evaluations show CHIME achieves up to 5.15$\times$ speedup over state-of-the-art HBM-PIM solutions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: disaggregated inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qingyuan Liu, Liyan Chen, Haocheng Wang, Yanning Yang, Dong Du, Zhigang Mao, Naifeng Jing, Yubin Xia, Haibo Chen
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
