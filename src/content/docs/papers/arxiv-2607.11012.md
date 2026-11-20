---
title: "EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models"
description: "Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.11012) · [PDF](https://arxiv.org/pdf/2607.11012)

## 一句话摘要

Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy. On-policy distillation (OPD) instead collects teacher or evaluator supervision on student-generated rollouts. However, existing OPD methods differ substantially in supervision form, tokenizer compatibility, teacher access, and supervision granularity, leading to fragmented implementations that are difficult to reproduce and extend. We present \textsc{EasyOPD}, an on-policy distillation framework built on verl, a distributed reinforcement-learning framework for large language models. \textsc{EasyOPD} separates user-side configuration, method-specific supervision logic, and verl-based execution. Its method modules connect to the shared backend through extension boundaries for loss construction, rollout metadata, reward processing, tokenizer alignment, and teacher-side computation. We instantiate representative methods for three OPD settings -- cross-tokenizer OPD, on-policy self-distillation, and step-wise OPD. Experiments on reasoning, code-generation, scientific-knowledge, and tool-use benchmarks show that these implementations can be executed through the same verl-based backend while retaining their method-specific objectives and task-dependent performance profiles. We release \textsc{EasyOPD} with runnable YAML configurations, documentation, and an installable demonstration package and video.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jie Sun, Mao Zheng, Mingyang Song, Qiyong Zhong, Gengsheng Li, Zhepei Hong, Chang Wu, Pengfei Liu, Junfeng Fang, Xiang Wang
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
