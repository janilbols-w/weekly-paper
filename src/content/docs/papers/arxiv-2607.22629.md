---
title: "Masked Distillation: Internalizing the Chain-of-Thought in Language Models"
description: "Large Reasoning Models (LRMs) produce long, explicit chains of intermediate steps before generating a final answer at inference time."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.22629) · [PDF](https://arxiv.org/pdf/2607.22629)

## 一句话摘要

Large Reasoning Models (LRMs) produce long, explicit chains of intermediate steps before generating a final answer at inference time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Reasoning Models (LRMs) produce long, explicit chains of intermediate steps before generating a final answer at inference time. These intermediate traces dominate latency, memory usage, and serving cost, even though the final answer correctness is not causally related to the trace correctness and the trace length is not a reliable indicator of the problem complexity. This raises a natural question: can the computation expressed in these intermediate tokens be internalized into the parameters of a language model, enabling it to produce answers directly (or with much shorter intermediate traces)? We introduce \textit{masked distillation}, a knowledge-distillation framework in which a student LLM is trained to predict only the solution tokens conditioned on the question, while a reasoning teacher provides feedback on the student's responses after conditioning on the question and its own CoT trace. We instantiate this framework in two settings: (i) a \textit{self-distillation} setting, in which the same model serves as the teacher in thinking mode and as the student in non-thinking mode, and (ii) a \textit{dual-model} setting, in which a larger reasoning teacher supervises a separate smaller non-thinking student over the solution tokens. By treating intermediate tokens as a scaffold which reasoning models use to fit over the solution tokens, We additionally vary the length of intermediate-token scaffolding the student is supervised on, interpolating between full internalization (the student emits only the solution) and no internalization (the student emits the full trace before the answer). We evaluate the framework through controlled experiments on two reasoning domains: GSM8K (grade-school arithmetic) and Countdown (a number-puzzle search task).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Durgesh Kalwar, Vardhan Palod, Subbarao Kambhampati
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
