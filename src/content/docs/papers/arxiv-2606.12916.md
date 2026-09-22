---
title: "MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback"
description: "Molecular dynamics (MD) is the canonical in-silico method for atomistic molecular science, simulating molecular behavior from first-principle physics."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2606.12916) · [PDF](https://arxiv.org/pdf/2606.12916)

## 一句话摘要

Molecular dynamics (MD) is the canonical in-silico method for atomistic molecular science, simulating molecular behavior from first-principle physics.

## 为什么值得关注

待编辑增强。

## 摘要原文

Molecular dynamics (MD) is the canonical in-silico method for atomistic molecular science, simulating molecular behavior from first-principle physics. Designing an MD pipeline for a new system requires substantial expert knowledge: running it on even one molecule is expensive, ruling out trial-and-error. We automate this expert pipeline-design process with an LLM agent. Unlike existing MD agents that orchestrate a predefined tool set, we treat pipeline design as open-ended code generation in which the agent's behavior is reshaped online by verbal reward. Specifically, we build MDForge, an LLM agent whose in-context update rule densifies the sparse reward via a multi-agent debate among physics experts. On three SAMPL host-guest binding free-energy benchmarks, MDForge automatically designs MD pipelines competitive with human experts. Deployed on a library of unseen candidate guests, its CB[7] pipeline discovers a novel binder that wet-lab competition NMR confirms is a high-affinity, picomolar CB[7] binder. Our data and code are available at https://github.com/Zehong-Wang/MDForge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zehong Wang, Yijun Ma, Connor R. Schmidt, Tianyi Ma, Weixiang Sun, Ziming Li, Xiaoguang Guo, Chuxu Zhang, Matthew J. Webber, Yanfang Ye
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Zehong-Wang/MDForge](https://github.com/Zehong-Wang/MDForge)
- 阅读深度：metadata
