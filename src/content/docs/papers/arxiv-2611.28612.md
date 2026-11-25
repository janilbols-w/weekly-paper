---
title: "Reducing Permutation Sensitivity in Multimodal Large Language Models via Shared Positions and Attention-Only Distillation"
description: "In this paper, we conduct a systematic study on improving permutation robustness while preserving accuracy."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.28612) · [PDF](https://arxiv.org/pdf/2611.28612)

## 一句话摘要

In this paper, we conduct a systematic study on improving permutation robustness while preserving accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this paper, we conduct a systematic study on improving permutation robustness while preserving accuracy. First, we categorize permutation bias phenomena into four representative scenarios. Then, we take the multiple-choice question answering (MCQA) dataset as an example under text-option reordering scenario to analyze the root cause of permutation bias. Based on this root cause analysis and set encoding strategy, we investigate shared positions with blocked cross-unit attention (SP-B) and extend this design to bidirectional cross-unit attention (SP-V) for modality exchange. However, these structural changes may reduce predictive accuracy. To recover model capability across different scenarios under the SP structure, an attention-only distillation from frozen native models is proposed. Shared positions reduce permutation sensitivity, and attention-only distillation improves accuracy under the shared-position structure. Across all three models, our method is comparable to or better than majority voting in macro-average all-permutation accuracy, and outperforms supervised fine-tuning by 1.95-4.20 percentage points. This work provides valuable insight into permutation bias mitigation and model capability recovery.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yifei Cheng, Xiaolin Zhang, Yu-Xuan Qiu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
