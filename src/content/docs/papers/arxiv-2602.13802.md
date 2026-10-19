---
title: "Learning Agentic Time Series Forecasting via Trajectory Distillation and Memory-Based Reinforcement Learning"
description: "Recent agentic time series forecasting (TSF) approaches use large language models (LLMs) to autonomously orchestrate analytical and forecasting tools and reason about temporal patterns using the resulting evidence."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.13802) · [PDF](https://arxiv.org/pdf/2602.13802)

## 一句话摘要

Recent agentic time series forecasting (TSF) approaches use large language models (LLMs) to autonomously orchestrate analytical and forecasting tools and reason about temporal patterns using the resulting evidence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent agentic time series forecasting (TSF) approaches use large language models (LLMs) to autonomously orchestrate analytical and forecasting tools and reason about temporal patterns using the resulting evidence. However, many such approaches rely on powerful LLMs in training-free, prompt-driven workflows, leaving open whether smaller models can learn these interaction and reasoning capabilities. In this paper, we introduce Cast-R1, an 8Bparameter agentic forecasting model trained through trajectory distillation and multi-turn reinforcement learning with structured memory. First, we develop a forecasting agent harness with specialized analysis and prediction tools to generate multi-turn interaction trajectories using a teacher LLM, which are subsequently evaluated and selected for supervised fine-tuning. Second, we apply group relative policy optimization (GRPO) across multi-turn forecasting episodes, with structured memory preserving diagnostic evidence and intermediate forecasts for state construction. Rewards based on prediction accuracy and temporal structure guide tool selection, model routing, and forecast refinement. A difficulty-aware curriculum combines sample filtering and progressive sample ordering during training. Extensive experiments on multiple datasets demonstrate the effectiveness of Cast-R1. These findings highlight the potential of forecasting-specific post-training to equip smaller LLMs with multi-turn, tool-augmented forecasting capabilities within structured workflows.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoyu Tao, Mingyue Cheng, Yaguo Liu, Xingpeng Gao, Qingsong Wen, Shijin Wang, Enhong chen
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
