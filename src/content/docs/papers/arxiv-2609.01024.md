---
title: "PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition"
description: "Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.01024) · [PDF](https://arxiv.org/pdf/2609.01024)

## 一句话摘要

Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token. However, modern MoE inference remains heavily constrained by the rigid, whole-expert abstraction. Existing frameworks manage, schedule, or prune experts as atomic execution units, which fixes the optimization boundary too early and leaves fine-grained intra-expert computational redundancy underexplored. In this work, we present PCoMoE, a path-compositional execution framework that shifts MoE inference from coarse-grained expert selection to fine-grained path composition. PCoMoE incorporates a path-level formulation of expert computation, a compatibility-aware layer-wise pruning strategy to suppress low-value path combinations, and a hardware-friendly execution engine to exploit reusable sub-expert structures under strictly bounded overheads. Experimental results demonstrate that PCoMoE achieves up to a 1.31x end-to-end inference speedup while enhancing model accuracy by 10%. The code is available at https://github.com/gzyyy0/PCoMoE

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ziyan Gan, Fangxin Liu, Chenyang Guan, Junjie Wang, Ning Yang, Haomin Li, Xiang Li, Siran Yang, Jiamang Wang, Lin Qu, Zongwu Wang, Li Jiang, Haibing Guan
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/gzyyy0/PCoMoE](https://github.com/gzyyy0/PCoMoE)
- 阅读深度：metadata
