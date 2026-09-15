---
title: "An Efficient and Modular Framework for Targeted Harm Mitigation in LLMS"
description: "Large Language Models (LLMs) are powerful zero-shot learners but remain prone to misalignment with human preferences, often producing biased, toxic, or otherwise harmful outputs."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.13624) · [PDF](https://arxiv.org/pdf/2609.13624)

## 一句话摘要

Large Language Models (LLMs) are powerful zero-shot learners but remain prone to misalignment with human preferences, often producing biased, toxic, or otherwise harmful outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are powerful zero-shot learners but remain prone to misalignment with human preferences, often producing biased, toxic, or otherwise harmful outputs. Existing alignment methods, while effective, are costly and tightly coupled to the model, limiting flexibility and scalability. We propose a modular correction framework that augments pretrained LLMs with Activated LoRA (aLoRA) adapters and a context-aware routing mechanism to eliminate harms from misaligned model responses. Our approach enables expert adapters to activate mid-sequence without invalidating the KV cache, allowing low-latency, targeted correction during generation. Each expert is trained to detect and mitigate specific harms, such as bias or toxicity. A learned router dynamically selects appropriate experts based on the models intermediate outputs. We demonstrate that our system improves alignment on standard safety benchmarks while preserving task performance, offering a lightweight and efficient path toward safer and more controllable LLM deployments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Roberto Campbell, Momin Abbass, Muneeza Azmat, Michal Ulewicz, Raya Horesh, Kristjan Greenewald, Rog\'erio Abreu de Paula, Nathalie Baracaldo
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
