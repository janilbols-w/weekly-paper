---
title: "PV-Decoding: Progressive Verification Decoding with Decode Gating for Diffusion Language Models"
description: "Discrete diffusion language models (dLLMs) offer an attractive alternative to autoregressive generation by updating multiple tokens in parallel, but their inference efficiency is still limited by the cost of safely committing tentative predictions."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.24722) · [PDF](https://arxiv.org/pdf/2610.24722)

## 一句话摘要

Discrete diffusion language models (dLLMs) offer an attractive alternative to autoregressive generation by updating multiple tokens in parallel, but their inference efficiency is still limited by the cost of safely committing tentative predictions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Discrete diffusion language models (dLLMs) offer an attractive alternative to autoregressive generation by updating multiple tokens in parallel, but their inference efficiency is still limited by the cost of safely committing tentative predictions. In particular, speculative decoding for dLLMs is challenging because speculative tokens within the same diffusion block may depend on one another, making aggressive acceptance prone to error propagation and strict verification computationally expensive. We present PV-Decoding, a confidence-driven speculative decoding framework with progressive verification for block diffusion inference. PV-Decoding partitions masked positions into directly decoded tokens, speculative tokens, and unresolved tokens using two confidence thresholds, and then verifies speculative tokens with progressively stronger policies, including single-batch, dual-batch, and multi-batch verification. This design exposes a practical accuracy--efficiency trade-off: weaker verification minimizes overhead, whereas stronger verification improves acceptance precision and robustness. Experiments on three diffusion language models across GSM8K, MBPP, and HumanEval show that PV-Decoding reduces sequential model forward passes (MFPs) by 8%--37% relative to confidence-based decoding, while keeping the largest observed accuracy drop to 1.3%. On Dream-7B-Instruct/GSM8K, PV-Decoding (1-batch) and PV-Decoding (2-batch) improve throughput by 7.0%--13.6% under the same hardware budget, whereas PV-Decoding (multi-batch) is slower under the current runtime. These results suggest that confidence-guided speculation with structured verification is a practical path toward efficient and reliable dLLM inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding, verification decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Renxi Liu, Yiming Li, Shengyin Sun, Chen Chen, Xian Wang, Shuai Yang, Huiling Zhen, Xianzhi Yu, Yaoyuan Wang, Weizhe Lin, Xiaosong Li
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
