---
title: "RT-Lynx: Putting GEMM Sparsity in the Right Place for Diffusion Models"
description: "Diffusion Transformers (DiT) achieve strong performance in image generation but incur substantial inference costs."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.26632) · [PDF](https://arxiv.org/pdf/2605.26632)

## 一句话摘要

Diffusion Transformers (DiT) achieve strong performance in image generation but incur substantial inference costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Transformers (DiT) achieve strong performance in image generation but incur substantial inference costs. While prior work has reduced this cost via quantization and distillation, semi-structured sparsity, which can nearly halve FLOPs, remains underexplored. A key reason is that most existing approaches focus on weight sparsification, and pruning 50% of the weights can remove critical model capacity and degrade generation quality. Our study, however, shows that DiT activations are intrinsically sparse and significantly more robust to N:M semi-structured sparsification than weights. Motivated by this observation, we advocate a paradigm shift from weight sparsification to activation sparsification. We propose RT-Lynx, which applies N:M sparsification to activations and incorporates error-compensation techniques to mitigate accuracy loss. We further implement highly optimized CUDA kernels tailored to this setting, achieving up to a 1.55x speedup on average in linear layers. Extensive experiments across multiple diffusion models demonstrate that our method preserves the generation quality of the original models while substantially accelerating inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning, sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xing Cong, Hanlin Tang, Kan Liu, Tao Lan, Lin Qu, Chenhao Xie
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
