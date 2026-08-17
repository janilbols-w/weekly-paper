---
title: "BCIJelly: An integrated ecosystem for brain-computer interface research"
description: "Brain-computer interface (BCI) research relies on multistage computational pipelines, yet progress remains constrained by fragmented data formats, heterogeneous decoder implementations and hardware-specific deployment toolchains, and researchers lack an integrated workflow."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.13576) · [PDF](https://arxiv.org/pdf/2608.13576)

## 一句话摘要

Brain-computer interface (BCI) research relies on multistage computational pipelines, yet progress remains constrained by fragmented data formats, heterogeneous decoder implementations and hardware-specific deployment toolchains, and researchers lack an integrated workflow.

## 为什么值得关注

待编辑增强。

## 摘要原文

Brain-computer interface (BCI) research relies on multistage computational pipelines, yet progress remains constrained by fragmented data formats, heterogeneous decoder implementations and hardware-specific deployment toolchains, and researchers lack an integrated workflow. Here, we fill this gap with BCIJelly, a unified computational ecosystem that integrates 18 curated BCI datasets, 15 benchmark decoders and an algorithmic library of 80 reusable modules, an automated architecture search (AAS) procedure, and hardware-aware deployment through the toChip pipeline within a single Python framework. AAS constructs task-specific decoders without manual architecture design. It is further extended into a closed-loop mode guided by a large language model (LLM), which uses task specifications, module descriptions and search history to support multitask and cross-species decoding. The toChip pipeline compiles trained decoders for execution on neuromorphic chips, enabling energy-efficient deployment for BCI systems. An accompanying visualization software provides a graphical interface to the full workflow, making BCIJelly accessible without programming. We validate BCIJelly across five BCI paradigms (motor, visual, speech, emotion and auditory) with recordings from humans, macaques and mice, and single-task, multitask and cross-species decoding settings. BCIJelly establishes a unified and extensible infrastructure that bridges decoder development and hardware-aware deployment for BCI research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liyuan Han, Xinrui Yang, Tianyu Zheng, Qizhi Yang, Yitao Qin, Liang Chen, Qinglai Wei, Binjie Hong, Xinhe Zhang, Rui Xiong, Yong Gu, Mu-ming Poo, Bo Xu, Chengyu Li, Tielin Zhang
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
