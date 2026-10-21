---
title: "Sleep Stage Classification across Heterogeneous EEG/EOG Channels with Multi-Channel Differential Transformer"
description: "Classification of sleep stages is essential for assessing sleep quality and diagnosing sleep disorders."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2508.15215) · [PDF](https://arxiv.org/pdf/2508.15215)

## 一句话摘要

Classification of sleep stages is essential for assessing sleep quality and diagnosing sleep disorders.

## 为什么值得关注

待编辑增强。

## 摘要原文

Classification of sleep stages is essential for assessing sleep quality and diagnosing sleep disorders. However, manual inspection of EEG characteristics for each stage is time-consuming and prone to human error. Although machine learning and deep learning methods have been actively developed, they continue to face challenges arising from the non-stationarity and variability of electroencephalography (EEG) and electrooculography (EOG) signals across diverse clinical configurations, often resulting in poor generalization. In this work, we propose SleepDIFFormer, a multi-channel differential transformer framework for heterogeneous EEG-EOG representation learning. SleepDIFFormer is trained across multiple sleep staging datasets, each treated as a source domain, with the goal of generalizing to unseen target domains. Specifically, it employs a Multi-channel Differential Transformer Architecture (MDTA) designed to process raw EEG and EOG signals while incorporating cross-domain alignment. Our approach mitigates spatial and temporal attention noise and learns a domain-invariant EEG-EOG representation through feature distribution alignment across datasets, thereby enhancing generalization to new domains. Empirically, we evaluated SleepDIFFormer on five diverse sleep staging datasets under domain generalization settings and benchmarked it against existing approaches, achieving superior performance. Furthermore, comprehensive ablation analyses and interpretation of the differential attention weights demonstrated their relevance to learning discriminative sleep EEG representations. These findings support the development of more generalizable approaches to automated sleep-stage classification. Our source code and checkpoint are made publicly available at https://github.com/Ben1001409/SleepDIFFormer

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Benjamin Wei Hao Chin, Yuin Torng Yew, Jia Hong Puah, Haocheng Wu, Lanxin Liang, Chow Khuen Chan, Norita Mohd Zain, Siti Balqis Samdin, Sim Kuan Goh
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Ben1001409/SleepDIFFormer](https://github.com/Ben1001409/SleepDIFFormer)
- 阅读深度：metadata
