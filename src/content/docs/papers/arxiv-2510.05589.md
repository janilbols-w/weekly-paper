---
title: "Invariant Representation Learning for Source-Free Time Series Forecasting with LLM-Centric Proxy Denoising"
description: "Effective time series forecasting enables various real-world applications, benefiting from the proliferation of mobile devices."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.05589) · [PDF](https://arxiv.org/pdf/2510.05589)

## 一句话摘要

Effective time series forecasting enables various real-world applications, benefiting from the proliferation of mobile devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Effective time series forecasting enables various real-world applications, benefiting from the proliferation of mobile devices. However, the volume of time series data may vary significantly across domains due to high data acquisition costs and data regulations. To maximally create value from sparse data, this study focuses on a new problem of source-free time series forecasting, aiming to adapt a pretrained model from sufficient source time series to the sparse target time series without access to the source data, enabling data protection. To achieve this, we propose TimeID, a novel source-free time series forecasting framework with a large language model (LLM) centric proxy denoising inspired by the powerful generalization capabilities of LLMs. Specifically, TimeID consists of three key components: (1) dual-branch invariant disentangled feature learning that enforces representation- and gradient-wise invariance by means of season-trend decomposition; (2) lightweight, parameter-free proxy denoising that dynamically calibrates systematic biases of LLMs; and (3) knowledge distillation that bidirectionally aligns the denoised prediction and the original target prediction. Extensive experiments on real-world datasets demonstrate that TimeID outperforms state-of-the-art baselines, improving MSE and MAE by 10.7% and 9.3% on average. The code is available at https://github.com/decisionintelligence/TimeID.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Kangjia Yan, Chenxi Liu, Hao Miao, Xinle Wu, Yan Zhao, Chenjuan Guo, Bin Yang
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/decisionintelligence/TimeID](https://github.com/decisionintelligence/TimeID)
- 阅读深度：metadata
