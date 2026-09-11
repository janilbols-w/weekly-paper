---
title: "Longitudinal Risk Prediction in Mammography with Privileged History Distillation"
description: "Longitudinal mammography screening has become an important source of information for improving future breast cancer risk prediction."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.15814) · [PDF](https://arxiv.org/pdf/2603.15814)

## 一句话摘要

Longitudinal mammography screening has become an important source of information for improving future breast cancer risk prediction.

## 为什么值得关注

待编辑增强。

## 摘要原文

Longitudinal mammography screening has become an important source of information for improving future breast cancer risk prediction. However, the performance of current longitudinal mammography models degrades when prior examinations are unavailable at inference, creating a structured privileged-information setting in which temporal context is available during training but absent at deployment. We propose Single-Exam Mammography risk prediction with privileged History Distillation (SEM-HD), a framework that uses longitudinal history as privileged information available only during training to preserve the predictive benefits of longitudinal modeling while requiring only the current screening examination at deployment. During training, the student relies on the current examination to predict latent representations of prior visits, while horizon-specific teachers provide additional supervision from the observed longitudinal history. Together, latent history prediction and teacher distillation preserve the temporal modeling structure of longitudinal predictors under current-exam-only inference. We validate SEM-HD on three longitudinal mammography cohorts, the CSAW-CC, EMBED, and OMI-DB, using the transformer-based Longitudinal Mammography Risk (LoMaR) and recurrent Visual Memory Recurrent Attention (VMRA) backbones. Under current-exam-only inference, SEM-HD consistently improves long-horizon AUC and pAUC over longitudinal models evaluated without history, particularly in the clinically relevant low false-positive-rate region. It also recovers much of the performance gap with respect to full-history inference across datasets and backbones. Ablations further show that these gains are not reproduced by masking or heuristic history imputation. The strongest performance is achieved by combining patient-specific latent history prediction with distilled temporal risk supervision.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Banafsheh Karimian, Soufiane Belharbi, Alexis Guichemerre, Luke McCaffrey, Mohammadhadi Shateri, Eric Granger
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
