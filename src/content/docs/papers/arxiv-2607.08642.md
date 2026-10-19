---
title: "DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding"
description: "Speculative decoding speeds up large language model inference: a small drafter proposes several tokens, and the target model verifies them in one parallel pass."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2607.08642) · [PDF](https://arxiv.org/pdf/2607.08642)

## 一句话摘要

Speculative decoding speeds up large language model inference: a small drafter proposes several tokens, and the target model verifies them in one parallel pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding speeds up large language model inference: a small drafter proposes several tokens, and the target model verifies them in one parallel pass. Drafting a tree lets the target verify many alternative continuations at once. DDTree builds such trees from the block-diffusion drafter DFlash, but scores each position independently of the tokens earlier in its branch; Domino conditions on those tokens but drafts only a single chain. DominoTree combines the two: a training-free best-first tree scored by Domino's path-dependent causal correction, restricted to top-M candidates. In a research harness at temperature zero, it averages 5.33x speedup over autoregressive (AR) decoding on Qwen3-4B and 6.89x on Qwen3-8B, peaking at 8.77x; across temperatures it is 20-26% faster than Domino on Qwen3-4B and 27-36% on Qwen3-8B, and 11-20% faster than the stronger of DDTree and its cost-aware variant CaDDTree. A controlled decomposition attributes +10.1% (Qwen3-4B) and +10.7% (Qwen3-8B) accepted length to the correction, and +4.7% and +4.4% to conditioning on the realized path. Served in SGLang on one RTX 5090, it reaches 4.11x and 4.83x AR at batch size 1, 1.17x and 1.09x the speed of Domino's chain, and up to 1.71x AR on 8K-token HELMET summarization, 14-21% above the chain. The lead holds at 2 concurrent requests but reverses from 8 onward, where the chain sustains more goodput despite DominoTree's 28% higher acceptance. DominoTree accepts more tokens than the chain in every serving setting. On the hybrid Gated-DeltaNet Qwen3.6-27B, correct output requires tree-aware recurrent verification; with it, DominoTree matches the chain at batch size 1 (4.58x versus 4.54x AR) and reaches up to 2.11x AR at long context, 15% above the chain.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Saw S. Lin (Zhiqi Zhang), Jyh-Shing Roger Jang
- 发布：2026-08-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
