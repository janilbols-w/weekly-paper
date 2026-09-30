---
title: "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards"
description: "Reinforcement Learning with Verifiable Rewards (RLVR) is widely used for post-training Large Language Models, but practical verifiers can make errors."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2604.07666) · [PDF](https://arxiv.org/pdf/2604.07666)

## 一句话摘要

Reinforcement Learning with Verifiable Rewards (RLVR) is widely used for post-training Large Language Models, but practical verifiers can make errors.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning with Verifiable Rewards (RLVR) is widely used for post-training Large Language Models, but practical verifiers can make errors. We study how the rate and structure of reward noise affect RLVR in code generation, with a preliminary scientific-reasoning check. In multi-seed Qwen3 8B experiments on MBPP, mean validation reward over two fixed late evaluations is within 1 percentage point of the clean baseline at the tested resampled group-rollout noise rates through 20%, and within about 2 points at 30%. Confidence intervals allow larger losses; these point estimates do not establish a general tolerance threshold. We also examine full-program pass@k, four controlled noise structures, two model-based verifiers, and policy models from three families spanning 4B-9B parameters. We derive conditional advantage distributions for symmetric and asymmetric group noise, including retained format penalties, and show why clipping limits simple gradient-scaling arguments. The analysis identifies information preserved by whole-group corruption and limits on interpreting our asymmetric sweep as a precision-recall comparison. Overall, the results indicate that imperfect verification can support effective RLVR in the tested settings, while aggregate error rates alone do not characterize the learning signal.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andreas Plesner, Francisco Guzm\'an, Anish Athalye
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
