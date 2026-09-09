---
title: "Evaluating the Scalability and Adversarial Generalization of GRPO-Trained NLI Models"
description: "Natural Language Inference (NLI) is a central task in natural language understanding with applications in fact-checking, question answering, and information retrieval."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2504.18376) · [PDF](https://arxiv.org/pdf/2504.18376)

## 一句话摘要

Natural Language Inference (NLI) is a central task in natural language understanding with applications in fact-checking, question answering, and information retrieval.

## 为什么值得关注

待编辑增强。

## 摘要原文

Natural Language Inference (NLI) is a central task in natural language understanding with applications in fact-checking, question answering, and information retrieval. Despite its importance, current NLI systems heavily rely on supervised learning with datasets that often contain annotation artifacts and biases, limiting generalization and real-world applicability. In this work, we apply a reinforcement learning-based approach using Group Relative Policy Optimization (GRPO) for Chain-of-Thought (CoT) learning in NLI, eliminating the need for human-labeled rationales and enabling this type of training on challenging datasets such as ANLI. We fine-tune 7B, 14B, and 32B language models using parameter-efficient techniques (LoRA and QLoRA), demonstrating strong performance across standard and adversarial NLI benchmarks. At the 32B scale, GRPO-trained models generalize better than other supervised baselines in adversarial sets. With AWQ quantization, the 32B model fits within 22GB of CUDA memory. This work provides a scalable and practical framework for building robust NLI systems without sacrificing inference quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pablo Miralles-Gonz\'alez, Javier Huertas-Tato, Alejandro Mart\'in, David Camacho
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
