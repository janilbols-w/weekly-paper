---
title: "Reference-Compatible Parallel Execution for Quantized LLM Inference"
description: "Batching can change a quantized language model's logits even when token positions and causal masks are unchanged."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.03228) · [PDF](https://arxiv.org/pdf/2610.03228)

## 一句话摘要

Batching can change a quantized language model's logits even when token positions and causal masks are unchanged.

## 为什么值得关注

待编辑增强。

## 摘要原文

Batching can change a quantized language model's logits even when token positions and causal masks are unchanged. We present a method for executing known queries in parallel while retaining the numerical behavior of a scalar deployment fixed before optimization. The method derives physical KV-prefix and backend arithmetic requirements, groups compatible queries, and keeps independent projection work batched. On CUDA, it packs independent four-column reductions into a broadcast batch without widening the reference-sensitive reduction. On Vulkan, it preserves projection activation arithmetic and extends a scalar attention path across query groups. Controlled interventions and frozen-input studies cover Llama, Qwen and SmolLM2. CUDA packing reduces complete resident-service time by 4.00% on four fresh inputs. Vulkan batched attention reduces ordinary-request time by 32.34% versus per-query attention and 52.87% versus scalar execution on twelve fresh inputs. Equally optimized whole-graph boundary cuts match local grouping on aligned natural prefill and outperform it at some wider Vulkan query sizes. At deliberately crossing CUDA appends, local grouping gives a $1.307\times$ speedup over whole-graph cuts; this conditional result is not a workload-average speedup. These results identify how numerical compatibility constrains parallel execution and how width and alignment determine the benefit of local cuts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chengzhan Li
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
