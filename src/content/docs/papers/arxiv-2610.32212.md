---
title: "SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection"
description: "Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.32212) · [PDF](https://arxiv.org/pdf/2610.32212)

## 一句话摘要

Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content. While Reinforcement Learning with Verifiable Rewards (RLVR) has shown promising applications in reasoning tasks, its application to span-level hallucination detection is challenged by localization ambiguity, reward sparsity on hard examples, and uncontrolled length inflation. To address these issues, we introduce Socratic Guided Policy Optimization (SOPO), a multi-turn RL framework for robust hallucination detection. The key innovation of SOPO is a Socratic feedback mechanism, where a teacher model guides the reasoning trajectories during rollout by providing indirect hints inferred from the ground truth. This teacher-guided approach enables the model to generate more effective reasoning trajectories for hard examples, thus alleviating reward sparsity. Furthermore, we incorporate Turn-based Advantage Scaling to penalize verbosity bias, encouraging the model to develop efficient and autonomous reasoning capabilities. Empirical results on RAGTruth demonstrate that SOPO (4B) achieves state-of-the-art performance, surpassing leading proprietary models (e.g., GPT-5) and standard RL baselines, while obtaining higher reported mean scores than GRPO on four out-of-domain benchmarks, with mixed evidence against CAPO. We release our training and evaluation code alongside the 1.7B and 4B SOPO models at https://github.com/patsnap/SOPO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jiawei Dong, Zilong Bai, Pengtian zhu, Peng Zhou
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/patsnap/SOPO](https://github.com/patsnap/SOPO)
- 阅读深度：metadata
