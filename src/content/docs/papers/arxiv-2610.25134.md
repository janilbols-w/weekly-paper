---
title: "TIRE: Top-Down Formula Instantiation with Reliable Execution for Physics Problem Synthesis"
description: "Advancing physics reasoning in large language models requires scalable training data that connect physical laws, concrete problem scenarios, and verifiable numerical answers."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.25134) · [PDF](https://arxiv.org/pdf/2610.25134)

## 一句话摘要

Advancing physics reasoning in large language models requires scalable training data that connect physical laws, concrete problem scenarios, and verifiable numerical answers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Advancing physics reasoning in large language models requires scalable training data that connect physical laws, concrete problem scenarios, and verifiable numerical answers. Expert-designed problems offer top-down control over physical laws, conditions, and scenarios, but require costly human effort. LLM-based synthesis from texts scales efficiently, but model-generated answers and assessments leave supervision vulnerable to hallucinations. We introduce TIRE, a framework for Top-Down Formula Instantiation with Reliable Execution that brings knowledge-driven problem construction to large-scale data generation. Top-down instantiation uses reusable physical formulas and their applicability conditions to control the physical relations and numerical configurations of generated problems. Reliable execution establishes reference answers before problem generation, providing a common numerical foundation for problem construction and teacher distillation. Together, these mechanisms combine control over problem content with execution-grounded supervision for both supervised fine-tuning and reinforcement learning. Using TIRE, we construct TIRE-19k, spanning nine subfields of physics. Across 3 backbone LLMs and 4 benchmarks, TIRE-19k outperforms 5 representative datasets with equal amounts of SFT data, exceeding the strongest baseline by 2.86 percentage points on average. Further GRPO raises Qwen3-8B's average accuracy by 1.52 percentage points over its TIRE-19k SFT checkpoint. These results demonstrate the value of generating physics training data from explicit physical knowledge with reliable execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoyu Wu, Zhaoxin Yu, Xinglin Xiao, Nan Xu
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
