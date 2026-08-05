---
title: "ATFlash: Per-RoPE-Wavelength Attention Windows for Compute/Memory-Efficient LLM Inference"
description: "The attention score with rotary position embeddings (RoPE) decomposes exactly into a sum over its 2D-rotation frequency pairs, and each pair's wavelength limits how far it can discriminate position."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.02947) · [PDF](https://arxiv.org/pdf/2608.02947)

## 一句话摘要

The attention score with rotary position embeddings (RoPE) decomposes exactly into a sum over its 2D-rotation frequency pairs, and each pair's wavelength limits how far it can discriminate position.

## 为什么值得关注

待编辑增强。

## 摘要原文

The attention score with rotary position embeddings (RoPE) decomposes exactly into a sum over its 2D-rotation frequency pairs, and each pair's wavelength limits how far it can discriminate position. Aligned with this structure, we propose the per-RoPE-wavelength distance window: it prunes the query--key inner-product terms beyond a wavelength-proportional distance. Unlike a sliding window, every key remains reachable, at least through the low-frequency pairs. The reduction rate is input-independent, with a closed form logarithmic in the sequence length $N$, in contrast to dynamic-sparse methods like MInference. Such token-level selection is orthogonal to our frequency-level pruning. The window can therefore be applied on top of those methods. On Qwen2.5-0.5B and Llama-3.2-3B, the window prunes 37--48\% of the query--key inner-product terms within each model's native context length. Relative to full attention, the top-1 match rate stays at 96--98\% and the mean output-distribution KL at the $10^{-3}$-nat level on LongBench-v2 contexts. We examine absolute scores on long-context benchmarks such as RULER, OpenAI-MRCR, LongCodeQA, and $\infty$Bench: they are broadly preserved. We implement the window as a slice of the query--key contraction axis, leaving the online-softmax recurrences untouched, and port it with minimal diffs into the released FlashAttention-4 prefill and FlashInfer decode. On RTX PRO 6000 with Llama, both ports outpace stock with gains growing with context length, up to $1.29\times$ at 128K. End to end on Qwen2.5-7B-1M, with 57\% of the inner-product terms pruned, the speedup reaches $1.31\times$ at a 1M-token context.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Takahiro Katagiri
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
