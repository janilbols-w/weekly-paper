---
title: "VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?"
description: "For years, we have built LLM serving systems like any other critical infrastructure, with a single general-purpose stack hand-tuned over many engineer-years to support every model and workload."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2605.06068) · [PDF](https://arxiv.org/pdf/2605.06068)

## 一句话摘要

For years, we have built LLM serving systems like any other critical infrastructure, with a single general-purpose stack hand-tuned over many engineer-years to support every model and workload.

## 为什么值得关注

待编辑增强。

## 摘要原文

For years, we have built LLM serving systems like any other critical infrastructure, with a single general-purpose stack hand-tuned over many engineer-years to support every model and workload. In this paper, we instead let coding agents build bespoke serving systems for different usage scenarios. We propose VibeServe, the first agentic loop that generates entire LLM serving stacks end-to-end. VibeServe uses an outer loop to plan and track the search over system designs, and an inner loop to implement candidates, check correctness, and measure performance on the target benchmark. In standard serving settings, VibeServe matches vLLM and SGLang on Llama-3.1-8B, and delivers 2.3x the goodput of a tuned SGLang for a 397B MoE model on four AMD MI300As. In five non-standard scenarios, VibeServe outperforms existing systems by exploiting opportunities that generic systems miss, spanning non-standard model architectures, workload knowledge, and hardware-specific optimizations. Together, these results show that coding agents can construct and specialize competitive serving systems across heterogeneous deployment targets. Code is available at https://github.com/uw-syfi/vibesys.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Keisuke Kamahori, Shihang Li, Simon Peter, Baris Kasikci
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/uw-syfi/vibesys](https://github.com/uw-syfi/vibesys)
- 阅读深度：metadata
