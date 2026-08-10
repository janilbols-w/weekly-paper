---
title: "An AI4AI Framework for Visual Token Pruning"
description: "Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.07193) · [PDF](https://arxiv.org/pdf/2608.07193)

## 一句话摘要

Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error. As pruning objectives, budgets, and model architectures diversify, manually navigating the expanding design space becomes increasingly difficult. This paper aims to build an AI4AI framework for visual-token pruning by addressing a natural question: Can large language models automatically design effective visual-token reduction algorithms? Although LLMs possess broad algorithmic knowledge and strong reasoning capabilities, translating such general knowledge into effective solutions for a specialized task remains nontrivial. We argue that the key lies in designing an appropriate search-state representation that connects the internal knowledge of LLMs with the structural requirements and constraints of visual-token pruning. Based on this insight, we propose AutoPrune, a training-free framework for LLM-driven visual-token pruning policy design. At its core, AutoPrune introduces a Token Pruning Domain-Specific Language (TPDSL) comprising 131 reusable atoms for budget control, token scoring, selection constraints, and token reassembly. A key property of TPDSL is that it represents each search state as a residual modification of a strong base policy. This residual formulation narrows the search space and directs the LLM's attention toward the policy components that are most consequential for performance. Experiments on 14 multimodal benchmarks and three MLLM backbones demonstrate the effectiveness, efficiency, and transferability of AutoPrune. Even when removing 94.4% of visual tokens, AutoPrune preserves more than 99% of full-token performance while reducing FLOPs by 9.9x and prefill latency by 6.4x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhen Liu, Wenli Huang, Wei Song, Yuhan Liu, Zhiqin Yang, Jingwen Fu
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
