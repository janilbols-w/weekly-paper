---
title: "AIMER: Calibration-Free Task-Agnostic MoE Expert Pruning"
description: "Mixture-of-Experts (MoE) language models increase parameter capacity without proportional per-token computation, yet deployment still requires storing the full expert pool, making expert pruning important for reducing memory and serving overhead."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.18492) · [PDF](https://arxiv.org/pdf/2603.18492)

## 一句话摘要

Mixture-of-Experts (MoE) language models increase parameter capacity without proportional per-token computation, yet deployment still requires storing the full expert pool, making expert pruning important for reducing memory and serving overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) language models increase parameter capacity without proportional per-token computation, yet deployment still requires storing the full expert pool, making expert pruning important for reducing memory and serving overhead. Existing task-agnostic expert-pruning methods are typically calibration-dependent: they estimate expert importance from routing or activation statistics on a calibration set, making pruning decisions sensitive to calibration-data variation while introducing substantial preprocessing cost. We propose AIMER (\textbf{A}bsolute mean over root mean square \textbf{IM}portance for \textbf{E}xpert \textbf{R}anking), a simple calibration-free criterion that identifies more distinct experts by capturing the concentration pattern of expert weights, making it well suited for task-agnostic expert pruning. Across 7B to 47B MoE language models with distinct architectures and 16 diverse benchmarks, AIMER consistently delivers stronger capability balance across diverse tasks than existing calibration-free methods. Surprisingly, AIMER also achieves better balance than strong calibration-based expert-pruning baselines calibrated on the widely used task-agnostic C4 corpus, while requiring only 0.22--2.06 seconds to score all experts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zongfang Liu, Guangyi Chen, Yifan Shen, Shengkun Tang, Huan Wang, Xin Yuan
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
