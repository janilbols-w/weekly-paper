---
title: "Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped Transformer Memory Overhead"
description: "Nanbeige4.2-3B is a 3B-parameter agentic model built around a Looped Transformer (LT) that reuses one stack of layers for a second forward pass, adding effective depth without additional parameters."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.13987) · [PDF](https://arxiv.org/pdf/2608.13987)

## 一句话摘要

Nanbeige4.2-3B is a 3B-parameter agentic model built around a Looped Transformer (LT) that reuses one stack of layers for a second forward pass, adding effective depth without additional parameters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Nanbeige4.2-3B is a 3B-parameter agentic model built around a Looped Transformer (LT) that reuses one stack of layers for a second forward pass, adding effective depth without additional parameters. Evaluated on Apple Silicon (MPS), we identify five independent bugs which prevent the released checkpoint from running via Hugging Face transformers out of the box (including a silently-zeroed RoPE buffer and calls to removed transformers cache APIs). Furthermore, we show that fixing these bugs is still not sufficient for agentic tasks, due to the LT's layer-reuse strategy (which effectively doubles peak attention memory) used to achieve parameter efficiency. We thus introduce a chunked-prefill strategy which alleviates the incurred memory-capacity penalty, extending allowable context width by $2.7 \times$ on 32~GiB shared memory. However, even with the reduced memory overhead, we show that patches are required to render Nanbeige4.2-3B usable; resolving both system prompt and MPS-native memory bugs finally allows reliable evaluation on standard MCP and tool-calling benchmarks. On a subset of MCPMark, the debugged model completes up to 30\% of real agentic tasks (up from the original's 0\%), while, on BFCL, it is near-perfect at single tool calls (yet fails the majority of multi-tool tests). We release the patched checkpoint, system prompt optimizer, and evaluation harnesses at https://github.com/johnhalloran321/Nanbeige4.2-3B-mps-fix.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：John T. Halloran
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/johnhalloran321/Nanbeige4.2-3B-mps-fix](https://github.com/johnhalloran321/Nanbeige4.2-3B-mps-fix)
- 阅读深度：metadata
