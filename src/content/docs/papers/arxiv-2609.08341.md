---
title: "TV-Regulated OPD: Direction Matters in On-Policy Distillation"
description: "On-Policy Distillation (OPD) facilitates the transfer of knowledge from domain expert to student in the post-training phase of Large Language Models (LLMs)."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.08341) · [PDF](https://arxiv.org/pdf/2609.08341)

## 一句话摘要

On-Policy Distillation (OPD) facilitates the transfer of knowledge from domain expert to student in the post-training phase of Large Language Models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

On-Policy Distillation (OPD) facilitates the transfer of knowledge from domain expert to student in the post-training phase of Large Language Models (LLMs). However, the supervision signals in mainstream OPD methods suffer from high variance and noise which is generally instable during training. In this work, we systematically investigated what really matters to the performance and the fundamental mechanisms behind the instability during training. We found that retaining only the sign of token-level advantages is sufficient to achieve the performance comparable to standard OPD. Meanwhile, smoother and bounded advantages can stabilize the training process without sacrificing its performance. These motivated us to shape the advantages using the Total Variation (TV) and propose a robust TV regulated On-Policy Distillation (TV-OPD) method. Benefiting from the bounded and diminished advantages, TV-OPD exhibits stable training dynamics and steady late-stage performance. We conducted comprehensive experiments and found that, across various settings, TV-OPD consistently achieved better performance and lower variance in the late-stage of training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Han Xiao, Yifan Niu, Dongyi Liu, Chang Luo, Jia Li
- 发布：2026-09-08；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
