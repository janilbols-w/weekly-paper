---
title: "Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation"
description: "Foundation multimodal large language models are designed to support a broad spectrum of capabilities across diverse domains."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02324) · [PDF](https://arxiv.org/pdf/2610.02324)

## 一句话摘要

Foundation multimodal large language models are designed to support a broad spectrum of capabilities across diverse domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

Foundation multimodal large language models are designed to support a broad spectrum of capabilities across diverse domains. Multi-teacher on-policy distillation (MOPD) provides an effective framework for consolidating domain-specific expertise into a single student model. However, MOPD training gradually drives the student away from its initialization model, and general capabilities decline as the displacement grows, resulting in capability interference. A direct remedy is constraining the student toward its initialization, but this suppresses the acquisition of domain expertise as well. We propose Slow-Fast Multi-Teacher On-Policy Distillation (SF-MOPD), which couples a fast model, the current student updated directly by each teacher, with a slow model, an exponential moving average of the student. The slow model absorbs the learning signal gradually, serving as a moving capability reference that fuses the general foundation with confirmed domain expertise. For each teacher, SF-MOPD computes the teacher-induced update in log-probability space and removes only the component that pushes the fast model further away from the slow model, while retaining aligned and orthogonal components. Experiments across multiple model scales demonstrate that SF-MOPD effectively mitigates capability interference, enhances specialized multimodal capabilities, and reduces the average degradation on general-capability benchmarks, consistently outperforming vanilla MOPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaofei Yin, Tong Chu, Jiyuan Fu, Jun Lan, Shuheng Zhou, Huijia Zhu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
