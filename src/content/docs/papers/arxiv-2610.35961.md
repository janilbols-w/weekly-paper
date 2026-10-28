---
title: "Knowledge distillation across teacher architectures for compact diabetic retinopathy grading"
description: "Diabetic retinopathy grading from retinal fundus photographs is important but difficult to deploy on resource-constrained hardware."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.35961) · [PDF](https://arxiv.org/pdf/2610.35961)

## 一句话摘要

Diabetic retinopathy grading from retinal fundus photographs is important but difficult to deploy on resource-constrained hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diabetic retinopathy grading from retinal fundus photographs is important but difficult to deploy on resource-constrained hardware. We conducted a controlled study of offline response-based knowledge distillation for five-class diabetic retinopathy grading on APTOS 2019, comparing ResNet-50, MobileNetV3-Large, and Swin Transformer-Tiny (Swin-T) teachers distilled into a MobileNetV3-Small student. A 3 x 4 x 2 grid of teacher, temperature, and hard-label weight was screened at one seed, while six configurations and the no-distillation baseline were evaluated across three seeds. The highest observed single-seed quadratic weighted kappa was 0.9093 (macro-F1 0.6851) for Swin-T at temperature 4 and hard-label weight 0.7; the corresponding three-seed mean was 0.9024, compared with 0.8804 for the baseline. The student used 1.52 M parameters and 5.94 MB, representing an 18.07x parameter reduction relative to Swin-T. Temperature and hard-label weight effects were teacher- and configuration-dependent, while small performance differences were sensitive to random seed. Knowledge distillation produced a compact student with competitive performance under the evaluated protocol, but independent external validation remains necessary.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mossa Manisa, Habiba Jahan Priya, A. K. M. Fakhrul Hossain
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
