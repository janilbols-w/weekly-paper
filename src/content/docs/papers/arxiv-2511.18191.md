---
title: "Accelerating Time Series Foundation Models with Speculative Decoding"
description: "Time series forecasting drives operational decisions under tight latency budgets, and autoregressive time series foundation models (TSFMs) increasingly deliver the most accurate forecasts."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2511.18191) · [PDF](https://arxiv.org/pdf/2511.18191)

## 一句话摘要

Time series forecasting drives operational decisions under tight latency budgets, and autoregressive time series foundation models (TSFMs) increasingly deliver the most accurate forecasts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time series forecasting drives operational decisions under tight latency budgets, and autoregressive time series foundation models (TSFMs) increasingly deliver the most accurate forecasts. That accuracy is paid for at inference, since a horizon of $H$ steps takes $\lceil H / P\rceil$ sequential forward passes of a large model, so latency grows with exactly the long horizons these models are prized for. Yet a far cheaper model predicts most next patches nearly as well as the large one, and causal models can verify a block of future patches in one parallel pass even though they generate them one at a time. These are precisely the conditions under which speculative decoding thrives in LLMs, but its ingredients are all defined over discrete vocabularies. We therefore develop speculative decoding for continuous patch autoregression. A cheap draft proposes $K$ future patches, and the target verifies all of them in a single causal pass, accepting each by a log-domain Gaussian likelihood-ratio test and correcting the first rejection with its own prediction. We prove that the accelerated output stays within a squared-error radius of target-only decoding set by an acceptance temperature, and that throughput follows a capped-geometric law that makes speedups predictable before deployment. The method delivers up to $3.0 \times$ inference speedup at accuracy between target and draft across five TSFM families, and we characterize which architectures admit single-pass verification and when speculation does not pay.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pranav Subbaraman, Fang Sun, Jinxi Yu, Yue Yao, Huacong Tang, Xiao Luo, Yizhou Sun
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
