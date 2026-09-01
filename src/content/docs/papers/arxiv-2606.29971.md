---
title: "NeuReasoner: Theory-grounded Mapping of Reasoning Elicitation Boundaries"
description: "A growing body of work suggests that the reasoning capabilities of large language models are largely latent in their base form, with post-training primarily amplifying rather than introducing them."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.29971) · [PDF](https://arxiv.org/pdf/2606.29971)

## 一句话摘要

A growing body of work suggests that the reasoning capabilities of large language models are largely latent in their base form, with post-training primarily amplifying rather than introducing them.

## 为什么值得关注

待编辑增强。

## 摘要原文

A growing body of work suggests that the reasoning capabilities of large language models are largely latent in their base form, with post-training primarily amplifying rather than introducing them. However, this evidence comes mainly from mathematical and coding benchmarks, leaving the boundary conditions of that claim largely unexplored, namely which cognitive tasks can be recovered through elicitation and where that recovery fails. To investigate this, we introduce NeuReasoner, a theory-grounded elicitation instrument. At each step, an orchestrator pairs a Neuro Lens, inspired by functional specificity, with a Cognitive Lens, drawn from the Erotetic Theory of Reasoning, and integrates their outputs through internal modularization of a single model, without external tools. We evaluate NeuReasoner on CogBench, a suite of behavioral tasks from cognitive psychology, alongside standard mathematical and coding benchmarks, measuring both its improvement over vanilla inference and its ability to match a model's post-trained thinking mode. At sufficient scale, NeuReasoner matches or exceeds thinking-mode baselines on arithmetic reasoning, code generation, Bayesian reasoning, and reward learning; these gains persist against self-consistency and iterative-refinement baselines matched to NeuReasoner's per-decision call budget. Using NeuReasoner allows us to find clear boundaries: risk-taking and decision making under uncertainty remains hard to recover through elicitation alone, and model scale interacts with elicitation in both directions: widening its advantage on some cognitive signatures while erasing it on others. Overall, through NeuReasoner as a modular, interpretable, theory-grounded elicitation instrument, we empirically map where reasoning elicitation succeeds and fails, beyond the mathematical and coding benchmarks where prior claims have rested.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aydin Javadov, Shyngys Aitkazinov, Tobias Hoesli, Florian von Wangenheim, Bjoern Schuller, Joseph Ollier
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
