---
title: "ViCo: Visual-oriented Coding with Self-Reflection for Chart Replication"
description: "This paper addresses the challenge of generating high-quality academic charts that match the visual standards of human-authored papers."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.16014) · [PDF](https://arxiv.org/pdf/2609.16014)

## 一句话摘要

This paper addresses the challenge of generating high-quality academic charts that match the visual standards of human-authored papers.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper addresses the challenge of generating high-quality academic charts that match the visual standards of human-authored papers. While existing AI agents can produce well-structured text and code, their generated visualizations often lack the stylistic and semantic fidelity of human designs. Advanced coding agents that employ self-reflection mechanisms exhibit poor visual reasoning and limited reflection following, resulting in sparse reward signals that severely undermine their reinforcement learning (RL). We propose ViCo, a training framework for visual-oriented coding that employs iterative reflections to align generated chart images progressively with the reference. We first introduce a self-supervised warm-up stage, which augments Monte Carlo Tree Search with consistency-based pruning to synthesize high-quality reflection trajectories, ensuring that each coding step strictly follows the outcomes of prior reflections. A multi-step RL algorithm is then developed, using counterfactual baselines to estimate advantage for reflection and action steps within each refinement cycle, thereby addressing the reward sparsity. To enable efficient reward in massive training, we propose an automatic, multifaceted evaluation framework that assesses charts' style, layout, and semantic consistency via a hierarchical heterogeneous layout graph structure. Experiments on three public benchmarks demonstrate that ViCo, trained on an 8B model, achieves performance close to proprietary LLMs with adequate reflection capabilities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaxin Duan, Dian Jiao Shuai Zhao, Jiabing Leng, Yiran Zhang, Feng Huang
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
