---
title: "RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges"
description: "LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.24231) · [PDF](https://arxiv.org/pdf/2608.24231)

## 一句话摘要

LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers. In this work, we eliminate external gold supervision from the RL training reward: the model's own evaluative capability generates learning signals for its optimization -- a closed-loop setting of bounded recursive self-improvement (RSI) termed Recursive Self-Evaluation (RecurSE). We study two central questions: when can self-improvement occur, and when must it stop? First, RecurSE pairs a trainable judge evaluating candidate responses under per-rule rubrics (Pass 1) with a synchronized policy-copy checker that audits the judge's reasoning against meta-rubrics to supply a scalar process reward (Pass 2). To enable learning, interface decoupling structurally isolates the checker's scalar score from the judge's verdict tokens, eliminating a degenerative token-copying shortcut that inflates self-assigned rewards. Second, because unanchored recursive learning is inherently bounded, Pairwise Advantage Validity (PAV) serves as an unbiased validation monitor that jointly tracks judge accuracy and checker fidelity to reliably identify the optimal early-stopping window. Across Qwen3.5-9B, Gemma-4-E4B-it, and Qwen3.6-27B, RecurSE achieves consistent generalization gains across held-out medical, pairwise, summarization, and professional benchmarks. Ablations demonstrate that synchronized judge-checker co-evolution outperforms frozen checkers, external meta-judges, self-consistency, and scaled teacher distillation. Furthermore, preference pairs curated by our judge effectively enhance downstream policy alignment. Bounded RSI for LLM-as-judge is thus viable when self-produced reward validity is explicitly decoupled and monitored.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng, Jieping Ye
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
