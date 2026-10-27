---
title: "VETTA: Coordinating Turn- and Token-Level Credit Assignment for Multi-Turn LLM Agents"
description: "Multi-turn LLM agents often receive sparse task feedback across several interactions, while generating each response token by token."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.08402) · [PDF](https://arxiv.org/pdf/2610.08402)

## 一句话摘要

Multi-turn LLM agents often receive sparse task feedback across several interactions, while generating each response token by token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-turn LLM agents often receive sparse task feedback across several interactions, while generating each response token by token. This creates two related credit-assignment questions: which responses helped achieve the outcome, and which generation decisions mattered within each response? Existing methods typically focus on only one level: turn-level methods evaluate complete responses but do not distinguish the decisions within them; token-level methods can propagate feedback across turns but do not explicitly model credit for each response. These complementary limitations motivate learning credit at both levels and coordinating it in a single policy update. We introduce VETTA, a credit assignment method that jointly learns turn- and token-level values through separate heads on a shared lightweight critic. VETTA computes advantages along both temporal sequences and combines each turn advantage with a within-response-centered token residual for PPO updates. Furthermore, to reduce value-learning cost, the critic retains only early Transformer blocks from the pretrained checkpoint used to initialize the actor. Experiments on four agent benchmarks demonstrate VETTA's strong performance. With Qwen2.5-7B-Instruct, VETTA achieves success rates of 95.5% on ALFWorld, 76.0% on WebShop, and 52.2% on ScienceWorld. With Qwen2.5-VL-3B-Instruct, it reaches 84.9% and 80.7% success on Sokoban under sparse and dense rewards, respectively. Critic-depth comparisons further show strong task performance with substantially lower critic-side computation. These results demonstrate that coordinating turn- and token-level credit with a lightweight shared critic improves agent performance while keeping value estimation efficient. Code is available at https://github.com/Jiaju-Chen/VETTA-official.

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

- 作者：Jiaju Chen, Min Yang, Jinghua Piao, Xiaochong Lan, Xu Xia, Xiangnan He, Yong Li
- 发布：2026-10-07；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Jiaju-Chen/VETTA-official](https://github.com/Jiaju-Chen/VETTA-official)
- 阅读深度：metadata
