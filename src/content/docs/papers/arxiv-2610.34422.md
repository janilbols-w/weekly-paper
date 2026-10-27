---
title: "From GPU to TPU with Coding Agents: What Works, What Fails, and What It Costs?"
description: "A coding agent can migrate a machine learning workload, report success, and still change how the model trains."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.34422) · [PDF](https://arxiv.org/pdf/2610.34422)

## 一句话摘要

A coding agent can migrate a machine learning workload, report success, and still change how the model trains.

## 为什么值得关注

待编辑增强。

## 摘要原文

A coding agent can migrate a machine learning workload, report success, and still change how the model trains. Rising compute costs, limited accelerator capacity, and vendor dependence are pushing organizations toward alternatives to graphics processing units (GPUs); a key question is whether agent-generated migrations to tensor processing units (TPUs) can be trusted and at what cost. We build a dataset of 148 PyTorch ML research projects and use Claude Code to migrate ten of them from NVIDIA GPUs to Google Cloud TPUs. We independently assess whether each migration runs, preserves numerical behavior, executes on the intended hardware, maintains the project's goal, and delivers acceptable performance. We also examine failures, human effort, and costs. Eight projects meet our project-goal criterion, and migrations require 2.4 human interventions on average. Of 70 execution attempts, 53 fail (76%), and 26 of these failures (49%) raise no error. The most frequent cause is repeated compilation and other execution inefficiencies, while interactions with third-party libraries can silently change the computation: in one four-chip migration, the agent reports success despite a change in gradient clipping that reduces accuracy from 86.53% to 84.89%. Execution costs vary widely: in one workload, TorchTPU, a PyTorch execution backend for TPUs, trains 1.86 times faster and 25% cheaper per run than the GPU. For practitioners, these findings motivate independent reference runs, verification under the intended hardware configuration, and workload-specific acceptance and stopping criteria that account for both computational and human costs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hui Sun, Anderson Uch\^oa, Wesley K. G. Assun\c{c}\~ao
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
