---
title: "TriCalRAG: A Three-Strategy, Retrieval-Augmented Benchmark for On-Premise LLM-Based Root Cause Analysis in AIOps"
description: "Operational logs create a need for private, resource-efficient incident analysis, but aggregate detection scores can conceal severe prediction bias."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.14762) · [PDF](https://arxiv.org/pdf/2609.14762)

## 一句话摘要

Operational logs create a need for private, resource-efficient incident analysis, but aggregate detection scores can conceal severe prediction bias.

## 为什么值得关注

待编辑增强。

## 摘要原文

Operational logs create a need for private, resource-efficient incident analysis, but aggregate detection scores can conceal severe prediction bias. We present TriCalRAG, a reproducible benchmark for log-anomaly detection with generated root-cause and remediation outputs across BGL, HDFS, Thunderbird, and OpenStack. The primary evaluation compares Qwen2.5-14B and Mistral-Small-22B, served through vLLM on one NVIDIA RTX PRO 6000 GPU (96 GB), under zero-shot, few-shot, and retrieval-augmented generation (RAG) prompting across three data-sampling seeds. We report F1, bootstrap confidence intervals, predicted-positive rates, throughput, and memory use, with DeepLog as a held-out classical baseline. Mistral-Small attains a higher macro-averaged F1 than Qwen2.5-14B (0.644 versus 0.560), whereas Qwen provides approximately twice the throughput. A separate log-probability evaluation compares raw decisions with Contextual Calibration (CC) and Batch Calibration (BC): neither correction consistently improves prediction-balance diagnostics across prompting strategies. Supplementary single-run comparisons extend evaluation to 4-bit Llama-3.1-70B via local Ollama and Claude Haiku 4.5 via Anthropic's cloud API; RAG improves F1 on all four datasets for both models. Claude's reported aggregate F1 increases from 0.566 to 0.695, while the estimated API cost rises from \$0.94 to \$2.15 per 1,000 incidents. Local deployment ablations show approximately 41-fold throughput scaling with batching and 20% lower latency with 4-bit quantization on the tested workload. These findings support retrieval as useful context for anomaly decisions, while the supplementary protocols, unvalidated explanation quality, and prediction-balance diagnostics limit broader claims about RCA accuracy and probabilistic calibration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 17 |
| practical impact | 13 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rohit Patel, Susil Kumar Mohanty, Jeenal Chaudhary
- 发布：2026-09-13；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
