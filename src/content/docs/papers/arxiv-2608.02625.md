---
title: "Speculative Correction: Draft-then-Refine Decoding for Diffusion Language Models"
description: "Diffusion language models (DLMs) can revise tokens bidirectionally, but standard decoding procedures often adapt them to left-to-right generation by producing text block by block."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.02625) · [PDF](https://arxiv.org/pdf/2608.02625)

## 一句话摘要

Diffusion language models (DLMs) can revise tokens bidirectionally, but standard decoding procedures often adapt them to left-to-right generation by producing text block by block.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) can revise tokens bidirectionally, but standard decoding procedures often adapt them to left-to-right generation by producing text block by block. We study a simple plug-and-play inference pattern: first generate a complete draft, then refine the full response using bidirectional diffusion. Using LLaDA2.1-Flash and LLaDA2.1-Mini, we evaluate two configurations. In Flash-Flash, the same Flash model serves as both drafter and refiner, testing whether an existing model can improve its own block-autoregressive output through global refinement. In Mini-Flash, inspired by speculative decoding, we introduce speculative correction: Mini drafts a full response, and Flash revises it as an editable initialization. Flash-Flash improves GSM8K-384 accuracy from 0.848 to 0.899 while running 1.20 times faster than the selected Flash block-autoregressive baseline, and improves MBPP-384 from 0.545 to 0.693. Latency-window-matched Flash-only controls indicate that these gains persist after targeted tuning of block-autoregressive decoding. Causal ablations indicate that completed drafts provide useful initializations: refinement from a fully masked span performs poorly, full global refinement provides a clear additional gain on GSM8K, and local refinement captures much of the gain on MBPP and MATH. Mini-Flash provides useful quality-latency trade-offs, including MATH-384 performance of 0.294 versus 0.300 for Flash while running 2.17 times faster. These results support a Pareto-frontier interpretation rather than the claim that the heterogeneous cascade uniformly matches Flash quality. Overall, same-model draft-and-refine provides evidence that bidirectional refinement is a useful decoding primitive for DLMs, while speculative correction demonstrates a training-free route to fast DLM generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Brian K Chen, Chong Wu, Kenji Kawaguchi
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
