---
title: "When Perplexity Lies: Generation-Focused Distillation of Hybrid Sequence Models"
description: "Converting a pretrained Transformer into a more efficient hybrid model through distillation offers a promising approach to reducing inference costs."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.26556) · [PDF](https://arxiv.org/pdf/2603.26556)

## 一句话摘要

Converting a pretrained Transformer into a more efficient hybrid model through distillation offers a promising approach to reducing inference costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Converting a pretrained Transformer into a more efficient hybrid model through distillation offers a promising approach to reducing inference costs. However, achieving high-quality generation in distilled models requires careful joint design of both the student architecture and the distillation process. Many prior distillation works evaluate downstream multiple-choice benchmarks by ranking candidate answers with log-likelihood rather than requiring autoregressive generation, which can obscure important differences in model quality. For example, on overlapping benchmarks, we show that a 7B distilled model that nearly matches its teacher to within 0.2 pp under log-likelihood scoring falls behind by 20.8 pp when it must generate answers autoregressively. We investigate this phenomenon with GenDistill, a multi-stage pipeline we designed for distilling a pretrained Transformer into an efficient Hybrid Kimi Delta Attention (Hybrid-KDA) student. Using it as a controlled testbed on Qwen3-0.6B, we systematically ablate six design axes (training objective, loss masking, training duration, dataset selection, parameter freezing, and architecture choice) and evaluate every choice under both log-likelihood and generation-based protocols. We find that log-likelihood-based evaluation consistently underestimates the gap between teacher and student, and can in some cases reverse the ranking of design choices, so conclusions drawn from perplexity-only evaluation may be misleading. Among the factors we study, dataset selection, completion-only masking, and freezing attention layers during post-training have the largest impact on generation quality. Our best distillation recipe, using a Hybrid-KDA model as the student, retains 86-90% of teacher accuracy on knowledge benchmarks while reducing KV cache memory by up to 75% and improving time-to-first-token by 2-4x at 128K-token contexts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Juan Gabriel Kostelec, Qinghai Guo
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
