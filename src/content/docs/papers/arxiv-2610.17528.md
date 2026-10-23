---
title: "ATTUNE: Agentic Throughput Tuning for LLM Training"
description: "The throughput of an LLM training job depends on its recipe: how the model is split across GPUs, how memory is traded for compute, and which kernels and communication overlaps it uses."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.17528) · [PDF](https://arxiv.org/pdf/2610.17528)

## 一句话摘要

The throughput of an LLM training job depends on its recipe: how the model is split across GPUs, how memory is traded for compute, and which kernels and communication overlaps it uses.

## 为什么值得关注

待编辑增强。

## 摘要原文

The throughput of an LLM training job depends on its recipe: how the model is split across GPUs, how memory is traded for compute, and which kernels and communication overlaps it uses. The best recipe changes with every model, accelerator and framework version. Automated tuners search a fixed space of knobs and check only that a job runs, so they miss levers outside that space and can ship a configuration that silently changes training. ATTUNE is a coding agent that tunes any working recipe unattended within a GPU-hour budget. Guided by a skill of search rules, scripts and lessons from past tuning campaigns, it diagnoses each run and changes one lever at a time. A correctness gate outside the agent refuses any argument known to change the training objective. ATTUNE tunes Amazon's production post-training recipes on H100, H200 and B200 clusters, raising throughput by 1.7x on average. It beats the published throughput of four of NVIDIA's own benchmark recipes on NVIDIA's AutoModel framework by 6-17%. On models held out from its development, it improves the strongest public recipes most where they were written for another setting, by up to 2.6x on MiniMax-M2, and least where the vendor tuned them for the same hardware. Given the same GPU-hour budget, it outperforms existing automated tuners, including Bayesian optimization, random search and OptiCo, a recent LLM-agent tuner. Its gain on GLM-4.5 is more than four times the best alternative's. The same coding agent without ATTUNE's skill gains less and fails half its launches. We release ATTUNE at https://github.com/amazon-science/attune and OpenRecipes, a leaderboard of tuned and verified training recipes, at https://openrecipes.ai.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Leo Fan, Hongyang Wang, Wenbo Chen, Jingguo Liu, Xian Li, Xuan Wang, Ruochen Wen, Yiming Yan, Hao Wu, Zheshen Wang, Benoit Dumoulin
- 发布：2026-10-13；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/amazon-science/attune](https://github.com/amazon-science/attune)
- 阅读深度：metadata
