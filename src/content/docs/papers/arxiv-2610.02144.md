---
title: "Faynt: Scaling and Optimizing Policies for Competitive Melee"
description: "We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02144) · [PDF](https://arxiv.org/pdf/2610.02144)

## 一句话摘要

We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros. Melee, each controlling all 26 characters with a single checkpoint. After reinforcement learning (RL), the 10M wins 240 of 244 same-character games (98.4%) against fourteen specialist and multi-character releases on their supported rosters, with a winning record against every release. These opponents retain 21- or 24-frame action delays; Faynt uses no added delay, and we have not isolated the effect of this difference. In a separate evaluation against a privately supplied zero-delay Slippi-AI model, the 10M wins all 68 games across two conditioning settings. We study architecture, optimization, scaling, and hyperparameter transfer to guide pretraining on approximately 840,000 human replays. Post-training combines rank- and outcome-based curricula, 75M-to-10M distillation, and RL restricted to Fox mirror matches. On the initial 152-game benchmark, the supervised 10M wins 69.7% of games, compared with 45.4% for the pretrained 75M, despite higher overall held-out controller-prediction loss. The weighted validation loss used for supervised checkpoint selection agrees with the win-rate ordering of all four pretrained and supervised policies. After supervised post-training, both models take less damage per minute, build larger early leads, and win more often after losing the first life. Optimized inference on recorded game states averages 5.2 ms per decision for the 10M and 8.7 ms for the 75M on an NVIDIA T4, excluding emulator execution and communication. We open-source the weights, both benchmark suites, and a platform for automated model tournaments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ali Janati, Nikita Kuzmin, Rohit Swamy, Charles Niu
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
