---
title: "MedPsy: State-of-the-Art Small Medical Language Models for Efficient Edge Deployment"
description: "Medical language models promise expert clinical support, but the strongest open-source LLMs remain too large for private edge-device deployment, while compact medical models still trail substantially on knowledge-intensive and real-world healthcare tasks."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.02011) · [PDF](https://arxiv.org/pdf/2611.02011)

## 一句话摘要

Medical language models promise expert clinical support, but the strongest open-source LLMs remain too large for private edge-device deployment, while compact medical models still trail substantially on knowledge-intensive and real-world healthcare tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Medical language models promise expert clinical support, but the strongest open-source LLMs remain too large for private edge-device deployment, while compact medical models still trail substantially on knowledge-intensive and real-world healthcare tasks. Reasoning models that fit edge memory budgets can produce long reasoning traces, increasing sequential decoding, end-to-end latency, energy consumption, and KV-cache memory pressure. We present MedPsy, a family of text-only 1.7B and 4B medical language models designed for edge deployment, targeting this accuracy-generation-efficiency trade-off. Our recipe combines a synthetic medical data pipeline over biology, medicine, and health seeds with chain-of-thought targets from a 235B medical-focused LLM teacher; a four-stage post-training curriculum comprising two SFT stages followed by two RL stages with hard-sample mining; and an edge deployment evaluation spanning multiple GGUF quantization variants and real-device inference on laptop and smartphone hardware. On seven closed-ended medical benchmarks, MedPsy-4B surpasses MedGemma-1.5-4B by 19.34 points and matches MedGemma-27B while being 6.75x smaller; MedPsy-1.7B outperforms MedGemma-1.5-4B by 11.42 points despite being less than half its size. On HealthBench-Hard, MedPsy-4B surpasses MedGemma-27B by 15.33 points, while MedPsy-1.7B surpasses it by 11.66 points despite being ~16x smaller. Beyond accuracy, MedPsy reduces average response length by 1.7x (1.7B) and 3.2x (4B) versus its Qwen3 backbones, while Q4_K_M quantization preserves the aggregate score within 1 point of BF16 with ~69% lower disk footprint. In real-device inference, MedPsy-4B's shorter generations translate into 75% lower median end-to-end latency and estimated energy per answer than its Qwen3 backbone at matched quantization, while peak RAM remains below 5 GB across our tested laptop and smartphone configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Davide Vitabile, Alexandro Buffa, Akshay Nambiar, Amril Nazir
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
