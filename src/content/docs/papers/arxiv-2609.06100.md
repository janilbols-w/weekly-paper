---
title: "VERPO: Verified Evidence Regularized Policy Optimization"
description: "Verifiable rewards improve language models through reliable task-level feedback, but methods based on Group Relative Policy Optimization (GRPO) apply a sequence-level advantage uniformly across all tokens."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06100) · [PDF](https://arxiv.org/pdf/2609.06100)

## 一句话摘要

Verifiable rewards improve language models through reliable task-level feedback, but methods based on Group Relative Policy Optimization (GRPO) apply a sequence-level advantage uniformly across all tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Verifiable rewards improve language models through reliable task-level feedback, but methods based on Group Relative Policy Optimization (GRPO) apply a sequence-level advantage uniformly across all tokens. This coarse credit assignment reinforces or penalizes entire responses without identifying which local decisions to preserve, reinforce, or revise. Conversely, evidence-conditioned self-distillation provides denser token-level supervision, yet teacher imitation can transfer stylistic artifacts and miscalibrated confidence that destabilize training when misaligned with task success. We introduce VERPO, which converts evidence-conditioned guidance into reward-aligned token-level credit assignment while retaining the outcome objective. VERPO decomposes teacher guidance into an evidence-free reference term and signed, evidence-induced corrections at each token. A stopped controller combines selective acceptance, token-wise localization, and cost-aware scaling by balancing alignment with the local GRPO update direction against Fisher movement cost. Furthermore, we introduce Fisher Evidence Contrast (FEC), which attenuates nuisance shifts along an estimated evidence-presence direction through a regularized projection. Across five scientific reasoning and tool-use tasks, VERPO prevents optimization collapse and consistently achieves the highest multi-task average across model backbones, yielding marked improvements particularly on smaller models over strong baselines. Qualitative diagnostics confirm that token acceptance selectively targets reasoning bottlenecks consistent with local reward alignment and Fisher movement cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haijiang Li, Chengyu Lv, Yi Zhang, Rui Qian, Zhibing Zhang, Xiangqing Shen, Junjie Yang, Yuchen Zhang, Wenyuan Jiang, Hanqing Hu, Cangqi Zhou
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
