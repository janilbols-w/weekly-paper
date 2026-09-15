---
title: "TriCalRAG: A Three-Strategy, Retrieval-Augmented Benchmark for On-Premise LLM-Based Root Cause Analysis in AIOps"
description: "Cloud-hosted large language models (LLMs) are increasingly used for root cause analysis (RCA) in AIOps pipelines, but they introduce data privacy risk, network latency, and per-query cost that scale poorly with production log volumes."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.14762) · [PDF](https://arxiv.org/pdf/2609.14762)

## 一句话摘要

Cloud-hosted large language models (LLMs) are increasingly used for root cause analysis (RCA) in AIOps pipelines, but they introduce data privacy risk, network latency, and per-query cost that scale poorly with production log volumes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Cloud-hosted large language models (LLMs) are increasingly used for root cause analysis (RCA) in AIOps pipelines, but they introduce data privacy risk, network latency, and per-query cost that scale poorly with production log volumes. We present TriCalRAG, a benchmark evaluating open-weight LLMs served locally via vLLM on a single high-memory workstation GPU (NVIDIA RTX PRO 6000, 96GB) against a classical LSTM-based log anomaly detector (DeepLog), across four real, publicly available log datasets (BGL, HDFS, Thunderbird, OpenStack). We evaluate two open-weight models (Qwen2.5-14B, Mistral-Small) under three prompting strategies: zero-shot, few-shot, and retrieval-augmented generation (RAG) over a labeled incident history, reporting accuracy, precision/recall, and F1 with bootstrap 95% confidence intervals across 3 random seeds, alongside throughput and VRAM footprint. Our results show that RAG not only improves mean F1 by 0.10-0.27 over zero-shot prompting but, more importantly, substantially stabilizes model calibration: zero-shot prompting drives both models toward near-degenerate behavior (predicting "anomaly" on up to 100% of incidents on some datasets), while RAG keeps predicted-positive rates close to the true class balance in the majority of configurations. Mistral-Small achieves higher macro-averaged F1 than Qwen2.5-14B (0.644 vs. 0.560) but exhibits calibration failures in more configurations (7 vs. 5 of 12), while running at roughly half the throughput - indicating the better model choice depends on whether a deployment prioritizes peak accuracy or predictable behavior across prompting conditions. Ablations show batching scales throughput 41 times on a single card and that 4-bit quantization reduces latency 20% with no measurable accuracy loss. We release our benchmark harness, dataset splits, and evaluation code to support reproducible on-premise AIOps research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 16 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rohit Patel, Susil Kumar Mohanty, Jeenal Chaudhary
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
