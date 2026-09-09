---
title: "JEDI: JEPA-to-Edge Distillation for Efficient Cropland Segmentation from Satellite Imagery"
description: "Large vision models provide useful representations for remote-sensing segmentation but are often too expensive for deployment at the satellite or field edge."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.07915) · [PDF](https://arxiv.org/pdf/2609.07915)

## 一句话摘要

Large vision models provide useful representations for remote-sensing segmentation but are often too expensive for deployment at the satellite or field edge.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large vision models provide useful representations for remote-sensing segmentation but are often too expensive for deployment at the satellite or field edge. Existing feature-level distillation methods also tend to assume similar teacher and student architectures and often stop feature alignment when task training begins. We introduce JEDI (JEPA-to-Edge Distillation), a two-stage framework that transfers representations from a large I-JEPA Vision Transformer teacher to a compact SegFormer student. First, JEDI aligns the student's terminal representation with the teacher's token space using cross-architecture projection and spatial alignment. It then jointly optimizes supervised segmentation, temperature-scaled response distillation, and persistent feature alignment throughout task adaptation. On CalCROP21, JEDI-B0 achieves 68.0 mean Intersection-over-Union (mIoU) with 4.04M parameters, improving over the standalone student by 16.0 points and coming within 2.0 points of the 70.0 mIoU achieved by the 639M-parameter teacher. We evaluate SegFormer B0, B1, and B2 students with 4.04M, 14.33M, and 28M parameters, respectively. Across all three variants, JEDI consistently outperforms response-, structure-, channel-, and relational-distillation baselines under the same teacher-student setting. These results show that persistent representation alignment is especially valuable under aggressive compression, substantially reducing model size and computation while preserving segmentation performance.

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

- 作者：Kishor Kumar Bhaumik, Nicolas Roque dos Santos, Jia Chen, Evangelos E. Papalexakis
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
