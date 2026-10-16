---
title: "Beyond the Trial-and-Error Loop: Hybrid Projection and Automated Tuning for Distributed Training"
description: "Configuring distributed LLM training across hundreds of GPUs requires jointly optimizing tensor, pipeline, expert, context, and data parallelism alongside micro-batch size, recomputation, sharding, and overlap, a combinatorial space where memory legality can hinge on a single byte of activation accounting."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.19423) · [PDF](https://arxiv.org/pdf/2610.19423)

## 一句话摘要

Configuring distributed LLM training across hundreds of GPUs requires jointly optimizing tensor, pipeline, expert, context, and data parallelism alongside micro-batch size, recomputation, sharding, and overlap, a combinatorial space where memory legality can hinge on a single byte of activation accounting.

## 为什么值得关注

待编辑增强。

## 摘要原文

Configuring distributed LLM training across hundreds of GPUs requires jointly optimizing tensor, pipeline, expert, context, and data parallelism alongside micro-batch size, recomputation, sharding, and overlap, a combinatorial space where memory legality can hinge on a single byte of activation accounting. Today, teams navigate it through expensive multi-node trial and error, burning GPU-hours on crashes and suboptimal recipes. We present Primus Projection, which closes this loop with two coupled components. First, a hybrid projection engine that measures what it can and simulates what it cannot: GPU microbenchmarks on as few as a single device capture compute kernels and any in-scope communication; a sub-node downscale-measure-upscale workflow analytically restores out-of-scope collectives, FSDP overlap, and the full pipeline schedule at the multi-node target. A pure simulation mode runs entirely on CPU, enabling pre-silicon planning without any GPU. Second, the Primus Tuning Agent treats the projection engine as a fast scoring oracle (seconds per candidate instead of tens of minutes) and uses it to drive an intelligent search over the configuration space. A deterministic seed planner sweeps single axes; an LLM investigation loop proposes cross-axis combinations the planner cannot reach, with an analytic memory pre-filter that rejects infeasible candidates before any GPU time is spent. Validated on Llama 3.1 (dense) and Mixtral 8x22B (MoE) across two GPU generations, all projections stay within ~10% of measured multi-node throughput, and fidelity holds at production scale: 4.7% error on DeepSeek V3 671B at 1,024 GPUs and 1.9% on Qwen3-235B-A22B at 256 GPUs. In a Mixtral 8x22B case study, the Primus Tuning Agent discovers a configuration delivering +27% throughput over the published 4-node BF16 reference at the same scale, in under 30 minutes of single-node exploration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anshu Raina, Peyman Razaghi, Yuankai Chen, Cheng Yao, Yao Fu, Vidushi Goyal, Devang Patel, Wen Xie, Zhenyu Gu, Emad Barsoum
- 发布：2026-10-14；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
