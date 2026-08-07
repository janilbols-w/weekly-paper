---
title: "ARCHead: Activation-Metric Residual Correction for Large Language Model Output Heads"
description: "Weight-only quantization substantially reduces the storage of large language model (LLM) transformer blocks, but practical backends often retain the final language-modeling head (LM-head) in BF16 or FP16."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.02703) · [PDF](https://arxiv.org/pdf/2608.02703)

## 一句话摘要

Weight-only quantization substantially reduces the storage of large language model (LLM) transformer blocks, but practical backends often retain the final language-modeling head (LM-head) in BF16 or FP16.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-only quantization substantially reduces the storage of large language model (LLM) transformer blocks, but practical backends often retain the final language-modeling head (LM-head) in BF16 or FP16. Quantizing this projection naively can strongly perturb the vocabulary-logit distribution. We present ARCHead, a packed LM-head compressor that combines a quantized low-rank core, group-wise INT4 residuals, and a low-rank correction fitted in an activation-derived metric. ARCHead stores no dense BF16 head and reduces persistent LM-head storage by 3.7-3.9x. On Qwen3-8B-Base, it uses 25.6% of BF16 head storage while attaining 1.007 relative perplexity; storage-matched naive INT4 yields 1.14-1.16. Replacing the BF16 head left by AWQ or bitsandbytes adds only 0.006-0.007 cross-entropy, with less than 2% throughput change in our measurements. ARCHead therefore complements block quantizers by compressing the large output projection they can leave untouched. Code is available at https://github.com/suayptalha/archead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization, quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Şuayp Talha Kocabay, Talha Rüzgar Akkuş, Kamer Ali Yuksel
- 发布：2026-08-03；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/suayptalha/archead](https://github.com/suayptalha/archead)
- 阅读深度：metadata
