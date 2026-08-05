---
title: "TempoNet: Slack-Quantized Transformer-Guided Reinforcement Scheduler for Adaptive Deadline-Centric Real-Time Dispatchs"
description: "Real-time schedulers must reason about tight deadlines under strict compute budgets."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.18109) · [PDF](https://arxiv.org/pdf/2602.18109)

## 一句话摘要

Real-time schedulers must reason about tight deadlines under strict compute budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Real-time schedulers must reason about tight deadlines under strict compute budgets. We present TempoNet, a reinforcement learning scheduler that pairs a permutation-invariant Transformer with a deep Q-approximation. An Urgency Tokenizer discretizes temporal slack into learnable embeddings, stabilizing value learning and capturing deadline proximity. A latency-aware sparse attention stack with blockwise top-k selection and locality-sensitive chunking enables global reasoning over unordered task sets with near-linear scaling and sub-millisecond inference. A multicore mapping layer converts contextualized Q-scores into processor assignments through masked-greedy selection or differentiable matching. Extensive evaluations on industrial mixed-criticality traces and large multiprocessor settings show consistent gains in deadline fulfillment over analytic schedulers and neural baselines, together with improved optimization stability. Diagnostics include sensitivity analyses for slack quantization, attention-driven policy interpretation, hardware-in-the-loop and kernel micro-benchmarks, and robustness under stress with simple runtime mitigations; we also report sample-efficiency benefits from behavioral-cloning pretraining and compatibility with an actor-critic variant without altering the inference pipeline. These results establish a practical framework for Transformer-based decision making in high-throughput real-time scheduling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rong Fu, Yibo Meng, Zeyu Zhang, Ziming Guo, Jia Yee Tan, Xiaojing Du, Simon James Fong
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
