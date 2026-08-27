---
title: "Beyond Scaling: Self-Evolving LLM Agents for Hardware Kernel Optimization via an Experience-Driven Workflow and Experience Graph Memory"
description: "Hardware kernel optimization requires repeated compilation, correctness testing, profiling, and revision."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.25570) · [PDF](https://arxiv.org/pdf/2608.25570)

## 一句话摘要

Hardware kernel optimization requires repeated compilation, correctness testing, profiling, and revision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hardware kernel optimization requires repeated compilation, correctness testing, profiling, and revision. LLM agents can automate parts of this process, and stronger foundation models, longer context windows, and longer execution horizons have improved optimization within individual tasks. These advances alone do not enable an agent to learn from completed optimization runs. Existing kernel-optimization agents seldom preserve a decision, its observed execution feedback, and the later decisions that use that evidence. Retaining every prior trajectory is also impractical because an expanding history competes with the current task for context. We present KOPE, an experience-driven framework for hardware kernel optimization. KOPE records optimization trajectories with correctness and performance feedback in Experience Graph Memory, then uses Active Context Management and Injection to retrieve relevant experience under a fixed token budget. The graph retains decision order, observed outcomes, and alternative branches, allowing evidence collected on the target hardware to inform later optimization steps and tasks. Under the same GLM-5.2 setting, the geometric mean of KOPE's per-operator speedups is $1.54\times$ that of CANNBot, the strongest competing baseline. In a complete 53-operator ablation, Active Context Management and Injection raises pass rate from 60.0\% to 84.6\%, increases the evaluator-reported positive-field geometric mean from 0.0382 to 0.0661, and reduces optimization token consumption from 15.9B to 1.113B tokens relative to passive agent-led context construction. Enabling Experience Graph Memory raises full-suite pass rate from 55.2\% to 84.6\% and yields a $1.43\times$ geometric-mean speedup on valid timing comparisons. These results support continual optimization through external experience while the foundation model remains fixed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siyuan Chen, Runlin Hou, Shenxiu Wu, Yansong Sun, Junming Cao, Yiyu Zhang, Shudi Shao, Junhao Qiu, Zhichao Lu, Qingfu Zhang
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
