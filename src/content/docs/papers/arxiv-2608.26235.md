---
title: "The Reasoning Tax: Token Economics of LLM Reasoning Across Task Types and Deployment Contexts"
description: "Accuracy-only benchmarking of reasoning-capable large language models misses a central deployment question: when do extended thinking tokens earn their cost?"
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.26235) · [PDF](https://arxiv.org/pdf/2608.26235)

## 一句话摘要

Accuracy-only benchmarking of reasoning-capable large language models misses a central deployment question: when do extended thinking tokens earn their cost?

## 为什么值得关注

待编辑增强。

## 摘要原文

Accuracy-only benchmarking of reasoning-capable large language models misses a central deployment question: when do extended thinking tokens earn their cost? We introduce the Token Economy Score (TES), a marginal benchmarking metric that measures the accuracy gain of a reasoning model over a non-reasoning baseline, normalized by the generated-token multiplier. We define paired and approximated TES variants for model families with reasoning toggles and frontier models without direct non-reasoning counterparts. We then conduct an empirical benchmarking analysis across 151 model-benchmark evaluation runs on seven benchmarks spanning mathematics, code generation, science reasoning, instruction following, expert knowledge, knowledge recall, and research-level physics. The analysis examines three deployment-facing dimensions: which task structures yield positive marginal reasoning efficiency, how increasing reasoning effort changes TES within model families, and how deployment context changes economic viability. Results show that task structure predicts reasoning efficiency better than nominal difficulty: sequential inferencechain tasks such as AIME 2025 and LiveCodeBench show high TES, while knowledge-recall tasks such as MMLU-Pro show low TES despite their difficulty. We also find systematic diminishing returns at higher reasoning effort levels, including cases where additional thinking reduces accuracy. Finally, Reasoning Cost Share (RCS) shows that inference spend is often dominated by internal thinking, while Deployment Cost Multiplier (DCM) shows how on-premises deployment can change the economics of otherwise costly reasoning workloads. These findings support a benchmarking-driven model-selection rule: enable reasoning selectively by task type, effort level, and deployment context rather than treating it as a universally beneficial mode.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sachin Gopal Wani, Ajay Dholakia, David Ellison
- 发布：2026-08-26；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
