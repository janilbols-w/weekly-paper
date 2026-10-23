---
title: "AI Mindmeld: A Latent Interconnect Protocol"
description: "LLMs can act as scientific agents using tools to consult specialists and run experiments."
---

**评分：45/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2610.30215) · [PDF](https://arxiv.org/pdf/2610.30215)

## 一句话摘要

LLMs can act as scientific agents using tools to consult specialists and run experiments.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLMs can act as scientific agents using tools to consult specialists and run experiments. Yet specialist information must enter their context, generally as text, images, audio or video: a bottleneck between models with rich, high-dimensional representations. We advocate direct representation exchange: a mindmeld conveying many properties, including information an LLM would not think to request. It should be extensible to new specialists, flexible across questions and tasks, and compositional across independently connected specialists without joint training. The Latent Interconnect Protocol (LIP) learns connectors mapping specialist representations into LLM internal states. Training only connectors keeps this practical as LLMs grow and evolve. We connect three protein and three small molecule specialists to Gemma 3 (4B and 12B parameters) and Kimi K2.6 (1T total, 32B active), freezing all pretrained models. Independently trained connectors provide useful information without changing the LLM or existing connectors, supporting familiar and new question types about unseen objects. We demonstrate zero-shot transfer to cross-domain tasks without joint training. Task performance and compositionality generally improve with LLM capability, with especially strong gains in zero-shot task transfer. Limitations remain: current LLMs were not trained for specialist representations as native inputs; access does not ensure reliable interpretation, integration or use in reasoning. We call on specialist developers to provide consistent representation interfaces and, especially, on LLM developers to train models to receive, combine and reason with these inputs. These efforts could expand scientific agents' information while preserving conventional tools' flexibility. Data, pretrained connectors, and code for training, evaluation and interactive inference: https://github.com/PolymathicAI/AI-Mindmeld

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Siavash Golkar, Jake Kovalic, Shirley Ho
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/PolymathicAI/AI-Mindmeld](https://github.com/PolymathicAI/AI-Mindmeld)
- 阅读深度：metadata
