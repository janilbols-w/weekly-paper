---
title: "AgentDecarbonizer: Carbon-Aware Execution for AI Agents"
description: "AI agents extend large language models from single prompt-response interactions to long-running, goaldirected workflows that issue many model calls, invoke tools, and interact with external environments."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.20566) · [PDF](https://arxiv.org/pdf/2608.20566)

## 一句话摘要

AI agents extend large language models from single prompt-response interactions to long-running, goaldirected workflows that issue many model calls, invoke tools, and interact with external environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI agents extend large language models from single prompt-response interactions to long-running, goaldirected workflows that issue many model calls, invoke tools, and interact with external environments. These workflows enable tasks such as software repair, data analysis, and experiment management, but their repeated model invocations can incur substantial carbon emissions. This paper characterizes the carbon emissions of OpenClaw agent workloads using WildClawBench, and shows that emissions depend on token consumption, context cache reuse, and the carbon intensity of the grid. Our characterization identifies deadline flexibility as an opportunity for carbon-aware execution: agent tasks can wait for lower-carbon-intensity periods or shift to lower-carbon grids. However, doing so requires handling uncertain execution time for temporal shifting and cached context recomputation during spatial shifting. We present AgentDecarbonizer, a carbon optimizer for AI agents that runs alongside OpenClaw. Given a task prompt and user-specified deadline, AgentDecarbonizer conservatively estimates task duration and selects deadline-feasible execution schedules, while accounting for cache recomputation overhead during spatial shifting. Evaluated on WildClawBench workloads with 60 agent tasks across four grids, AgentDecarbonizer reduces carbon emissions by up to 57.9 % compared with a carbon-agnostic baseline and by up to 37.5 % compared with a baseline that selects the carbon-optimal grid at task start time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: context cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leyi Yan, Shuangning Li, Sihang Liu
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
