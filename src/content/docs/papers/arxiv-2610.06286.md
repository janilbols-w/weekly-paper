---
title: "DeferKV: Rethinking Eviction Timing for One-Shot KV Cache Compression"
description: "Long-context large language models (LLMs) have demonstrated strong capabilities across a wide range of tasks, but the growing KV cache introduces substantial memory and inference overhead."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.06286) · [PDF](https://arxiv.org/pdf/2610.06286)

## 一句话摘要

Long-context large language models (LLMs) have demonstrated strong capabilities across a wide range of tasks, but the growing KV cache introduces substantial memory and inference overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context large language models (LLMs) have demonstrated strong capabilities across a wide range of tasks, but the growing KV cache introduces substantial memory and inference overhead. Existing one-shot KV cache compression methods typically commit to irreversible eviction immediately after prefill, before any signal from actual generation becomes available. Our quantitative analysis shows that early queries from the actual generation stage provide attention signals that are more consistent with subsequent decode attention, with the largest single-step gain occurring at the prefill-decode boundary. Based on this observation, we propose DeferKV, which moves the eviction decision from the end of prefill to the first real decoding step and temporally combines prompt-side and decode-side observations, thereby better aligning KV importance estimation with subsequent generation requirements. DeferKV requires no additional training, draft model, or future-query prediction module, making it simple and easy to deploy. Experiments on LongBench, RULER, and Needle-in-a-Haystack demonstrate that DeferKV consistently improves model performance under KV cache compression while maintaining low inference latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhe Wang, Jiakai Li, Yujia Sun, Rongzheng Wang, Shuang Liang
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
