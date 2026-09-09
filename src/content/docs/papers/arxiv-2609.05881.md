---
title: "Broken on Arrival: Silently Defective LLM Artifacts in Public Model Registries and How to Catch Them"
description: "Developers increasingly run large language models locally by pulling quantized GGUF artifacts from public registries, yet nothing in the distribution pipeline functionally tests these conversions before they reach users."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.05881) · [PDF](https://arxiv.org/pdf/2609.05881)

## 一句话摘要

Developers increasingly run large language models locally by pulling quantized GGUF artifacts from public registries, yet nothing in the distribution pipeline functionally tests these conversions before they reach users.

## 为什么值得关注

待编辑增强。

## 摘要原文

Developers increasingly run large language models locally by pulling quantized GGUF artifacts from public registries, yet nothing in the distribution pipeline functionally tests these conversions before they reach users. We executed 327 quantized code-capable model artifacts: 305 from the official Ollama library, spanning 15 model lines at every eligible quantization level at or under 8 GB, and 22 from the most-downloaded community repositories on HuggingFace. Each ran a 15-task smoke suite calibrated so that healthy artifacts pass while a known-broken one fails; suspects then faced full 164-task evaluation, a second inference backend, an independent distributor's conversion of the same model and quantization as referee, and, for community files, re-testing under the artifact's own template. The official library carries five silently defective artifacts, a batch of four Qwen2.5-Coder-3B conversions and one phi3.5-mini conversion, that solve zero of 164 tasks and zero of the smoke suite on both backends while independent conversions of the same models work: 1.6% of official artifacts, 2 of 29 model-and-size conversion groups. The adjudication chain cleared small-model artifacts that a naive threshold would condemn as broken when they are merely collapsed by extreme quantization, and it exposed two older community conversions that degrade badly on CUDA yet pass on Metal: not defective files but backend-dependent failures, a third phenomenon no registry currently tests for. Two confirmed defects produce output whose surface statistics sit inside the healthy range, invisible to any low-noise heuristic short of execution. We release the audit dataset, the quantcheck acceptance-testing tool, and disclosure reports for every confirmed defect (https://github.com/aditi-p31/quantcheck), and argue that model registries need the acceptance gate that package registries already run.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Aditi Patodiya
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/aditi-p31/quantcheck](https://github.com/aditi-p31/quantcheck)
- 阅读深度：metadata
