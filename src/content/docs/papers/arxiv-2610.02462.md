---
title: "Capability Scaling-Down Laws for LLM Compression"
description: "LLM compression reduces inference costs and memory requirements, but selecting a method and configuration remains largely empirical because comparable resource reductions can produce different capability losses."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02462) · [PDF](https://arxiv.org/pdf/2610.02462)

## 一句话摘要

LLM compression reduces inference costs and memory requirements, but selecting a method and configuration remains largely empirical because comparable resource reductions can produce different capability losses.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM compression reduces inference costs and memory requirements, but selecting a method and configuration remains largely empirical because comparable resource reductions can produce different capability losses. We systematically investigate capability scaling-down laws for LLM compression across pruning, quantization, and distillation. Our framework measures capability loss in mathematics, code generation, and question answering, and relates these measurements to model size, training stage, compression settings, data availability, and training exposure. We develop simple predictive relations and evaluate their accuracy, measurement efficiency, and generalization to unseen configurations and model states. Sharing the density response across pruning levels halves the configuration measurements needed to fit a pruning predictor: on new Pythia states, on pre-registered OLMo-2 test states and under Wanda pruning, the compact relation matches a regression fitted with all measurements on math and code to within 0.020 nats per token, with coefficients refitted for each setting. Controlled distillation experiments show that the cost of heavy data reuse recurs across question-answering distributions, while the net benefit depends on the evaluation distribution. We further evaluate the decision value of these predictions by comparing numerical selection with configuration medians and fixed method priorities. Independent evaluations across two model families show that selection captures most of the available cross-method benefit for question answering within the tested candidate sets, where a fixed method priority attains the same regret, with smaller opportunities for mathematics and code. These results clarify the predictive scope of capability scaling-down laws and their use in compression method selection. Our code is publicly available at: https://github.com/LabRAI/scaling_down_law.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xueqi Cheng, Liang Wu, Kelly Wan, Liangjie Hong, Yushun Dong
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LabRAI/scaling_down_law](https://github.com/LabRAI/scaling_down_law)
- 阅读深度：metadata
