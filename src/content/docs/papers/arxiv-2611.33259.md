---
title: "Fast and Scalable Abstract Interpretation for Deep Neural Networks"
description: "Abstract interpretation can certify properties of Deep Neural Networks (DNNs), but precise analyses remain expensive."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.33259) · [PDF](https://arxiv.org/pdf/2611.33259)

## 一句话摘要

Abstract interpretation can certify properties of Deep Neural Networks (DNNs), but precise analyses remain expensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Abstract interpretation can certify properties of Deep Neural Networks (DNNs), but precise analyses remain expensive. General implementations repeat work when analyzing the same architecture under different inputs and properties. Interleaving this work with numerical operations limits GPU utilization and restricts how much of the analysis a tensor compiler can process together. We present Scepter, a framework for specializing DNN abstract interpreters through structural semantics. The semantics determine the structure of intermediate abstract values while deferring their numerical evaluation. Structural computations from successive operations can therefore be performed together before certification, generating an executable tensor program. With the abstract interpreter and DNN architecture fixed, the program can be reused with different weights and input regions. We prove that it computes the same bounds as the general interpreter in exact arithmetic. The generated program also exposes operations and their dependencies for tensor compilation and memory planning. We implement Scepter for the tensor programs that Neuton generates from ConstraintFlow specifications. We evaluate Scepter on eight abstract interpreters and 44 DNNs against six baseline systems on GPUs and CPUs. Scepter handles networks with up to 153x as many neurons as the largest completed by the corresponding baselines. It completes DeepPoly on ResNet50 and VGG-16, whereas none of the evaluated DeepPoly baselines completes either network. On configurations completed by both systems, GPU geometric-mean speedups over Neuton range from 11.9x to 44.4x across eight analyses, with a 2.60x geometric-mean reduction in peak memory. In an input-splitting case study, Scepter proves 68 properties for which the baselines time out. Code: https://github.com/uiuc-focal-lab/constraintflow.git

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tensor compiler
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Avaljot Singh, Dushyant Bharadwaj, Yasmin Chandini Sarita, Heng Zhong, Charith Mendis, Gagandeep Singh
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/uiuc-focal-lab/constraintflow.git](https://github.com/uiuc-focal-lab/constraintflow.git)
- 阅读深度：metadata
