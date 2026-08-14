---
title: "OC-Distill: Ontology-aware Contrastive Learning with Cross-Modal Distillation for ICU Risk Prediction"
description: "Early prediction of severe clinical deterioration and remaining length of stay can enable timely intervention and better resource allocation in high-acuity settings such as the ICU."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.16878) · [PDF](https://arxiv.org/pdf/2604.16878)

## 一句话摘要

Early prediction of severe clinical deterioration and remaining length of stay can enable timely intervention and better resource allocation in high-acuity settings such as the ICU.

## 为什么值得关注

待编辑增强。

## 摘要原文

Early prediction of severe clinical deterioration and remaining length of stay can enable timely intervention and better resource allocation in high-acuity settings such as the ICU. This has driven the development of machine learning models that leverage continuous streams of vital signs and other physiological signals for real-time risk prediction. Despite their promise, existing methods have important limitations. Contrastive pretraining treats all patients as equally strong negatives, failing to capture clinically meaningful similarity between patients with related diagnoses. Meanwhile, downstream fine-tuning typically ignores complementary modalities such as clinical notes, which provide rich contextual information unavailable in physiological signals alone. To address these challenges, we propose OC-Distill, a two-stage framework that leverages multimodal supervision during training while requiring only vital signs at inference. In the first stage, we introduce an ontology-aware contrastive objective that exploits the ICD hierarchy to quantify patient similarity and learn clinically grounded representations. In the second stage, we fine-tune the pretrained encoder via cross-modal knowledge distillation, transferring complementary information from clinical notes into the model. Across multiple ICU prediction tasks on MIMIC, OC-Distill demonstrates improved label efficiency and achieves state-of-the-art performance among methods that use only vital signs at inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhongyuan Liang, Junhyung Jo, Hyang-Jung Lee, Sang Kyu Kim, Irene Y. Chen
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
