---
title: "Stabilizing Knowledge, Promoting Reasoning: Dual-Token Constraints for RLVR"
description: "Reinforcement Learning with Verifiable Rewards (RLVR) has become an effective post-training method for improving the reasoning abilities of Large Language Models (LLMs)."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2507.15778) · [PDF](https://arxiv.org/pdf/2507.15778)

## 一句话摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has become an effective post-training method for improving the reasoning abilities of Large Language Models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning with Verifiable Rewards (RLVR) has become an effective post-training method for improving the reasoning abilities of Large Language Models (LLMs). However, existing methods mainly apply uniform optimization constraints across all tokens, ignoring their heterogeneous roles. Prior work shows that high-entropy tokens are closely tied to reasoning, while low-entropy tokens primarily encode factual knowledge, and recent approaches attempt to exploit this distinction by isolating token updates via masking or asynchronous training. We argue that retaining training signals across token types can lead to more effective learning. To address this, we propose Archer, an entropy-aware RLVR framework with dual-token constraints that preserves joint optimization while modulating update strength across token types. Our method introduces response-level entropy normalization for stable token classification and applies differentiated clipping ranges and KL regularization to encourage exploration on reasoning tokens while preserving knowledge tokens. Experiments on mathematical reasoning and code generation benchmarks show that Archer consistently outperforms strong baselines across multiple model scales, improving both pass@1 and pass@K performance. These results highlight the importance of respecting sequence-level dependencies when designing fine-grained RL optimization strategies for LLMs. The code is available at https://github.com/wizard-III/ArcherCodeR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Runze Liu, Jiakang Wang, Fuzheng Zhang, Xiu Li, Guorui Zhou, Kun Gai, Ling Pan
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/wizard-III/ArcherCodeR](https://github.com/wizard-III/ArcherCodeR)
- 阅读深度：metadata
