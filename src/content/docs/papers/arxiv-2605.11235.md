---
title: "Internalizing Curriculum Judgment for LLM Reinforcement Fine-Tuning"
description: "In LLM Reinforcement Fine-Tuning (RFT), curriculum learning drives both efficiency and performance."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.11235) · [PDF](https://arxiv.org/pdf/2605.11235)

## 一句话摘要

In LLM Reinforcement Fine-Tuning (RFT), curriculum learning drives both efficiency and performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

In LLM Reinforcement Fine-Tuning (RFT), curriculum learning drives both efficiency and performance. Yet, current methods externalize curriculum judgment via handcrafted heuristics or auxiliary models, risking misalignment with the policy's training dynamics. In this paper, we introduce METIS (METacognitive Internalized Self-judgment), a novel framework that internalizes curriculum judgment as a native capability. Leveraging a critical observation that within-prompt reward variance effectively gauges prompt informativeness, METIS predicts this metric based on recent training outcomes as lightweight in-context learning examples. This intrinsic self-judgment then dynamically dictates the training allocation. Moreover, METIS closes the loop between judgment and optimization by jointly optimizing the standard RFT rewards and a self-judgment reward. This allows the policy to learn what to learn next, as a form of metacognition. Across mathematical reasoning, code generation, and agentic function-calling benchmarks, METIS delivers superior performance while achieving up to a 2.1x training speedup, with controlled ablations and in-depth analysis further validating the benefits of internalized curriculum judgment. By bypassing handcrafted heuristics and auxiliary models, our work establishes a simple, closed-loop, and highly efficient curriculum internalization paradigm for LLM reinforcement fine-tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Han Zheng, Yining Ma, Karthick Gunasekaran, Bharathan Balaji, Zheng Du, Shiv Vitaladevuni, Cathy Wu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
