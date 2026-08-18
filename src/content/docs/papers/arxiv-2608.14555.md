---
title: "Discovering KV Cache Eviction Policies via LLM-Guided Program Evolution"
description: "KV cache compression is critical for long-context inference, yet effective eviction policies remain difficult to design: existing prefill-stage methods often rely on hand-crafted salience heuristics that can be brittle across models, context lengths, and compression ratios."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.14555) · [PDF](https://arxiv.org/pdf/2608.14555)

## 一句话摘要

KV cache compression is critical for long-context inference, yet effective eviction policies remain difficult to design: existing prefill-stage methods often rely on hand-crafted salience heuristics that can be brittle across models, context lengths, and compression ratios.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache compression is critical for long-context inference, yet effective eviction policies remain difficult to design: existing prefill-stage methods often rely on hand-crafted salience heuristics that can be brittle across models, context lengths, and compression ratios. We present CacheCraft, a program-evolution methodology for automatically discovering KV cache eviction policies using an LLM-guided code-evolution engine. CacheCraft discovers FRC (Feature-Rich Compression), a fixed-weight three-signal scorer that combines local attention received, neighborhood attention density, and KV-head maximum salience with chunk-level top-k selection. Without per-model retuning, FRC ranks first among the evaluated single-pass KVPress baselines at every RULER 4k/8k cell with r >= 0.75 across Llama-3.1-8B-Instruct and Qwen3-8B (12 of 20 grid cells), gaining +15.4 points on Llama-4k and +13.9 points on Qwen-8k at 88% compression. A scorer-versus-structure decomposition shows that the scoring family, not chunk selection, is the load-bearing design choice: incorporating the scorer contributes +67.2 RULER points, while improving chunk structure contributes only ~0.1. Beyond FRC itself, CacheCraft provides a transferable recipe for automated eviction-policy discovery: a compact policy interface, a cascade evaluator with strict output invariants, and a diagnostic loop that treats search plateaus and reward-hacking failures as evidence for reformulating the editable interface.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pratik Poudel, Yanzhao Wu, Sumit Jha, Jason Liu
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
