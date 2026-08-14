---
title: "LoongReflect: Boosting Long-Horizon Reflection in Search Agents via Global Perspective Distillation"
description: "Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.11967) · [PDF](https://arxiv.org/pdf/2608.11967)

## 一句话摘要

Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model agents increasingly rely on long-horizon reasoning to solve complex tasks involving planning, tool use, and memory. A critical capability in such settings is reflection: assessing trajectory progress, identifying missing evidence and unreliable intermediate states, and deciding whether to continue, revise, or abandon the current branch. Learning effective reflection, however, is challenging because reflection is performed locally within the current branch, whereas its utility can only be determined by its contribution to the final trajectory outcome. This local-global mismatch makes outcome-based reinforcement learning provide only local, sparse and delayed supervision for reflective decisions. To solve these, we propose LoongReflect, a training framework that formulates reflection as a memory-control policy. The agent operates over a reversible trajectory tree using explicit reflect and backtrack actions. Reflection consolidates verified facts, missing evidence, and branch-specific risks into working memory, while backtracking removes an unreliable branch from the active context and preserves a concise corrective lesson. To learn this policy, LoongReflect combines two complementary signals through a look-ahead, extragradient-style coordination mechanism. A fast channel distills globally informed reflective behavior from a privileged teacher, with supervision restricted to reflection and backtracking tokens. A slow channel optimizes complete trajectories using outcome-based GRPO, aligning local control decisions with final task success. Experiments on multi-hop retrieval-augmented generation and mathematical reasoning benchmarks demonstrate consistent improvements over outcome-only reinforcement learning and self-distillation baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhixin Zhang, Xinke Jiang, Zhibang Yang, Weixuan Xu, Guohong Qiu, Xu Chu, Junfeng Zhao, Yasha Wang
- 发布：2026-08-12；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
