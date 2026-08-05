---
title: "Learning What to Remember: Test-Time Training via Context Distillation"
description: "Effective long-context modeling is not merely about retaining more of the past, but about preserving the information that may prove relevant later."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.01672) · [PDF](https://arxiv.org/pdf/2608.01672)

## 一句话摘要

Effective long-context modeling is not merely about retaining more of the past, but about preserving the information that may prove relevant later.

## 为什么值得关注

待编辑增强。

## 摘要原文

Effective long-context modeling is not merely about retaining more of the past, but about preserving the information that may prove relevant later. Test-time training (TTT) is an appealing approach that performs online parameter updates for long-context modeling, yet existing TTT methods only optimize either reconstruction or online adaptation objectives without considering the future utility of retained information. In this work, we propose \textbf{T}est-\textbf{T}ime \textbf{C}ontext \textbf{D}istillation (TTCD), a TTT framework that introduces a self-supervised objective for allocating limited memory capacity for future use. Specifically, TTCD uses a long-window teacher to supervise the fast weights of a short-window student, where the hidden-state discrepancy between them offers a dense, self-supervised signal guiding the model to memorize the contextual information crucial for future token predictions. We focus on an in-place variant: In-Place TTCD (IP-TTCD), which uses the existing MLP parameters as the fast weights. Experiments on long-context language modeling tasks show IP-TTCD consistently outperforms DeltaNet, Gated DeltaNet, sliding-window attention, and TTT when pre-trained from scratch. Furthermore, IP-TTCD allows pre-trained transformer models to adapt their parameters during inference through continual pre-training, gaining long-context capabilities with only a lightweight architectural augmentation. Our results position TTCD as a step toward architectural continual learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zixuan Wang, Xingyu Dang, Rui-Jie Zhu, Zixin Wen, Hengyu Fu, Wenhao Chai, Jason D. Lee
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
