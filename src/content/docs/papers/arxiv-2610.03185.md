---
title: "Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective"
description: "On-policy distillation (OPD) has become an important approach to language model post-training."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.03185) · [PDF](https://arxiv.org/pdf/2610.03185)

## 一句话摘要

On-policy distillation (OPD) has become an important approach to language model post-training.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes through a reinforcement learning perspective: the teacher implicitly rewards student behaviors, even those it rarely exhibits itself. From this perspective, our experiments show that OPD improves performance without expanding the student's capabilities. When the implicit reward model is reliable, OPD makes correct responses easier to sample. In contrast, when the preference misaligns with quality, reward hacking happens: the implicit reward model amplifies overlong, repetitive student rollouts, even though it rarely generates such text itself. Guided by this diagnosis, we find that masking unhealthy responses during training and using SFT initialization can each effectively mitigate the collapse. Together, these findings show that OPD amplifies student behaviors favored by the teacher's implicit feedback, shifting the focus from how well the teacher generates to how reliably it evaluates student rollouts. Our code is available at https://github.com/HancCui/opd_hacking.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Han Cui, Jianhao Yan, Yun Luo, Hongbo Zhang, Zhizhang Fu, Yue Zhang
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HancCui/opd_hacking](https://github.com/HancCui/opd_hacking)
- 阅读深度：metadata
