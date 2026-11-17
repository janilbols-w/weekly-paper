---
title: "BigCodeArena: Unveiling More Reliable Human Preferences in Code Generation via Execution"
description: "Crowdsourced model evaluation platforms, such as Chatbot Arena, enable real-time evaluation from human perspectives to assess the quality of model responses."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2510.08697) · [PDF](https://arxiv.org/pdf/2510.08697)

## 一句话摘要

Crowdsourced model evaluation platforms, such as Chatbot Arena, enable real-time evaluation from human perspectives to assess the quality of model responses.

## 为什么值得关注

待编辑增强。

## 摘要原文

Crowdsourced model evaluation platforms, such as Chatbot Arena, enable real-time evaluation from human perspectives to assess the quality of model responses. In the coding domain, manually examining the quality of LLM-generated content is extremely challenging, as it requires understanding long chunks of raw code and deliberately simulating code execution. To this end, we introduce BigCodeArena, an open human evaluation platform for code generation backed by a comprehensive and on-the-fly execution environment. Built on top of Chatbot Arena, BigCodeArena enables the execution of LLM-generated code and allows humans to interact with the execution process and outcomes. We collected over 14,000 raw code-centric conversation sessions across 10 widely used LLMs, spanning 10 languages and 8 types of execution environments. Among these conversations, we identified more than 4,700 multi-turn samples with pairwise human preferences. Further analysis uncovers underexplored preferences of LLMs in fine-grained domains characterized by tasks, languages, and frameworks. To systematically examine code understanding and generation capabilities of frontier LLMs, we curated two benchmarks based on the collected data, namely BigCodeReward and AutoCodeArena. For BigCodeReward, we post-processed the 4,700 conversations and evaluated the consistency between reward models and human preferences. The evaluation shows that most LLMs have superior performance in judging coding preferences when the execution results are available. Inspired by these findings, we propose AutoCodeArena, an automatic Elo rating benchmark designed to assess the coding quality of LLMs without human involvement. We find that proprietary LLMs like GPT-5, Claude-Sonnet-4, and Claude-Opus-4 still lead in code generation performance among recent emerging models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Terry Yue Zhuo, Xiaolong Jin, Hange Liu, Juyong Jiang, Tianyang Liu, Chen Gong, Bhupesh Bishnoi, Vaisakhi Mishra, Marek Suppa, Noah Ziems, Saiteja Utpala, Ming Xu, Guangyu Song, Kaixin Li, Yuhan Cao, Bo Liu, Zheng Liu, Sabina Abdurakhmanova, Wenhao Yu, Mengzhao Jia, Jihan Yao, Kenneth Hamilton, Kumar Shridhar, Minh Chien Vu, Dingmin Wang, Jiawei Liu, Zijian Wang, Qian Liu, Binyuan Hui, Meg Risdal, Ahsen Khaliq, Atin Sood, Zhenchang Xing, Wasi Uddin Ahmad, John Grundy, David Lo, Banghua Zhu, Xiaoning Du, Torsten Scholak, Leandro von Werra
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
