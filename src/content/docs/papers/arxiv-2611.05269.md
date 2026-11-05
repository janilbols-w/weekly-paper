---
title: "ToolSched: Resource-Efficient Tool Scheduling for Shared-Host LLM Agents"
description: "Local LLM agents often work on shared hosts."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.05269) · [PDF](https://arxiv.org/pdf/2611.05269)

## 一句话摘要

Local LLM agents often work on shared hosts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Local LLM agents often work on shared hosts. Unlike multi-tenant cloud clusters, these hosts often have tightly bounded memory, CPU, and I/O resources. Concurrent agents frequently suffer from resource contention, leading to failures such as OOM and reduced resource efficiency. Considering that agents' resource demands are bursty and shell command delay is imperceptible to agents, there is a huge scheduling opportunity to arrange when and in what order commands are actually executed. Thus, we present ToolSched, a Shell MCP Server for shared local hosts that serves multiple agents and schedules their operations. ToolSched embeds a resource model into the MCP interface: agents estimate resource demands along with command requests. These hints, together with real-time host resource conditions, determine when commands are actually executed. Internally, ToolSched applies a scheduling algorithm to stagger commands, reducing contention and improving resource utilization. Prediction correction and checkpoint-based recovery mitigate estimation bias and resource errors. Our evaluation on Terminal Bench shows that, compared with unscheduled execution, ToolSched improves resource utilization by 148.4% and end-to-end command throughput by 29.4%, demonstrating its effectiveness and practicality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shucheng Zou, Yuhao Gu, Long Chen, Zhongchun Zheng, BinZe Xie, Xianwei Zhang
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
