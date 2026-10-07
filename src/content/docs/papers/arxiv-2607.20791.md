---
title: "Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling"
description: "Recent advances in truncation-based sampling have helped mitigate drawbacks of high-temperature sampling such as neural text degeneration, thereby enabling greater diversity without sacrificing coherence."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.20791) · [PDF](https://arxiv.org/pdf/2607.20791)

## 一句话摘要

Recent advances in truncation-based sampling have helped mitigate drawbacks of high-temperature sampling such as neural text degeneration, thereby enabling greater diversity without sacrificing coherence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in truncation-based sampling have helped mitigate drawbacks of high-temperature sampling such as neural text degeneration, thereby enabling greater diversity without sacrificing coherence. However, increasing the entropy of the token probability distribution via high temperatures has also been shown to weaken the model's refusal response. Existing solutions for maintaining the refusal behavior of LLMs either replace the model's own refusal decision with a separate safety classifier or alter its output distribution for every prompt. To address this gap, we propose refusal-gated decoding (RGD): an efficient sequential decoding approach which preserves a model's greedy decoding refusal response at high temperatures and samples all other prompts from its exact direct high-temperature distribution, while incurring minimal additional latency. RGD runs a short greedy probe that reuses the prompt's KV cache and exits as soon as it becomes incompatible with a learned set of refusal prefixes; it returns the greedy response if the probe remains compatible and otherwise discards the probe and samples from the original prompt. Across seven models and three benchmark datasets at T=2.0, RGD raises greedy-refusal preservation from 91.9% under direct sampling to 98.3% on average while adding only 2.2-4.3% to the median per-request latency of non-refusals across temperatures. Unlike prompt-screening baselines which route many greedy non-refusals to greedy decoding, RGD keeps at least 98.1% of greedy non-refusals on unchanged high-temperature sampling, thereby preserving the model's natural high-temperature sampling behavior. We also propose a residual-stream variant of our method which lowers this latency overhead to at most 0.5% with comparable prompt routing accuracy. Our work shows that unlocking greater diversity via high-temperature sampling need not erode a model's refusal behavior.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Phillip Howard, Xin Su, Allen Roush, Manikandan Ravikiran, Runyan Tan, Amir Abdullah
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
