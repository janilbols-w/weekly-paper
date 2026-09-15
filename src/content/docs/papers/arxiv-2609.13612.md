---
title: "AttnFuse: A Composable DSL for Compiling Attentions to Fused GPU Kernels"
description: "Modern AI systems are built on the Transformer architecture, whose core operation, attention, accounts for the majority of computation and memory cost."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.13612) · [PDF](https://arxiv.org/pdf/2609.13612)

## 一句话摘要

Modern AI systems are built on the Transformer architecture, whose core operation, attention, accounts for the majority of computation and memory cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern AI systems are built on the Transformer architecture, whose core operation, attention, accounts for the majority of computation and memory cost. Researchers continually propose new attention variants to improve quality, efficiency, or context length, but each variant currently requires expert-written GPU code to run at usable speeds. PyTorch's recent flex\_attention lets researchers describe custom attention patterns in Python and compile them to fused kernels, but its design is limited to modifications applied after the central matrix multiplication, excluding Rotary Position Embedding (RoPE), the positional encoding used by every major LLM. We introduce AttnFuse, a small DSL for attention that makes pre-multiplication transformations like RoPE first-class operations. Researchers compose ten high-level building blocks to describe a variant, and AttnFuse's compiler emits a single fused GPU kernel for the entire computation. On an RTX 3090, AttnFuse achieves a 2.10$\times$ speedup over flex\_attention on the RoPE+causal pattern. On an H100, it runs a full Llama-3-8B training step within 5\% of PyTorch's hand-tuned backend. Our investigation reveals the Rotation Calculus: whether to fuse RoPE or apply it separately depends on the GPU's compute-to-bandwidth ratio, with a derived crossover that matches measurement. AttnFuse demonstrates that a small, attention-specific compiler can close the gap between flexible research code and production kernels.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Varun Kumar Dasoju, Tian Zhao
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
