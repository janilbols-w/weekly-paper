---
title: "Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign"
description: "Modern ML workloads, with stringent latency and energy constraints, are increasingly hard to run efficiently on homogeneous commodity hardware."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.10970) · [PDF](https://arxiv.org/pdf/2609.10970)

## 一句话摘要

Modern ML workloads, with stringent latency and energy constraints, are increasingly hard to run efficiently on homogeneous commodity hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern ML workloads, with stringent latency and energy constraints, are increasingly hard to run efficiently on homogeneous commodity hardware. We argue that operator-level disaggregation--tailoring microarchitecture, batching, and memory hierarchy to each operator--is essential to overcome these limitations, though the resulting highly bespoke accelerators incur prohibitive Non-Recurring Engineering (NRE) costs. Chiplet-based integration amortizes NRE across applications, but choosing which chiplets to build and how to compose them into accelerators is circularly dependent--a chiplet pool's value depends on the constructed accelerators, while accelerator quality is constrained by available chiplets. This paper introduces Fengshui, a chiplet ecosystem and accelerator co-design framework that jointly optimizes chiplet pool composition and bespoke application-specific integrated circuit (BASIC) design. Fengshui constructs BASICs through operator-level disaggregation, co-exploring chiplet and memory heterogeneity, tensor fusion, and pipeline/tensor/expert parallelism with place-and-route validation for physical implementability. With just 8 strategically selected chiplets, encompassing network switches, processing-in-memory units, and accelerators with diverse microarchitectures, Fengshui-generated BASICs achieve 48.5%, 88.1%, 93.0%, and 97.8% reductions in energy, energy-cost product (EC), energy-delay product (EDP), and energy-delay-cost product (EDPC) over homogeneous accelerators, while scoring within 4.1% of unconstrained heterogeneous designs across diverse neural networks. For datacenter MoE and dense LLM serving, Fengshui reduces prefill energy and EC by up to 16.8% and 28.7%, respectively; for edge autonomous vehicle perception, it achieves 12.0% energy and 23.6% EC reductions under real-time latency constraints.

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

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoran Jin, Jirong Yang, Zhiheng Zhang, Justin Shin, Barry Lyu, Kangqi Zhang, Yunpeng Liu, Nathan Bleier
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
