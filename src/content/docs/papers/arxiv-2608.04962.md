---
title: "SPARK: Learning from Verification in Speculative GRPO Rollouts"
description: "Group Relative Policy Optimization (GRPO) has become a standard approach for improving the reasoning abilities of large language models, but its training is costly because each step requires generating many long reasoning responses."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.04962) · [PDF](https://arxiv.org/pdf/2608.04962)

## 一句话摘要

Group Relative Policy Optimization (GRPO) has become a standard approach for improving the reasoning abilities of large language models, but its training is costly because each step requires generating many long reasoning responses.

## 为什么值得关注

待编辑增强。

## 摘要原文

Group Relative Policy Optimization (GRPO) has become a standard approach for improving the reasoning abilities of large language models, but its training is costly because each step requires generating many long reasoning responses. Recent methods use speculative decoding to accelerate the rollouts, where a draft model proposes tokens that the target model verifies. However, we find that the draft model repeatedly misses the same tokens within a response and across responses in the same GRPO group, and the verification feedback on these misses is not used to update the draft during the rollout. Motivated by this analysis, we introduce SPARK, a lightweight self-adaptive mechanism designed to enhance draft models used in speculative GRPO training. SPARK leverages target verification feedback to refine draft predictions during generation while preserving their existing training procedures. Averaged across 21 model-dataset settings, SPARK improves generation speedup by 32.7% and 11.4%, and end-to-end GRPO training speedup by 32.2% and 8.5%, over EAGLE3-style and DFlash-style baselines, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nhat Minh Pham, Duy Tung Doan, Thi Duyen Ngo, Vinh Van Nguyen, Khac-Hoai Nam Bui
- 发布：2026-08-05；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
