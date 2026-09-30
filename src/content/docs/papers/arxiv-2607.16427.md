---
title: "Multi-level context Modeling for consistent expert selection in Mixture-of-Experts"
description: "Mixture-of-Experts (MoE) enables efficient scaling of Transformer models by routing tokens to a small subset of experts."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2607.16427) · [PDF](https://arxiv.org/pdf/2607.16427)

## 一句话摘要

Mixture-of-Experts (MoE) enables efficient scaling of Transformer models by routing tokens to a small subset of experts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) enables efficient scaling of Transformer models by routing tokens to a small subset of experts. However, existing routers typically condition expert selection on shallow or isolated token representations, which often produce unstable and semantically inconsistent routing decisions across layers. In this work, we revisit expert selection from a representation perspective and identify context incompleteness as a key bottleneck limiting effective expert specialization. To address this issue, we propose Multi-level Context Fusion MOE (MCF-MOE), a framework that constructs context-aware representations by integrating complementary signals from cross-layer semantic aggregation and local token-level interactions, enabling more informative and consistent expert selection. Experiments on language modeling and understanding benchmarks demonstrate that MCF-MOE consistently improves routing consistency and downstream performance over strong MoE baselines, highlighting the importance of contextual completeness in expert routing. The code is available at https://github.com/shuhanhuang/MCF-MOE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shuhan Huang, Naifan Zhang, Yuanbo Tang, Yang Li, Wai Kin Victor Chan
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/shuhanhuang/MCF-MOE](https://github.com/shuhanhuang/MCF-MOE)
- 阅读深度：metadata
