---
title: "FronTalk: Benchmarking Front-End Development as Conversational Code Generation with Multi-Modal Feedback"
description: "We present FronTalk, a benchmark for front-end code generation that pioneers the study of a unique interaction dynamic: conversational code generation with multi-modal feedback."
---

**评分：53/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2601.04203) · [PDF](https://arxiv.org/pdf/2601.04203)

## 一句话摘要

We present FronTalk, a benchmark for front-end code generation that pioneers the study of a unique interaction dynamic: conversational code generation with multi-modal feedback.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present FronTalk, a benchmark for front-end code generation that pioneers the study of a unique interaction dynamic: conversational code generation with multi-modal feedback. In front-end development, visual artifacts such as sketches, mockups and annotated creenshots are essential for conveying design intent, yet their role in multi-turn code generation remains largely unexplored. To address this gap, we focus on the front-end development task and curate FronTalk, a collection of 100 multi-turn dialogues derived from real-world websites across diverse domains such as news, finance, and art. Each turn features both a textual instruction and an equivalent visual instruction, each representing the same user intent. To comprehensively evaluate model performance, we propose a novel agent-based evaluation framework leveraging a web agent to simulate users and explore the website, and thus measuring both functional correctness and user experience. Evaluation of 20 models reveals two key challenges that are under-explored systematically in the literature: (1) a significant forgetting issue where models overwrite previously implemented features, resulting in task failures, and (2) a persistent challenge in interpreting visual feedback, especially for open-source vision-language models (VLMs). We propose a strong baseline to tackle the forgetting issue with AceCoder, a method that critiques the implementation of every past instruction using an autonomous web agent. This approach significantly reduces forgetting to nearly zero and improves the performance by up to 9.3% (56.0% to 65.3%). Overall, we aim to provide a solid foundation for future research in front-end development and the general interaction dynamics of multi-turn, multi-modal code generation. Code and data are released at https://github.com/shirley-wu/frontalk

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xueqing Wu, Zihan Xue, Da Yin, Shuyan Zhou, Kai-Wei Chang, Nanyun Peng, Yeming Wen
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/shirley-wu/frontalk](https://github.com/shirley-wu/frontalk)
- 阅读深度：metadata
