---
title: "DeltaBox: Millisecond-Scale Sandbox Checkpoint and Rollback for Stateful AI Agents"
description: "Emerging LLM-powered AI agent workloads, such as test-time tree search and reinforcement learning (RL), require high-frequency state exploration, relying on rapid checkpoint/restore (C/R) of the complete sandbox state, including files and process state."
---

**评分：51/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2605.22781) · [PDF](https://arxiv.org/pdf/2605.22781)

## 一句话摘要

Emerging LLM-powered AI agent workloads, such as test-time tree search and reinforcement learning (RL), require high-frequency state exploration, relying on rapid checkpoint/restore (C/R) of the complete sandbox state, including files and process state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging LLM-powered AI agent workloads, such as test-time tree search and reinforcement learning (RL), require high-frequency state exploration, relying on rapid checkpoint/restore (C/R) of the complete sandbox state, including files and process state. Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs. We observe that consecutive sandbox states between checkpoints differ only marginally. Therefore, instead of full duplication, a sandbox should only duplicate the changes between consecutive checkpoints (Key Insight), yet the lack of OS support makes this hard to realize. We propose a new OS-level abstraction, DeltaState, that delivers change-based C/R for agents through co-designed OS mechanisms. First, DeltaFS checkpoints file state by freezing the writable layer and inserting a new one, turning updates into copy-on-write and rollback into a layer switch. Second, DeltaCR quickly restores process state by forking from a frozen template process. A coordinator pairs the two so each checkpoint is one consistent (filesystem, memory) state. Building on these mechanisms, we present DeltaBox, an agent sandbox with millisecond-level C/R. On SWE-bench, DeltaBox hides its checkpoint work (10.83 ms) under inference and rolls back in a mean 1.86 ms, with the same warm-template fork driving low-cost RL rollout fan-out. DeltaBox is open-sourced at https://github.com/delta-box.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yunpeng Dong, Jingkai He, Shiqi Liu, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Baochuan Yang, Yubin Xia, Haibo Chen
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/delta-box](https://github.com/delta-box)
- 阅读深度：metadata
