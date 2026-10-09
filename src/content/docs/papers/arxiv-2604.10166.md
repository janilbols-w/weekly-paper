---
title: "Virtual Smart Metering in District Heating Networks via Heterogeneous Spatial-Temporal Graph Neural Networks"
description: "Intelligent operation of thermal energy networks aims to improve energy efficiency, reliability, and operational flexibility through data-driven control, predictive optimization, and early fault detection."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2604.10166) · [PDF](https://arxiv.org/pdf/2604.10166)

## 一句话摘要

Intelligent operation of thermal energy networks aims to improve energy efficiency, reliability, and operational flexibility through data-driven control, predictive optimization, and early fault detection.

## 为什么值得关注

待编辑增强。

## 摘要原文

Intelligent operation of thermal energy networks aims to improve energy efficiency, reliability, and operational flexibility through data-driven control, predictive optimization, and early fault detection. Achieving these goals relies on sufficient observability, requiring continuous and well-distributed monitoring of thermal and hydraulic states. However, district heating systems are typically sparsely instrumented and frequently affected by sensor faults, limiting monitoring. Virtual sensing offers a cost-effective means to enhance observability, yet its development and validation remain limited in practice. Existing data-driven methods generally assume dense synchronized data, while analytical models rely on simplified hydraulic and thermal assumptions that may not adequately capture the behavior of heterogeneous network topologies. Consequently, modeling the coupled nonlinear dependencies between pressure, flow, and temperature under realistic operating conditions remains challenging. In addition, the lack of publicly available benchmark datasets hinders systematic comparison of virtual sensing approaches. To address these challenges, we propose a heterogeneous spatial-temporal graph neural network (HSTGNN) for constructing virtual smart heat meters. The model incorporates the functional relationships inherent in district heating networks and employs dedicated branches to learn graph structures and temporal dynamics for flow, temperature, and pressure measurements, thereby enabling the joint modeling of cross-variable and spatial correlations. To support further research, we introduce a controlled laboratory dataset collected at the Aalborg Smart Water Infrastructure Laboratory, providing synchronized high-resolution measurements representative of real operating conditions. Extensive experiments demonstrate that the proposed approach significantly outperforms existing baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Keivan Faghih Niresi, Christian M{\o}ller Jensen, Carsten Skovmose Kalles{\o}e, Rafael Wisniewski, Olga Fink
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
