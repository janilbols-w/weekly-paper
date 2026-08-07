---
title: "On the Limits of Layer Pruning for Generative Reasoning in Large Language Models"
description: "Recent work has shown that layer pruning can effectively compress large language models (LLMs) while retaining strong performance on classification benchmarks, often with little or no finetuning."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.01997) · [PDF](https://arxiv.org/pdf/2602.01997)

## 一句话摘要

Recent work has shown that layer pruning can effectively compress large language models (LLMs) while retaining strong performance on classification benchmarks, often with little or no finetuning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent work has shown that layer pruning can effectively compress large language models (LLMs) while retaining strong performance on classification benchmarks, often with little or no finetuning. In contrast, generative reasoning tasks, such as GSM8K and HumanEval\textsuperscript{+}, exhibit substantially weaker recovery. We show that beyond surface-level text degradation, pruning leads to a loss of key algorithmic capabilities, including arithmetic computation and balanced parenthesis generation. Under realistic post-training constraints, using a single 80GB GPU and without access to pretraining-scale data or compute, we evaluate a simple recovery strategy based on supervised finetuning with self-generated responses. This approach recovers up to 90\% of baseline performance on classification tasks, but recovery for generative reasoning remains limited. We further find that this gap persists even under a favorable task-aligned recovery setting, where pruned models are fully finetuned on self-generated GSM8K responses, suggesting that the degradation is not merely due to generic instruction data or parameter-efficient tuning. As complementary evidence, we analyze a depth-pruned model trained with nearly 100B post-pruning tokens and find that deficits persist even on simple arithmetic tasks that do not require multi-step generation. Overall, we characterize practical recovery limits of layer pruning for generative reasoning and provide guidance on when depth reduction is effective under constrained post-training regimes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Safal Shrestha, Anubhav Shrestha, Minwu Kim, Aadim Nepal, Keith Ross
- 发布：2026-08-05；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
