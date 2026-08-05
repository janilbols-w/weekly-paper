---
title: "Energy Efficiency of Locally Deployed LLMs: A Preliminary Quantitative GPU Power Benchmark on Consumer Hardware"
description: "在单张 RTX 4060 Ti 上对 9 个 1B–7B 开源 LLM 进行 Ollama 推理能耗测试，同时报告功率、每提示/每输出 token 能耗与吞吐，结果显示架构和量化方式比参数量更能解释能效差异。"
---

**评分：50/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.00008) · [PDF](https://arxiv.org/pdf/2608.00008)

## 一句话摘要

在单张 RTX 4060 Ti 上对 9 个 1B–7B 开源 LLM 进行 Ollama 推理能耗测试，同时报告功率、每提示/每输出 token 能耗与吞吐，结果显示架构和量化方式比参数量更能解释能效差异。

## 为什么值得关注

它把本地部署的比较指标从单纯吞吐扩展到 J/token，并揭示推理模式、量化和模型架构会显著改变成本，适合用于端侧选型与容量规划。

## 摘要原文

The local deployment of large language models (LLMs) is gaining traction due to privacy concerns and the desire for on-premise inference. However, the energy costs on consumer hardware remain poorly characterized, as most benchmarks focus solely on accuracy. This paper presents a reproducible, hardware-level energy benchmark of nine open-source LLMs (1B to 7B parameters) executed on a single consumer GPU (RTX 4060Ti 16GB). Using the Ollama inference engine, GPU power draw was sampled at 2Hz via nvidia-smi across a fixed prompt set. We evaluate mean/peak power, total energy per prompt (J/prompt), energy per output token (J/token), and throughput (tok/s). Our findings suggest that factors beyond raw parameter count, including model architecture and quantization strategy, drive energy efficiency. Specifically, gemma3:1b and llama3.2:1b achieve the lowest energy cost (0.56 J/token and 0.65 J/token) and the highest throughput (>170 tok/s). In contrast, the 7B-Mistral model consumes up to 4.4x more energy per token than the most efficient model. Notably, qwen3.5:2b exhibits anomalously high per-prompt energy due to extended internal reasoning, highlighting the need to distinguish between token generation modes in efficiency metrics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata
- 限制：仅覆盖单一消费级 GPU、固定提示集和 2Hz 功耗采样；内部推理长度会混淆每提示能耗，结论尚不能直接外推到数据中心 GPU 或在线并发负载。

## 元数据

- 作者：Philipp M. Z\"ahl, Anika Hennig
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
