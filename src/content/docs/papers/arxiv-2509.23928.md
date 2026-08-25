---
title: "HiViS: Hiding Visual Tokens from the Drafter for Speculative Decoding in Vision-Language Models"
description: "Speculative decoding has proven effective for accelerating inference in Large Language Models (LLMs), yet its extension to Vision-Language Models (VLMs) remains limited by the computational burden and semantic inconsistency introduced by visual tokens."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2509.23928) · [PDF](https://arxiv.org/pdf/2509.23928)

## 一句话摘要

Speculative decoding has proven effective for accelerating inference in Large Language Models (LLMs), yet its extension to Vision-Language Models (VLMs) remains limited by the computational burden and semantic inconsistency introduced by visual tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding has proven effective for accelerating inference in Large Language Models (LLMs), yet its extension to Vision-Language Models (VLMs) remains limited by the computational burden and semantic inconsistency introduced by visual tokens. Recent studies reveal that visual tokens in large VLMs are highly redundant, and most of them can be removed without compromising generation quality. Motivated by this observation, we propose HiViS (Hiding Visual Tokens from the Drafter for Speculative Decoding in Vision-Language Models), a framework that utilizes the target VLM as a semantic fusion model, allowing the drafter to obtain visual information without explicitly processing visual tokens, ensuring that the drafter's prefill sequence length matches that of the textual tokens. Furthermore, HiViS employs a time-step-aware aligned training scheme that allows the drafter to autonomously propagate and refine instructive visual-textual semantics during independent drafting, guided by step-dependent bias-correction residuals. Extensive experiments across representative VLMs and benchmarks demonstrate that HiViS achieves significant improvements in average acceptance length and speedup ratio.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhinan Xie, Peisong Wang, Shuang Qiu, Jian Cheng
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
