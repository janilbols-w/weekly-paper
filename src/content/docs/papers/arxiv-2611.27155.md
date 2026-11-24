---
title: "The Vulnerability Window: Decision Instability in Quantized Reward Models"
description: "Reward models and LLM judges are routinely quantized to 4 bits so that scoring many candidates stays affordable, and the usual check is that benchmark accuracy barely moves."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.27155) · [PDF](https://arxiv.org/pdf/2611.27155)

## 一句话摘要

Reward models and LLM judges are routinely quantized to 4 bits so that scoring many candidates stays affordable, and the usual check is that benchmark accuracy barely moves.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reward models and LLM judges are routinely quantized to 4 bits so that scoring many candidates stays affordable, and the usual check is that benchmark accuracy barely moves. That check is close to blind. Across eight reward models from two families (0.6B-8B), three generative judges and four 4-bit quantizers, quantization rewrites 1.1-12.3% of pairwise preference decisions on RewardBench while aggregate accuracy moves by as little as 0.03 points (p = 1.00), because the errors it fixes and introduces cancel. Flips concentrate where the full-precision margin is small relative to the quantization noise scale sigma: a Gaussian approximation Phi(-|m|/sigma) describes the aggregate rate, over-predicting it in all 30 scalar settings and failing for generative judges, and occupancy of the resulting vulnerability window falls from 25% to 7% with model size, which is what makes small judges fragile. The churn stays within noise under benign best-of-16 and becomes clear under adversarial pressure for some quantizers (146:54 harmful:helpful flips on one family, reversing sign on another). Downstream it changes what ships: across six (model, quantizer) pairs from two families, 14.6-65.7% of problems get a different best-of-64 selection while only 2.6-9.6% get a different final answer, with selections changing 5-8x more often than answers in every pair, and the pair the benchmark calls identical (0.03 points, p = 1.00) still changes 34.5% of them. Benchmark churn ranks that downstream change (rho = 0.89); benchmark accuracy does not order it reliably. Held-out audits then locate the useful diagnostic in the margin rather than the Gaussian: every margin-based predictor orders flips identically (AUC 0.927), and on the level a directly measured churn rate wins in-distribution. As a routing signal it is matched by plain top-k. The contribution is the characterization, not the model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
