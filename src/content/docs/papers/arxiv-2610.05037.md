---
title: "SparseCraft: Agentic Hardware-Software Co-Optimization for Sparse Computing"
description: "Sparse-accelerator design spaces are usually searched against analytical models, so a design is judged by a model's prediction rather than by a measurement of the hardware."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.05037) · [PDF](https://arxiv.org/pdf/2610.05037)

## 一句话摘要

Sparse-accelerator design spaces are usually searched against analytical models, so a design is judged by a model's prediction rather than by a measurement of the hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse-accelerator design spaces are usually searched against analytical models, so a design is judged by a model's prediction rather than by a measurement of the hardware. SparseCraft is a closed loop on the CHIA framework in which a large language model (LLM) agent co-designs the configuration, memories and sparse-kernel schedule of a Gemmini accelerator. A candidate counts only after it passes a legality check, cycle-accurate simulation, a bit-for-bit comparison of every output and synthesis. Post-synthesis timing analysis checks its clock, and its energy is computed from measured counters, with per-event energies validated against gate-level and SRAM-macro data. We compare the agent with expert Gemmini configurations and with random, greedy and multi-objective TPE search at the agent's budget of 15 evaluations, all measured by the same flow. On a GraphChallenge sparse-DNN layer, the agent's designs reach 159-164$\times$ the inverse energy-delay-area product of stock Gemmini and 2.07-2.14$\times$ that of the best expert configuration. Their Pareto hypervolume is 0.5557-0.5704, against at most 0.2806 for search. On a power-law graph and a pruned BERT layer, the agent raises perf/W by 11.45$\times$ and 4.43$\times$, and held-out transfer shows that its designs specialise to their workload. The loop is also resilient to faulty designs. When a design fails a check, a repair agent diagnoses the failure from its evidence and fixes it automatically, or declines when the only fix would undo the intended change. In a fault-injection benchmark, it fixed every scorable fault at its first attempt.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rajatabha Chakraborty, M P Samartha, Vedant Pahariya, Priyesh Shukla
- 发布：2026-10-06；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
