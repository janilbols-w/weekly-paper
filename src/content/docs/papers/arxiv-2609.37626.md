---
title: "SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving"
description: "No single way of parallelizing attention serves large language models well under all loads."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.37626) · [PDF](https://arxiv.org/pdf/2609.37626)

## 一句话摘要

No single way of parallelizing attention serves large language models well under all loads.

## 为什么值得关注

待编辑增强。

## 摘要原文

No single way of parallelizing attention serves large language models well under all loads. Low concurrency favors tensor parallelism, many independent requests favor data-parallel attention, and long prompts favor context parallelism. Reasoning, agentic, and RL-rollout workloads make a fixed choice untenable: a batch that begins as many short requests ends as a few very long ones, so the best layout changes while the same requests run. Serving engines nevertheless fix one layout at launch, because changing it has meant draining requests and restarting workers. We present SPLASH, a serving system that switches the parallel layout of attention while requests are running. It builds on one observation: modern attention, with few or no KV heads, decouples where a request's KV cache lives from how attention weights are sharded. This has two consequences. First, layouts differ only in who owns the weights and the cache, and most of that state already sits where the next layout needs it; SPLASH reuses it, moves the rest in the background of ongoing inference, and hands off at a batch boundary, making a switch nearly free: its median overhead is under 0.51% of the step it runs in. Second, the decoupling exposes a layout that existing engines lack: Decoupled Ownership Parallelism (DOP) shards attention weights as tensor parallelism does while keeping each request's cache on a single owner as data-parallel attention does. DOP replicates neither, offers 27-60% more KV capacity than data-parallel attention, and gives the scheduler a choice when KV memory limits admission. A transition-aware scheduler follows the best of the four layouts as load changes. On B200 GPUs serving GLM-5.3, SPLASH improves end-to-end serving throughput by 1.3-1.73x over fixed-layout deployments, and the same layout regimes appear with DeepSeek-V3.2 on H200 and GLM-5.3-Flash on DCU.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Chuan Liu, Shuoming Zhang, Zhicheng Li, Qianqi Sun, Ruiyuan Xu, Qiuchu Yu, Xiyu Shi, Huimin Cui, Jiacheng Zhao
- 发布：2026-09-29；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ict-agent/SPLASH-sglang](https://github.com/ict-agent/SPLASH-sglang)
- 阅读深度：metadata
