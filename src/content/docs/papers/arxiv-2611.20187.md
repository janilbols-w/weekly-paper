---
title: "Cyber-Secure Wearable, Ultra-Low-Power Networked Sensors for Soldier Health Monitoring: Insights from the CAPSARII project"
description: "The CAPSARII project advances a cyber-secure, ultra-low-power wearable platform and Internet of Battlefield Things (IoBT) framework to support real-time monitoring of military personnel and data-driven decision support."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.20187) · [PDF](https://arxiv.org/pdf/2611.20187)

## 一句话摘要

The CAPSARII project advances a cyber-secure, ultra-low-power wearable platform and Internet of Battlefield Things (IoBT) framework to support real-time monitoring of military personnel and data-driven decision support.

## 为什么值得关注

待编辑增强。

## 摘要原文

The CAPSARII project advances a cyber-secure, ultra-low-power wearable platform and Internet of Battlefield Things (IoBT) framework to support real-time monitoring of military personnel and data-driven decision support. The architecture integrates smart-textile sensing, a body/squad area mesh, edge-deployed AI on secure RISC-V microcontrollers, and cloud/federated analytics for cross-mission learning and comparative studies. Two representative use cases--pilot fatigue and warfighters operating in harsh environments--guide requirements, validation, and interface design (including HUD and haptic feedback). As an initial step toward embedded models, we benchmark stress classification on a public wearable dataset: tree-ensemble baselines achieve state-of-the-art performance for accuracy and F1 (e.g., XGBoost: $\mathrm{Accuracy}=0.901\!\pm\!0.023$, $\mathrm{F1}=0.920\!\pm\!0.019$), while a feature-based Transformer attains the highest AUC ($0.963\!\pm\!0.025$), informing feature-engineering and compression choices for edge deployment. Building on these results, CAPSARII employs HW/SW co-design, model compression (pruning, quantization, distillation), and precision tuning to meet stringent energy and memory budgets; it further investigates Processing-in-Memory accelerators for future efficiency gains. A structured gap analysis highlights the remaining challenges: establishing validation standards for physiological signal quality and textile durability; achieving low-latency, scalable BAN/SAN communications under mobility and interference; and deploying hybrid lightweight/post-quantum cryptography with robust device identity and side-channel resilience on constrained endpoints. By consolidating these elements into a coherent, secure IoBT stack, CAPSARII delineates a practical roadmap from laboratory baselines to mission-ready soldier monitoring in both training and operational scenarios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luciano Bozzi, Christian Celidonio, Umberto Nuzzi, Massimo Biagini, Stefano Cherubin, Asbj{\o}rn Djupdal, Tor Andre Haugdahl, Andrea Aliverti, Alessandra Angelucci, Giovanni Agosta, Gerardo Pelosi, Paolo Belluco, Samuele Polistina, Gaia Strada, Luigi Sossi Ortega, Alexandra-Ioana Albu, Riccardo Volpi, Luigi Malag\`o, Michael Schneider, Xabier Eguiluz, Haritz Saiz, Mar\'ia Viqueria
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
