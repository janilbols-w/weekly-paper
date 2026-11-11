---
title: "MINE: Entropy-coded Memory-efficient Inference for Large Language Models"
description: "We present MINE (Memory-efficient INference Engine), a lossless entropy coding approach that accelerates single-stream inference of Large Language Models (LLMs), where existing lossless compression methods yield speedups only for specific data types such as BF16 and under additional assumptions."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.09424) · [PDF](https://arxiv.org/pdf/2611.09424)

## 一句话摘要

We present MINE (Memory-efficient INference Engine), a lossless entropy coding approach that accelerates single-stream inference of Large Language Models (LLMs), where existing lossless compression methods yield speedups only for specific data types such as BF16 and under additional assumptions.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present MINE (Memory-efficient INference Engine), a lossless entropy coding approach that accelerates single-stream inference of Large Language Models (LLMs), where existing lossless compression methods yield speedups only for specific data types such as BF16 and under additional assumptions. Single-stream decoding is strongly memory-bound, since every weight must be streamed from memory once per generated token and requests cannot be batched in local or low-latency deployments. At the core of MINE is dtANS-LLM, a GPU entropy coding scheme adapted from the prior dtANS to the needs of LLM inference. It exploits the non-uniform distribution of weights, which persists even after quantization, and exposes hyper-parameters that trade compression ratio against decoding cost. We auto-tune these parameters for each tensor and GPU to obtain the Pareto front between model size and decoding latency. MINE integrates into vLLM as a plugin and selects the best kernel configuration for a given memory budget. On Llama 3.1 8B Instruct with a 2.1-bit EntQuant checkpoint, MINE achieves speedups of 2.52x and 1.48x over the fastest baseline on an RTX 4060 Ti and an RTX 5090, at effective bitrates of 2.24 and 3.43 bits per weight. MINE is available as open source.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Emil Sch\"atzle, Markus P\"uschel
- 发布：2026-11-09；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
