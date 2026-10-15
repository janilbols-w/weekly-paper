---
title: "REVEAL: Reverse Engineering Agentic Latents from Frontier-Model Traces"
description: "Frontier LLM agents perform complex interactive tasks, but their inference costs motivate transferring their experience to smaller open-source agents."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.16288) · [PDF](https://arxiv.org/pdf/2610.16288)

## 一句话摘要

Frontier LLM agents perform complex interactive tasks, but their inference costs motivate transferring their experience to smaller open-source agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

Frontier LLM agents perform complex interactive tasks, but their inference costs motivate transferring their experience to smaller open-source agents. Distillation and latent communication typically require target-model training or access to source-model internals. We study how textual frontier-model trajectories can provide reusable local controls for a frozen agent. Inspired by protocol reverse engineering, we introduce $\textit{Agentic Latents}$, comprising anchored states and dynamic profiles of feedback--response cycles elicited by replay in the target model. Our training-free framework, $\textbf{REVEAL}$ ($\textbf{REV}$erse $\textbf{E}$ngineering $\textbf{A}$gentic $\textbf{L}$atents), uses these profiles and trajectory outcomes to match and select local events from successful and failed rollouts of the same task and source model. Their response-transition contrasts yield a target-specific steering direction, applied before each response. Within-benchmark evaluations on Terminal-Bench 2.1 and Humanity's Last Exam with tools report higher accuracy than unmodified agents across three targets. Representation analyses and behavioral case studies support reusing frontier-model experience as local activation control.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuetian Du, Meng Wang, Yucheng Wang, Zhangzhe Chen, Wei Wang, Boyu Yang, Weiqi Zhai, Bing Zhao, Ming Kong, Zhan Zhou, Jie Liu, Qiang Zhu
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
