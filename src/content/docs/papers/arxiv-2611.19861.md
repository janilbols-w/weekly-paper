---
title: "HBF-EventLab: A Discrete-Event Simulator for Studying Host-Device Coordination in High Bandwidth Flash"
description: "High Bandwidth Flash (HBF) combines NAND flash density with high-bandwidth accelerator connectivity, offering additional memory capacity for large language model inference."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.19861) · [PDF](https://arxiv.org/pdf/2611.19861)

## 一句话摘要

High Bandwidth Flash (HBF) combines NAND flash density with high-bandwidth accelerator connectivity, offering additional memory capacity for large language model inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

High Bandwidth Flash (HBF) combines NAND flash density with high-bandwidth accelerator connectivity, offering additional memory capacity for large language model inference. However, limited hardware availability makes it difficult to evaluate how host behavior and device resource constraints jointly affect HBF request processing. We present HBF-EventLab, an open-source, transaction-level discrete-event simulator based on the Open Compute Project HBF specification. HBF-EventLab connects host request dispatch, command admission, fragmented write assembly, read dispatch, NAND execution, and completion feedback within a shared event loop. It explicitly models distinct resource lifetimes and separates configurable scheduling policies from ordering and resource constraints, enabling controlled exploration of host-device coordination. Experiments show how resource limits, address interleaving, fragment arrival patterns, and scheduling policies affect write completion and request latency. The results highlight the need to consider resource limits and scheduling policies jointly, accounting for their interactions with write assembly and read eligibility. We also integrate HBF-EventLab with real GPU execution of Qwen3-0.6B, combining profiled GPU activity durations with simulated weight-access delays to estimate time to first token and time per output token, with logits and output tokens remaining bitwise identical to those from native GPU execution. HBF-EventLab provides a configurable foundation for studying HBF mechanisms, exploring scheduling policies, and assessing how HBF access delays affect application-level timing. The source code is publicly available at https://github.com/sjtu-epcc/HBF-EventLab.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ziqing Mei, Yiwei Huang, Zhiyi Zeng, Yuhao Xiao, Pu Pang, Quan Chen, Deze Zeng, Minyi Guo
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/sjtu-epcc/HBF-EventLab](https://github.com/sjtu-epcc/HBF-EventLab)
- 阅读深度：metadata
