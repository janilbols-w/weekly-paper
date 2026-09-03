---
title: "GMTRouter: Personalized LLM Router over Multi-turn User Interactions"
description: "Large Language Model (LLM) routing has demonstrated strong capability in balancing response quality with computational cost."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2511.08590) · [PDF](https://arxiv.org/pdf/2511.08590)

## 一句话摘要

Large Language Model (LLM) routing has demonstrated strong capability in balancing response quality with computational cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) routing has demonstrated strong capability in balancing response quality with computational cost. As users exhibit diverse preferences, personalization has attracted increasing attention in LLM routing, since even identical queries may require different models to generate responses tailored to individual needs. However, existing approaches are not fully personalized and often fail to faithfully capture the complex interactions between users and LLMs. Moreover, user preference data is typically scarce and inconsistent in format, which limits the effectiveness of methods that directly leverage user-specific data. To address these challenges, we propose GMTRouter, which represents multi-turn user-LLM interactions as a heterogeneous graph with five node types: user, LLM, query, response and turn, thereby maximally preserving the rich relational structure of the interaction. Through a lightweight inductive graph learning framework combined with a tailored user-conditioned graph sampling mechanism, GMTRouter learns to capture user preferences from few-shot data, enabling effective personalization. Extensive experiments demonstrate that GMTRouter outperforms the strongest baselines, achieving up to a 0.108 absolute improvement in accuracy and a 0.124 improvement in AUC. More importantly, we further demonstrate that GMTRouter can adapt to new users using only few-shot data, without extensive fine-tuning. The code for GMTRouter is publicly available at https://github.com/ulab-uiuc/GMTRouter.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm router
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yihang Sun, Encheng Xie, Tao Feng, Jiaxuan You
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ulab-uiuc/GMTRouter](https://github.com/ulab-uiuc/GMTRouter)
- 阅读深度：metadata
