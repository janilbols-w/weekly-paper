---
title: "AgentPerfBench: A Benchmarking and Evaluation Suite for Inference Performance of Agentic LLMs"
description: "The optimization of LLM serving engines, such as vLLM and SGLang, is largely benchmark-driven: optimizations, scheduling policies, hardware and system designs are all selected based on representative workloads."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.34683) · [PDF](https://arxiv.org/pdf/2609.34683)

## 一句话摘要

The optimization of LLM serving engines, such as vLLM and SGLang, is largely benchmark-driven: optimizations, scheduling policies, hardware and system designs are all selected based on representative workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

The optimization of LLM serving engines, such as vLLM and SGLang, is largely benchmark-driven: optimizations, scheduling policies, hardware and system designs are all selected based on representative workloads. However, a significant mismatch has emerged in the agentic era. Existing benchmarks primarily focus on simple single-turn chatbot workloads. LLM applications are increasingly agentic: coding agents, terminal execution systems, and tool-use agents issue multi-turn requests with growing context lengths. We introduce AgentPerfBench, a benchmark suite for agentic inference. It uses real traces from agentic benchmarks, such as SWE-Bench and TerminalBench, alongside standard chat baselines. This enables benchmarking of models on multi-turn tasks involving tool calling, skill utilization, and increasing context lengths. AgentPerfBench also samples from empirical distributions of input length, output length, and turn count derived from the real traces, generating representative synthetic profiles for cheap and accurate measurements on new hardware. In addition, we further find that several existing benchmarks fail to accurately reflect real hardware performance for two key reasons: 1) they do not account for realistic context-length growth, and 2) they measure inference performance without operating at hardware saturation. We discuss these issues in detail and provide rich kernel-level Nsight Compute (NCU) traces to construct a new multi-dimensional roofline model that captures hardware-system limitations in both memory bandwidth and memory capacity footprint. The benchmarking suite then includes automated scripts to identify potential bottleneck conditions on emerging hardware when evaluated with diverse agentic traces. Together, these contributions quantify the chat-to-agentic gap in current inference benchmarks and characterise per-kernel GPU resource utilisation via roofline analysis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Cheuk Hang Lau, Zeyu Cao, Kevin Wong Cheuk Yin, Yao Lai, Haoran Wu, Nicholas D. Lane, Robert D. Mullins, Ilia Shumailov, Yiren Zhao
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
