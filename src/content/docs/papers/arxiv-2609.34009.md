---
title: "Fisher-Informed Recalibration for Feedback-Based On-Policy Self-Distillation of LLMs"
description: "Feedback-based on-policy self-distillation has emerged as a promising approach for enabling foundation models, more specifically Large Language Models (LLMs), to learn from their own outputs under external feedback, with a single model serving as both teacher and student."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.34009) · [PDF](https://arxiv.org/pdf/2609.34009)

## 一句话摘要

Feedback-based on-policy self-distillation has emerged as a promising approach for enabling foundation models, more specifically Large Language Models (LLMs), to learn from their own outputs under external feedback, with a single model serving as both teacher and student.

## 为什么值得关注

待编辑增强。

## 摘要原文

Feedback-based on-policy self-distillation has emerged as a promising approach for enabling foundation models, more specifically Large Language Models (LLMs), to learn from their own outputs under external feedback, with a single model serving as both teacher and student. However, such methods can exhibit unstable optimization, conducive to performance collapse during training. To address this limitation, we propose FIRE (Fisher-Informed REcalibration), a dual-branch framework that recalibrates the supervision applied to correct and incorrect on-policy outputs during fine-tuning. For correct responses, FIRE replaces self-distillation with re-weighted on-policy SFT, while for incorrect ones FIRE identifies feedback components that disproportionately influence the teacher-induced update and recalibrates the feedback-conditioned target accordingly. Both branches are influenced by a token-level radius derived in part from a softmax Fisher trace. FIRE separates which direction feedback should move the model from how far the model should move in that direction, while leaving well-behaved feedback supervision unchanged. Our experiments demonstrate that FIRE provides substantially more stable self-distillation while maintaining strong downstream performance, particularly in settings where standard feedback-conditioned distillation becomes unstable.

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

- 作者：Seohyun Lee, Dong-Jun Han, Seyyedali Hosseinalipour, Christopher G. Brinton
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
