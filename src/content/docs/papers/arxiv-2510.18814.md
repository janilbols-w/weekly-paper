---
title: "A Model Can Help Itself: Reward-Free Self-Training for LLM Reasoning"
description: "Can a language model improve reasoning by learning from its own imperfect responses, without rewards or teacher-provided solutions?"
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2510.18814) · [PDF](https://arxiv.org/pdf/2510.18814)

## 一句话摘要

Can a language model improve reasoning by learning from its own imperfect responses, without rewards or teacher-provided solutions?

## 为什么值得关注

待编辑增强。

## 摘要原文

Can a language model improve reasoning by learning from its own imperfect responses, without rewards or teacher-provided solutions? We present Self-evolving Post-Training (SePT), a simple method that alternates temperature-controlled self-generation with next-token likelihood training. Each round uses the updated model to generate new training responses, with one response per prompt by default and no correctness filtering. Across six mathematical benchmarks, SePT improves a temperature-selected no-training baseline by 11.4 and 6.7 AVG points on Qwen2.5-Math-7B and Qwen2.5-7B, respectively, where AVG averages Pass@1, Pass@8 and Pass@32 across benchmarks. We analyze how sampling temperature shapes the learning signal and investigate the value of the resulting responses. Responses from a SePT-trained model improve a student initialized from the original weights, while their reasoning prefixes help an unchanged model complete solutions, even when matched in length to prefixes from a colder initial model. Comparing next-token predictions at identical contexts also reveals changes in token rankings that decoding-temperature adjustment cannot reproduce. Further evaluations across nine starting models, general reasoning and code generation examine broader applicability. Together, these results show that reward-free self-training can improve both a model's predictions and the supervision it provides. Our code is available at https://github.com/ElementQi/SePT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mengqi Li, Lei Zhao, Anthony Man-Cho So, Ruoyu Sun, Xiao Li
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ElementQi/SePT](https://github.com/ElementQi/SePT)
- 阅读深度：metadata
