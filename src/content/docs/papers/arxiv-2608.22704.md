---
title: "WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs"
description: "Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.22704) · [PDF](https://arxiv.org/pdf/2608.22704)

## 一句话摘要

Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs. Prefill-only KV compression methods permanently discard audio KV positions once evicted, with no pathway to recover them during decoding. We show this is fragile on long-form audio: prefill attention concentrates near the audio start (an attention-sink effect), while decode-time attention distributes broadly, and the two rankings overlap weakly. We propose WnW (Waxing-and-Waning KV cache), which classifies KV-heads into anchor, tidal, and fixed roles via offline calibration. Anchor heads remain on GPU and serve as a decode-time importance observer; tidal heads keep a CPU-resident complement that is recalled chunk-by-chunk based on aggregated anchor-head scores; fixed heads keep only an on-GPU subset, with the rest permanently discarded. On LibriSpeech-Long with two 3B backbones (Voxtral-mini-3b and Qwen2.5-Omni-3B), WnW preserves near-Full-Cache accuracy while keeping only 20% of audio tokens on GPU, where prefill-only baselines fail to terminate. Results generalize across language, task, and domain shifts, and CPU-GPU recall adds little decode-time overhead in our measurements.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiming Yao, Chenyang Lyu, Xuanfan Ni, Longyue Wang, Weihua Luo, Yazheng Yang, Jinsong Su
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
