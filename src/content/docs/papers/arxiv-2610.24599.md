---
title: "Severity-Channel Conditioning: An Injection-Level Study for Consumer-Device Deblurring"
description: "Motion-deblurring models lose substantial accuracy when transferred from professional cameras to smartphone-derived imagery."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.24599) · [PDF](https://arxiv.org/pdf/2610.24599)

## 一句话摘要

Motion-deblurring models lose substantial accuracy when transferred from professional cameras to smartphone-derived imagery.

## 为什么值得关注

待编辑增强。

## 摘要原文

Motion-deblurring models lose substantial accuracy when transferred from professional cameras to smartphone-derived imagery. This paper studies whether a severity descriptor, partly derived from the paired sharp target, helps adaptation on the iPhoneBlur consumer-device benchmark. Under a shared update budget, input concatenation of a severity map is compared with global feature modulation by capture metadata, spatial feature modulation by the severity map, and a tier-contrastive output objective, together with an unconditioned spectral-loss control, all fine-tuned from the same domain-adapted latent-diffusion baseline. The primary experiment is an oracle diagnostic: target-derived information is supplied at inference. For the evaluated model pair, input concatenation improves overall peak signal-to-noise ratio from 31.23 to 31.30 dB, whereas feature modulation, the contrastive objective, and the spectral-loss control do not exceed the baseline. The gain is positive on 87.2% of test images and on 14 of 15 held-out source videos; this video-level analysis describes the evaluated checkpoint pair and does not establish robustness to retraining, and three training seeds are reported separately. The input-level gain recurs on a transformer backbone. In one exploratory run, zeroing the channel at inference retains most of the gain in peak signal-to-noise ratio but lowers structural similarity below the baseline. A normalized-step diagnostic does not support the expected larger-gradient explanation. The results characterize the evaluated configurations and do not establish injection location as the sole cause, a spatial-locality mechanism, or a reliable deployment advantage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Abdullah Al Shafi, Kazi Saeed Alam, Sumaiya Rahim Suma, Sk. Imran Hossain
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
