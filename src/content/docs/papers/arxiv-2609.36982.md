---
title: "SRJudge: Empowering Large Language Models with Selective Reasoning for Fine-Grained Knowledge Concept Tagging"
description: "Knowledge concept tagging aims to assign specific concept or topic labels to educational content, which is essential for both educators and learners in traditional and online teaching practices."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.36982) · [PDF](https://arxiv.org/pdf/2609.36982)

## 一句话摘要

Knowledge concept tagging aims to assign specific concept or topic labels to educational content, which is essential for both educators and learners in traditional and online teaching practices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge concept tagging aims to assign specific concept or topic labels to educational content, which is essential for both educators and learners in traditional and online teaching practices. Recent work has explored large language models (LLMs) for this task, achieving promising performance. However, LLMs still struggle to select the correct concept from a large-scale candidate set due to the high dimensionality of the decision space. In this paper, we propose a novel three-stage Select-Reason-Judge (SRJudge) framework, which empowers LLMs with selective reasoning capability for fine-grained knowledge concept tagging. Specifically, the Selector in Stage 1 first narrows the candidate concepts to a top-K shortlist by fine-tuning a small language model (SLM), e.g., BERT, since the top-$K$ predictions hit the correct concept in most cases, thereby reducing the decision space of correct candidates. Next, the Stage 2 Reasoner employs a lightweight LLM for refined reasoning over the shortlisted candidates. It further integrates an improved reinforcement learning strategy with a dynamic task-specific reward function and a pruning mechanism to better align with human reasoning preferences. Finally, a larger LLM acts as a judger that evaluates the overall rationality of the reasoning process and its explanations to determine the final output. In addition, we construct two high-quality datasets for further validation, i.e., the biology dataset S_Bio and the physics dataset S_Phy. Experimental results demonstrate that our method consistently outperforms state-of-the-art baselines across benchmark datasets, verifying its effectiveness and superiority. Resources are available at: https://github.com/Nicozwy/SRJudge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhiwei Yang, Jiahua Yang, Huiru Lin, Xing Chen, Quanlong Guan
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Nicozwy/SRJudge](https://github.com/Nicozwy/SRJudge)
- 阅读深度：metadata
