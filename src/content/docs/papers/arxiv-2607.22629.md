---
title: "Masked Self-Distillation: Internalizing the Chain-of-Thought in Language Models"
description: "Large Reasoning Models produce long, explicit chains of intermediate steps before generating a final answer at inference time."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.22629) · [PDF](https://arxiv.org/pdf/2607.22629)

## 一句话摘要

Large Reasoning Models produce long, explicit chains of intermediate steps before generating a final answer at inference time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Reasoning Models produce long, explicit chains of intermediate steps before generating a final answer at inference time. These intermediate traces dominate latency, memory usage, and serving cost, even though final answer correctness is not causally related to the trace correctness and the trace length is not a reliable indicator of the problem complexity. This raises an obvious question: can the computation expressed in these intermediate tokens be internalized into the parameters of a language model, enabling it to produce answers with much shorter intermediate traces? We propose masked self-distillation, a knowledge-distillation based post-training framework in which copies of the same model are instantiated as teacher and student, and the student model is trained to internalize all or part of the intermediate trace, thus becoming more efficient at inference. We vary the fraction of intermediate trace the student is trained to internalize, interpolating between full internalization and no internalization. We conduct controlled experiments on two reasoning domains: math and graph coloring. We use the masked self-distillation framework to post-train Qwen3-4B & 8B models. Our results demonstrate that this method can be used to improve task performance while increasing inference efficiency across various domains and model sizes. We systematically analyze whether improved efficiency gain in the post-trained models generalize to OOD problems. We find that masked self-distillation models generalize well for in-domain OOD problems, and the masked self-distillation training does not induce catastrophic forgetting in the student model on out-of-domain problems. Furthermore, our ablation study shows that supervised fine-tuning can train models to produce shorter traces, but at the cost of generalization, highlighting the importance of on-policy training in masked self-distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Durgesh Kalwar, Vardhan Palod, Subbarao Kambhampati
- 发布：2026-09-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
