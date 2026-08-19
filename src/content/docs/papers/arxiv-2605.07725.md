---
title: "SOD: Step-wise On-policy Distillation for Small Language Model Agents"
description: "Tool-integrated reasoning (TIR) is difficult to scale to small language models due to instability in long-horizon tool interactions and limited model capacity."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.07725) · [PDF](https://arxiv.org/pdf/2605.07725)

## 一句话摘要

Tool-integrated reasoning (TIR) is difficult to scale to small language models due to instability in long-horizon tool interactions and limited model capacity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tool-integrated reasoning (TIR) is difficult to scale to small language models due to instability in long-horizon tool interactions and limited model capacity. While reinforcement learning methods like group relative policy optimization provide only sparse outcome-level rewards. Recently, on-policy distillation (OPD) has gained popularity by supplying dense token-level supervision from a teacher on student-generated trajectories. However, our experiments indicate that applying OPD to TIR leads to a critical failure mode: erroneous tool calls tend to cascade across subsequent reasoning steps, progressively amplifying student-teacher divergence and rendering the teacher's token-level supervision increasingly unreliable. To address this, we propose SOD, a step-wise on-policy distillation framework for small language model agents, which adaptively reweights distillation strength at each step based on step-level divergence. Therefore, SOD can attenuate potentially misleading teacher signals in high-divergence regions while preserving dense guidance in well-aligned states. Experiments on challenging math, science, and code benchmarks show that SOD achieves up to 20.86% improvement over the second-best baseline. Notably, our 0.6B student achieves 26.13% on AIME 2025, demonstrating effective transfer of agentic reasoning to lightweight models. Our code is available at https://github.com/YoungZ365/SOD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Qiyong Zhong, Mao Zheng, Mingyang Song, Xin Lin, Jie Sun, Houcheng Jiang, Xiang Wang, Junfeng Fang
- 发布：2026-08-04；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/YoungZ365/SOD](https://github.com/YoungZ365/SOD)
- 阅读深度：metadata
