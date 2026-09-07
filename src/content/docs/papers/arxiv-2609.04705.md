---
title: "Sustainable Edge Vision via Empirically Calibrated DVFS: Eliminating Thermal Throttling on Passively Cooled Hardware"
description: "Passive cooling eliminates the energy overhead and mechanical failure modes of fans, making it attractive for edge deployment, yet sustained Deep Neural Network (DNN) inference on passively cooled edge Systems-on-Chip (SoCs) is bottlenecked by thermal throttling."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.04705) · [PDF](https://arxiv.org/pdf/2609.04705)

## 一句话摘要

Passive cooling eliminates the energy overhead and mechanical failure modes of fans, making it attractive for edge deployment, yet sustained Deep Neural Network (DNN) inference on passively cooled edge Systems-on-Chip (SoCs) is bottlenecked by thermal throttling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Passive cooling eliminates the energy overhead and mechanical failure modes of fans, making it attractive for edge deployment, yet sustained Deep Neural Network (DNN) inference on passively cooled edge Systems-on-Chip (SoCs) is bottlenecked by thermal throttling. To address this, we propose an empirically calibrated, state-aware Dynamic Voltage and Frequency Scaling (DVFS) scheduler. Unlike heuristic-driven controllers, our methodology utilizes time-domain guards and absolute temperature bounds, with derivative triggers acting as safeguards against sharp thermal spikes. Evaluated on a passively cooled Raspberry Pi 5 running YOLOv8n, our scheduler eliminates all observed thermal throttling events during sustained 30-minute workloads. It outperforms a temperature-only reactive baseline by achieving a 6.8% higher frame rate (Cohen's d = 8.73) while consuming 1.9% less energy per frame. Furthermore, our optimized passive scheduling surpasses an actively cooled reference system in energy efficiency (Joules/frame), though active cooling remains superior for raw throughput. Through isolated ablations, we show that the dwell guard is necessary for run-to-run reproducibility. Finally, exploratory boundary probes indicate that the passive operating envelope closes at ambient temperatures ($\ge 27^\circ$C) where nonlinear leakage defeats DVFS-based control. These results indicate that, within the mapped envelope, correct scheduling can make mechanical cooling unnecessary for sustained edge inference on this platform.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aayush Marasini, Zhaoxian Zhou
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
