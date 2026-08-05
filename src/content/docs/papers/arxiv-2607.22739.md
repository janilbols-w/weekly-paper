---
title: "Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features"
description: "We study how far a deliberately simple behavioral-cloning policy can progress in a visually rich first-person game before adding reinforcement learning or explicit memory."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2607.22739) · [PDF](https://arxiv.org/pdf/2607.22739)

## 一句话摘要

We study how far a deliberately simple behavioral-cloning policy can progress in a visually rich first-person game before adding reinforcement learning or explicit memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study how far a deliberately simple behavioral-cloning policy can progress in a visually rich first-person game before adding reinforcement learning or explicit memory. Cortex is a compact Quake policy with 10.98 million trainable parameters in a six-layer transformer over a frozen DINOv3 encoder. It is trained on the Quake subset of the public Pixels2Play corpus: 6,849 recordings (about 474.7 hours), represented as 17.09 million cached decision frames with keyboard and mouse actions. One sampled training epoch uses 517,048 four-frame windows and takes 3.3 minutes of policy-head optimization on one RTX 5080, excluding one-time feature extraction. We evaluate two independent batches of 20 stochastic, 120-second episodes on Quake E1M1. Cortex does not complete the level, but every episode reaches the opening door, button room, and gate descent; 19 of 20 episodes in each batch record at least one kill. Under the same time-controlled harness, released P2P-150M and NitroGen checkpoints remain shallower in five matched-duration episodes each. These comparisons are limited by small reference samples and different native interfaces. Ablations show that denser visual tokens improve combat and survival, while longer optimization and naive action history improve offline metrics without consistently improving play. The remaining failures are consistent with covariate shift and motivate targeted corrective data. We release the policy implementation, checkpoint, and a representative rollout.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dzmitry Malyshau
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
