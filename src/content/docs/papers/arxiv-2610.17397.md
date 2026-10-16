---
title: "JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models"
description: "On-policy distillation (OPD) is a post-training approach for large language models (LLMs) that enables a student model to learn a teacher model's distribution from sequences sampled from the student's own policy."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.17397v1) · [PDF](https://arxiv.org/pdf/2610.17397v1)

## 一句话摘要

On-policy distillation (OPD) is a post-training approach for large language models (LLMs) that enables a student model to learn a teacher model's distribution from sequences sampled from the student's own policy.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is a post-training approach for large language models (LLMs) that enables a student model to learn a teacher model's distribution from sequences sampled from the student's own policy. Despite its promising capability, OPD for diffusion language models (DLMs) remains underexplored and existing studies primarily focuses on DLM-to-DLM distillation. The limited availability of strong teacher DLMs and the flexible generation order of DLMs impose additional technical challenges as well. However, it remains unclear how to effectively distill knowledge from a strong autoregressive language model (ARM) into a weaker DLM, given the mismatch between the left-to-right decoding of ARMs and the flexible decoding order of DLMs. Inspired by Ni et al. (2026), we propose JustOPD, an ARM-to-DLM on-policy distillation method that uses autoregressive rollouts during training to align the student's generation process with the ARM teacher's left-to-right decoding. This alignment enables effective distillation from ARM teachers while preserving the DLM's flexible generation-order capability at inference time. Experiments using Qwen3-14B as the teacher and Dream-7B as the student demonstrate that JustOPD consistently improves mathematical reasoning performance over the base DLM across multiple divergence choices.

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

- 作者：Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
