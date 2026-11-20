---
title: "NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding"
description: "Speculative decoding is widely used to speed up generation in large language models (LLMs), with a small draft model proposing tokens that one forward pass of the target model verifies."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.23835) · [PDF](https://arxiv.org/pdf/2611.23835)

## 一句话摘要

Speculative decoding is widely used to speed up generation in large language models (LLMs), with a small draft model proposing tokens that one forward pass of the target model verifies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding is widely used to speed up generation in large language models (LLMs), with a small draft model proposing tokens that one forward pass of the target model verifies. Draft models that read the target's hidden states, such as DFlash and EAGLE-3, typically inherit the target's hidden width. We show that the draft's whole residual stream can run at half or a quarter of that width while largely preserving acceptance. For DFlash, which borrows the target's vocabulary projection, the trained output adapter folds into it, giving one narrower projection with logits unchanged up to floating-point rounding. We test two drafter families, DFlash and EAGLE-3, on two targets, Qwen3-8B (NVFP4) and GPT-OSS-20B (MXFP4), in SGLang on a B200 and a DGX Spark (GB10). At batch size 1 and temperature 0, narrowing the draft to half or a quarter width speeds up end-to-end decoding by 1.06-1.12x on B200 and 1.13-1.44x on GB10. The speedup holds at larger batch sizes. From batch 32 to the largest batch each GPU fits, narrowing reaches up to 1.21x on both GPUs, and no narrow draft is slower than full width.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Alagappan Valliappan, Ankit More, Dheevatsa Mudigere, Jatin Mitra
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
