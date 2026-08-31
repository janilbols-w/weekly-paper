---
title: "PRISM: Self-Pruning Intrinsic Selection Method for Training-Free Multimodal Data Selection"
description: "Visual instruction tuning adapts pre-trained Multimodal Large Language Models (MLLMs) to follow human instructions for real-world applications."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2502.12119) · [PDF](https://arxiv.org/pdf/2502.12119)

## 一句话摘要

Visual instruction tuning adapts pre-trained Multimodal Large Language Models (MLLMs) to follow human instructions for real-world applications.

## 为什么值得关注

待编辑增强。

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

## 元数据

- 作者：Jinhe Bi, Aniri, Zengjie Jin, Yifan Wang, Danqi Yan, Wenke Huang, Xiaowen Ma, Sikuan Yan, Artur Hecker, Mang Ye, Xun Xiao, Hinrich Schuetze, Volker Tresp, Yunpu Ma
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/bibisbar/PRISM}{this](https://github.com/bibisbar/PRISM}{this)
- 阅读深度：metadata
