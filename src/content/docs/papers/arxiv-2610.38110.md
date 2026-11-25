---
title: "SPARSEBLEED: Bypassing Attribute-Inference Defenses via Sparsity Optimizations"
description: "When a model trained on sensitive records is exposed through a prediction API, an attribute-inference attack (AIA) plugs each possible value of a missing field into a partially known record to infer which value belonged to the training record."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.38110) · [PDF](https://arxiv.org/pdf/2610.38110)

## 一句话摘要

When a model trained on sensitive records is exposed through a prediction API, an attribute-inference attack (AIA) plugs each possible value of a missing field into a partially known record to infer which value belonged to the training record.

## 为什么值得关注

待编辑增强。

## 摘要原文

When a model trained on sensitive records is exposed through a prediction API, an attribute-inference attack (AIA) plugs each possible value of a missing field into a partially known record to infer which value belonged to the training record. Current defenses mask confidence scores and hide internal activations. We show that sparsity optimizations, software and hardware routines (sparse kernels) that skip arithmetic and memory fetches on zero activations or weights, reopen attribute inference through the execution footprint. We introduce SparseBleed, the first hardware and execution-based AIA on training data. Training makes neuron firing selective to sensitive attributes, so each candidate value activates a different set of neurons and sparse kernels skip the rest; the candidate value therefore sets how many multiply-accumulate operations execute and which weight columns are read, shifting response time and shared-hardware contention even when only a class label is returned. SparseBleed calibrates each candidate's footprint against reference measurements for that value. Across 11 CPU and GPU sparse libraries (e.g., Intel oneDNN-AMX, NVIDIA cuSPARSE), MLPs, and FT-Transformers up to 1.5B parameters, execution time on TACO varies by up to ~25,000 timer ticks across prediction-confidence levels. The strongest SparseBleed variant gains +16.4 points in mean accuracy over label-only LOMIA and +8.9 over confidence-based CSMIA, up to +32 points over random guessing in a single query on CPU and +15 on GPU, reaches 60.5% mean AUC with 50 calibration records, and widens its margin over output-only attacks from +6.0 to +12.9 points as FT-Transformers scale from 288M to 1.5B. Response-time padding leaves co-resident channels open; thus, privacy requires equalizing executed work and memory access (4.8-13.7% overhead in our patches).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Darsh Asher, Farshad Dizani, Joshua Kalyanapu, Ro Cammarota, Aydin Aysu, Samira Mirbagher Ajorpaz
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
