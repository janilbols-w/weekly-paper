---
title: "Testing Processor Contracts in Speculative Decoding Engines"
description: "Speculative sampling can accelerate decoding without changing the target distribution."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.04042) · [PDF](https://arxiv.org/pdf/2611.04042)

## 一句话摘要

Speculative sampling can accelerate decoding without changing the target distribution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative sampling can accelerate decoding without changing the target distribution. Its standard guarantee assumes that logits processors, which enforce constraints or modify token scores, receive the appropriate token prefix and state at each verification position. We formalize this processor-prefix contract and present BADC (branch-aware differential conformance testing). BADC combines enumerated references on tiny random models, checks of processor inputs and state, and simultaneous confidence bounds on output-event probabilities. Preregistered, source-informed experiments on selected Transformers and llama-cpp-python releases confirm two causes: processors read unverified drafts or advance state without rollback. For one pilot-selected prompt on a trained checkpoint, fresh samples give a 60.26-percentage-point lower bound on the difference in the probability of a predefined first-token event between ordinary and prompt-lookup decoding, with nominal simultaneous 95% coverage under within-arm i.i.d. sampling. Controlled comparisons establish no cause-recovery advantage of directed selection over random selection, while permutation testing detects each tested family at least as often as BADC. These findings connect processor-interface failures to observable decoding differences without establishing diagnostic superiority or workload prevalence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianyu Ding, Yaocheng Tong, Muzhi Yang, Lei Yang, Fei Jiang
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
