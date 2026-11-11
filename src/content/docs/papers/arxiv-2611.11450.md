---
title: "How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?"
description: "On-policy distillation (OPD) trains a student language model on its own responses, guided by a fixed teacher."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.11450) · [PDF](https://arxiv.org/pdf/2611.11450)

## 一句话摘要

On-policy distillation (OPD) trains a student language model on its own responses, guided by a fixed teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) trains a student language model on its own responses, guided by a fixed teacher. Generating these responses is expensive, so systems use quantized inference and asynchronous rollouts to reduce the cost. Both, however, introduce training-inference mismatch between the rollout engine and the model being trained. Such mismatch can destabilize reinforcement learning (RL), but its effects on OPD remain unclear. This paper investigates how much mismatch OPD tolerates, where its effects arise, and how training systems can use this tolerance. Measuring all mismatch sources on one scale, we examine quantization across three student-teacher pairs, with additional tests of weight staleness and injected noise on one pair. OPD tolerates substantial mismatch without meaningful loss of training quality but degrades at higher levels, revealing an empirical mismatch budget. Both the quality cost of mismatch and the mismatch introduced by quantization depend on the model, with some layers particularly sensitive to reduced precision. In controlled comparisons, OPD remains stable under rollout configurations that destabilize RL methods. Under weight noise, mismatch also shifts the prefixes reached during generation, introducing errors that per-token corrections cannot address. To put these findings into practice, we introduce a lightweight admission check that screens rollout configurations against a calibrated budget without requiring a full training run for each candidate. Model-specific FP8 recipes preserve training quality while providing capacity for at least $1.93\times$ as many KV-cache tokens as BF16. Combining FP8 with asynchronous rollouts reaches the same training quality $1.62\times$ sooner than synchronous BF16 training. Code is available at https://github.com/benyucong/train-inference-mismatch-opd

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Cong Yu, Ziting Wang, Songlin Jiang, Sitong Zhang, Chengliang Chai, Youhe Jiang, Eiko Yoneki, Tuo Shi
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/benyucong/train-inference-mismatch-opd](https://github.com/benyucong/train-inference-mismatch-opd)
- 阅读深度：metadata
