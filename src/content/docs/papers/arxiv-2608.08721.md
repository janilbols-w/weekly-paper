---
title: "LibraSpec: Dynamic Diffusion-Based Speculative Decoding via Marginal-Gain-Driven Optimization"
description: "Speculative decoding accelerates large language model inference by drafting multiple tokens for parallel verification, with efficiency critically determined by the speculative length selected at each decoding round."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.08721) · [PDF](https://arxiv.org/pdf/2608.08721)

## 一句话摘要

Speculative decoding accelerates large language model inference by drafting multiple tokens for parallel verification, with efficiency critically determined by the speculative length selected at each decoding round.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by drafting multiple tokens for parallel verification, with efficiency critically determined by the speculative length selected at each decoding round. Existing dynamic speculation methods select the speculation length by estimating how many tokens will be accepted, which is reasonable for autoregressive drafters that generates tokens sequentially. The recent wave of diffusion-based drafters, however, generates candidate blocks in parallel at substantially lower drafting cost, shifting the key question from how many tokens to generate to how many generated tokens are worth verifying. We therefore reformulate dynamic speculative-length selection as expected-speedup optimization and derive a marginal criterion that extends the speculative sequence only when its acceptance gain outweighs the additional verification cost. Building on this criterion, we develop \textit{LibraSpec}, a training-free and plug-and-play algorithm that iteratively determines the speculative length using drafter confidence scores. Theoretically, we prove that LibraSpec monotonically converges toward the optimal speculative length. Experiments across six target models, three diffusion-based speculative decoding methods, and math, coding, and chat benchmarks show consistent improvements under both greedy and sampling settings, achieving a further $0.5\sim1.5\times$ improvement over baselines and up to $8.49\times$ speedup over autoregressive decoding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zexun Lin, Yuan Feng, Junlin Lv, Kevin S. Zhou, Xike Xie
- 发布：2026-08-09；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
