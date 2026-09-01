---
title: "ReTrace: Rejected-Trajectory Conditioning for Speculative Decoding"
description: "Speculative decoding accelerates autoregressive language model inference by having a lightweight draft model propose multiple candidate tokens, which are then verified in parallel by a larger target model."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.29748) · [PDF](https://arxiv.org/pdf/2608.29748)

## 一句话摘要

Speculative decoding accelerates autoregressive language model inference by having a lightweight draft model propose multiple candidate tokens, which are then verified in parallel by a larger target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates autoregressive language model inference by having a lightweight draft model propose multiple candidate tokens, which are then verified in parallel by a larger target model. However, after the first rejection, standard prefix-based verification discards the remaining draft suffix, so the computation spent generating and verifying those positions does not contribute to decoding progress. Focusing on DFlash, we show that rejected positions in a rejected suffix may still align with the target continuation, indicating that the draft model can retain useful semantic and structural information despite local token-level errors. Motivated by this observation and inspired by conditional diffusion, we introduce~\textbf{ReTrace}, a rejected-trajectory conditioning method that conditions each draft block on the rejected suffix from the previous round rather than generating it from fresh mask placeholders alone. ReTrace retains the hidden representations of the rejected suffixes, aligns them with the next draft block, refines them using target-aware correction signals from the same verification pass, and admits them into the drafter's input embeddings through gated residual fusion. Because rejected tokens are never committed and target-side verification remains unchanged, ReTrace preserves the lossless property of speculative decoding without requiring an additional model forward pass. Experiments with Qwen3 models across mathematical reasoning, code generation, and open-ended dialogue demonstrate that ReTrace consistently improves average acceptance length and end-to-end decoding speed over its DFlash backbone. By introducing cross-round conditioning without modifying within-round proposal generation, ReTrace is largely orthogonal to existing drafting improvements and might be combined with them for further gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luxi Lin, Zhanpeng Zeng, Shuang Peng, Songwei Liu, Rongrong Ji
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
