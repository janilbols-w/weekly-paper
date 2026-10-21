---
title: "Who Gets Unmasked? Sampler-Induced Bias in Diffusion Language Models"
description: "Diffusion language models (dLLMs) generate by gradually unmasking a canvas, so their samplers decide not only which token to write but also when to commit it."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.24795) · [PDF](https://arxiv.org/pdf/2610.24795)

## 一句话摘要

Diffusion language models (dLLMs) generate by gradually unmasking a canvas, so their samplers decide not only which token to write but also when to commit it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (dLLMs) generate by gradually unmasking a canvas, so their samplers decide not only which token to write but also when to commit it. We show that this second decision changes who appears in generated text, a sampler-induced bias on top of the model's own. Common commit rules, including LLaDA's default, commit the positions whose sampled tokens are most probable; this peeking favors majority options. To separate the sampler from the model, we read the model's belief about a fork, such as a protagonist's gender, in one forward pass, and show that this belief matches exact sampling from the model. Measured against it, peeking samplers on LLaDA and Dream amplify occupational gender stereotypes and collapse opinion distributions, and confidence-based ordering shifts gender-balanced occupations toward men, more so under faster parallel decoding. We propose Fork-First Sampling, which decides the fork before anything else is written: it follows the belief or any target distribution, improves fluency, and avoids the stories that remark on the protagonist's gender, which prompt-based fixes produce, at the cost of one forward pass. Fairness evaluations of dLLMs should report the commit rule.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xujun Che, Farsheed Haque, Depeng Xu, Xi Niu, Haopeng Zhang
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
