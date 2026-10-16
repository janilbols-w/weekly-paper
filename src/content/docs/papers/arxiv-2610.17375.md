---
title: "PIG: Parallel Inconsistency Guidance for Accelerating Diffusion Language Models"
description: "Diffusion language models accelerate generation by decoding multiple masked positions per forward pass."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](http://arxiv.org/abs/2610.17375v1) · [PDF](https://arxiv.org/pdf/2610.17375v1)

## 一句话摘要

Diffusion language models accelerate generation by decoding multiple masked positions per forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models accelerate generation by decoding multiple masked positions per forward pass. However, accuracy is known to drop when parallel decoding trajectories deviate from their sequential counterparts, which are slow and expensive "oracles" that adhere to the joint distribution of language. In this paper, we propose Parallel Inconsistency Guidance (PIG), a new paradigm that uses a trained auxiliary model to directly estimate the inconsistency between parallel and sequential generation from a single model forward pass. During inference, masked positions are traversed by decreasing confidence, and tokens are added to the parallel decode set one-at-a-time until the total estimated inconsistency between the parallel and sequential generation exceeds a threshold. Surprisingly, it suffices to train a lightweight ~2M parameter auxiliary model on a small mixture drawn from OpenCoder, GSM8K-train, MATH-train, and MBPP-train. For LLaDA-8B Instruct and NemotronDiffusion-3B Instruct, PIG extends the accuracy-TPF frontier on GSM8K, MATH500, MBPP, HumanEval, and MMLU, when compared to the industry standard Fast-dLLM and measures favorably on LLaDA-8B Instruct against DAPD, KLASS, EB-sampler, and other learned unmasking policies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Quentin Fruytier, Anton Xue, Sanjay Shakkottai, Sujay Sanghavi
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/Quentin-Fruytier/PIG-DLM-release](https://github.com/Quentin-Fruytier/PIG-DLM-release)
- 阅读深度：metadata
