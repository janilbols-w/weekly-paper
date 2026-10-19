---
title: "Prune the Leaky Neurons: Mitigating Private Data Leakage in Fine-Tuned LLMs via Joint-Embedding-Guided Pruning"
description: "Fine-tuning large language models (LLMs) on proprietary records enables domain adaptation but introduces two challenges: (i) privacy leakage of memorized private data, such as personally identifiable information (PII), and (ii) balancing private data removal with utility preservation."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.22792) · [PDF](https://arxiv.org/pdf/2610.22792)

## 一句话摘要

Fine-tuning large language models (LLMs) on proprietary records enables domain adaptation but introduces two challenges: (i) privacy leakage of memorized private data, such as personally identifiable information (PII), and (ii) balancing private data removal with utility preservation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuning large language models (LLMs) on proprietary records enables domain adaptation but introduces two challenges: (i) privacy leakage of memorized private data, such as personally identifiable information (PII), and (ii) balancing private data removal with utility preservation. Existing defenses, including data sanitization and differential privacy, often degrade performance, while privacy-neuron editing lacks a PII-free reference to distinguish identity-specific neurons from those supporting useful text. We propose JEPA-Prune, a post-hoc neuron pruning framework guided by a model trained exclusively on PII-free views. Alongside the fine-tuned private model, JEPA-Prune, trains a public model on surrogate and masked views of the same records using a joint-embedding predictive architecture (JEPA), capturing domain knowledge without identifiers. A cross-model representation probe quantifies deviations between private representations of leaked records and this PII-free reference. Integrated gradients and a scale-invariant specificity score then identify PII-responsive neurons, which are pruned without retraining. Experiments show that pruning just 1.6% of neurons reduces PII inference accuracy by up to 7.4x and PII extraction recall by up to 13.9x, while keeping unseen-text perplexity within 16% of that of the unpruned model for most LLMs. In contrast, privacy-neuron editing increases perplexity by at least 26x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mohamed Shaaban, Mohamed Elmahallawy
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
