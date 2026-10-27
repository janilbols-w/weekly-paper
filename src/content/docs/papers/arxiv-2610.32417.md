---
title: "Measuring the Energy Cost of Completing Tasks with Quantized Language-Model Agents"
description: "Quantization reduces the memory and energy needed to serve large language models (LLMs) and AI agents for coding and data analysis can now run on locally hosted LLMs."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.32417) · [PDF](https://arxiv.org/pdf/2610.32417)

## 一句话摘要

Quantization reduces the memory and energy needed to serve large language models (LLMs) and AI agents for coding and data analysis can now run on locally hosted LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization reduces the memory and energy needed to serve large language models (LLMs) and AI agents for coding and data analysis can now run on locally hosted LLMs. In practice, this benefit is commonly benchmarked per output token. Yet an agent calls its model repeatedly, runs tools, and revises its work, and quantization can change both how much the agent generates and whether it succeeds. Existing energy studies either compare quantized models on single requests or measure agents at one fixed precision, overlooking how a change in precision plays out across a complete agent task. To address this gap, this paper presents the first characterization of the task-level energy trade-offs of model quantization in locally hosted agents. We develop 29 agent tasks with automatic pass/fail checks in six families, ranging from single-answer SQL analytics to multi-step repository bug fixing, and measure CPU and GPU energy per output token and per completed task for 4-bit and 8-bit versions of two open-weight models on bare-metal NVIDIA A100 nodes with llama$.$cpp. Our findings reveal that 4-bit precision generally saves energy per token, though whether it saves energy per completed task is task dependent and changes with the model and the execution budget (i.e., limits on turns, tokens, and time). We trace this discrepancy to the extra tokens needed to complete a task in full, which translates into using up to 3.5 times as much energy per completed task. These findings offer actionable guidance for developers and operators choosing model precision for agents, showing how tokens per completed task, set against the per-token saving, reveal whether lower precision completes the work with less energy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Stephen Abkin, Aldric Yang, Alex Flesher, Nitheesh Kodarapu, Deepak Panigrahy, Aakash Tyagi, David Kebo Houngninou
- 发布：2026-10-26；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
