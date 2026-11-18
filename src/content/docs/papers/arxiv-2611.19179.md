---
title: "Isolating Perception for Multi-View Planning under Occlusion-Induced Partial Observability"
description: "Vision-language models (VLMs) are beginning to saturate visual planning benchmarks, yet they fail to resolve depth ambiguity and degrade sharply with problem size under occlusion-induced partial observability (PO)."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2611.19179) · [PDF](https://arxiv.org/pdf/2611.19179)

## 一句话摘要

Vision-language models (VLMs) are beginning to saturate visual planning benchmarks, yet they fail to resolve depth ambiguity and degrade sharply with problem size under occlusion-induced partial observability (PO).

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) are beginning to saturate visual planning benchmarks, yet they fail to resolve depth ambiguity and degrade sharply with problem size under occlusion-induced partial observability (PO). We introduce BW-PO based on the Blocksworld domain, a controlled benchmark that reduces existing VLM planners and formalizers to near-zero performance, and propose VLM-as-perceiver, a paradigm that narrows the VLM's role to local perception while delegating cross-view evidence reconciliation and plan generation to external solvers. Across model-specific challenging subsets of BW-PO, this raises plan success from 1% to 97% for Gemma-4-31B, 0% to 95% for Qwen3.5-122B-A10B, and 3% to 84% for Gemini-3.1-Pro. Isolating perception in this way separates two bottlenecks that are otherwise entangled: reconciliation under depth ambiguity, and completeness of visual extraction under scene density.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kevin Nguyen, Ceyhun Efe Kayan, Feng Liu, Li Zhang
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
