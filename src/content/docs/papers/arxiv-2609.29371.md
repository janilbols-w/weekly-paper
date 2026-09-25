---
title: "BanglaTurn: A Benchmark and Whisper-Based Model for End-of-Turn Detection in Bangla Speech"
description: "This paper presents BanglaTurn, a corpus for end-of-turn detection in Bangla conversational speech, and a model trained on it."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.29371) · [PDF](https://arxiv.org/pdf/2609.29371)

## 一句话摘要

This paper presents BanglaTurn, a corpus for end-of-turn detection in Bangla conversational speech, and a model trained on it.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper presents BanglaTurn, a corpus for end-of-turn detection in Bangla conversational speech, and a model trained on it. The corpus holds 35,374 samples of 3 to 15 s of podcast speech, labelled for turn state by combining speaker diarization with an LLM pass, with every label then checked by a human annotator. The model pairs a Whisper encoder with task-specific classification heads. On a class-balanced test set drawn from a held-out podcast, it reaches 84.33% accuracy (95% CI 80.3 to 88.1) against 69.28% for the Smart-Turn v3 baseline, and lowers the false negative rate from 51.57% to 7.55% at the cost of a higher false positive rate. We report what encoder layer fine-tuning, multi-scale pooling and INT8 quantization each contribute, and latency stays within 165 to 191 ms end to end on CPU.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mizbaul Haque Maruf
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
