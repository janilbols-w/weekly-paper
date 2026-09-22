---
title: "When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs"
description: "Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.24799) · [PDF](https://arxiv.org/pdf/2609.24799)

## 一句话摘要

Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) enables efficient deployment of large language models, and PTQ methods are usually optimized and evaluated with generic reconstruction, perplexity, or answer accuracy. But in explanation-critical domains, preserving only the final answer may be insufficient, since users may also inspect generated rationales to judge whether a prediction is trustworthy. We study this issue in medical multiple-choice question answering, where rationales should provide evidence that supports the selected answer. We propose an explanation-aware objective for transformation-based PTQ. Our method builds an offline faithfulness cache from full-precision teacher rationales and uses it during optimization to preserve answer-supporting evidence tokens and evidence-conditioned answer behavior. We instantiate it on OSTQuant under W4A4KV4 quantization and evaluate four 7B--8B medical and instruction-tuned LLMs on MedExQA, MedExpQA, and ChallengeClinicalQA. While a same-calibration OSTQuant baseline preserves task accuracy, it can substantially weaken answer-supporting rationales. Our objective is to preserve the full-precision model's answer-supporting behavior rather than improve gold-label accuracy, and our method better preserves the full-precision model's answer behavior and rationale-to-answer support. These results suggest that PTQ for explanation-critical settings should evaluate preservation of answer-supporting evidence, not only answer accuracy. Code and evaluation scripts are available at https://github.com/dut0817/EAQuant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yeji Kim, Mi-Young Kim, Randy Goebel
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/dut0817/EAQuant](https://github.com/dut0817/EAQuant)
- 阅读深度：metadata
