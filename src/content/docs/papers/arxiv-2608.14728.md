---
title: "Tail-Aware Top-$k$ On-Policy Distillation"
description: "On-policy distillation (OPD) has emerged as an effective paradigm for transferring knowledge between language models, where a student is trained to align its next-token distribution with the teacher's along its own trajectories."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.14728) · [PDF](https://arxiv.org/pdf/2608.14728)

## 一句话摘要

On-policy distillation (OPD) has emerged as an effective paradigm for transferring knowledge between language models, where a student is trained to align its next-token distribution with the teacher's along its own trajectories.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has emerged as an effective paradigm for transferring knowledge between language models, where a student is trained to align its next-token distribution with the teacher's along its own trajectories. To provide dense supervision at tractable cost, many works minimize the reverse Kullback-Leibler (KL) divergence between the student and teacher's normalized distributions over the teacher's top-$k$ tokens. However, this normalized objective discards the information about tail probability: the total probability outside the teacher's top-$k$ tokens. As a result, the optimization can steadily increase the student's tail probability and entropy, empirically degrading downstream accuracy. To address this issue, we propose Tail-Aware Top-$k$ OPD (\textbf{TA-OPD}), a novel distillation method that restores the missing tail probability signal. In particular, TA-OPD minimizes the reverse KL divergence over the top-$k$ tokens plus a tail token that carries the tail probability. In effect, TA-OPD better aligns the student's next-token distribution with the teacher's, preventing the increase in tail probability and entropy caused by top-$k$ normalization. Extensive experiments demonstrate the superiority of TA-OPD, improving Avg@8 by up to 8.05 points on common benchmarks. Our code is available at https://github.com/HuipengHuang/TA-OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Huipeng Huang, Hongxin Wei
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HuipengHuang/TA-OPD](https://github.com/HuipengHuang/TA-OPD)
- 阅读深度：metadata
