---
title: "JURIST: Training Small Data-Reweighted Reasoning Judges for Test-Time Scaling in Code Generation"
description: "Best-of-N selection for code generation is only as good as the judge that picks among the candidates, and the judges accurate enough for this role are costly frontier LLMs."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2601.22230) · [PDF](https://arxiv.org/pdf/2601.22230)

## 一句话摘要

Best-of-N selection for code generation is only as good as the judge that picks among the candidates, and the judges accurate enough for this role are costly frontier LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Best-of-N selection for code generation is only as good as the judge that picks among the candidates, and the judges accurate enough for this role are costly frontier LLMs. A small judge can be trained on abundant earlier data labeled by unit tests, but it is deployed on newer problems: the earlier problems are easier and teach it little, their tasks differ, and their candidates come from weaker policies, while data close to deployment are scarce. We present JURIST, a 1.7B reasoning judge that uses a small meta set close to deployment to learn how much each earlier training sample should count. In our experiments, we find that training on the meta set alone, or adding it to the training data, does not help, while using it to weight the earlier data through a bi-level objective adds 3.9 Hard points over adding it to the training data. On LiveCodeBench, JURIST reaches 84.7% Overall and matches Claude Sonnet 4.6 on Hard problems (73.8%) at 463x lower cost; on BigCodeBench, it surpasses all test-time scaling baselines (35.9%). Abundant earlier data, guided by a small deployment-aligned meta set, can thus train a compact judge that selects accurately at low cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Peijia Qin, Ruiyi Zhang, Qi Cao, Pengtao Xie
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
