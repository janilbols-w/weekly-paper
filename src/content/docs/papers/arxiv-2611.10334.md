---
title: "Reproducible LoRA Inference Through Deterministic Split-K Reduction"
description: "Reproducibility is important for LoRA-adapted language models used in repeated evaluation, auditing, and decision-making."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.10334) · [PDF](https://arxiv.org/pdf/2611.10334)

## 一句话摘要

Reproducibility is important for LoRA-adapted language models used in repeated evaluation, auditing, and decision-making.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reproducibility is important for LoRA-adapted language models used in repeated evaluation, auditing, and decision-making. However, Split-K kernels used to introduce parallelism in low-rank LoRA multiplications can have the unintended consequence of numerical nondeterminism when partial results are combined using floating-point atomic additions. We investigate this non-determinism in vLLM across GSM8K mathematical reasoning, MBPP code generation, and Jev-style structured toxicity decisions on Civil Comments and introduce a deterministic Triton Split-K implementation. Under identical-input replay, Atomic Split-K=8 produces different FP32 shrink outputs in 97.61% of comparisons, while our Deterministic Split-K=8 shows no observed variation. Repeated atomic inference changes generated outputs in 17.30% of GSM8K and 14.96% of MBPP comparisons, sometimes altering task correctness. Structured-decision probabilities vary in 81.47% of atomic comparisons, with decision flips. Controlled tracing demonstrates how shrink-output differences propagate into the KV cache and how accumulated cache differences can change token decisions and final answers. Our deterministic Triton Split-K=8 implementation preserves parallelism, achieving 16.8-21.1% latency-based speedup over unsplit reduction with only 1.02-2.62% additional latency relative to Atomic Split-K=8.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dhayaneshwar Balusamy, Ankur Mohan
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
