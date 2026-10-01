---
title: "Structure-augmented LLMs for High-Level Synthesis Pragma Optimization"
description: "Pragma insertion drives the quality of high-level synthesis (HLS) designs."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.38601) · [PDF](https://arxiv.org/pdf/2609.38601)

## 一句话摘要

Pragma insertion drives the quality of high-level synthesis (HLS) designs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pragma insertion drives the quality of high-level synthesis (HLS) designs. Choosing the right directives demands expert knowledge and reasoning about loop nesting, data dependences, and memory layout. While existing large language models (LLMs) show promise in code generation, they lack explicit program-structure awareness, limiting their ability to suggest effective pragmas. We present PRISM, a novel structure-augmented LLM that closes this gap by adding compiler-grade structural reasoning to a pretrained, frozen code LLM. It combines three hierarchical program representations, Abstract Syntax Tree (AST), Control-Flow Graph (CFG), and Data-Flow Graph (DFG), injecting them into a specific transformer layer while keeping original code tokens in a separate stream. The cross-attention gate at the injection point allows falling back to the pretrained representation when its structural signal is unhelpful. On zero-shot evaluation in HLS-Eval, PRISM synthesizes 3.5\times as many kernels as Llama3-8B (26.9\% vs. 7.7\%), and on the kernels where it does succeed, it produces designs that are 2.31\times faster (geomean) than GPT-5-mini's. In the agentic flow, the PRISM codegen outperforms other baselines when optimizing complex code and drives the average normalized improvement across the HLS-Eval suite to 26.4\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haocheng Xu, Ye Qiao, Phyo Pyae Moe Aung, Alok Mishra, Pavana Prakash, Rolando Pablo Hong Enriquez, Adam Han Wu, Zhiheng Chen, Dejan Milojicic, Sitao Huang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
