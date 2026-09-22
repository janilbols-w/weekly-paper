---
title: "Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery"
description: "Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.23924) · [PDF](https://arxiv.org/pdf/2609.23924)

## 一句话摘要

Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supervised comparator evaluated here outperforms every foundation-model configuration, including validation-selected fine-tuning. We then examine a key confound: foundation models and task-specific decoders are normally evaluated using different input pipelines. Retraining three supervised architectures on the broadband arrays consumed by the foundation models produces matched-input accuracy differences of opposite sign across architectures: broadband input improves ATCNet by 0.078 accuracy while reducing EEG Conformer accuracy by 0.088. None of the three individual matched-input terms is significant after multiple-comparison correction at n = 9, so we treat the sign variation descriptively rather than as a formal architecture-by-pipeline interaction. These observed sign differences suggest that a single comparator may not provide an architecture-invariant decomposition of a pretrained-versus-supervised performance gap. The four-class deficit also does not reproduce uniformly across motor-imagery datasets: on two-class BNCI2014-004 we cannot detect the same separation between fine-tuned CBraMod and the supervised comparators. Finally, validation-fitted temperature scaling returns foundation-model calibration error to the supervised range despite substantially lower four-class accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kevin Zhou, Sparsh Roy
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
