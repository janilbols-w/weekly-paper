---
title: "GreenBench: Benchmarking Energy Efficiency and Carbon Footprint of Open-Source LLM Inference on Apple Silicon"
description: "The rapid proliferation of Large Language Models (LLMs) has raised concerns about their environmental impact during inference."
---

**评分：51/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.28667) · [PDF](https://arxiv.org/pdf/2608.28667)

## 一句话摘要

The rapid proliferation of Large Language Models (LLMs) has raised concerns about their environmental impact during inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid proliferation of Large Language Models (LLMs) has raised concerns about their environmental impact during inference. While Green AI research has focused on datacenter GPUs and embedded platforms, the energy profile of LLM inference on Apple Silicon, with its unified memory architecture, remains unstudied. This paper presents GreenBench, a benchmarking framework that evaluates the energy efficiency, throughput, and carbon footprint of five open-source LLMs (3-9B parameters) across three NLP tasks on an Apple M4 Pro with 48 GB unified memory. Using macOS powermetrics for direct power measurement and Ollama's nanosecond-precision timing, we find that the M4 Pro draws only 0.47 W of CPU+GPU package power during sustained inference, with total system power of 8-12 W, achieving 30-40x better energy efficiency per token than datacenter GPUs in single-user deployment. Smaller models (3-3.8B) deliver 2.6-4.2x higher throughput and up to 62% less energy per token than larger models (7-9B). Pareto analysis identifies Qwen 2.5 (7B) as the optimal accuracy-efficiency trade-off at 57% MMLU and 59 tokens/s, while Llama 3.2 (3B) suits latency-critical applications at 175 tokens/s. We provide per-token energy at package and system levels with CO2 estimates for India and US grids.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rajeswari Kannan, Raj Firke, Shreya Bengle, Srushti Deshmukh
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
