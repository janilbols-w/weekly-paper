---
title: "Enhancing Language Model Reasoning with Structured Multi-Level Modeling"
description: "Inference-time scaling enhances a model's reasoning by extending its chain-of-thought (CoT)."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.00616) · [PDF](https://arxiv.org/pdf/2611.00616)

## 一句话摘要

Inference-time scaling enhances a model's reasoning by extending its chain-of-thought (CoT).

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference-time scaling enhances a model's reasoning by extending its chain-of-thought (CoT). However, existing approaches typically rely on a single policy trained with outcome-reward reinforcement learning (RL), which often suffers from long-horizon plan failures where the implicit plan drifts from valid strategies, especially for small LMs with limited capacity. To address this, we propose Multi-Level Reasoning (MLR), which reformulates long-CoT generation as a two-level stochastic process. A high-level planner generates structured step descriptors specifying both the reasoning mode and the semantic subgoal. The low-level executor then produces detailed reasoning conditioned on these descriptors, forming an alternating plan--execute loop. To maintain scalability, we adopt a minimal design where the base model serves as the low-level policy and a lightweight LoRA module implements the high-level policy. For training, we observe that outcome-reward RL provides sparse and delayed feedback for long trajectories (e.g., several thousand tokens), hindering credit assignment. We therefore introduce iterative Step-DPO, a process-level preference optimization scheme that leverages Twisted Sequential Monte Carlo (TSMC) to provide scalable stepwise supervision. This yields more effective training, improved stability, and higher accuracy. Extensive experiments on challenging math, science, and logical reasoning benchmarks show that, under the same reduced data budget (10% SFT and 5% preference relative to the DeepSeek-R1 distillation setup), MLR outperforms both SFT-based distillation and strong RL/preference-optimization baselines across multiple base models and tasks. Moreover, MLR exhibits slower performance degradation on long-horizon reasoning, demonstrating stronger robustness under extended CoT generation.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siheng Xiong, Ali Payani, Faramarz Fekri
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
