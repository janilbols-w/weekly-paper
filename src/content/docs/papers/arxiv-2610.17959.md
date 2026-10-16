---
title: "Virtual Head Attention"
description: "The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.17959v1) · [PDF](https://arxiv.org/pdf/2610.17959v1)

## 一句话摘要

The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA can compress the cache, but MLA suffers from quality loss while MFA substantially increases training and prefill compute. We propose Virtual Head Attention (VHA), which simultaneously improves all three vertices through two lightweight linear operations: Q Premix applies a near-identity transformation to queries within each KV group to recover virtual head diversity from halved physical query heads, and Linear Postmix fuses inter-head features via a low-rank $I + AB^\top$ residual structure. Since VHA introduces no nonlinear operations, Premix can be folded into the query projection and Postmix into the output projection at inference time, reducing the model to a standard GQA-2 architecture that directly reuses all existing GQA inference optimizations. With only two KV heads, the group size in large models readily reaches 64, fully exploiting Tensor Core parallelism during decoding. Across four scales with 4K-context 50B-token pretraining, VHA consistently surpasses the standard GQA baseline at every scale ($+$0.05\% to $+$0.81\%), while reducing KV cache by $4\times$ vs.\ GQA-8 at dense scales and $2\times$ vs.\ GQA-4 at the MoE scale, and lowering training and prefill FLOPs by 7.9\% (1.7B, $S{=}4096$). On an industrial 30B-A3B MoE model trained on 500B tokens at 8K context, VHA outperforms both MLA and GQA-4 by $+$0.70\,/\,$+$2.60\,\% on a 12-benchmark base-model evaluation suite; in a separate matched 10B-A1B MoE comparison after long-context mid-training, VHA attains an average RULER score of 84.4 over 8K--128K versus 73.0 for GQA, while using two rather than four KV heads in the full-attention layers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xibo Ding, Guoxia Wang, Jinle Zeng, Jiabin Yang, Sirui Tao, Chao Yang, Dianhai Yu
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
