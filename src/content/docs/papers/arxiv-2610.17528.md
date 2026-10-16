---
title: "ATTUNE: Agentic Throughput Tuning for LLM Training"
description: "Training recipes are tuned by hand for one model, cluster and workload, and every new model, accelerator, framework version or dataset means tuning again."
---

**评分：51/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](http://arxiv.org/abs/2610.17528v1) · [PDF](https://arxiv.org/pdf/2610.17528v1)

## 一句话摘要

Training recipes are tuned by hand for one model, cluster and workload, and every new model, accelerator, framework version or dataset means tuning again.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training recipes are tuned by hand for one model, cluster and workload, and every new model, accelerator, framework version or dataset means tuning again. Automated tuners search a fixed space of knobs and check only that a job runs, yet a configuration can run to completion while it silently changes training. ATTUNE is a single coding agent that tunes any working recipe for the workload and stack at hand, unattended, within a GPU-hour budget the user sets. It diagnoses each run and changes one lever at a time, guided by a catalog of lessons from past campaigns, and ships a recipe only if it passes a correctness gate: a configuration check against objective-changing settings and known stack defects, and a convergence check of its loss curve against the baseline's. On four held-out models at 64-128 GPUs, ATTUNE raises mean throughput over the strongest public recipe run on our stack by 6.7% on Llama-3.1-405B (best campaign 11.9%) and 33.9% on GLM-4.5 (54.7%), whose public recipe was written for H100. It keeps Mixtral-8x22B's recipe, where nothing it finds clears the noise band. Under a common GPU-hour budget it beats OptiCo, Bayesian optimization and random search on GLM-4.5 and MiniMax-M2; on GLM-4.5 its mean gain is more than four times the best alternative's at less than half the GPU-hours, and on both models its tuning pays for itself within a day of training. The gate rejects no legitimate run and catches 16 of 24 faulty runs, missing only ones that barely move the 20-step loss. Ablations tie its best campaigns to one of its search rules: retrying an out-of-memory layout with recomputation. We release ATTUNE's code and TrainingThroughputBench, a leaderboard of the fastest known recipes for MoE models up to 744B parameters on up to 256 GPUs, each with its throughput, cost per million tokens and a passed correctness check, at https://github.com/amazon-science/attune.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Leo Fan, Hongyang Wang, Wenbo Chen, Jingguo Liu, Xian Li, Xuan Wang, Ruochen Wen, Yiming Yan, Hao Wu, Zheshen Wang, Benoit Dumoulin
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/amazon-science/attune](https://github.com/amazon-science/attune)
- 阅读深度：metadata
