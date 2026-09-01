---
title: "ITP-STDP: A Hardware-Efficient Intrinsic-Timing Power-of-Two Synaptic Learning Engine for On-Chip SNNs"
description: "Spiking neural networks (SNNs) have the potential to emerge as the third generation of neural networks and have attracted increasing attention across a wide range of applications."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2606.06159) · [PDF](https://arxiv.org/pdf/2606.06159)

## 一句话摘要

Spiking neural networks (SNNs) have the potential to emerge as the third generation of neural networks and have attracted increasing attention across a wide range of applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) have the potential to emerge as the third generation of neural networks and have attracted increasing attention across a wide range of applications. However, the large number of synaptic connections in SNNs leads to intensive weight-update computation by on-chip learning algorithms during training, resulting in substantial hardware resource utilization and energy consumption. Among existing SNN learning algorithms, spike-timing-dependent plasticity (STDP) is one of the most extensively studied and widely adopted, serving as a fundamental learning component in SNNs. To address the hardware and energy overheads associated with SNN training, this paper presents intrinsic-timing power-of-two STDP (ITP-STDP) and its corresponding prototype learning engine hardware architecture. The proposed design is evaluated through a dedicated mean-field synaptic drift model for dynamical analysis and further validated across SNN networks of different scales and datasets. It is further implemented on both ASIC and FPGA platforms and compared with state-of-the-art approaches, including the original STDP and more complex STDP variants. The results demonstrate superior energy efficiency, higher operating speed, and substantially lower hardware resource utilization, as the proposed design eliminates most of the computational overhead of STDP through both algorithmic and hardware-level optimizations. On the FPGA platform, the proposed design improves energy efficiency by 4.5$\times$ to 219.8$\times$ over the compared designs. On the ASIC platform, the proposed design achieves a 4.8$\times$ to 22.01$\times$ speedup while consuming only 1.2% to 3.3% of the area required by prior works.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haihang Xia, Xinyu Zhao, Xuecheng Wang, John Goodenough, Charith Abhayaratne, Panagiotis A. Panagiotou, Chunyi Song, Tiantai Deng
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
