---
title: "The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning"
description: "Large language models (LLMs) trained to answer questions are natively poor at teaching."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.06446) · [PDF](https://arxiv.org/pdf/2610.06446)

## 一句话摘要

Large language models (LLMs) trained to answer questions are natively poor at teaching.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) trained to answer questions are natively poor at teaching. Reinforcement Learning (RL) against a simulated student is a promising approach to improve their pedagogy, but existing RL-trained tutors reward the student's success on the tutored problem with the tutor's words still in context. The reward is then easiest to raise by telling the student the answer, and a tuned penalty is needed to reduce telling. Drawing on learning sciences, we introduce a masked near-transfer post-test: the student is tested on an unseen variant of the tutored problem with the tutor's utterances masked, so the reward can rise only through what the student wrote in its own turns. This discourages cognitive offloading by the student and allows the continuous penalty to be replaced by two binary reward gates (factual correctness of tutor response, no solution handover). A leave-one-out ablation shows that the learning-gain reward on its own does not separate teaching from telling: the gates reduce solution handover while the near-transfer post-test improves out-of-domain transfer. Using these reward designs we develop Eduardo, a multi-turn RL recipe for training LLM tutors, and use it to train 4B, 9B, 14B and 27B models from two distinct LLM architectures. Our post-trained Eduardo-27B model matches Gemini-3.1-Pro on MathTutorBench and Claude Opus 4.8 on TutorMoments at 2.4-6.2x fewer thinking tokens than frontier models, which matters for interactive tutoring. Without being named in the reward, the model more than doubles its use of the push-for-justification teacher move while support fading (e.g., assigning independent work), whose payoff lies beyond a single-problem dialog episode, is trained out. We open-source our training environment, an 8,671-problem near-transfer dataset, and trained models for further development.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jakub Macina, Manu Kapur, Mrinmaya Sachan
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
