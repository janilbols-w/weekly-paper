---
title: "LLM Router: Rethinking Routing with Prefill Activations"
description: "Existing routers rely on semantic query features or handcrafted features, which often fail to capture model-specific failures or intrinsic task difficulty."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2603.20895) · [PDF](https://arxiv.org/pdf/2603.20895)

## 一句话摘要

Existing routers rely on semantic query features or handcrafted features, which often fail to capture model-specific failures or intrinsic task difficulty.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing routers rely on semantic query features or handcrafted features, which often fail to capture model-specific failures or intrinsic task difficulty. We instead route using internal LLM activations, specifically the residual stream. Our key idea, Encoder-Target Decoupling, separates the model that produces the predictive signal (the Encoder) from the model whose correctness is being estimated (the Target), allowing open-weight encoders to predict the performance of closed-source target models. We evaluate layerwise geometric probes, finding that Fisher Separability ($J$) effectively identifies informative layers, supported by Effective Dimensionality ($d_{\mathrm{eff}}$) diagnostics. We then utilize a SharedTrunkNet, a joint multi-output MLP that predicts simultaneous correctness probabilities across candidate models using concatenated prefill features. In our experiments, SharedTrunkNet consistently outperforms semantic baselines. At its best, SharedTrunkNet closes 45.58% of the gap between the strongest standalone model and the oracle while achieving 74.31% cost savings relative to the most expensive model. These results demonstrate that prefill activations provide a robust routing signal, establishing activation-based routing as a high-performance alternative to purely semantic selection.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm router
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tanay Varshney, Annie Surla, Michelle Xu, Gomathy Venkata Krishnan, Maximilian Jeblick, David Austin, Neal Vaidya, Davide Onofrio
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
