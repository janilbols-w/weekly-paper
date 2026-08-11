---
title: "Search-G1: Grounded Search Agents via Representation-Based Intrinsic Rewards"
description: "Search-augmented language agents should retrieve external information only when necessary and ground their answers in retrieved evidence."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.07531) · [PDF](https://arxiv.org/pdf/2608.07531)

## 一句话摘要

Search-augmented language agents should retrieve external information only when necessary and ground their answers in retrieved evidence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Search-augmented language agents should retrieve external information only when necessary and ground their answers in retrieved evidence. Existing external rewards provide either sparse outcome supervision or richer feedback from process annotations and LLM judges. Outcome rewards scale readily but cannot distinguish grounded retrieval from redundant search, whereas richer signals require costly annotation or inference during training. Internal rewards based on policy-side signals such as entropy, likelihood, or information gain are graded and inexpensive to evaluate, yet mainly reflect model confidence rather than evidence grounding. We propose Search-G1, a representation-based intrinsic reward framework that measures the operational grounding of an agent's answers through two intervention-calibrated readouts. A prompt-state readout predicts closed-book sufficiency, whose complement defines policy-relative retrieval necessity; an answer-commit readout estimates evidence reliance from answer-stage sensitivity to evidence deletion. Together, they provide additional credit to correct searched trajectories when retrieval is estimated necessary and the answer is evidence-sensitive, favor correct direct answers when closed-book knowledge suffices, and penalize repeated search. After calibration, reward scoring requires neither process annotations nor LLM-as-judge inference during policy optimization. Because reinforcement learning changes policy representations, Search-G1 periodically refits both readouts on trajectories from the latest checkpoint, allowing the reward to co-evolve with the policy. Experiments across multiple search-based question-answering benchmarks and two model scales show that Search-G1 improves the grounding--search-cost trade-off, producing shorter response-side trajectories at competitive task accuracy. Code is available at https://github.com/Rosy0912/Search-G1.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Cheng Ruoxi, Ma Haoxuan, Zhang Hongyi, Zhang Junming, Duan Ranjie, Xia Qiaolin, Wang Hao, Lu Yu, Shi Haibo, Ma Xingjun
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Rosy0912/Search-G1](https://github.com/Rosy0912/Search-G1)
- 阅读深度：metadata
