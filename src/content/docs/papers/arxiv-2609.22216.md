---
title: "The Effect of Quantization on Clinical Benchmarks: Accuracy and Safety Across Model Families"
description: "Quantization enables deployment of large language models on resource-constrained clinical edge devices, but its effect on clinical accuracy and safety remains understudied."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.22216) · [PDF](https://arxiv.org/pdf/2609.22216)

## 一句话摘要

Quantization enables deployment of large language models on resource-constrained clinical edge devices, but its effect on clinical accuracy and safety remains understudied.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization enables deployment of large language models on resource-constrained clinical edge devices, but its effect on clinical accuracy and safety remains understudied. We evaluate five 7-8B parameter models at FP16, GPTQ-INT8, and GPTQ-INT4 precision across five benchmarks: MedQA, MedMCQA, Med-HALT, a risk-stratified sample of HealthBench, and MedSafetyBench. The study jointly varies quantization bit width, model family, and clinical task type, with explicit risk stratification and safety measures. INT8 GPTQ is universally safe (max. degradation -1.9%-1.9%), while INT4 degradation is substantial and model-dependent: BioMistral-7B, clinically fine-tuned, loses 19.7% on MedMCQA, more than any general-purpose model, showing clinical fine-tuning does not confer compression robustness. MedMCQA degrades more than MedQA under INT4; Med-HALT is largely unaffected. On HealthBench's emergency-risk subgroup, Qwen2.5-7B degrades by 26.8% under INT4, suggesting high-risk scenarios are disproportionately vulnerable to compression. On MedSafetyBench, the model family dominates over precision (refusal rates range 10.2%-74.9% at FP16), though Qwen2.5-7B (-17.8%) and Meditron-7B (-28.3%) show substantial INT4 safety degradation; notably, Qwen2.5-7B is simultaneously the most accuracy-robust model, demonstrating that accuracy and safety robustness are independent properties. We additionally test two recovery methods, clinical calibration substitution and QLoRA fine-tuning, both producing the same trade-off: MedMCQA recovers while MedQA further degrades, indicating recovery strategies require task-specific validation rather than being assumed universally beneficial. These findings indicate INT8 is broadly safe for clinical deployment, while INT4 safety must be assessed per-model and per-task, and that safety alignment is determined primarily by instruction tuning rather than clinical domain adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leonard Twagirayezu, Prasenjit Mitra
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
