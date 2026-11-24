---
title: "Cannot Wait to Verify: Parallel Drafting to Eliminate Verifier Idle Time in Speculative Decoding"
description: "Autoregressive inference in large transformer models is limited by token-level sequential execution, resulting in high latency and low GPU utilization."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.27477) · [PDF](https://arxiv.org/pdf/2611.27477)

## 一句话摘要

Autoregressive inference in large transformer models is limited by token-level sequential execution, resulting in high latency and low GPU utilization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive inference in large transformer models is limited by token-level sequential execution, resulting in high latency and low GPU utilization. Speculative decoding (SD) mitigates this bottleneck by introducing a draft-and-verifier model. However, the drafting stage remains sequential, leaving the verifier idle and underutilizing compute. To address this, we propose a plug-and-play drafting adaptive drafting method that parallelizes inference across transformer layers during draft generation. Starting from a shared hidden state, our approach evaluates multiple layers in parallel and verifies consistency by measuring divergence in hidden-state space. Layer-wise draft states are accepted when deviations are small; otherwise, a correction step is applied. By exploiting redundancy across transformer layers, our method accelerates draft generation and improves hardware utilization without modifying architectures or requiring retraining. Experimental results on NLP tasks show that our method speeds up the drafting stage by up to $1.65\times$ with minimal degradation in accuracy, while maintaining the same performance as SD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
