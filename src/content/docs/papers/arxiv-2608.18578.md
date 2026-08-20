---
title: "Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs"
description: "Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior overwrites accumulate, mirroring a classical phenomenon in human working memory."
---

**评分：57/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.18578) · [PDF](https://arxiv.org/pdf/2608.18578)

## 一句话摘要

Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior overwrites accumulate, mirroring a classical phenomenon in human working memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior overwrites accumulate, mirroring a classical phenomenon in human working memory. Post-training quantization (PTQ) is now the default deployment path for open-weight models, yet its effect on this failure mode has not been tested. We evaluate three precision levels (FP16, INT8, INT4/NF4, via bitsandbytes) across three architecturally distinct instruction-tuned models (Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, Phi-3.5-mini-instruct), holding the retrieval task fixed. INT4 quantization significantly reduces accuracy under high interference in every model (e.g., from 81.0% to 68.3% for Qwen), confirmed by paired McNemar's tests ($p \le 2.6 \times 10^{-6}$) and a mixed-effects regression spanning all interference levels; INT8, often assumed safe, also carries a smaller but real penalty in two of three models. The effect is specific to semantically similar (word-type) distractors and reverses sign under a numeric control condition, and is mechanistically linked to a rise in same-key intrusion errors under INT4 (from 21.5% to 24.6% of trials, $p = 4.8 \times 10^{-7}$). A follow-up ablation shows the effect originates in the quantized transformer backbone rather than the output projection layer. These results suggest that bitsandbytes 4-bit quantization can impose an additional cost on applications relying on long, updatable, semantically dense contexts, even when aggregate benchmark accuracy appears largely unaffected. We release our code and tokenizer-verified vocabulary construction method at https://github.com/ShayanShahrabi/compress-and-forget

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shayan Shahrabi-Farahani (Shahid Beheshti University, Tehran, Iran), Dara Rahmati (Shahid Beheshti University, Tehran, Iran)
- 发布：2026-08-20；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ShayanShahrabi/compress-and-forget](https://github.com/ShayanShahrabi/compress-and-forget)
- 阅读深度：metadata
