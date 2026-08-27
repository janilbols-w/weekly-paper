---
title: "RTLGuard: A Lightweight Teacher-Student Defense for Poisoned RTL Code Generation Models"
description: "The rapid advancement of large language models (LLMs) is driving a shift toward automated register transfer level (RTL) code generation, enabling designers to translate high-level specs."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.26049) · [PDF](https://arxiv.org/pdf/2608.26049)

## 一句话摘要

The rapid advancement of large language models (LLMs) is driving a shift toward automated register transfer level (RTL) code generation, enabling designers to translate high-level specs.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid advancement of large language models (LLMs) is driving a shift toward automated register transfer level (RTL) code generation, enabling designers to translate high-level specs. into synthesizable hardware. However, this reliance on pre-trained (3rd-party) fine-tuned models may introduce critical trust issues, as the training data and adaptation process of these models are often opaque. Thus, adversaries (even model providers) may embed hidden backdoor threats during fine-tuning, allowing malicious behavior, e.g., hardware Trojans, to be triggered by seemingly benign prompts given by victim user at inference time. In this paper, we introduce RTLGuard, to mitigate such a trust issue in AI-enabled IC supply chain. Rather than prohibitive computational cost of full-parameter retraining, RTLGuard leverages a teacher-student framework designed to sanitize compromised RTL generation models by (1) fine-tuning a small-scale, "clean" teacher model on a limited set of trusted RTL data, (2) guiding the poisoned target model via a composite teacher-student objective, and (3) incorporating feature alignment and knowledge distillation to suppress malicious behaviors. Our experiments across various LLM architectures demonstrate that RTLGuard significantly reduces the Attack Success Rate (ASR) while preserving the functional correctness and synthesizability of the generated RTL code.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahshid Rezakhani, Kimia Azar, Hadi Kamali
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
