---
title: "From Search to Signal: Online Post-Training in Automatic Heuristic Design"
description: "Large language model (LLM)-based automatic heuristic design (AHD) iteratively proposes and refines heuristics, pairing design rationales with executable code."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.39383) · [PDF](https://arxiv.org/pdf/2609.39383)

## 一句话摘要

Large language model (LLM)-based automatic heuristic design (AHD) iteratively proposes and refines heuristics, pairing design rationales with executable code.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM)-based automatic heuristic design (AHD) iteratively proposes and refines heuristics, pairing design rationales with executable code. Task-specific evaluators assess programs; execution outcomes and performance scores guide search. Many AHD systems keep the generator frozen; EvoTune and Co-Evolution of Algorithms and Language Model (CALM) instead update it from evaluated candidates. When such outcomes drive reinforcement learning with verifiable rewards (RLVR), they create a search-coupled loop: the evaluated candidate stream supplies both search-state updates and training signals for the model that generates future candidates. Yet validity and performance do not uniquely determine useful model updates; converting them into learning signals must account for the prompt and evolving search state that produced each candidate. We formulate online post-training of small open-weight LLMs in AHD as context-dependent signal construction and develop alternative mappings from program validity, task performance, and generation context to update signals. Using shared evaluated rollouts and matched update budgets, controlled experiments across AHD tasks and model families compare these mappings with online post-training baselines, testing their effects on validity, performance among valid proposals, and the yield of valid proposals that improve under contextual comparisons. Complementary checkpoint, frozen-search, and live-system evaluations assess whether proposal-level gains appear in updated checkpoint behavior and subsequent search, rather than arising solely from accumulated search state. A resource-matched comparison under pre-specified cost accounting tests whether online updating adds value beyond additional search with a frozen generator. Together, this design avoids treating end-to-end search gains alone as evidence of stronger heuristic-design capabilities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yilun Yuan, Tianyu Zhou, Zhenzhou Tang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
