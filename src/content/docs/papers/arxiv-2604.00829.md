---
title: "LinguDistill: Recovering Linguistic Ability in Vision-Language Models via Selective Cross-Modal Distillation"
description: "Turning a pretrained language model (LM) into a vision-language model (VLM) through multimodal fine-tuning often erodes its native language ability, a form of catastrophic forgetting that shows up even on text-only tasks."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.00829) · [PDF](https://arxiv.org/pdf/2604.00829)

## 一句话摘要

Turning a pretrained language model (LM) into a vision-language model (VLM) through multimodal fine-tuning often erodes its native language ability, a form of catastrophic forgetting that shows up even on text-only tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Turning a pretrained language model (LM) into a vision-language model (VLM) through multimodal fine-tuning often erodes its native language ability, a form of catastrophic forgetting that shows up even on text-only tasks. This loss is hard to undo with further fine-tuning, and existing remedies add adapters or alignment modules that increase architectural complexity and inference cost. We propose LinguDistill, an adapter-free knowledge distillation method that uses the original frozen LM as the teacher during multimodal post-training. To let a text-only teacher supervise vision-conditioned outputs, we introduce layer-wise KV-cache sharing, which exposes the teacher to the student's multimodal representations without changing either architecture. We then apply distillation selectively, on language-heavy data only, so the teacher restores linguistic ability while the student keeps its visual grounding on document and OCR tasks. LinguDistill recovers the language and knowledge performance lost during multimodal fine-tuning, matching the original VLM on average over text-only benchmarks (ARC, HellaSwag) and exceeding it on ScienceQA, while keeping vision-heavy performance close to standard fine-tuning. Since the teacher is dropped after training, the final model adds no parameters and no inference cost. More broadly, our results show that a model's own pre-adaptation backbone is a practical teacher for undoing forgetting, suggesting a simple recipe for keeping language ability intact as models are extended to new modalities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Patrick Amadeus Irawan, Erland Hilman Fuadi, Shanu Kumar, Alham Fikri Aji, Yova Kementchedjhieva
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
