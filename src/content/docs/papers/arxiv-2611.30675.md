---
title: "Empirical Margin Sensitivity: An Interventional Neuron-Level Probe of Post-Trained Medical LLMs"
description: "Medical post-training raises benchmark accuracy, but accuracy does not show which internal components a model's decisions depend on, or whether components that support one benchmark also support another."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2611.30675v1) · [PDF](https://arxiv.org/pdf/2611.30675v1)

## 一句话摘要

Medical post-training raises benchmark accuracy, but accuracy does not show which internal components a model's decisions depend on, or whether components that support one benchmark also support another.

## 为什么值得关注

待编辑增强。

## 摘要原文

Medical post-training raises benchmark accuracy, but accuracy does not show which internal components a model's decisions depend on, or whether components that support one benchmark also support another. We apply the weight-space intervention paradigm of ROME and MEMIT at the granularity of one MLP down-projection column. Our measurement, Empirical Margin Sensitivity (EMS), replaces each coordinate magnitude of a column by its mean while preserving the column's sign pattern and L1 scale, and records the resulting change in the logit margin between the correct option and its hardest-wrong competitor. This isolates the margin's dependence on a column's fine-grained coordinate structure while the column stays in place. We discover high-EMS columns (anchors) on MedQA in ten public checkpoints (four general-purpose bases and six medical post-trained variants) across the Gemma, Llama, Qwen, and AFM families, and measure the same columns on MedMCQA and PubMedQA. Mean-ablating each discovered anchor set lowers MedQA accuracy in all six post-trained models, by 6 to 28 points. In the two pure-SFT checkpoints, crushing anchors raises the PubMedQA margin on correctly answered items (negative EMS), and anchors with this property sit significantly deeper than the same model's other anchors; the four checkpoints trained with RL or mixed recipes show positive PubMedQA EMS and no significant depth shift. The depth association recurs in each of three held-out checkpoints. Because the checkpoints differ in data and pipeline as well as objective, we report these as per-checkpoint observations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Aniruddh Shreyas, Aarnav Kembhavi, Minal Moharir
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/aarnav-kembhavi/MEDNSQ-CIRCUITS](https://github.com/aarnav-kembhavi/MEDNSQ-CIRCUITS)
- 阅读深度：metadata
