---
title: "SEER: Self-Enhancing Chain-of-Thought Compression for Reasoning Models"
description: "Chain-of-Thought (CoT) prompting can substantially improve the reasoning ability of large language models (LLMs), but it often comes with high inference cost due to long and poorly controlled reasoning traces."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2509.14093) · [PDF](https://arxiv.org/pdf/2509.14093)

## 一句话摘要

Chain-of-Thought (CoT) prompting can substantially improve the reasoning ability of large language models (LLMs), but it often comes with high inference cost due to long and poorly controlled reasoning traces.

## 为什么值得关注

待编辑增强。

## 摘要原文

Chain-of-Thought (CoT) prompting can substantially improve the reasoning ability of large language models (LLMs), but it often comes with high inference cost due to long and poorly controlled reasoning traces. This overhead is particularly problematic in software engineering tasks (e.g., code generation), where both latency and output reliability matter. To better understand this trade-off, we conduct an empirical study on widely used code generation benchmarks and observe that many modern reasoning models produce excessively verbose CoTs (often thousands of tokens), which frequently leads to truncation and unstable generation. Using a strict n-gram repetition detector, we find that most observed truncations are associated with degenerate looping behaviors. In addition, a HumanEval/129 case study shows that failed generations can be longer than successful ones, suggesting limited returns from overlong reasoning. Motivated by these findings, we propose SEER (Self-Enhancing Efficient Reasoning), a self-enhancing framework for adaptive CoT compression. SEER improves the conciseness of reasoning while preserving output quality, without relying on external compression tools. SEER refines self-generated CoT data via Best-of-N sampling to suppress looping and redundant traces, then applies a lightweight, data-driven filter to encourage concise yet correct reasoning. It then fine-tunes the model on the filtered data to internalize concise reasoning behaviors. Across four software engineering benchmarks on the evaluated DeepSeek-R1-Distill-Qwen-7B backbone, SEER reduces CoT length by 34.6% on average while improving task performance, with reduced truncation and fewer reasoning loops.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kerui Huang, Shuhan Liu, Xing Hu, Tongtong Xu, Lingfeng Bao, Xin Xia
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
