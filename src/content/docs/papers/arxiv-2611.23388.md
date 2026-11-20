---
title: "QDA: Closed-Loop LLM Quantization Design with Agents"
description: "Post-training quantization is the standard way to serve large language models at low cost."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.23388) · [PDF](https://arxiv.org/pdf/2611.23388)

## 一句话摘要

Post-training quantization is the standard way to serve large language models at low cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds lead to better recipes. However, evaluating one quantized reasoning model takes tens of GPU-hours, and combining methods from different codebases means porting each to the new architecture by hand. We present QDA, a system in which an agent designs the recipe for each model and precision. To make evaluation fast, QDA scores each candidate in minutes by its output KL divergence from the original model on reasoning traces that the agent never sees, and checks promising ones with long generations to catch failures such as repetition loops. To make building fast, QDA provides a library of public PTQ methods that are compatible with one another and with new model architectures. Across four reasoning models, QDA improves accuracy over the strongest public recipe by 0.9, 1.4 and 2.2 percentage points on average at W4A16, W4A8 and W3A16, using 64 GPU-hours per search. On the 320B-parameter MoE model GLM-5.3-Flash at NVFP4 W4A4, it recovers 98.3% of the FP8 model's accuracy, against 96.9% for the best vendor checkpoint. Every QDA checkpoint also runs on existing serving kernels with no inference overhead. We will release the library, the evaluator and the harness.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- 发布：2026-11-17；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
