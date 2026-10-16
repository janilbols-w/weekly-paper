---
title: "Think Before You Speak: Enabling Training-Free Latent Communication Between Language Models"
description: "Large language models (LLMs) have demonstrated remarkable capabilities in solving complex tasks in coding, mathematical logic, and iterative reasoning, especially by coordinating effectively within multi-agent systems (MAS)."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.16165v1) · [PDF](https://arxiv.org/pdf/2610.16165v1)

## 一句话摘要

Large language models (LLMs) have demonstrated remarkable capabilities in solving complex tasks in coding, mathematical logic, and iterative reasoning, especially by coordinating effectively within multi-agent systems (MAS).

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated remarkable capabilities in solving complex tasks in coding, mathematical logic, and iterative reasoning, especially by coordinating effectively within multi-agent systems (MAS). However, language agents traditionally communicate via text exchange, which introduces a bottleneck in information transfer and adds prefill latency for downstream agents. Recent work proposes that directly sharing the key-value (KV) cache between language models can enable efficient latent collaboration, entirely bypassing standard text-based communication. To enable latent communication between heterogeneous models of different sizes, prior work introduces trained fusion adapters for each model pair, which limits practical deployment. We introduce CacheFuse, a training-free method which demonstrates that augmenting a downstream model with an upstream model's KV cache using linear interpolation consistently enables superior performance than the standalone downstream model can achieve. We systematically analyze CacheFuse across four reasoning and knowledge benchmarks and demonstrate up to 8.6 percentage points higher accuracy compared to single-model baselines and up to 12.2x TTFT speedup compared to text-based communication in multi-model inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rishi Khare
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
