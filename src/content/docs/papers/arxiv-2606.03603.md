---
title: "World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning"
description: "World models and multimodal large language models (MLLMs) provide complementary capabilities for predicting future outcomes from static visual observations."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.03603) · [PDF](https://arxiv.org/pdf/2606.03603)

## 一句话摘要

World models and multimodal large language models (MLLMs) provide complementary capabilities for predicting future outcomes from static visual observations.

## 为什么值得关注

待编辑增强。

## 摘要原文

World models and multimodal large language models (MLLMs) provide complementary capabilities for predicting future outcomes from static visual observations. World models can generate concrete visual rollouts of possible futures, while MLLMs can reason abstractly over questions, goals, and rules. However, generated rollouts are stochastic and may be visually plausible but task-incorrect, making it necessary to determine when visual simulation is useful, whether a rollout is credible, and how it should influence the final answer. We formulate this problem as controlled concrete reasoning, where a model learns to invoke, verify, and integrate visual future simulation alongside abstract reasoning. To study this setting, we construct two human-verified benchmarks, VRQABench for controllable spatial lookahead and OpenWorldQA for open-domain physical prediction, and propose Privileged-Future On-Policy Self-Distillation (PF-OPSD). During training, PF-OPSD uses ground-truth future videos and answers only as teacher-side privileged context to evaluate on-policy concrete-reasoning trajectories, while the deployable student never observes true futures at test time. Experimental results show that PF-OPSD outperforms baseline by 10.6% and 10.9% on VRQABench and OpenWorldQA, respectively, while increasing robustness to noisy or conflicting rollouts. Our code and dataset are available at https://github.com/yczhou001/PF-OPSD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yucheng Zhou, Wei Tao, Yiwen Guo, Jianbing Shen
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/yczhou001/PF-OPSD](https://github.com/yczhou001/PF-OPSD)
- 阅读深度：metadata
