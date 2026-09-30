---
title: "Understanding the Synergy between SFT, RLVR, and OPD in LLM Post-Training"
description: "Modern LLM post-training composes supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and on-policy distillation (OPD) into multi-stage pipelines, yet these stages are typically designed and evaluated in isolation."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.31900) · [PDF](https://arxiv.org/pdf/2609.31900)

## 一句话摘要

Modern LLM post-training composes supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and on-policy distillation (OPD) into multi-stage pipelines, yet these stages are typically designed and evaluated in isolation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM post-training composes supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and on-policy distillation (OPD) into multi-stage pipelines, yet these stages are typically designed and evaluated in isolation. We show that this composition is consequential: a stage that improves the current model can make the next stage less effective. Through controlled experiments with Qwen3 models on math and science reasoning, we first characterize OPD across nine student-teacher pairs spanning 2x to 53x parameter ratios and show that OPD effectiveness depends on student-teacher compatibility rather than teacher scale alone. The surrounding stages of OPD reshape this compatibility in three ways: (1) A brief SFT warm-up improves subsequent OPD, while an RLVR-strengthened student regresses under distillation from the same teacher. (2) Adapting the teacher with RLVR raises downstream OPD accuracy in proportion to the capability it adds. Following these two interventions, we find that combining teacher adaptation and student warm-up alone raise average OPD accuracy from 29.2\% to 43.8\% (50\% relative improvement) after the same number of distillation steps, with additional preparatory training. (3) At comparable accuracy, OPD leaves a stronger initialization for downstream RLVR than SFT, with a gap that widens as RL compute scales. Our results suggest that each post-training stage should be chosen not only for the capability it adds, but for the learning interface it creates for the next stage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Emre Can Acikgoz, Yang Li, Zeyu Leo Liu, Srijan Bansal, Dilek Hakkani-T\"ur, Shafiq Joty, Semih Yavuz
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
