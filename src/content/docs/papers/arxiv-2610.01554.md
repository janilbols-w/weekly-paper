---
title: "QK-Wanda: Coupling Queries and Keys for Unstructured Pruning"
description: "Wanda (Sun et al., 2024) prunes large language models by scoring weights independently within each linear projection, although queries and keys interact through dot products."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.01554) · [PDF](https://arxiv.org/pdf/2610.01554)

## 一句话摘要

Wanda (Sun et al., 2024) prunes large language models by scoring weights independently within each linear projection, although queries and keys interact through dot products.

## 为什么值得关注

待编辑增强。

## 摘要原文

Wanda (Sun et al., 2024) prunes large language models by scoring weights independently within each linear projection, although queries and keys interact through dot products. We introduce QK-Wanda, which scores query and key weights by their individual deletion costs under an unmasked pre-RoPE reconstruction objective. It augments Wanda scores with information from the opposite projection (keys for query weights, and queries for key weights), allowing both projections to share a pruning budget. Its closed-form scores require no gradients or weight updates; full pruning takes 1.3% longer than Wanda on A100 and 3.1% longer on H200 with the calibration used in our main experiments. We evaluate QK-only pruning across 15 models from TinyLlama, Llama 2, Llama 3, and Qwen2.5, spanning 0.5B-72B parameters. Relative to Wanda, QK-Wanda reduces QK reconstruction error by an average of 60% at 50% sparsity and 45% at 80%. Downstream gains depend on the model. At 80% sparsity on Llama 2 70B, WikiText-2 and C4 perplexity decrease by 20.3% and 13.5%, while mean zero-shot accuracy rises by 5.94 percentage points. Qwen2.5-72B also improves, but Llama-3.1-70B has substantially higher perplexity despite lower reconstruction error. These results show both the promise of coupled pruning criteria and the limits of local reconstruction as a predictor of model quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ivan Ilin, Peter Richtárik
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
