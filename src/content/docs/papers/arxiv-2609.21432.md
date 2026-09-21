---
title: "GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation"
description: "Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs)."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.21432) · [PDF](https://arxiv.org/pdf/2609.21432)

## 一句话摘要

Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs). Despite recent advances in post-training methods, such as Group Relative Policy Optimization (GRPO), their practical deployment remains impeded by training instability arising from the reliance on importance sampling. We introduce Group Variance Policy Optimization (GVPO), a novel post-training method that integrates the analytical solution of KL-constrained reward maximization into its gradient weighting scheme. This formulation provides an intuitive interpretation: GVPO's gradient corresponds to the mean squared error between the central distance of implicit rewards and that of actual rewards. GVPO offers two key advantages: (1) it guarantees a unique optimal solution, exactly to the KL-constrained reward maximization objective, and (2) it enables flexible sampling distributions without requiring importance sampling. Beyond general post-training, we show that GVPO naturally extends to on-policy distillation (OPD). Furthermore, GVPO enables the optimization of a broad family of extended OPD objectives, providing a principled foundation for diverse objective design. By unifying theoretical guarantees with practical adaptability, GVPO establishes a new paradigm for reliable and versatile LLM post-training and on-policy distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaichen Zhang, Yuzhong Hong, Junwei Bao, Hongfei Jiang, Yang Song, Dingqian Hong, Hui Xiong
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
