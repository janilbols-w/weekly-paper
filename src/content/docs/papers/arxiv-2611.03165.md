---
title: "LaBraM at Scale: Scaling Data and Models for EEG Pretraining"
description: "LaBraM, an early EEG foundation model, demonstrated that large-scale EEG pretraining can yield strong representations for diverse downstream tasks."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.03165) · [PDF](https://arxiv.org/pdf/2611.03165)

## 一句话摘要

LaBraM, an early EEG foundation model, demonstrated that large-scale EEG pretraining can yield strong representations for diverse downstream tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

LaBraM, an early EEG foundation model, demonstrated that large-scale EEG pretraining can yield strong representations for diverse downstream tasks. Building on this foundation, we expand pretraining data and model capacity while retaining its core encoder and objective. We train ten encoders with 5.8 million to 1.97 billion parameters on three EEG collections spanning 25,067 to 79,910 hours, adapting signal preparation and training to heterogeneous recordings. Across 23 tasks, Atom-L* reaches 59.05% mean balanced accuracy at its best evaluated full fine-tuning (Full-FT) checkpoint, 3.61 percentage points above the strongest baseline EEG foundation model. Quark-G leads linear probing (LP) at 54.33%, a 1.24-point margin. Both also lead average task rank. At the last evaluated checkpoints, larger encoders improve Full-FT more consistently than LP, and stronger LP does not guarantee stronger Full-FT. Preserving patch structure improves LP over average pooling. Data-fraction experiments suggest capacity-dependent saturation, while checkpoint trajectories show that downstream performance can decline as pretraining loss falls. Joint classification with a shared Qwen3 readout reaches 50.50% with Molecule-H and Qwen3-8B; increasing language-model size provides no consistent gain. These results demonstrate the value of scaling LaBraM and the importance of matching pretraining scale to downstream adaptation.

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

- 作者：Jun-Yu Pan, Ruicheng Yin, Bao-Liang Lu, Dongsheng Li, Wei-Long Zheng, Yansen Wang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
