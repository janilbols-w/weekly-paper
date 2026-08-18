---
title: "LOCAL: Enabling Learning On-device Contiguously for Agent LLMs"
description: "On-device LLM agents interact repeatedly with users on local hardware, producing private traces that are valuable for adaptation but should not be sent to a remote trainer."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.15241) · [PDF](https://arxiv.org/pdf/2608.15241)

## 一句话摘要

On-device LLM agents interact repeatedly with users on local hardware, producing private traces that are valuable for adaptation but should not be sent to a remote trainer.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device LLM agents interact repeatedly with users on local hardware, producing private traces that are valuable for adaptation but should not be sent to a remote trainer. Ideally, such agents would learn contiguously---adapting from every interaction without pausing or suspending user-facing inference---yet existing inference runtimes assume stable weights and existing RL systems assume separated resources, so neither can support this continuity. We present LOCAL, the first single-GPU runtime that enables contiguous on-device learning for LLM agents. The key insight is that GPU scheduling, adapter version management, and KV-cache validity cannot be handled by independent subsystems: adapter updates invalidate cached KV tensors from older versions, and cache retention affects the memory available for training. LOCAL makes adapter version, task priority, and cache state visible to three cooperating components---a cooperative scheduler, a version-aware KV-cache manager, and a multi-agent model runtime---that share this state to keep scheduling, execution, and cache maintenance mutually consistent. On a single 24 GB GPU with 7B-class models, LOCAL lowers foreground queue-wait p95 by 3.1x over FIFO, lowers p95 time-to-first-token (TTFT) by 1.55x versus non-preemptible training, cuts post-publish first-hit prefill p99 by 25.6% and cross-agent TTFT p99 by 21.9%, and keeps background learning progressing under tight KV budgets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xinxin Liu, Jiaxin Li, Zibo Wang, Yun Ji, Zhangqi Zhu, Qing Hu, Zhibin Wang, Rong Gu, Sheng Zhong, Chen Tian
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
