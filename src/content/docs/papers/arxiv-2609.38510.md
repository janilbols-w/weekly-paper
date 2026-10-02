---
title: "DEdit: Iterative Draft Editing for Speculative Decoding"
description: "Speculative decoding accelerates autoregressive LLMs by having a lightweight drafter propose tokens that the target model verifies in parallel."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](http://arxiv.org/abs/2609.38510v1) · [PDF](https://arxiv.org/pdf/2609.38510v1)

## 一句话摘要

Speculative decoding accelerates autoregressive LLMs by having a lightweight drafter propose tokens that the target model verifies in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates autoregressive LLMs by having a lightweight drafter propose tokens that the target model verifies in parallel. Diffusion-based drafters further reduce drafting latency by proposing multiple tokens at once. However, these tokens are predicted independently, so a single early error causes prefix verification to discard the rest of the draft, even when it contains useful downstream predictions. We introduce DEdit, a diffusion-based drafter that can not only draft by conventional parallel unmasking but also iteratively edit its draft through token-to-token predictions. Through editing, later predictions can serve as bidirectional context for repairing earlier errors and extending the accepted prefix. To teach the model to repair errors while preserving correct predictions, we propose ProposalMix, a training scheme that mixes draft predictions with ground-truth tokens based on first-pass confidence during training. Across seven benchmarks on Qwen3-4B and Qwen3-8B, DEdit achieves the highest macro-average token acceptance and speedup among the evaluated drafters, reaching macro-average speedups of $5.72\times$ and $5.97\times$ over autoregressive generation under greedy decoding, respectively. Further analysis shows that acceptance improves with more editing passes and wider drafting windows, and that ProposalMix halves harmful edits that shorten the accepted prefix. Moreover, restricting the editor to causal attention lowers acceptance, especially on highly predictable outputs, indicating that future context is a key source of these gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Longxuan Yu, Bingsen Chen, Peng Shi, Dongkyu Lee, Yi Xiang, Hideo Kobayashi, Sheng Zhang, Shuaichen Chang, Xing Niu, Zhuoyan Xu, Greg Ver Steeg, Jiarong Jiang
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
