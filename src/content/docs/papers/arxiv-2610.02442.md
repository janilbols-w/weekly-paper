---
title: "AI-driven Thermal-aware Data Center Capacity Planning"
description: "The emerging of large language models (LLMs) has posed significant challenges to the thermal management of data center."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.02442) · [PDF](https://arxiv.org/pdf/2610.02442)

## 一句话摘要

The emerging of large language models (LLMs) has posed significant challenges to the thermal management of data center.

## 为什么值得关注

待编辑增强。

## 摘要原文

The emerging of large language models (LLMs) has posed significant challenges to the thermal management of data center. Intense GPU computation for LLMs results in localized hotspots. Moreover, spiking thermal loads during training and inference bursts make real-time cooling response more difficult to predict and control. Thermal-aware capacity planning of data center requires massive expensive high-fidelity CFD simulations. AI models can perform real-time prediction for unseen designs. However, existing works either have large prediction error, or have over-simplified assumptions for data center operations. This work presents an AI-driven framework that can perform thermal-aware capacity planning for a real-world data center in seconds. The embedded AI model learns from numerous key parameters (rack power, server power, server placement, HVAC settings etc.), and provides temperature prediction within milliseconds. This AI model is tested against high-fidelity CFD simulations, and results show that for unseen data center designs, model can achieve high accuracy with 10000X speedup. Driven by the AI model, the authors design the thermal-aware capacity planning framework. This framework can help data center designers and operators instantaneously optimize both workload distribution and HVAC cooling efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: thermal management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yixing Li, Mark Fenton, Matthew Kaufeler, Ka Ming Leung, Xin Ai, Zhiyu Zeng
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
