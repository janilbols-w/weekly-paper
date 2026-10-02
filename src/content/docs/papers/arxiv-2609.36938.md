---
title: "Efficient Agentic LLM Serving over SSD-based Sparse KV Storage"
description: "Agentic sessions driven by Large language models (LLMs) often alternate between model inference and tool use, accumulating long histories across successive rounds."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.36938) · [PDF](https://arxiv.org/pdf/2609.36938)

## 一句话摘要

Agentic sessions driven by Large language models (LLMs) often alternate between model inference and tool use, accumulating long histories across successive rounds.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic sessions driven by Large language models (LLMs) often alternate between model inference and tool use, accumulating long histories across successive rounds. Serving these sessions efficiently requires reducing attention computation and retaining history key-value (KV) caches to avoid recomputation. Recently, frontier open-source LLMs adopt sparse attention to reduce computation by selecting only part of the history, while SSDs provide a cheaper alternative to CPU DRAM for storing KV caches. However, sparse KV selection depends on the ad hoc intermediate values during model inference, so it forces SSD reads to lie on the inference critical path. These reads are further slowed by fragmented accesses and read-write interference in SSDs. To address these challenges, we present Janus, an agentic serving framework for sparse attention LLMs with SSD-centric KV storage. Janus focuses on append prefill, which processes each round's newly added inputs and accounts for most history KV loading. To move SSD reads out of the critical path, Janus runs the model's own KV selection module on earlier intermediate values, predicting KV demand without additional training. The predicted reads overlap with model computation, and any prediction misses are fetched before attention executes to preserve model outputs. To improve SSD efficiency, Janus coalesces adjacent reads, packs scattered KV pages into sequential writes on the CPU, and limits background writes while reads are active. Across three models and three agentic traces, Janus outperforms existing works by up to 1.57-3.69 times (1.22-1.85 times on average) in terms of the time to first token latency, while maintaining decode efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Wenhao He, Ping Zhang, Xiaohe Hu, Chutian Wang, Jinlong Hou, Yuan Cheng, Peng Sun, Fangcheng Fu
- 发布：2026-09-29；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
