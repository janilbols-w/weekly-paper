---
title: "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR"
description: "Reward hacking is a form of misalignment in which models overoptimize proxy rewards without genuinely solving the underlying task."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.07084) · [PDF](https://arxiv.org/pdf/2603.07084)

## 一句话摘要

Reward hacking is a form of misalignment in which models overoptimize proxy rewards without genuinely solving the underlying task.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reward hacking is a form of misalignment in which models overoptimize proxy rewards without genuinely solving the underlying task. Precisely measuring reward hacking occurrence remains challenging because true task rewards are often expensive or impossible to compute. We introduce Countdown-Code, a minimal environment where models can both solve a mathematical reasoning task and manipulate the test harness. This dual-access design creates a clean separation between proxy rewards (test pass/fail) and true rewards (mathematical correctness), enabling accurate measurement of reward-hacking rates. Using this environment, we study reward hacking in open-weight LLMs and find that such behaviors can be unintentionally learned during supervised fine-tuning (SFT) when even a small fraction of reward-hacking trajectories leak into training data. As little as 1\% contamination in distillation SFT data is sufficient for models to internalize reward hacking which resurfaces during subsequent reinforcement learning (RL). We further show that RL amplifies misalignment and drives its generalization beyond the original domain. We open-source our environment and code to facilitate future research on reward hacking in LLMs. Our results reveal a previously underexplored pathway through which reward hacking can emerge and persist in LLMs, underscoring the need for more rigorous validation of synthetic SFT data. Code is available at https://github.com/zohaib-khan5040/Countdown-Code.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Muhammad Khalifa, Zohaib Khan, Omer Tafveez, Hao Peng, Lu Wang
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zohaib-khan5040/Countdown-Code](https://github.com/zohaib-khan5040/Countdown-Code)
- 阅读深度：metadata
