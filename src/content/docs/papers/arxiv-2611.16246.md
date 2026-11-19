---
title: "What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation"
description: "Vision-language-action (VLA) models drive the robot directly from camera views, yet a VLA alone shows three typical failures."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.16246) · [PDF](https://arxiv.org/pdf/2611.16246)

## 一句话摘要

Vision-language-action (VLA) models drive the robot directly from camera views, yet a VLA alone shows three typical failures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language-action (VLA) models drive the robot directly from camera views, yet a VLA alone shows three typical failures. It walks past the goal, stops before reaching it, and rarely recovers after going off track. Pairing a VLA with a large language model (LLM) planner fixes these failures, but queries the LLM throughout every episode, adding token costs and latency. We introduce Harness-to-Executor (H2E), a task-level distillation method that pairs an LLM planner and a frozen VLA as a heterogeneous training agent, keeps only sessions that reach the goal, and then trains a VLA alone on them so no LLM is used at test time. In these sessions, the planner gives sub-instructions and moves the robot with its own tools, detours are common, and the planner decides when to stop. H2E therefore labels every motion as a VLA action for the original task, whoever made it. It masks the loss on steps moving away from the goal and assigns end labels to states near it, so the VLA learns where the task ends. H2E sets a new state of the art on REVERIE-CE and NavRAG-CE. It raises an 8B VLA's success rate by 15.6% and 11.1% respectively, surpassing a method trained on 10M samples. The distilled VLA exceeds its agent on unseen episodes with zero LLM tokens and runs 3.7 times faster.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu, Bokui Chen, Houde Liu
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
