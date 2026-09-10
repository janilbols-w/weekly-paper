---
title: "SurF: A Generative Model for Multivariate Irregular Time Series Forecasting"
description: "Irregularly sampled multivariate event streams remain a difficult modality for generative modeling: tokenization-based approaches break down when inter-event intervals vary by orders of magnitude."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2605.14069) · [PDF](https://arxiv.org/pdf/2605.14069)

## 一句话摘要

Irregularly sampled multivariate event streams remain a difficult modality for generative modeling: tokenization-based approaches break down when inter-event intervals vary by orders of magnitude.

## 为什么值得关注

待编辑增强。

## 摘要原文

Irregularly sampled multivariate event streams remain a difficult modality for generative modeling: tokenization-based approaches break down when inter-event intervals vary by orders of magnitude. We (i) propose \textbf{SurF}, a generative model that uses the Time Rescaling Theorem (TRT) as a learnable bijection between event sequences and i.i.d.\ unit-rate exponential noise, enabling a single model to be trained across heterogeneous event-stream datasets; (ii) three efficient parameterizations of the cumulative intensity that scale to long sequences; and (iii) a Transformer-based encoder for multi-dataset pretraining. On six real-world benchmarks, SurF achieves the best reported time RMSE on Earthquake, Retweet, and Taobao, and is within trial-level noise of the strongest specialist on the remaining three. Under a strict leave-one-out protocol, the held-out checkpoint beats every classical and neural-autoregressive baseline on $5/6$ datasets and beats every baseline on Amazon and Earthquake, an initial step toward foundation models over asynchronous event streams (Code is available at https://github.com/MrRezaeiUofT/SurF).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mohammad R. Rezaei, Tejas Balaji, Rahul G. Krishnan
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MrRezaeiUofT/SurF](https://github.com/MrRezaeiUofT/SurF)
- 阅读深度：metadata
