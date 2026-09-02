---
title: "SFAD: Speculative Factuality-Aware Decoding"
description: "As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.00796) · [PDF](https://arxiv.org/pdf/2609.00796)

## 一句话摘要

As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications. This task is particularly challenging as it requires balancing factual consistency with generation efficiency. Contrastive decoding methods require dual forward passes (with and without context) to compare model outputs, doubling inference computational overhead, while post-training alignment demands extensive reinforcement learning with substantial computational overhead. To address this challenge, we present \textbf{SFAD}, a speculative decoding framework that enhances contextual faithfulness without inference degradation. We first construct \textbf{ConFide}, a preference dataset with fine-grained atomic perturbations, to train a context-faithful draft model via Direct Preference Optimization. During inference, Epistemic Friction detects potential hallucinations by quantifying distributional tension weighted by specialist certainty. When friction exceeds the threshold, Asymmetric Logit Steering refines the target distribution through residual-based logit injection; otherwise, standard speculation proceeds. Extensive experiments demonstrate that SFAD substantially improves faithfulness while achieving $2.48\times$ speedup, offering a practical solution for efficient LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guanqiao Chen, Di Wang, Lijie Hu
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
