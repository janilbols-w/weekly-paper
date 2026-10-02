---
title: "OneSign: Unifying Sign Language Understanding Tasks with One Model"
description: "SLU encompasses a diverse set of tasks, including ISLR, CSLR, and SLT."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.33090) · [PDF](https://arxiv.org/pdf/2609.33090)

## 一句话摘要

SLU encompasses a diverse set of tasks, including ISLR, CSLR, and SLT.

## 为什么值得关注

待编辑增强。

## 摘要原文

SLU encompasses a diverse set of tasks, including ISLR, CSLR, and SLT. Although these tasks share basic semantic and linguistic foundations, they are typically addressed with task-specific architectures and training pipelines, which hinders knowledge sharing and requires costly pretraining and finetuning for each task. In this paper, we focus on two aspects of SLU tasks: (1) training and inference pipelines are highly fragmented: most methods rely on pretraining on large-scale SL datasets followed by task- or dataset-specific finetuning, which leads to multiple specialized models rather than a single checkpoint. (2) current LLM-based methods may overlook the inherent modality discrepancy between sign and text tokens, simply concatenating them and processing both modalities with the same decoder layers. In this paper, we present OneSign, a unified framework that addresses multiple SLU tasks within a single model and a single checkpoint. OneSign reformulates ISLR, CSLR, and SLT under a single training paradigm. To accommodate the heterogeneous characteristics of sign and text representations, we introduce a Modality-Adaptive Mixture-of-Experts (MA-MoE) architecture, consisting of a shared expert and modality-specific experts for sign and text tokens. A modality router dynamically activates the corresponding experts, and their outputs are aggregated to form the final token representations. By enabling modality-dependent expert specialization while preserving a shared expert path, MA-MoE can effectively model the modality differences between continuous sign representations and discrete text tokens. Extensive experiments on multiple benchmarks demonstrate that OneSign achieves competitive or state-of-the-art performance on several benchmarks, highlighting its effectiveness as a unified SLU model. Datasets are available at : https://github.com/gswycf/OneSign.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shiwei Gan, Yafeng Yin, Xiao Liu, Desibieer Tuerdaken, Lei Xie, Sanglu Lu
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/gswycf/OneSign](https://github.com/gswycf/OneSign)
- 阅读深度：metadata
