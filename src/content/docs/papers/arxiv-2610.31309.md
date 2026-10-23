---
title: "Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization"
description: "Scaling embedding capacity alongside Transformer computation is an emerging trend in language models."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.31309) · [PDF](https://arxiv.org/pdf/2610.31309)

## 一句话摘要

Scaling embedding capacity alongside Transformer computation is an emerging trend in language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling embedding capacity alongside Transformer computation is an emerging trend in language models. This trend makes high compression rates increasingly useful. Hence, we study extreme compression of Per-Layer Embeddings (PLE), which follow this trend and account for 35.2% of the parameters of Gemma 4 E4B. At such rates, conventional quantizers give each token-layer vector its own code of only a few bytes. We instead develop OPTIC (Output-Path-fitted, Token-shared Indexed Codes), which stores one quantized code tuple per token and decodes it at every layer with a layer-specific affine decoder. Codes and decoders are fitted to the PLE output path rather than to the stored vectors. At about $100\times$ PLE compression of bfloat16 (BF16) E4B, OPTIC retains an aggregate 97.8% of the uncompressed model's performance across seven benchmarks, whereas product quantization, the strongest of six conventional baselines, retains 66.3%. At $594\times$ and $1,002\times$ PLE compression of BF16 E4B, OPTIC retains 90.5% and 84.1%. On the official E4B release with 4-bit linear weights and 16-bit activations (W4A16), OPTIC retains 96.9% at about $100\times$ PLE compression. During inference at about $100\times$ PLE compression, BF16 E4B uses 29.7% less GPU memory than with uncompressed PLE at the same key-value cache size, while running at most 0.40% slower.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiacheng Liu, Yaxin Luo, Xiaohan Zhao, Peng Sun, Xinyi Shang, Jiacheng Cui, Yonina C. Eldar, Zhiqiang Shen
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
