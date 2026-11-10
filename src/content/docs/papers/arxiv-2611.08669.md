---
title: "ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding"
description: "Speculative decoding has become a standard way to accelerate LLM inference: a lightweight drafter proposes tokens that the target verifies in one parallel pass."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.08669) · [PDF](https://arxiv.org/pdf/2611.08669)

## 一句话摘要

Speculative decoding has become a standard way to accelerate LLM inference: a lightweight drafter proposes tokens that the target verifies in one parallel pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding has become a standard way to accelerate LLM inference: a lightweight drafter proposes tokens that the target verifies in one parallel pass. Existing drafters face trade-offs that limits their speedups: autoregressive drafters generate tokens one at a time, so drafting cost grows with draft length, while diffusion drafters generate tokens in parallel but predict each position independently, ignoring inter-token dependencies. We introduce ChainFlow, a new speculative decoding paradigm and the first flow-matching drafter conditioned on the target's hidden states. ChainFlow treats drafting as a short transport over hidden states, needing one or two flow steps instead of the many denoising steps of generation from noise. A variational autoencoder compresses these states so drafting cost barely grows with target size, lightweight feedback heads restore inter-token dependencies, and tree drafting raises acceptance. On Qwen3.5 models, at matched drafter size and training data, ChainFlow outperforms EAGLE-3 and DFlash in vLLM by 39% and 11%, respectively. These gains further widen as drafters are adapted to new languages sequentially. Our ablations cover drafter design and concurrent serving, and we open-source our code and drafter models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Selim Aktas, Yusuf Erdem Erdem, Ahmed Zeer, Himmet Toprak Kesgin, Muzaffer Kaan Yuce, Mehmet Fatih Amasyali
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
