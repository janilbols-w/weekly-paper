---
title: "Swarm Telepathy: Prefill-Free KV-Cache Transfer Across Families"
description: "LLM multi-agent systems split work across agents that communicate through text."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.15095v1) · [PDF](https://arxiv.org/pdf/2610.15095v1)

## 一句话摘要

LLM multi-agent systems split work across agents that communicate through text.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM multi-agent systems split work across agents that communicate through text. An agent summarizes its findings, another agent receives the text. This constrains communication to discrete tokens and costs redundant compute, limiting bandwidth and capabilities of multi-agent systems. Recent works demonstrate KV-cache transfer between LLMs but they either require the LLMs to be within the same family or cannot function across context, thus requiring the receiver to prefill text. We present SwaT (Swarm Telepathy), the first cross-family KV-cache transfer method that allows prefill-free communication in multi-family multi-agent systems. In an agent-to-agent communication setting, combining SwaT with recent advances in KV-cache compaction beats text-to-text communication in both accuracy and speed, with a mean of $40\%$ higher accuracy and a mean of $4\times$ faster wall-clock time. Experiments show SwaT achieves high performance on 17 benchmarks across 12 LLMs and 6 families. Additionally, given a sender Vision-Language Model (VLM), SwaT is able to transfer the vision capabilities to a text-only receiver LLM exceeding text-to-text communication despite SwaT being trained on text-only data. SwaT keeps both sender and receiver models frozen without fine-tuning and only requires $<50M$ tokens and $<1$ GPU-day to train.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Abdulrahman Alabdulkareem, Irene Tenison, Yang Zhang, Yada Zhu, Boris Katz, Dan Gutfreund
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
