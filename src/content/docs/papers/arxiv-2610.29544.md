---
title: "RISK-KV: Quality-Aware Selective KV Cache Reconstruction for Distributed LLM Inference"
description: "Request migration and interruption recovery in distributed large language model (LLM) inference rely on historical key-value (KV) caches."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.29544) · [PDF](https://arxiv.org/pdf/2610.29544)

## 一句话摘要

Request migration and interruption recovery in distributed large language model (LLM) inference rely on historical key-value (KV) caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Request migration and interruption recovery in distributed large language model (LLM) inference rely on historical key-value (KV) caches. Retaining or transferring a complete cache incurs substantial state overhead, whereas replaying historical tokens requires additional computation. This paper proposes RISK-KV, a quality-aware method for selective historical KV reconstruction in pretrained models. RISK-KV uses exact KV states on both sides of a target layer and cross-layer ridge regression to predict the missing layer's attention-projection input; it then folds in the original model's KV projection matrices to reduce predictor storage. Reconstruction risk is measured by the change in negative log-likelihood (NLL) caused by actual reconstruction, and low-overhead topology search with quality gating selects the layer groups to reconstruct. Independent tests on three language models show that representative recovery configurations omit 18.2 percent to 33.3 percent of historical KV, with perplexity changes below 0.5 percent. In a local request-recovery experiment with a 512-token history, RISK-KV achieves a 1.51 to 3.31 times speedup over full Token Replay. These results indicate that selective KV reconstruction can reduce historical cache overhead with small changes in predictive quality and improve request-recovery efficiency under the evaluated deployment conditions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Wang Yuekai
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
