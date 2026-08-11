---
title: "Attn-QAT: 4-Bit Attention With Quantization-Aware Training"
description: "Achieving reliable 4-bit attention is a prerequisite for end-to-end FP4 computation on emerging FP4-capable GPUs, yet attention remains the main obstacle due to FP4's tiny dynamic range and attention's heavy-tailed activations."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2603.00040) · [PDF](https://arxiv.org/pdf/2603.00040)

## 一句话摘要

Achieving reliable 4-bit attention is a prerequisite for end-to-end FP4 computation on emerging FP4-capable GPUs, yet attention remains the main obstacle due to FP4's tiny dynamic range and attention's heavy-tailed activations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Achieving reliable 4-bit attention is a prerequisite for end-to-end FP4 computation on emerging FP4-capable GPUs, yet attention remains the main obstacle due to FP4's tiny dynamic range and attention's heavy-tailed activations. This paper presents the first systematic study of 4-bit quantization-aware training (QAT) for attention. We find ``drop-in'' QAT -- naively combining an FP4 forward pass with high-precision Flash Attention (FA)-style backward pass -- leads to training instability. We identify two key principles for stable FP4 attention: (1) matching low-precision recomputation of attention scores in the backward pass and (2) resolving implicit precision assumptions in FA's gradient calculation. Based on these insights, we propose Attn-QAT and implement fused Triton kernels for training and FP4 inference kernels. Across diffusion and language models, Attn-QAT recovers the quality drop from FP4 attention without explicit outlier-mitigation heuristics used in prior FP4 attention, and delivers up to a 1.5x speedup on an RTX 5090 over SageAttention3 and up to a 1.74x speedup over FA4 on a GB300. Video demos can be found at https://drive.google.com/drive/folders/190F6xbBDUF2kGQYIcXBt3ehSYij5jlim?usp=sharing. Code can be found at https://haoailab.com/FastVideo/training/attn_qat/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Peiyuan Zhang, Matthew Noto, Wenxuan Tan, Chengquan Jiang, Will Lin, Wei Zhou, Hao Zhang
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
