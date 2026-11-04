---
title: "Mixture-of-Models: Distributed Inference over Heterogeneous LLMs as Model-Level Mixture-of-Experts"
description: "Switch Transformers scale MoE model capacity by routing tokens in memory for one jointly trained model, requiring high-bandwidth interconnects, large memory, centralised ownership, and lack scalable composability."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2601.16863) · [PDF](https://arxiv.org/pdf/2601.16863)

## 一句话摘要

Switch Transformers scale MoE model capacity by routing tokens in memory for one jointly trained model, requiring high-bandwidth interconnects, large memory, centralised ownership, and lack scalable composability.

## 为什么值得关注

待编辑增强。

## 摘要原文

Switch Transformers scale MoE model capacity by routing tokens in memory for one jointly trained model, requiring high-bandwidth interconnects, large memory, centralised ownership, and lack scalable composability. We propose Mixture-of-Models (MoM) architecture as Switch Transformer scaling to semantic level which composes inference across independently trained distributed LLMs, each run on its own GPU. The models reach joint consensus using N-Way Self-Evaluating Deliberation protocol: a combination of social-choice methods such as Delphi method and Quadratic Voting as well as Inference-Time scaling paradigm. We start with an empirical model that characterizes consensus as an inference-time trade-off between signal extraction and contextual noise accumulation, establishing a mathematical basis for convergence driven inference stopping strategies. We show experimental results where ensemble of smaller (<21B) models matches closely 120B MoE (GPT-OSS-120B) on AIME 2025 while larger ensemble of open-weight models reaches 90.0%, close to proprietary models at time of writing.

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

- taxonomy keywords: distributed inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tims Pecerskis, Aivars Smirnovs
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
