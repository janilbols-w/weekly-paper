---
title: "FocusAgent: Simple Yet Effective Ways of Trimming the Large Context of Web Agents"
description: "Web agents powered by large language models (LLMs) must process lengthy web page observations to complete user goals; these pages often exceed tens of thousands of tokens."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.03204) · [PDF](https://arxiv.org/pdf/2510.03204)

## 一句话摘要

Web agents powered by large language models (LLMs) must process lengthy web page observations to complete user goals; these pages often exceed tens of thousands of tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Web agents powered by large language models (LLMs) must process lengthy web page observations to complete user goals; these pages often exceed tens of thousands of tokens. This saturates context limits and increases computational cost processing; moreover, processing full pages exposes agents to security risks such as prompt injection. Existing pruning strategies either discard relevant content or retain irrelevant context, leading to suboptimal action prediction. We introduce FocusAgent, a simple yet effective approach that leverages a lightweight LLM retriever to extract the most relevant lines from accessibility tree (AxTree) observations, guided by task goals. By pruning noisy and irrelevant content, FocusAgent enables efficient reasoning while reducing vulnerability to injection attacks. Experiments on WorkArena and WebArena benchmarks show that FocusAgent matches the performance of strong baselines, while reducing observation size by over 50%. Furthermore, a variant of FocusAgent significantly reduces the success rate of prompt-injection attacks, including banner and pop-up attacks, while maintaining task success performance in attack-free settings. Our results highlight that targeted LLM-based retrieval is a practical and robust strategy for building web agents that are efficient, effective, and secure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Imene Kerboua, Sahar Omidi Shayegan, Megh Thakkar, Xing Han L\`u, L\'eo Boisvert, Massimo Caccia, J\'er\'emy Espinas, Alexandre Aussem, V\'eronique Eglin, Alexandre Lacoste
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
