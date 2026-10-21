---
title: "SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models"
description: "Speculative Decoding (SD) has demonstrated its efficacy in accelerating large language model inference, but for Vision-Language Models (VLMs), the diverse input modalities make it difficult for a small trained drafter to achieve consistently high throughput."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.18735) · [PDF](https://arxiv.org/pdf/2610.18735)

## 一句话摘要

Speculative Decoding (SD) has demonstrated its efficacy in accelerating large language model inference, but for Vision-Language Models (VLMs), the diverse input modalities make it difficult for a small trained drafter to achieve consistently high throughput.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative Decoding (SD) has demonstrated its efficacy in accelerating large language model inference, but for Vision-Language Models (VLMs), the diverse input modalities make it difficult for a small trained drafter to achieve consistently high throughput. Self-speculative decoding reuses parts of the target model as a drafter which retains the multi-modal capability of the VLMs, yet its efficiency depends on choosing a suitable draft configuration for each prompt. We propose Single-Peak SPeculative decoding (SP$^2$ec), a training-free bandit algorithm that adapts the draft configuration during generation. SP$^2$ec exploits the single-peak throughput pattern observed in existing self-speculative methods, including SWIFT, KnapSpec, SpecVLM, and our simple cosSim. Our algorithmic design explicitly minimizes a novel notion of wall-time regret for each given query, corresponding to the empirical wall-time latency. Theoretical guarantees on the wall-time regret show that SP$^2$ec can exploit the optimal draft configuration, with negligible exploration cost. Extensive experiments on Qwen2.5-VL-7B-Instruct and LLaVA-NeXT-Mistral-7B across visual and textual tasks show consistent improvements of up to 11% over the original self-speculative methods, demonstrating the wide applicability of the proposed SP$^2$ec algorithm.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuqi Huang, Xingyao Li, Yunlong Hou, Fengzhuo Zhang, Jiachun Pan, Vincent Y. F. Tan
- 发布：2026-10-13；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
