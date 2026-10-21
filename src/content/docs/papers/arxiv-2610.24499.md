---
title: "TideKV: Delayed KV Eviction via Layer-Wise Chunked Prefill for Memory-Efficient Long-Context LLM Inference"
description: "Long-context large language model (LLM) inference is important for modern intelligent applications but remains constrained by peak memory during prompt prefill."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.24499) · [PDF](https://arxiv.org/pdf/2610.24499)

## 一句话摘要

Long-context large language model (LLM) inference is important for modern intelligent applications but remains constrained by peak memory during prompt prefill.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context large language model (LLM) inference is important for modern intelligent applications but remains constrained by peak memory during prompt prefill. Existing KV cache compression reduces decoding memory but typically requires full-prompt prefill to preserve global context, retaining a high construction peak. Online chunk-level eviction lowers memory earlier but selects before each layer has observed the complete prompt, potentially degrading cache construction and decoding. We present TideKV, an on-GPU cache-construction architecture using layer-major delayed eviction. TideKV processes all prompt chunks within each Transformer layer, retains full-prompt KV only for the active layer, and evicts at layer end. This schedule preserves full-prompt-aware selection while reducing activation and temporary memory. Experiments across multiple computing platforms show that TideKV preserves the inference quality and final cache size of the evaluated compression methods. At 64K on A100, it reduces the construction-time transient footprint by 83.89%. On RTX 4090, it increases time to first token by only 1.06% at 64K and enables 128K prefill. TideKV also completes 128K on Jetson, whereas matched post-prefill compression runs out of memory on both resource-constrained platforms. These results show that delayed layer-end eviction substantially expands feasible context lengths without sacrificing cache utility.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yu Wang, Zhu Wang, Ning Hu, Yifan Guo, Xiu Ma, Bin Guo, Zhiwen Yu
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
