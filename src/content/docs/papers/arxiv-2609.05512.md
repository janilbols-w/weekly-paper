---
title: "Reasoning-Aware Compression: Identifying and Protecting Vulnerable Reasoning Circuits for Energy-Efficient LLM Deployment"
description: "Large Reasoning Models (LRMs) impose substantial energy costs during deployment, yet current compression methods apply uniform quantization across all components, risking damage to critical reasoning circuits."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.05512) · [PDF](https://arxiv.org/pdf/2609.05512)

## 一句话摘要

Large Reasoning Models (LRMs) impose substantial energy costs during deployment, yet current compression methods apply uniform quantization across all components, risking damage to critical reasoning circuits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Reasoning Models (LRMs) impose substantial energy costs during deployment, yet current compression methods apply uniform quantization across all components, risking damage to critical reasoning circuits. We present a reasoning-aware compression framework that benchmarks quantization conditions across five reasoning benchmarks, GSM8K, FOLIO, MATH-500, ProofWriter, and MuSiQue, with hardware-level GPU energy measurement; profiles per-module INT4 vulnerability across all 196-224 (layer, projection) pairs via a perturbation sweep on a held-out calibration split, then selectively restores the most sensitive circuits to FP16. Three findings emerge. First, INT4 quantization can increase energy by extending reasoning chains; a 25% power reduction becomes a net energy increase on GSM8K. Second, vulnerability is task-dependent: attention projections are more critical for mathematical reasoning, and sensitivity patterns differ by architecture in logical inference. Third, selective compression achieves Pareto-optimal points inaccessible to uniform methods: R1-Qwen-7B Top-10% on ProofWriter gains +12 pp over FP16 at -9.7% energy, validated on held-out data across five reasoning benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leonard Twagirayezu, Prasenjit Mitra
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
