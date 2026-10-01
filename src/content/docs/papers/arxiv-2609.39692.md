---
title: "GFD-OPD: Guidance-Folded On-Policy Distillation of Diffusion Models Across Scales"
description: "On-policy distillation (OPD) has demonstrated two important capabilities in language models: compressing large teachers into smaller students and merging expert models into a single model."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.39692) · [PDF](https://arxiv.org/pdf/2609.39692)

## 一句话摘要

On-policy distillation (OPD) has demonstrated two important capabilities in language models: compressing large teachers into smaller students and merging expert models into a single model.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has demonstrated two important capabilities in language models: compressing large teachers into smaller students and merging expert models into a single model. Existing diffusion OPD, however, mostly focus on the latter, with teachers and students sharing the same backbone and scale. We investigate large-to-small diffusion opd from large teachers to a small student and find that the standard recipe fails. To find the underlying cause, we propose Fixed-State KL, an effective and fair way to measure the distribution gap between student and teacher during OPD training for diffusion models. We are the first to clarify why large-to-small OPD is challenging for diffusion models: a smaller student struggles to perfectly match the distribution of a larger teacher, while classifier-free guidance can accumulate and amplify the distributional discrepancies between the student's conditional and unconditional branches and those of the teacher. To solve this problem, we propose GFD-OPD, a simple yet effective method that reduces the student-teacher gap while avoiding the error amplification of the CFG composition. Across numerous experiments, GFD outperforms previous baselines in both training efficiency and final performance, achieving state-of-the-art results on all benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenxing Zhang, Jiayan Teng, Wenxu Wu, Zhuoyi Yang, Jiazheng Xu, Wendi Zheng, Jie Tang, Dan Guo, Meng Wang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
