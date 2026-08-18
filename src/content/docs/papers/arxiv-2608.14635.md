---
title: "Belayer: Efficient Fault Tolerance for LLM Agentic RL Training"
description: "Large language model (LLM) agents are increasingly trained with reinforcement learning in long-horizon, sandboxed environments."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2608.14635) · [PDF](https://arxiv.org/pdf/2608.14635)

## 一句话摘要

Large language model (LLM) agents are increasingly trained with reinforcement learning in long-horizon, sandboxed environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents are increasingly trained with reinforcement learning in long-horizon, sandboxed environments. Unlike conventional RL, agentic RL couples GPU-intensive rollout engines with stateful environment containers whose actions may produce visible side effects, such as file edits, command execution, and dependency installation. A single trajectory can span many rounds of gen- eration and environment interaction, so a component failure can discard completed work or expose the model to an environment state that is inconsistent with its context. However, existing systems lack efficient and correct recovery mechanisms for this distributed execution model. This paper presents Belayer, an efficient fault-tolerant system for LLM agentic RL training. Belayer handles failures in both rollout engines and environment execution while targeting low failure-free overhead. For scoped worker-local rollout failures, Belayer equips each pre-initialized shadow worker with a selective GPU-state reuse protocol that retains independently owned weights and raw KV-arena allocations after owner and GPU health checks, reinitializes worker-local state, and rebuilds request-specific KV contents from logged token prefixes. For environment failures, Belayer introduces full checkpoint and full restore to jointly capture and restore container file-system and runtime state, and coordinates the recovered environment with the LLM context to preserve prefix consistency. An adaptive policy opportunistically overlaps full-state checkpointing with natural LLM inference bubbles when the predicted interval is long enough. Empirical results show low measured overhead during failure-free training, a worker-recovery-time reduction of up to 42 times faster compared with a full engine cold start, and 1.5 to 3.5 times faster recovery from environment failures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiecheng Zhou, Qinghao Hu, Peng Sun, Xingcheng Zhang, Weiming Zhang
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
