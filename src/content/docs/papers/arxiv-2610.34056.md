---
title: "INTRA: Interleaved Non-contiguous Token spaRse Attention"
description: "Transformers achieve strong performance across modalities but are bottlenecked by the quadratic cost of attention."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.34056) · [PDF](https://arxiv.org/pdf/2610.34056)

## 一句话摘要

Transformers achieve strong performance across modalities but are bottlenecked by the quadratic cost of attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformers achieve strong performance across modalities but are bottlenecked by the quadratic cost of attention. Sparse attention can reduce this cost, but effective sparsity must preserve useful long-range communication and map well to GPU hardware. We introduce INTRA--Interleaved Non-contiguous Token spaRse Attention--a hardware-aware static sparse attention design based on a relay-communication view under Computational Query Set (CQS) constraints. Rather than directly covering all token-to-token interactions within each sparse layer, INTRA uses complementary sparse groups to provide short mediated communication paths across layers. Scatter forms relay groups that sample broadly across local neighborhoods, while Gather reconnects these groups in subsequent layers. Under a partition model, this structure guides CQS-compatible sparse patterns with global reachability. Our CQS-aware FlashAttention-style kernel computes structured indices at runtime, loads selected non-contiguous tokens, and packs them densely for computation. On an A100, INTRA achieves a $1.53\times$ speedup in $2K$ FLUX.1-dev generation, with better measured image quality than evaluated CLEAR configurations after LoRA self-distillation. On LLaMA-3.1-8B, it improves long-context prefill efficiency with strong teacher-forced retrieval performance under matched LoRA adaptation. Attention-only benchmarks further show up to $8.4\times$ and $10.4\times$ speedups over MoBA and density-constrained NSA, respectively. Code is available at https://github.com/NovTi/INTRA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuxuan Xia, Wenbo Lu, Shaoyi Zheng, Shengjie Wang
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/NovTi/INTRA](https://github.com/NovTi/INTRA)
- 阅读深度：metadata
