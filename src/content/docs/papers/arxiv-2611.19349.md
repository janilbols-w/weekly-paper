---
title: "SMELL: Sparsity-aware Memory Efficient Federated Fine-tuning for Long-context LLMs"
description: "Federated fine-tuning enables Large Language Models (LLMs) to collaboratively adapt to distributed private data."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.19349) · [PDF](https://arxiv.org/pdf/2611.19349)

## 一句话摘要

Federated fine-tuning enables Large Language Models (LLMs) to collaboratively adapt to distributed private data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Federated fine-tuning enables Large Language Models (LLMs) to collaboratively adapt to distributed private data. However, long-context fine-tuning on resource-constrained devices faces substantial challenges arising from excessive activation memory, heterogeneous token-importance patterns across clients, and communication overhead. To address these challenges, we propose SMELL, a Sparsity-aware and Memory-Efficient federated fine-tuning framework for Long-context LLMs. SMELL integrates three complementary mechanisms: Local Sparse-Forward Adaptation (LSFA), Consensus-Anchored Sparsity Coordination (CASC), and Communication-Efficient Progressive Update Recovery (CPUR). These mechanisms jointly enable memory-efficient local adaptation, heterogeneity-aware sparsity coordination, and lightweight model-update transmission. Experiments on OPT-350M and LLaMA2-7B demonstrate that SMELL reduces peak memory consumption by up to 88.35% compared with conventional fine-tuning and 13.25% compared with forward-only LoRA fine-tuning at a 16K context length. Furthermore, SMELL improves fine-tuning performance under certain non-IID settings and supports compact update transmission with progressive reconstruction, demonstrating its potential for resource-efficient federated long-context LLM adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yin Xu, Yongbo Yang, He Sun, Miao Sun, Mingjun Xiao
- 发布：2026-11-14；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
