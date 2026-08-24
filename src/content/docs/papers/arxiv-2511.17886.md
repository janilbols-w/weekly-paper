---
title: "When Better Teachers Don't Make Better Students: Revisiting Knowledge Distillation for CLIP Models in VQA"
description: "Vision-language models (VLMs) have achieved remarkable success across multimodal tasks, yet their substantial computational demands hinder efficient deployment."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.17886) · [PDF](https://arxiv.org/pdf/2511.17886)

## 一句话摘要

Vision-language models (VLMs) have achieved remarkable success across multimodal tasks, yet their substantial computational demands hinder efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) have achieved remarkable success across multimodal tasks, yet their substantial computational demands hinder efficient deployment. Knowledge distillation (KD) has emerged as a powerful approach for building lightweight but competitive models, with strong evidence from both language and vision domains. However, its application to VLMs, particularly CLIP-style models, remains limited, often constrained to small-scale teachers and narrow evaluation tasks such as classification or retrieval. In this work, we present the first systematic study of distillation across a range of CLIP-style teacher models, ranging from standard baselines to large-scale state-of-the-art models. Contrary to trends observed in NLP and vision, we find that stronger teachers do not consistently yield better students; in fact, existing distillation frameworks often fail to scale, leading to degraded performance in downstream multimodal tasks such as visual question answering. Our findings challenge prevailing assumptions in KD and point toward new directions for designing parameter-efficient multimodal models.

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

- 作者：Pume Tuchinda, Parinthapat Pengpun, Romrawin Chumpu, Patomporn Payoungkhamdee, Sarana Nutanong, Peerat Limkonchotiwat
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
