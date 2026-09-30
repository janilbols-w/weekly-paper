---
title: "When Keywords Drop but Classifiers Hold: Soft Refusals under KV Cache Compression"
description: "KV cache compression is widely used for long context LLM inference under memory constraints, while deployed systems typically score refusals after generation with keyword filters or learned classifiers."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.31678) · [PDF](https://arxiv.org/pdf/2609.31678)

## 一句话摘要

KV cache compression is widely used for long context LLM inference under memory constraints, while deployed systems typically score refusals after generation with keyword filters or learned classifiers.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache compression is widely used for long context LLM inference under memory constraints, while deployed systems typically score refusals after generation with keyword filters or learned classifiers. Such monitors are intended to indicate whether a model declined a harmful request under the serving regime actually used. However, it remains unclear whether matched compression that preserves task accuracy also preserves agreement between lightweight lexical monitors and stronger refusal classifiers. We study this with a paired protocol on n=200 harmful prompts with a long filler context: each prompt is answered once under full retention and once under matched eviction after a shared prefill, and the same replies are scored by keyword heuristics, the HarmBench Llama-2-13B classifier, an auxiliary LLM judge, and humans on disagreements. On Qwen2.5-3B, keyword refusal falls from 98.0% to 80.5% (McNemar p~1e-8) while classifier refusal stays near ceiling (99.0%-99.5%) and MMLU accuracy is unchanged (50.0%); human labels predominantly follow the classifier, consistent with soft refusals. The gap is not universal and weakens under short fillers and paired SnapKV, so safety auditing under compression should rely on several judges matched to the serving context rather than on keyword rates alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kang Chen, Xiuze Zhou, Hong Chen, Yuanguo Lin
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
