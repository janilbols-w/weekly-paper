---
title: "CriPO: Enhancing Rubric-based RL via Self-Distillation"
description: "Rubric-based RL has recently shown promise in improving LLMs on open-ended tasks."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.18082) · [PDF](https://arxiv.org/pdf/2607.18082)

## 一句话摘要

Rubric-based RL has recently shown promise in improving LLMs on open-ended tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Rubric-based RL has recently shown promise in improving LLMs on open-ended tasks. A widely recognized limitation of rubric-based RL is limited exploration: criteria that no rollout manages to satisfy (Unexplored Criteria, UC) receive no optimization signal. Recent methods address this by incorporating rubric information as external guidance during rollout, yet they introduce a train-inference mismatch: the policy is optimized on rollouts produced under external guidance while this guidance is absent at inference time, causing error accumulation through autoregressive decoding. Moreover, these exploration-focused approaches overlook a fundamentally different failure mode that we term Suppressed Criteria (SC) -- criteria that are satisfied by some rollouts yet whose learning signals are lost during optimization because scalar reward aggregation assigns them non-positive aggregate advantages. Our analysis reveals that SC are remarkably prevalent: over 57% of samples exhibit this failure mode throughout training, with an average of 1.8 SC per sample. To simultaneously address both UC and SC without introducing training-inference mismatch, we propose Criterion-Distilled Policy Optimization (CriPO), which enhances rubric-based RL via on-policy self-distillation. For UC, CriPO constructs a criterion-injection self-teacher and computes a localized forward-KL loss to inject missing behaviors into the policy. For SC, CriPO employs a counterfactual self-teacher to locate criterion-relevant tokens in negative-advantage rollouts and flips their token-level advantages to positive values, preserving useful patterns that would otherwise be suppressed. Experiments on medicine and science benchmarks demonstrate that CriPO consistently outperforms rubric-based RL, achieving stronger final performance with approximately $2\times$ fewer optimization steps.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingxuan Xia, Yuhang Yang, Chao Ye, Shuai Zhu, Shenzhi Yang, Guangcheng Zhu, Yuhang Zhang, Cheng Peng, Haobo Wang, Siqing Wang
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
