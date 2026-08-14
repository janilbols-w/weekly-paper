---
title: "SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding"
description: "Large language models (LLMs) increasingly read long inputs in the agentic era, from whole documents and codebases to conversations across many turns."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.07915) · [PDF](https://arxiv.org/pdf/2608.07915)

## 一句话摘要

Large language models (LLMs) increasingly read long inputs in the agentic era, from whole documents and codebases to conversations across many turns.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) increasingly read long inputs in the agentic era, from whole documents and codebases to conversations across many turns. Their inference memory is then dominated by the key-value (KV) cache, the stored attention keys and values of every token the model has read and generated. Because the cache grows with context length and is re-read in full at every generated token, a longer context means more GPU memory. To reduce this cost, most existing methods compress the KV cache by lowering every stored value to the same low precision, a technique known as quantization. They can push this to nearly two bits per value, but rarely further, because quality drops sharply at this 2-bit cliff: four levels are too few for the cache's outlier-heavy values, where a few large entries consume the levels and collapse the rest into noise. A natural remedy is to spend more bits on the channels (feature dimensions) that matter and fewer on the rest, but the raw cache offers no handle: its channels are strongly correlated, so none stands out as more important. Our analysis shows that this handle appears once the cache is rotated into a coordinate system computed from its own statistics, removing these correlations. There, a small fraction of channels carries almost all the information, and spending the budget on those few is far more accurate than spreading it evenly. Guided by this analysis, we develop SPECTRA, a training-free, drop-in codec that re-encodes the cache into this coordinate system and concentrates the bit budget on the channels that carry the signal. On Llama-3.1-8B and Qwen2.5-7B over long-context benchmarks, SPECTRA is near-lossless at 4x compression, competitive at 8x where uniform quantization has collapsed, and reaches up to 12x, pushing usable compression past the 2-bit cliff so the same GPU holds longer contexts and larger batches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiamu Zhang, Liang Wu, Kelly Wan, Hanjie Chen, Liangjie Hong
- 发布：2026-08-08；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
