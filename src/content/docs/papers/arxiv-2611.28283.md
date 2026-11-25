---
title: "HandXFM: Semantic-Structural Distillation for Hand Radiograph Foundation Models"
description: "Hand radiographs support diverse clinical tasks, including skeletal maturity assessment, rheumatoid arthritis scoring, abnormality screening, and anatomical localization, yet existing models are typically trained separately for each task and dataset."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.28283) · [PDF](https://arxiv.org/pdf/2611.28283)

## 一句话摘要

Hand radiographs support diverse clinical tasks, including skeletal maturity assessment, rheumatoid arthritis scoring, abnormality screening, and anatomical localization, yet existing models are typically trained separately for each task and dataset.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hand radiographs support diverse clinical tasks, including skeletal maturity assessment, rheumatoid arthritis scoring, abnormality screening, and anatomical localization, yet existing models are typically trained separately for each task and dataset. We present HandXFM, a domain-specific foundation model that leverages cross-modality knowledge for comprehensive hand X-ray understanding. HandXFM distills semantic priors from BiomedCLIP and structural cues from a chest X-ray Vision Transformer (ViT) through a unified alignment framework, integrating complementary medical knowledge in an interpretable way. After pretraining, HandXFM can be adapted to a range of musculoskeletal tasks, including bone age estimation, SvH score prediction, abnormality detection, joint localization, bone segmentation, and visual question answering. It consistently outperforms task-specific and single-expert baselines, achieving up to 0.11 improvement in Pearson correlation coefficient (PCC) for bone age prediction and a 12\% accuracy gain in abnormality classification. Moreover, HandXFM generalizes to unseen datasets and yields cross-attention maps linking clinical terms to anatomical regions. These results demonstrate that multi-expert distillation effectively unifies semantic and structural supervision within a single pretrained model, establishing HandXFM as an interpretable and generalizable foundation model for hand radiograph analysis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuxi Long, Ganlin Feng, Lianghong Chen, Liam J. O'Neil, Carol A. Hitchon, Pingzhao Hu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
