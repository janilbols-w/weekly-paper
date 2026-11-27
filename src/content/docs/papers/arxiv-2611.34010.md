---
title: "Asymmetric Speculative Decoding: Unlocking In-Context Learning in Draft Models"
description: "Speculative decoding addresses Large Language Model (LLM) inference latency by first drafting and then verifying in parallel."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.34010) · [PDF](https://arxiv.org/pdf/2611.34010)

## 一句话摘要

Speculative decoding addresses Large Language Model (LLM) inference latency by first drafting and then verifying in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding addresses Large Language Model (LLM) inference latency by first drafting and then verifying in parallel. Yet practical speedups fall far short of theoretical bounds, especially on reasoning tasks. We identify the root cause as task isomorphism: existing methods provide identical prompts to both models, forcing the draft model to solve problems beyond its capacity. This produces high rejection rates that eliminate parallelization gains. We discover that acceptance rates increase monotonically during generation, revealing a latent in-context learning (ICL) effect wherein the draft model progressively aligns with the target distribution by learning from verified tokens. Controlled experiments with varying context window sizes confirm this improvement stems from ICL-driven alignment rather than token difficulty. Motivated by this finding, we propose Asymmetric Speculative Decoding (AsymSpec), a training-free framework that decouples the prompts provided to draft and target models. By supplying the draft model with task-relevant example solutions, we reformulate its objective from reasoning to simulation, amplifying the ICL effect from the first token. We prove AsymSpec produces exact samples and converges exponentially to the target distribution. Across reasoning, code generation, and summarization tasks, AsymSpec achieves 2.29$\times$ to 4.95$\times$ speedup over autoregressive decoding, outperforming standard speculative decoding without model retraining.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guang Huang, Zeyi Wen
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
