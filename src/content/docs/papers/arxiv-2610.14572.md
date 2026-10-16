---
title: "Reward-Aligned Distillation"
description: "Reinforcement learning with verifiable rewards improves the reasoning capabilities of large language models, but remains computationally expensive and sample inefficient."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.14572v1) · [PDF](https://arxiv.org/pdf/2610.14572v1)

## 一句话摘要

Reinforcement learning with verifiable rewards improves the reasoning capabilities of large language models, but remains computationally expensive and sample inefficient.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards improves the reasoning capabilities of large language models, but remains computationally expensive and sample inefficient. On-policy distillation (OPD) provides dense token-level supervision from a stronger teacher, yet standard OPD distills every token regardless of whether the teacher's preference actually improves task reward. Existing token-selection methods rely on proxies such as uncertainty or teacher--student divergence, which need not identify reward-improving supervision. We introduce Reward-Aligned Distillation (RAD), a bilevel framework that weights distillation signals based on their predicted effect on the student's post-update reward. RAD differentiates through a temporary optimizer step to score each token's supervision, then updates the token weights by projected ascent from the initial token weights. The resulting weights can strengthen, suppress, or reverse individual distillation-gradient contributions. At a matched training-response budget, RAD improves mean accuracy on six competition-math benchmarks over the strongest baselines by 6.5 percentage points for Qwen3-1.7B (non-thinking) and 2.5 points for Qwen3-4B-Instruct-2507. RAD-Simple, a simplified variant, achieves comparable math accuracy at the same training-response budget. On LiveCodeBench-v6, RAD reaches 54.69\% and 58.67\% pass@1 with Qwen3-1.7B (non-thinking) and OLMo3-7B-Instruct, respectively, exceeding the strongest baselines by 8.7 and 6.4 points. These results support reward-guided weighting of teacher supervision across model families and tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yilan Chen, Zian Su, Manish Prajapat, Dingmin Wang, Rein Houthooft, Rui Song, Vijay Lingam
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
