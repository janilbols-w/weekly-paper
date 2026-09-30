---
title: "Don't stop me now: How Validation Criteria Affect Checkpoint Selection and Early Stopping"
description: "Checkpoint selection is a standard component of neural network training, yet the validation criterion used to select a checkpoint is often chosen heuristically."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2602.22107) · [PDF](https://arxiv.org/pdf/2602.22107)

## 一句话摘要

Checkpoint selection is a standard component of neural network training, yet the validation criterion used to select a checkpoint is often chosen heuristically.

## 为什么值得关注

待编辑增强。

## 摘要原文

Checkpoint selection is a standard component of neural network training, yet the validation criterion used to select a checkpoint is often chosen heuristically. Moreover, the same criterion may be used either only to rank checkpoints after completion of a predefined training run or also to determine when training should stop, thereby affecting both the selected checkpoint and the set of checkpoints available for selection. In this work, we systematically investigate the role of validation criteria under these two settings. We separately vary the training loss, the validation criterion, and the target evaluation metric, and compare post-hoc checkpoint selection, in which training proceeds for all predefined epochs, with patience-based early stopping, in which the validation criterion also controls training termination. We consider three Cross-Entropy, C-Loss, and PolyLoss as training losses, and accuracy, macro-F1, and Matthews correlation coefficient as target metrics. Selection quality is assessed through the relative gap between the test performance of the validation-selected checkpoint and the best-observed test performance for the same target metric over the complete predefined training run.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andrea Apicella, Francesco Isgr\`o, Andrea Pollastro, Roberto Prevete
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
