---
title: "Self-Evaluation Is Already There: Eliciting Latent Judge Calibration in Base LLMs with Minimal Data"
description: "Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own output?"
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.05122) · [PDF](https://arxiv.org/pdf/2606.05122)

## 一句话摘要

Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own output?

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly evaluated by other models, raising a natural question: can a model predict how a judge will score its own output? We find that the ability is largely present before any targeted training: prompted few-shot, a base model already predicts an external judge's multi-attribute quality scores on open-ended responses well above chance across three benchmarks. We introduce Self-Evaluation Elicitation (SEE), a method that surfaces this latent ability through a short cycle comprising a calibration-coupled reinforcement learning phase that improves the answer and predicts the judge, followed by a masked distillation phase that sharpens the prediction while leaving the answer untouched. From 160 unique examples, roughly 31x fewer than a reinforcement learning baseline, SEE improves held-out calibration across three benchmarks while preserving answer quality. The elicited self-evaluation is sharply localized within the model's own token distribution and stable across judges it was never trained against, indicating a transferable notion of quality rather than a single judge's preference. These results reframe judge-aligned self-evaluation as a problem of elicitation rather than acquisition.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：XiuYu Zhang, Yi Shan, Junfeng Fang, Zhenkai Liang
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
