---
title: "LLM Agents Factory: Retrieval of Domain-Specific LLM Agents"
description: "Large language model (LLM) agents improve task performance by decomposing problems into role-specialized behaviors."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.09934) · [PDF](https://arxiv.org/pdf/2608.09934)

## 一句话摘要

Large language model (LLM) agents improve task performance by decomposing problems into role-specialized behaviors.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents improve task performance by decomposing problems into role-specialized behaviors. However, their practical deployment is often limited by the computational cost and instability associated with the on-the-fly agent design for each user request. To address this, we present LLM Agents Factory, a retrieval-based framework that constructs domain-specific and Wikipedia-grounded agents on demand using a base of over 20K predetermined agent profiles. Our framework supports two modes: (1) agent profile retrieval via semantic search and (2) distillation into a compact model fine-tuned for direct agent generation. Experiments on MMLU, BIG-bench, and BIG-bench Hard in a single-agent scenario demonstrate that our retrieval-based agent construction surpasses non-agent baselines in accuracy while matching AutoGen generation quality with a 120B backbone at a substantially lower inference cost. Our work reveals that retrieval from a structured agent repository provides a cost-efficient, accurate, and controllable alternative to dynamic agent generation, responding to the strict demands of industrial applications. We provide the implementation code and the agent base in https://huggingface.co/frontier-ai/llm-agent-factory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vitalii Belov, Artyom Sosedka, Andrey Sakhovskiy, Elizaveta Kovtun, Artyom Boyarskikh, Semen Budennyy
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
