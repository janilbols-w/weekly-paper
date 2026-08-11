---
title: "Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation"
description: "Key-value (KV) cache quantization is widely used to reduce Large Language Model (LLM) inference memory, yet existing evaluations solely focus on measuring perplexity and accuracy without assessing the safety impact."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.09864) · [PDF](https://arxiv.org/pdf/2606.09864)

## 一句话摘要

Key-value (KV) cache quantization is widely used to reduce Large Language Model (LLM) inference memory, yet existing evaluations solely focus on measuring perplexity and accuracy without assessing the safety impact.

## 为什么值得关注

待编辑增强。

## 摘要原文

Key-value (KV) cache quantization is widely used to reduce Large Language Model (LLM) inference memory, yet existing evaluations solely focus on measuring perplexity and accuracy without assessing the safety impact. In this study, we explore alignment preservation under KV cache quantization. Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics. We identify that the root cause is geometric: safety features occupy a low-dimensional activation subspace 10^2-10^3x more vulnerable to quantization noise than the full representation space perplexity averages over. Inspired by this observation, we propose Per-Channel Reduction (PCR), a diagnostic that classifies each model into one of three mechanistic failure modes: outlier-crushes-safety, where safety lives in non-outlier channels collaterally damaged by outlier-driven scale factors; outlier-as-safety, where safety overlaps outlier channels and finer granularity cannot rescue it; and multi-layer dilution, where safety is distributed across many layers and per-layer fixes fail. PCR predicts the correct mitigation direction on all nine primary models and one held-out model from an independent family using 20 calibration prompts. PCR generalizes across unseen prompts, models, and production quantizers, including KIVI with up to 97.2% recovery, succeeding where attention-based allocation methods fail. The resulting training-free protocol, requiring approximately 35 GPU-minutes, recovers up to 97% of lost alignment at minimal memory overhead, addressing vulnerabilities confirmed in production vLLM serving with FP8 KV cache on NVIDIA GPUs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Bruce Changlong Xu, Adarsh Kumarappan, Mu Zhou
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
