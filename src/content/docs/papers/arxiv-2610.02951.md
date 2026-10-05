---
title: "Dynamic Expert Pruning for Multi-Agent Systems"
description: "Mixture-of-Experts (MoE) architectures scale language models efficiently by activating only a few experts per token, but the saving is confined to computation: every expert must stay resident on the accelerator, so memory bounds where these models can be deployed."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02951) · [PDF](https://arxiv.org/pdf/2610.02951)

## 一句话摘要

Mixture-of-Experts (MoE) architectures scale language models efficiently by activating only a few experts per token, but the saving is confined to computation: every expert must stay resident on the accelerator, so memory bounds where these models can be deployed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) architectures scale language models efficiently by activating only a few experts per token, but the saving is confined to computation: every expert must stay resident on the accelerator, so memory bounds where these models can be deployed. Expert pruning reduces this footprint, yet existing methods are static --- a single mask, calibrated offline, is applied to the model for every subsequent request. This assumption can fail when the workload is heterogeneous, most prominently in multi-agent systems, where one backbone serves many tasks and roles at once: our analysis shows that different tasks and roles recruit different experts, while static methods assign one fixed subset to all of them. We therefore propose Dynamic Expert Pruning (DEP), which rests on a finding we establish here: an agent's system and task prompts are by themselves sufficient to identify the experts that agent and its task require, since that text already describes what the agent will do. A lightweight predictor, trained once on workflow transcripts, turns those prompts into a specialized per-request mask in a single forward pass, with no per-configuration calibration. Across diverse tasks and roles, model scales, and MoE architectures, DEP achieves better overall accuracy than static pruning and merging baselines, and generalizes to workflows unseen in training without retraining. Its margin over those baselines is largest when few experts are retained, suggesting that the role specialization inherent to multi-agent systems permits sparser serving than static pruning allows.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jabin Koo, Soheil Abbasloo, Sungjae Lee, Jungseul Ok
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
