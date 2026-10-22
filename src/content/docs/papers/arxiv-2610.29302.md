---
title: "Compressing Onboard Language Models for Space Robots under a Behavioral-Fidelity Requirement"
description: "Language models are being explored as the interface through which space robots interpret operator commands and select among verified skills."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.29302) · [PDF](https://arxiv.org/pdf/2610.29302)

## 一句话摘要

Language models are being explored as the interface through which space robots interpret operator commands and select among verified skills.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language models are being explored as the interface through which space robots interpret operator commands and select among verified skills. Running them onboard calls for low-bit compression, and flight use adds requirements that generic post-training quantization leaves implicit: a fixed memory budget and storage format, a static artifact under configuration control, and behavior close to the full-precision model validated on the ground. We treat compression as a ground-segment step and study QSelect, which composes one static low-bit model from compatible AWQ, GPTQ, and AutoRound checkpoints by assigning each linear module to one quantizer family and scoring every substitution at the final next-token distribution. The default fidelity mode needs no labels or tuned thresholds and accepts a substitution only when the forward KL divergence from the BF16 reference decreases; an optional target-adapted mode adds answer likelihood on a small labeled set. On DeepSeek-R1-Distill-Qwen-7B, Llama-3.1-8B, and Llama-3.2-3B at 3 and 4 bits, composed models reach lower mean held-out perplexity than every single-family model in all six settings, and the fidelity mode lowers perplexity and KL further. In a matched scaffold, final-output scoring gives lower held-out KL than representation-similarity scoring in all 12 paired runs. With labels from training or development splits of the evaluated task families, the target-adapted mode raises 3-bit pooled accuracy on the two Llama models by 4.3 and 4.5 points over the best single-family model. At 3 bits, unquantized embedding and output layers make up 43-46% of the packed artifact. All evaluations use general-domain benchmarks on a ground GPU; space-domain tasks and flight hardware are left to future work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jia Deng, Zizhe Wang, Xin Lu, Yi Huang, Zehao Jia
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
