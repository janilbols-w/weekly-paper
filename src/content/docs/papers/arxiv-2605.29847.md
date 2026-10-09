---
title: "EvoRubric: Self-Evolving Rubric-Driven RL for Open-Ended Generation"
description: "Reinforcement Learning (RL) has advanced Large Language Models (LLMs) in verifiable domains, while open-ended generation remains challenging due to the absence of definitive rewards."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2605.29847) · [PDF](https://arxiv.org/pdf/2605.29847)

## 一句话摘要

Reinforcement Learning (RL) has advanced Large Language Models (LLMs) in verifiable domains, while open-ended generation remains challenging due to the absence of definitive rewards.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning (RL) has advanced Large Language Models (LLMs) in verifiable domains, while open-ended generation remains challenging due to the absence of definitive rewards. Rubric-based RL provides explicit evaluation criteria, but learning to construct these criteria remains challenging when final-answer correctness is not verifiable. We propose EvoRubric, a co-evolutionary RL framework that combines criterion-validity feedback, response discrimination, and peer agreement to learn rubrics for open-ended generation. A shared policy acts as both a Reasoner and a Rubric Generator, using its current responses and historical rubrics to discover new evaluation dimensions. To combine adaptive rubric discovery with a stable validity check, a frozen copy of the initial policy serves as the Meta-Verifier, while a frozen Grader scores responses against the retained criteria. Discriminative feedback, Leave-One-Out peer consensus, and a persistent memory pool transform this feedback into complementary rewards that jointly optimize both policy roles, closing the loop between response improvement and rubric discovery. EvoRubric improves over matched static and external evolving-rubric baselines across five benchmarks in Medical, Writing, and Science. Across three training seeds, it achieves five-benchmark averages of 56.28 at 8B and 61.13 at 14B, exceeding the strongest matched baselines by 3.09 and 2.06 points, respectively. Human audits assess criterion validity and response quality, and experiments with expert-initialized rubrics demonstrate compatibility with human priors.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory pool
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xin Guan, Xiaomeng Hu, Shen Huang, Zhenyi Wang, Bo Zhang, Zijian Li, Pengjun Xie, Bo Liu, Jiuxin Cao
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
