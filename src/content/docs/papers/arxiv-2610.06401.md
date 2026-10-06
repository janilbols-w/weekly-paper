---
title: "RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents"
description: "Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.06401) · [PDF](https://arxiv.org/pdf/2610.06401)

## 一句话摘要

Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content. Existing training-time defenses can reduce attack success rates, but often at the cost of general capabilities. We show that training-based defenses induce substantial drift in the model's output distribution, altering its behavior even in benign settings and providing a potential mechanism for utility degradation. We further identify a failure mode of these defenses: On benign tool-use tasks, the model refrains from a step needed to finish an authorized task, particularly when that step is indicated by a tool output. To address these limitations, we introduce RAISED (Robust Attack Invariance through Self-Distillation), a training framework that combines self-generation and self-distillation. The model first generates its own tool-use scenarios, with an emphasis on cases where task completion requires acting on legitimate guidance from tool outputs. Then, through self-distillation, the student is trained to match the teacher's clean-context behavior on both clean and injected variants of the same trajectory. RAISED substantially reduces the attack success rate of prompt injections in tool responses while, unlike prior training-based defenses, preserving utility on both agentic and general-purpose benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohamed Dhouib, Clement Elliker, Alexi Canesse, Ma\"el Jenny, Lucas-Andrei Thil, Mahammed El-Sharkawy, Sonia Vanier, Elie Bursztein
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
