---
title: "SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving"
description: "Hybrid models combine softmax attention with linear attention, which compresses history into fixed-size recurrent states to balance model quality and inference efficiency."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.14246) · [PDF](https://arxiv.org/pdf/2611.14246)

## 一句话摘要

Hybrid models combine softmax attention with linear attention, which compresses history into fixed-size recurrent states to balance model quality and inference efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid models combine softmax attention with linear attention, which compresses history into fixed-size recurrent states to balance model quality and inference efficiency. However, linear attention has not pushed this compression to its limit: we find that the queries, keys, and values of linear layers concentrate in a stable, low-dimensional subspace, a phenomenon we call the linear attention sink, so each state is effectively low-rank, with a rank that varies across states. Yet existing serving systems keep these redundant states dense, reading and rewriting them in full at every decoding step, so their memory traffic grows with the batch size and dominates the decoding cost. Thus SinkState stores each recurrent state in an adaptive low-rank form throughout inference with buffered updates and a local SVD restricted to the top subspace. SinkState further consolidates the remaining components asynchronously on the CPU. On four hybrid models with Mamba-2 and Gated DeltaNet (GDN) layers, from 4B to 120B parameters, SinkState reduces the peak memory of recurrent states by up to 2.6x (1.9x on average) and speeds up decoding by up to 1.58x (1.25x on average) over Mamba-SSM and FLA, while maintaining accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haolin Jiang, Weihang Li, Zhongzhu Zhou, Jinwen Pan, Santosh Pandey, Hang Liu
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
