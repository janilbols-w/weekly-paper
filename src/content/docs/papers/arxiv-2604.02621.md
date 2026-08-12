---
title: "Reinforcement Learning-based Semi-supervised Knowledge Distillation with LLM-as-a-Judge"
description: "Reinforcement Learning (RL) substantially improves the reasoning capabilities of language models, but most existing RL fine-tuning approaches rely entirely on ground-truth verifiable rewards and thus labeled datasets with verifiable answers."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.02621) · [PDF](https://arxiv.org/pdf/2604.02621)

## 一句话摘要

Reinforcement Learning (RL) substantially improves the reasoning capabilities of language models, but most existing RL fine-tuning approaches rely entirely on ground-truth verifiable rewards and thus labeled datasets with verifiable answers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning (RL) substantially improves the reasoning capabilities of language models, but most existing RL fine-tuning approaches rely entirely on ground-truth verifiable rewards and thus labeled datasets with verifiable answers. To overcome this, we propose a RL framework for reasoning distillation that leverages continuous, LLM-based rewards. Our method employs an efficient mechanism that computes a continuous CoT reward (CCR) directly from a single-token logit of a judge LLM, evaluating the student model's reasoning trajectory. This formulation provides an effective and scalable online training signal that can be applied to large volumes of unlabeled data. We demonstrate that, when paired with a strong judge, simply using CCR achieves performance comparable to that of ground-truth or pseudo-label verifiable rewards, and even surpasses them as the amount of unlabeled data increases. Furthermore, we find that combining them in a semi-supervised setup is highly synergistic: verifiable rewards help stabilize the CCR, while CCR improves the generalizability of verifiable rewards to related tasks. We also provide a comprehensive empirical comparison of various reward sources across multiple model architectures and dataset sizes. Our results show that this semi-supervised approach consistently enhances mathematical reasoning, yielding an absolute improvement of 5-10% on multiple reasoning tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiyang Shen, Lifu Tu, Weiran Wang
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
