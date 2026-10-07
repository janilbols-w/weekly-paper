---
title: "SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding in Diffusion Language Models"
description: "Diffusion large language models (DLLMs) generate text through iterative block denoising, and multi-branch speculative decoding accelerates this process by verifying a main branch together with multiple draft branches in a single forward pass."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.04875) · [PDF](https://arxiv.org/pdf/2610.04875)

## 一句话摘要

Diffusion large language models (DLLMs) generate text through iterative block denoising, and multi-branch speculative decoding accelerates this process by verifying a main branch together with multiple draft branches in a single forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (DLLMs) generate text through iterative block denoising, and multi-branch speculative decoding accelerates this process by verifying a main branch together with multiple draft branches in a single forward pass. While prior DLLM acceleration methods primarily exploit temporal redundancy across denoising steps, we identify a complementary redundancy axis within each speculative verification step: multi-branch computational redundancy. During speculative verification, draft branches inherit most tokens from their parents while unmasking a small set of additional positions, causing large portions of hidden states to remain highly similar across branches. We propose SpecFold, an algorithm-system co-design that exploits this multi-branch redundancy to reduce the cost of multi-branch speculative verification. Algorithmically, SpecFold performs token-level residual gating and selectively reuses parent computation through folded attention and FFN while preserving residual hidden states. Systemically, a Triton kernel implementation translates this fine-grained reuse into end-to-end throughput gains through efficient sparse multi-branch execution. SpecFold is orthogonal to temporal caching and compatible with existing DLLM speculation strategies. Across two DLLM families, five models, and five standard benchmarks, SpecFold achieves up to 1.64x throughput over Spiffy and up to 1.99x over vanilla decoding, while maintaining comparable task performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Chung-En Ho (Celine), Weiyu Sun (Celine), Cheng-Jhih Shih (Celine), He Li (Celine), Yong Liu (Celine), Yingyan (Celine), Lin
- 发布：2026-10-06；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
