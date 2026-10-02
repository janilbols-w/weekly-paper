---
title: "Does This Action Still Explain the Task? Reverse Scoring for Diffusion Language Model Agents"
description: "Diffusion-based large language models (dLLMs) promise to break the sequential latency bottleneck of autoregressive agents through parallel decoding, but recent evaluations show this efficiency does not transfer to embodied agentic competence: dLLM-backed agents repeatedly fall into retry loops, re-issuing an action long after it has failed."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.38536) · [PDF](https://arxiv.org/pdf/2609.38536)

## 一句话摘要

Diffusion-based large language models (dLLMs) promise to break the sequential latency bottleneck of autoregressive agents through parallel decoding, but recent evaluations show this efficiency does not transfer to embodied agentic competence: dLLM-backed agents repeatedly fall into retry loops, re-issuing an action long after it has failed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion-based large language models (dLLMs) promise to break the sequential latency bottleneck of autoregressive agents through parallel decoding, but recent evaluations show this efficiency does not transfer to embodied agentic competence: dLLM-backed agents repeatedly fall into retry loops, re-issuing an action long after it has failed. We give a mechanistic account of this failure and a training-free remedy. We trace the retry loop to the adaptivity of masked decoding: the sampler commits the positions it is most confident about and defers the uncertain ones, and at a failure state the context already offers a confident fill for the deferred decision, i.e. the failed action itself, so the retry is committed without the failure feedback ever being confronted. We model the resulting distortion of the action distribution as a task-blind corruption: contextually salient actions (e.g., the action just taken) receive inflated probability by a factor that depends on the state and the action but not on the task. Under this model, we analyse an invariance proposition: the task-blind factor cancels exactly from the reverse conditional, i.e. the likelihood of the task given the state and a candidate action, which coincides with the task posterior of an idealized uncorrupted model. Masked dLLMs evaluate the reverse conditional natively, unlike autoregressive models, by masking the task tokens and denoising, at the cost of a few parallel passes per candidate. We instantiate the rule as Reflect Reverse and evaluate it on four multi-turn embodied benchmarks, where it improves task success and progression rates over forward-scoring baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiacheng Qiu, Christopher E. Mower, Jan Peters, Haitham Bou-Ammar, Matthieu Zimmer
- 发布：2026-09-29；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
