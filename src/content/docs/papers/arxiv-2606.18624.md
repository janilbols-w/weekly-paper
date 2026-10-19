---
title: "PragReST: Self-Reinforcing Counterfactual Reasoning for Pragmatic Language Understanding"
description: "Natural language understanding often depends on meanings that are implied rather than explicitly stated, requiring pragmatic reasoning."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.18624) · [PDF](https://arxiv.org/pdf/2606.18624)

## 一句话摘要

Natural language understanding often depends on meanings that are implied rather than explicitly stated, requiring pragmatic reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Natural language understanding often depends on meanings that are implied rather than explicitly stated, requiring pragmatic reasoning. Despite strong performance on math and logical reasoning, large language models (LLMs) still struggle with making pragmatic inferences, often choosing literal interpretations. To improve LLM pragmatic reasoning, we introduce PragReST, a self-supervised framework that constructs pragmatic QA data, generates counterfactual reasoning traces, and trains models to internalize them through supervised fine-tuning and reinforcement learning, without human-labeled training data or distillation from a stronger teacher. Across four pragmatic benchmarks (PragMega, Ludwig, MetoQA, and AltPrag), PragReST improves over backbone models, task-specific pragmatic tuning baselines, and non-counterfactual variants of the same pipeline. On accuracy-based benchmarks, PragReST improves over the instruct backbone by 5.37 and 5.50% (absolute) for Qwen3-8B and Qwen3-14B, respectively. Our error analysis and ablations underscore the importance of counterfactual reasoning: PragReST primarily reduces errors caused by failures to contrast observed utterances with plausible alternatives, and removing counterfactual reasoning substantially reduces performance. Moreover, our training preserves out-of-domain performance on general-knowledge and mathematical reasoning benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jihyung Park, Minchao Huang, Leqi Liu, Elias Stengel-Eskin
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
