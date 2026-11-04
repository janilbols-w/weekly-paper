---
title: "Beyond Accuracy: How Quantization Affects Coding Agents"
description: "Agents are increasingly used for coding tasks, but the inference cost of large language models (LLMs) limits where they can run."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.02368) · [PDF](https://arxiv.org/pdf/2611.02368)

## 一句话摘要

Agents are increasingly used for coding tasks, but the inference cost of large language models (LLMs) limits where they can run.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agents are increasingly used for coding tasks, but the inference cost of large language models (LLMs) limits where they can run. Quantization reduces model size, but its effects on coding agents that execute and revise programs remain underexplored. We compare BF16 with 4-bit AWQ and GPTQ for Qwen2.5-Coder-Instruct (7B, 14B, and 32B) and Devstral-Small-2507 (24B) on OJBench coding problems across three seeds. We detect no statistically significant accuracy loss for any of the coding agents. However, final accuracy can conceal substantial behavioral changes: AWQ reduces Qwen-7B one-shot solves from 17 to 0 while increasing loop-based solves from 10 to 25. All Qwen-32B successes involve tool use, whereas Devstral rarely makes a valid executor call. Failure profiles also differ: Qwen-32B produces far more compilation errors than the smaller Qwen models, rising slightly under quantization, while Devstral's failures shift significantly from runtime errors toward wrong answers and timeouts. These findings indicate that quantization robustness in coding agents should be assessed through solution trajectories, tool use, and failure modes, in addition to final accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer, Hamza Farooq
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
