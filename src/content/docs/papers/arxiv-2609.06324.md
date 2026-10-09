---
title: "A Ticket from Marginals to Joints: Coupled-Noise Distillation for One-Step Block Generation in Diffusion Language Models"
description: "Can a diffusion language model generate a coherent token block in one forward pass?"
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06324) · [PDF](https://arxiv.org/pdf/2609.06324)

## 一句话摘要

Can a diffusion language model generate a coherent token block in one forward pass?

## 为什么值得关注

待编辑增强。

## 摘要原文

Can a diffusion language model generate a coherent token block in one forward pass? Masked models already predict every position at once, but each prediction is the marginal distribution given the visible context, so the tokens can be mutually inconsistent and later steps revise those already committed. We introduce CONDOR (Coupled-Noise Distillation for One-Step Readout), trained from scratch to map different noise samples to different coherent blocks. Initially, random noise is not naturally paired with a target. Winner-take-all supervision lets different samples specialize, and self-distillation trains the one-pass output to match the refined coherent block. TinyStories experiments show diverse, coherent continuations over successive blocks, one forward pass each. Qualitative MNIST experiments show that the same approach can extend to multimodal generation, such as text-to-image and unconditional text-and-image generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lin Yao
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
