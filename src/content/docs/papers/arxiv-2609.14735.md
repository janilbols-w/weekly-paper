---
title: "HELENA for 5G NR LEO NTN Channel Estimation: A Comparative Evaluation"
description: "Deep Learning (DL)-based channel estimation has shown high accuracy and low latency in terrestrial 5G NR, but Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) introduce Doppler and synchronization impairments that may require NTN-specific architectures."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.14735) · [PDF](https://arxiv.org/pdf/2609.14735)

## 一句话摘要

Deep Learning (DL)-based channel estimation has shown high accuracy and low latency in terrestrial 5G NR, but Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) introduce Doppler and synchronization impairments that may require NTN-specific architectures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep Learning (DL)-based channel estimation has shown high accuracy and low latency in terrestrial 5G NR, but Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) introduce Doppler and synchronization impairments that may require NTN-specific architectures. We test whether High-Efficiency Learning-based channel Estimation using dual Neural Attention (HELENA), originally designed for terrestrial channels, remains effective after NTN retraining and suitable across high-performance and power-constrained inference platforms. Its unchanged architecture is trained on paired receiver-compensated (NTN-1) and residual-impaired (NTN-2) datasets and compared with eight terrestrial-origin models trained on the same NTN data and the NTN-specific MDELAN-SISO. HELENA achieves the lowest observed SNR-averaged NMSE among the DL estimators in both conditions, including 55.8-62.7% lower linear-scale NMSE than MDELAN-SISO. All DL models degrade in NTN-2, demonstrating the challenge posed by residual Doppler and its associated impairments. On an RTX PRO 4500, HELENA achieves 0.0595 ms 99th-percentile (P99) inference latency, 88.1% below the 0.5 ms budget, with lower energy than its closest attention-based competitors. On a 10 W Jetson Orin NX, it retains a favorable accuracy-energy trade-off, but no model meets the P99 budget. Thus, HELENA needs no NTN-specific redesign for the evaluated task, while embedded tail latency remains an open challenge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tail latency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Miguel Camelo Botero, Nina Slamnik-Krije\v{s}torac, Johann Marquez-Barja
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
