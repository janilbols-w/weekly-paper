---
title: "ESSA: Evolutionary Strategies for Scalable Alignment"
description: "Online alignment of large language models (LLMs) is dominated by reinforcement learning from human feedback (RLHF) with gradient-based optimizers such as PPO or GRPO."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2507.04453) · [PDF](https://arxiv.org/pdf/2507.04453)

## 一句话摘要

Online alignment of large language models (LLMs) is dominated by reinforcement learning from human feedback (RLHF) with gradient-based optimizers such as PPO or GRPO.

## 为什么值得关注

待编辑增强。

## 摘要原文

Online alignment of large language models (LLMs) is dominated by reinforcement learning from human feedback (RLHF) with gradient-based optimizers such as PPO or GRPO. While effective, these pipelines require backpropagation through long rollouts, gradient synchronization across devices, and careful hyperparameter tuning, all of which become increasingly costly at scale. We present ESSA (Evolutionary Strategies for Scalable Alignment), a gradient-free online alignment stage that follows supervised fine-tuning (SFT) and replaces the gradient loop with inference-only black-box search. ESSA optimizes only the singular values of low-rank adaptation (LoRA) factors after a short SFT warm-start, restricting the search to a compact, task-aligned subspace where evolutionary search is practical even for 72B-parameter models. Because the loop is inference-only, ESSA is compatible with INT4/INT8 weight quantization and reduces inter-GPU communication to a few bytes per iteration. Across instruction following (IFEval), preference-based assistant tuning (HelpSteer2, HH-RLHF), and mathematical reasoning (GSM8K, MATH500), ESSA matches or exceeds LoRA-GRPO in the reported LoRA comparisons; on GSM8K it also outperforms Online DPO and PPO, while remaining competitive with both methods on IFEval. At scale, ESSA reaches a fixed MATH500 accuracy on Qwen2.5-32B/PRM800K up to 7.8x faster than LoRA-GRPO on 128 GPUs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Daria Korotyshova, Boris Shaposhnikov, Alexey Malakhov, Alexey Khokhulin, Nikita Surnachev, Kirill Ovcharenko, George Bredis, Alexey Gorbatovski, Viacheslav Sinii, Daniil Gavrilov
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
