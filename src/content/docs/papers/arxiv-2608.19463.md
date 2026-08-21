---
title: "LLM as Detector: An In-context Learning Approach for Tabular Anomaly Detection"
description: "Anomaly detection in tabular data is challenging because abnormal samples often arise as violations of cross-feature dependencies rather than simple marginal deviations."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.19463) · [PDF](https://arxiv.org/pdf/2608.19463)

## 一句话摘要

Anomaly detection in tabular data is challenging because abnormal samples often arise as violations of cross-feature dependencies rather than simple marginal deviations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Anomaly detection in tabular data is challenging because abnormal samples often arise as violations of cross-feature dependencies rather than simple marginal deviations. Existing detectors rely on geometric or reconstruction signals, while prior LLM-based approaches mainly fine-tune LLMs with normal samples or generate synthetic anomalies. We propose LLM-Detector, a framework that utilizes the in-context learning capacity of LLMs for structured, prompt-conditioned scoring synthesis, enabling LLMs to derive anomaly detection logic from structured normal-state knowledge. Specifically, normal training data are converted into statistical summaries, causal dependencies, and distilled prototypes that are organized into a prompt for code generation. The resulting scoring engine evaluates statistical deviation, structural inconsistency, and density-based abnormality then computes an anomaly score for each test sample. We evaluate LLM-Detector on 24 tabular datasets, comparing against 15 SOTA baselines. Results show consistent improvements across both mixed-type and continuous-only settings. Moreover, this design eliminates the need for LLM fine-tuning or neural network training, reducing computational cost and enabling practical anomaly detection in real-world tabular systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tu Anh Hoang Nguyen, Dang Nguyen, Thuc Duy Le, Trung Le, Sunil Gupta
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
