---
title: "Qwen-Image-Flash: Rethinking the Training Recipe for Few-Step Distillation"
description: "Few-step distillation has emerged as a critical component in the development of advanced visual generative foundation models, substantially reducing inference overhead while enabling real-time generation and cost-efficient deployment across a broad range of practical scenarios."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.03746) · [PDF](https://arxiv.org/pdf/2606.03746)

## 一句话摘要

Few-step distillation has emerged as a critical component in the development of advanced visual generative foundation models, substantially reducing inference overhead while enabling real-time generation and cost-efficient deployment across a broad range of practical scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

Few-step distillation has emerged as a critical component in the development of advanced visual generative foundation models, substantially reducing inference overhead while enabling real-time generation and cost-efficient deployment across a broad range of practical scenarios. However, prior work has predominantly focused on advancing training objectives, while comparatively overlooking the training recipe, which has become increasingly critical in the era of large-scale foundation models. In this work, we systematically revisit the training recipe under the well-established distribution matching distillation (DMD) framework for both text-to-image generation and image editing, focusing on three key dimensions: training data composition, teacher guidance within DMD, and task mixture. Our empirical analysis reveals several non-obvious and counterintuitive phenomena, ultimately motivating the development of Qwen-Image-Flash. These findings highlight that effective few-step distillation depends not only on carefully designed objectives, but also on a principled training recipe.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhe Wu, Zikai Zhou, Kun Yan, Kaiyuan Gao, Lihan Jiang, Jiahao Li, Jie Zhang, Ningyuan Tang, Shengming Yin, Xiaoyue Chen, Xiao Xu, Yilei Chen, Yuxiang Chen, Yan Shu, Yixian Xu, Yanran Zhang, Zihao Liu, Zhendong Wang, Zekai Zhang, Deqing Li, Liang Peng, Yi Wang, Zeke Xie, Jingren Zhou, Bo Zheng, Chenfei Wu
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
