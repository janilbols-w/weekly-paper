---
title: "Compression Effects on Low-Resource Multilingual Translation"
description: "We present a pilot study characterising the effect of post-training quantisation on multilingual machine translation quality and inference cost for three African languages - Hausa, Swahili, and Yoruba - across three model families: a small general-purpose LLM (Qwen2.5-1.5B), a larger multilingual instruction-tuned LLM (Aya-23-8B), and a dedicated multilingua"
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.24043) · [PDF](https://arxiv.org/pdf/2611.24043)

## 一句话摘要

We present a pilot study characterising the effect of post-training quantisation on multilingual machine translation quality and inference cost for three African languages - Hausa, Swahili, and Yoruba - across three model families: a small general-purpose LLM (Qwen2.5-1.5B), a larger multilingual instruction-tuned LLM (Aya-23-8B), and a dedicated multilingua

## 为什么值得关注

待编辑增强。

## 摘要原文

We present a pilot study characterising the effect of post-training quantisation on multilingual machine translation quality and inference cost for three African languages - Hausa, Swahili, and Yoruba - across three model families: a small general-purpose LLM (Qwen2.5-1.5B), a larger multilingual instruction-tuned LLM (Aya-23-8B), and a dedicated multilingual MT model (NLLB-200-distilled-1.3B). Evaluating on the FLORES-200 devtest set (1,012 sentences per direction) under FP16, bitsandbytes INT8, and NF4 INT4 precisions on consumer-grade NVIDIA T4 GPUs, we find: (i) the specialised MT model outperforms both LLMs by 32.7-43.3 chrF on the Hausa and Swahili directions, and by 12.9-24.7 chrF on Yoruba, despite being roughly a sixth the size of the 8B instruction-tuned LLM; (ii) post-training quantisation preserves aggregate translation quality within approximately 1 chrF across all model families and language directions, with a single worst case of 2.19 chrF; (iii) on consumer GPUs, INT8 and INT4 quantisation provide substantial memory savings (49-61% at INT4) but do not reduce inference latency relative to FP16 - in fact, latency increases by 1.3x to 5.3x; (iv) a clear performance gradient tracking training-resource availability is visible across languages (Swahili > Hausa > Yoruba). These findings motivate a research agenda focused on hardware-aware compression and error-type analysis beyond aggregate metrics for low-resource deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Abbas Sani
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
