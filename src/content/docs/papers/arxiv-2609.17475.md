---
title: "JustFit: Just-in-Time State Management for Local LLM Serving"
description: "Local agents need memory for model execution and working history."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.17475) · [PDF](https://arxiv.org/pdf/2609.17475)

## 一句话摘要

Local agents need memory for model execution and working history.

## 为什么值得关注

待编辑增强。

## 摘要原文

Local agents need memory for model execution and working history. We present JustFit, an MLX runtime that coordinates their overlapping allocations: KVExec executes and checkpoints four-bit KV with bounded workspace, PhaseSwap loads phase-dependent components, and StateTrans preserves history across execution modes. With Qwen3.8-27B MXFP4 on a 24 GiB M4 Pro MacBook, JustFit reaches 327,680 retained positions across two requests, 10.67 times the evaluated baseline's 30,720-position single-request record. One request completes the full 262,144-position native window at median 5.986 tokens/s. Each shape completes 16,384 outputs per request in three fresh processes: B1 uses one cold build and two prefix extensions; B2 uses three ordered prefix extensions (Section 4). Image encoding can proceed while preserving a live 196,608-input text request. A controlled, repetitive 32K+6K workload reaches median 18.284 tokens/s at 15,626 MiB; a separate AIME 2026 evaluation scores 29/30. Coordinating execution and state lifetimes makes longer histories feasible on personal hardware.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuhua Chen
- 发布：2026-09-15；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
