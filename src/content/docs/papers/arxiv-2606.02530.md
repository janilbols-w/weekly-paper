---
title: "SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment"
description: "Aligning Large Language Models (LLMs) with human values often degrades their general capabilities, termed the alignment tax."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.02530) · [PDF](https://arxiv.org/pdf/2606.02530)

## 一句话摘要

Aligning Large Language Models (LLMs) with human values often degrades their general capabilities, termed the alignment tax.

## 为什么值得关注

待编辑增强。

## 摘要原文

Aligning Large Language Models (LLMs) with human values often degrades their general capabilities, termed the alignment tax. Existing methods mitigate this by balancing dual objectives, which heavily rely on massive general-purpose data or auxiliary reward models. In this paper, we argue that, because safety features are inherently sparse within the output distribution, alignment requires localized modifications rather than global trade-offs. To this end, we propose SafeSteer, which performs on-policy distillation confined to safety tokens. First, we construct a safety teacher via activation steering. Based on this teacher, we develop a safety token selection algorithm. Consequently, SafeSteer restricts the reverse KL penalty to these tokens during training to preserve general capabilities. Experimental results across diverse models show that our SafeSteer achieves a superior trade-off between safety and general capability compared with existing methods, attaining strong safety performance on seven safety benchmarks with only minimal degradation on five general capability benchmarks. Notably, SafeSteer requires only 100 harmful samples without using any general-purpose data, less than 1% of what previous baselines used, considerably reducing alignment cost. More details are on our project page at https://anjingkun.github.io/SafeSteer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hao Li, Jingkun An, Zijun Song, Pengyu Zhu, Rui Li, Hao Wang, Wendi Feng, Yesheng Liu, Lijun Li, Jin-Ge Yao, Lei Sha
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
