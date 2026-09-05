---
title: "GreenBench: Benchmarking Energy Efficiency and Carbon Footprint of Open-Source LLM Inference on Apple Silicon"
description: "GreenBench 面向 Apple Silicon 上的开源 LLM 推理，同时测量能耗、吞吐与碳排。作者在配备 48 GB 统一内存的 M4 Pro 上测试 5 个 3B—9B 模型和 3 类 NLP 任务；摘要报告整机功耗为 8—12 W，小模型相较 7B—9B 模型可取得 2.6—4.2 倍吞吐，并最多降低 62% 的单 token 能耗。"
---

**评分：51/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.28667) · [PDF](https://arxiv.org/pdf/2608.28667)

## 一句话摘要

GreenBench 面向 Apple Silicon 上的开源 LLM 推理，同时测量能耗、吞吐与碳排。作者在配备 48 GB 统一内存的 M4 Pro 上测试 5 个 3B—9B 模型和 3 类 NLP 任务；摘要报告整机功耗为 8—12 W，小模型相较 7B—9B 模型可取得 2.6—4.2 倍吞吐，并最多降低 62% 的单 token 能耗。

## 为什么值得关注

该工作补充了数据中心 GPU 之外的本地推理能效证据，并把模型规模、吞吐、准确率与电网碳强度放在同一评估框架中，可用于边缘部署和单用户服务的硬件选型。

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
- 限制：结论来自单台 M4 Pro、5 个中小规模模型和 3 类任务，不能直接外推到多用户连续批处理、服务器级负载或其他 Apple 芯片。摘要中的数据中心 GPU 能效对比也缺少统一硬件、负载与测量口径细节。

## 元数据

- 作者：Rajeswari Kannan, Raj Firke, Shreya Bengle, Srushti Deshmukh
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
