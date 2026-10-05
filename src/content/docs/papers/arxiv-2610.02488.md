---
title: "Harnessing LLMs as Agents: What Does It Cost?"
description: "Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model capability do not quantify the computational resources these mechanisms consume."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.02488) · [PDF](https://arxiv.org/pdf/2610.02488)

## 一句话摘要

Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model capability do not quantify the computational resources these mechanisms consume.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model capability do not quantify the computational resources these mechanisms consume. We introduce the Language Model Agent Machine (LAM), a resource-bounded abstraction that fixes the underlying semantic model while explicitly charging harness-level resources. We establish four classes of results. Communication: LAM execution is instancewise equivalent to red--blue pebbling under simultaneous call--transfer budgets, transferring classical I/O lower bounds to context--memory traffic. Access: memory interfaces induce asymptotic separations, including a $\Theta(n)$ gap between random and non-speculative sequential access on pointer chasing. Recomputation: bit-reversal DAGs require $\Theta(n^2/(C+S)+n)$ model calls with context capacity $C$ and persistent-memory capacity $S$, quantifying when stored intermediate state avoids repeated semantic computation. Reliability: we derive tight stage-local sampling bounds, exact imperfect-verification costs, and a Young--Daly-type checkpoint law with a closed-form optimal verification interval. Controlled and held-out experiments on GPT-6 Astra test communication and reliability predictions, including checkpoint optima, policy selection under programmatic checking, and tradeoffs among call granularity, logical input traffic, and reliability on chained MATH tasks. Together, these results provide a resource theory for the computational cost of language-model agent harnesses.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zelin Zhao (Georgia Institute of Technology), Xinyu Guo (Georgia Institute of Technology), Jingyuan Zhang (Georgia Institute of Technology), Yuxuan Zhang (Etude AI), Yongxin Chen (Georgia Institute of Technology)
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
