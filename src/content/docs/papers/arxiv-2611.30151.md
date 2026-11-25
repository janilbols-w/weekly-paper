---
title: "Revisiting Continual Learning in Language Models: A Three-Interface Diagnosis of Stability and Plasticity"
description: "Continual learning in language models is commonly studied in the incremental learning (IL) setting, where a model learns a sequence of tasks and is evaluated through its final classifier or language-model (LM) head."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.30151) · [PDF](https://arxiv.org/pdf/2611.30151)

## 一句话摘要

Continual learning in language models is commonly studied in the incremental learning (IL) setting, where a model learns a sequence of tasks and is evaluated through its final classifier or language-model (LM) head.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continual learning in language models is commonly studied in the incremental learning (IL) setting, where a model learns a sequence of tasks and is evaluated through its final classifier or language-model (LM) head. This interface, however, does not indicate where forgetting occurs: a drop in accuracy may reflect representation degradation in the backbone, readout mismatch in the head, or both. We therefore argue that backward transfer (BWT) and forward transfer (FWT) should be interpreted as interface-dependent quantities rather than as single modellevel properties. We study three evaluation interfaces: the trained head, which is updated sequentially with the backbone; a probe newly trained on frozen backbone features; and a classifier-free backbone diagnostic. They measure deployed performance, recoverability under a new readout, and representation separability, respectively. Across class-incremental experiments with encoder and decoder language backbones, plus task-incremental sanity checks, conclusions about forgetting and plasticity change with the interface: the trained head often indicates severe forgetting, the probe near-complete recoverability, and the backbone diagnostic intermediate representation drift with a consistent negative relation between stability and plasticity. This relation holds for clustering-free diagnostics such as nearest-class-mean accuracy and across five clustering algorithms and three metrics. Finally, Just LM-Head Tuning (JLT), a head-only intervention on a fixed incrementally trained backbone, recovers 96-99% of the gap to joint training for replayand distillation-based methods but only about three quarters for plain sequential fine-tuning, suggesting that many failures attributed to catastrophic forgetting reflect head-backbone mismatch plus partial representation drift. Our results call for reporting where forgetting is measured, not only how much.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Keuntae Kim, Beomseok Lee, Hyunwoo Kim, Yong Suk Choi
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
