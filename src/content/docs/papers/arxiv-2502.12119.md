---
title: "PRISM: Self-Pruning Intrinsic Selection Method for Training-Free Multimodal Data Selection"
description: "PRISM 将视觉特征分布的各向异性归因于全局语义漂移，并用隐式重中心化提取内在视觉语义，在无需训练代理模型的情况下筛选视觉指令数据。摘要报告，其数据选择与模型微调总耗时为常规流程的 30%，且在八个多模态和三个语言理解基准上优于全量数据微调。"
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2502.12119) · [PDF](https://arxiv.org/pdf/2502.12119)

## 一句话摘要

PRISM 将视觉特征分布的各向异性归因于全局语义漂移，并用隐式重中心化提取内在视觉语义，在无需训练代理模型的情况下筛选视觉指令数据。摘要报告，其数据选择与模型微调总耗时为常规流程的 30%，且在八个多模态和三个语言理解基准上优于全量数据微调。

## 为什么值得关注

它把数据筛选本身的训练与推理开销移出流程，可同时减少多模态模型的数据冗余和微调成本；对 AI 基础设施的价值主要在训练前的数据管线效率，而非在线推理加速。

## 摘要原文

Visual instruction tuning adapts pre-trained Multimodal Large Language Models (MLLMs) to follow human instructions for real-world applications. However, the rapid growth of these datasets introduces significant redundancy, leading to increased computational costs. Existing methods for selecting instruction data aim to prune this redundancy, but predominantly rely on computationally demanding techniques such as proxy-based inference or training-based metrics. Consequently, the substantial computational costs incurred by these selection processes often exacerbate the very efficiency bottlenecks they are intended to resolve, posing a significant challenge to the scalable and effective tuning of MLLMs. To address this challenge, we first identify a critical, yet previously overlooked, factor: the anisotropy inherent in visual feature distributions. We find that this anisotropy induces a \textit{Global Semantic Drift}, and overlooking this phenomenon is a key factor limiting the efficiency of current data selection methods. Motivated by this insight, we devise \textbf{PRISM}, the first training-free framework for efficient visual instruction selection. PRISM surgically removes the corrupting influence of global background features by modeling the intrinsic visual semantics via implicit re-centering. Empirically, PRISM reduces the end-to-end time for data selection and model tuning to just 30\% of conventional pipelines. More remarkably, it achieves this efficiency while simultaneously enhancing performance, surpassing models fine-tuned on the full dataset across eight multimodal and three language understanding benchmarks, culminating in a 101.7\% relative improvement over the baseline. The code is available for access via \href{https://github.com/bibisbar/PRISM}{this repository}.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected
- 限制：摘要中的 101.7% 相对提升未交代所指指标与基线，不能据此推断普遍收益；也未说明数据集、模型规模、保留比例、硬件和选择阶段的独立耗时。效果是否迁移到其他模态或分布仍待验证。

## 元数据

- 作者：Jinhe Bi, Aniri, Zengjie Jin, Yifan Wang, Danqi Yan, Wenke Huang, Xiaowen Ma, Sikuan Yan, Artur Hecker, Mang Ye, Xun Xiao, Hinrich Schuetze, Volker Tresp, Yunpu Ma
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/bibisbar/PRISM}{this](https://github.com/bibisbar/PRISM}{this)
- 阅读深度：abstract
