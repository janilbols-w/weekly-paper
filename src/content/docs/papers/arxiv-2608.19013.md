---
title: "Harness Continual Learning: Continual Adaptation Beyond Model Parameters"
description: "Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2608.19013) · [PDF](https://arxiv.org/pdf/2608.19013)

## 一句话摘要

Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continual learning has largely been model-centric, treating model parameters as the state that changes with sequential experience. Modern agents can also adapt through a harness of prompts, memories, tools, skills, and routing rules. Because these contents jointly shape later execution, a harness update can disrupt previously reliable behavior even when the model is frozen. This raises a new question: how can an agent continually improve its state outside the model while retaining behavior acquired earlier? We formulate Harness Continual Learning (HCL), a new continual learning paradigm in which the harness evolves around a frozen foundation model, and define the resulting loss of earlier behavior as harness-level forgetting. We instantiate HCL with four execution-facing components: the Task Interface, Experience Memory, Capability Map, and Adaptive Router. We further introduce guarded harness evolution to separate update generation from state commitment. A Continual Optimizer proposes candidate harnesses from post-execution feedback, and a Continual Evaluator commits the resulting candidate harness only after checking current improvement, historical retention, and validity. Experiments on textual reasoning, multimodal perception, and open-world interaction demonstrate capability accumulation and failure recovery, with relative gains exceeding 10% over corresponding baselines in multiple settings. Component ablations assess the contribution of each harness component, while controlled retention sweeps reveal measurable harness-level forgetting and show that the stability--plasticity trade-off can be explicitly adjusted.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: failure recovery
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Borui Kang, Jinrui Gu, Junhan Lv, Wenbin Li, Lei Wang, Yang Gao
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
