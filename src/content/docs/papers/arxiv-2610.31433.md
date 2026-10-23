---
title: "Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation"
description: "KV cache compression for multimodal LLMs usually selects the visual tokens to keep once, at prefill, and reuses that selection for the whole generation."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.31433) · [PDF](https://arxiv.org/pdf/2610.31433)

## 一句话摘要

KV cache compression for multimodal LLMs usually selects the visual tokens to keep once, at prefill, and reuses that selection for the whole generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache compression for multimodal LLMs usually selects the visual tokens to keep once, at prefill, and reuses that selection for the whole generation. We show that this one-shot selection is severely limited on long-form generation: on detailed image description, even an oracle that selects with the attention of the uncompressed answer reaches only 0.44-0.52 ROUGE-L agreement with the uncompressed output, because the evidence the model reads moves as the description unfolds. Re-selecting whenever attention drifts out of the kept set is the natural remedy, but we find that a fixed drift threshold fails systematically: drift magnitudes are not comparable across samples, so low-drift samples are almost never refreshed although they benefit the most. We propose Rate-Controlled Refresh (RCR), which lets drift decide when and where to re-select while a per-sample controller regulates how often, combined with a low-rank drift detector, candidate-restricted re-selection, and a decision that stays on the GPU. With one setting for all models and tasks, RCR outperforms the per-step retrieval method InfiniGen by 1.6-3.8 ROUGE-L points on five of six model-task settings with no significant difference on the sixth, while staying within 1.7 points of exact per-step re-selection, with comparable estimated data movement per step and a 4x smaller GPU-resident detector. On DetailCaps, drift-chosen timing beats random timing at the same refresh rate and periodic timing even at a higher rate, by 2.0-5.0 points. On pre-registered video description, where drift is homogeneous across samples, RCR is on par with InfiniGen on Qwen2-VL and exceeds it on Qwen3-VL but no longer beats a fixed threshold at the nearest tested rates, consistent with the diagnosis; object-level evaluation shows that RCR achieves higher object F1 against the uncompressed output than InfiniGen on two of three models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Bin Hu, Yingbo Xiao
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
