---
title: "Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models"
description: "Large language models (LLMs) excel at multi-step reasoning but incur substantial inference cost."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.19350) · [PDF](https://arxiv.org/pdf/2606.19350)

## 一句话摘要

Large language models (LLMs) excel at multi-step reasoning but incur substantial inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) excel at multi-step reasoning but incur substantial inference cost. We introduce Causal Attribution Pruning (CAP), a training-free method that identifies critical attention heads by measuring their causal impact on reasoning tasks and uses these head-level scores to guide fine-grained weight pruning. For each attention head, CAP estimates the expected performance degradation when the head is masked during forward passes on a small calibration set of reasoning problems. These causal scores are then converted into weight-level importance values for the corresponding projection matrices. Unlike magnitude-only or activation-based criteria, CAP's interventional measurement directly captures each head's functional contribution, yielding relative accuracy gains of up to 61% over Wanda on ARC-Challenge at 20% sparsity. We evaluate CAP on GSM8K, StrategyQA, and ARC-Challenge using Llama-3-8B-Instruct and Mistral-7B-Instruct at 10%, 20%, and 50% sparsity. At moderate sparsity (10-20%), CAP improves over Wanda in most model-benchmark configurations. with especially large gains on ARC-Challenge for Llama-3. Our results suggest that attention-head-level causal attribution can better preserve reasoning performance on downstream benchmarks than correlational pruning criteria at equivalent sparsity, while remaining limited by coarse MLP attribution at 50% sparsity.

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

- 作者：Amogh Sheth, Andrew Lin, Biruk Assefa, Yi Wen Huang, Yuhao Ge
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
