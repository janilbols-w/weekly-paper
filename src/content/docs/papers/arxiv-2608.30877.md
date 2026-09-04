---
title: "Deploying DeepSeek 175B Locally on a Single Consumer-Grade RTX 4060 Laptop with 32GB RAM for 200k-Scale Protein-Ligand Virtual Screening"
description: "Recent advances in large language models (LLMs) have demonstrated exceptional performance in protein-ligand interaction prediction, but state-of-the-art pipelines for large-scale virtual screening almost exclusively rely on high-end GPU clusters with hundreds of gigabytes of memory, creating prohibitive hardware barriers for small academic teams."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.30877) · [PDF](https://arxiv.org/pdf/2608.30877)

## 一句话摘要

Recent advances in large language models (LLMs) have demonstrated exceptional performance in protein-ligand interaction prediction, but state-of-the-art pipelines for large-scale virtual screening almost exclusively rely on high-end GPU clusters with hundreds of gigabytes of memory, creating prohibitive hardware barriers for small academic teams.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in large language models (LLMs) have demonstrated exceptional performance in protein-ligand interaction prediction, but state-of-the-art pipelines for large-scale virtual screening almost exclusively rely on high-end GPU clusters with hundreds of gigabytes of memory, creating prohibitive hardware barriers for small academic teams. In this work, we present a fully local low-resource framework that deploys the 175-billion-parameter DeepSeek 175B LLM on a single consumer-grade RTX 4060 laptop equipped with 32GB system RAM and 8GB VRAM, completing a full 200k-scale protein-ligand virtual screening workflow across 20 distinct protein targets. Our implementation achieves 100x throughput of an 8-card A100 cluster baseline under identical task configurations within 72 hours, with an average binding affinity prediction error of 0.88 kcal/mol across all targets, satisfying the 1.0 kcal/mol chemical accuracy requirement for preclinical drug discovery. Systematic runtime profiling reveals that heterogeneous memory management overhead accounts for 72% of total execution time, while accuracy loss introduced by model optimization contributes less than 10% to total prediction error. This work validates the engineering feasibility of running industrial-scale trillion-parameter LLM-driven biomedical computing tasks on consumer hardware, establishing a new low-barrier paradigm for AI-powered early stage drug discovery.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rui Xiao, Yili Xu
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
