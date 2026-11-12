---
title: "Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study"
description: "Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.14051) · [PDF](https://arxiv.org/pdf/2611.14051)

## 一句话摘要

Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reusing key--value (KV) caches across language model updates could avoid repeated computation of shared context, but changes in model weights raise a fundamental question about what these caches preserve. We investigate direct cache reuse across four model updates, with a detailed study of DeepSeek-V4-Flash to Flash-0731. Our central finding is that caches can retain useful task information without faithfully reproducing the updated model's behavior. Retrieval accuracy varies substantially across updates, ranging from near-native performance to large losses. With source caches already available, reuse achieves median time-to-first-token speedups of $2.10$--$5.08\times$ on three longer-prefix QA benchmarks. To characterize the behavioral differences behind these outcomes, we introduce Functional Cache Divergence, which compares next-token distributions under reused and native caches. Direct KV cache reuse better preserves native model behavior in natural-text continuation, whereas compatibility degrades with increasing prefix length in single-token retrieval tasks. Answer-margin analyses help explain how correct retrieval decisions survive substantial internal state changes. Yet even agreement on the first generated token does not ensure agreement in answer content or stopping behavior. These findings establish task utility and fidelity to native inference as distinct criteria for evaluating cross-version KV cache reuse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhikun Tao, Fangyong Jin, Junping Zhao
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
