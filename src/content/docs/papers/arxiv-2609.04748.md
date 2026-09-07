---
title: "Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving"
description: "Prefix caching, in which a serving engine reuses the key and value tensors of a shared prompt prefix across requests, is enabled by default in the major open-source stacks and treated as a transparent optimization."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.04748) · [PDF](https://arxiv.org/pdf/2609.04748)

## 一句话摘要

Prefix caching, in which a serving engine reuses the key and value tensors of a shared prompt prefix across requests, is enabled by default in the major open-source stacks and treated as a transparent optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix caching, in which a serving engine reuses the key and value tensors of a shared prompt prefix across requests, is enabled by default in the major open-source stacks and treated as a transparent optimization. We measure what it costs in reproducibility, and find that the cost rises sharply with weight quantization. Holding the model, decoding parameters, seed, and request order fixed, and issuing every request serially at batch size one, we ran an eighty-episode multi-turn agentic tool-use workload with caching enabled and disabled across two engines and four weight formats. Enabling the cache changed the agent's trajectory on 36.2 percent of episodes at 16-bit precision and on 75.0 percent at four-bit, a gradient that survives re-measurement under a controlled cache configuration. With caching disabled, repeated execution was bit-identical in every configuration, 0 of 800 episodes, which bounds other sources of nondeterminism at 0.5 percent. Repeated cache-enabled runs did diverge, and three experiments locate the cause: a single server-level prompt-cache setting moves run-to-run divergence by 37.5 percentage points, execution order acts only while that setting is active, and restoring cache state makes the cached and recompute paths each reproduce on 40 of 40 items while still differing from each other on 14. Cached serving is deterministic given cache state, and irreproducible in practice because that state is absent from the request and never reset by default. A single-turn bridge shows the divergence reaching task outcomes without shifting aggregate accuracy. We release the harness, logs, and analysis pipeline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aditi Patodiya
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
