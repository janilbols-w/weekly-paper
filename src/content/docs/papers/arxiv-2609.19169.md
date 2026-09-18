---
title: "SiliconBench: Speed, Memory, and Fidelity for LLM Serving on Unified-Memory Desktops"
description: "Concurrent local LLM serving on unified-memory desktops must preserve memory headroom and output fidelity, which speed-only rankings overlook."
---

**评分：55/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.19169) · [PDF](https://arxiv.org/pdf/2609.19169)

## 一句话摘要

Concurrent local LLM serving on unified-memory desktops must preserve memory headroom and output fidelity, which speed-only rankings overlook.

## 为什么值得关注

待编辑增强。

## 摘要原文

Concurrent local LLM serving on unified-memory desktops must preserve memory headroom and output fidelity, which speed-only rankings overlook. We introduce SiliconBench, which evaluates nine Apple Silicon serving engines through three lenses: speed, memory, and fidelity. We evaluate chat and agent serving on Qwen3, Qwen3.5, and Gemma 4. We use a classification task to check for quality regressions against an NVIDIA reference. DGX Spark provides a complementary serving-performance reference. Three desiderata guide interpretation: serving architecture readiness, memory discipline, and multi-node scaling. On Qwen3-0.6B, vllm-metal alone more than doubles throughput on both workloads from concurrency 1 to 16. CUDA vLLM and SGLang show stronger concurrency scaling on the same prompts. Explicit memory budgets do not guarantee memory headroom: two stacks complete every request while memory use approaches physical capacity and throughput declines. The newer model architectures have narrower engine support. Their evaluated implementations match the fidelity reference. Only three stacks satisfy the completion, fidelity, and model-coverage gates. Comparisons on larger dense and MoE models reinforce the importance of scheduling prompt processing alongside ongoing generation: vllm-metal's packed prefill-decode path maintains lower first-token latency than omlx under concurrent load. In the tested two-machine configurations, tensor parallelism over Thunderbolt RDMA scales while pipeline parallelism over TCP regresses. We release benchmark code, per-run results, and maintenance journals, supported by a workflow combining bounded agent fixes with human review.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ranran Haoran Zhang, Aysa Xuemo Fan, David Munhá Correia, Alex Cheema, Rui Zhang
- 发布：2026-09-12；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/WindChimeRan/SiliconBench](https://github.com/WindChimeRan/SiliconBench)
- 阅读深度：metadata
