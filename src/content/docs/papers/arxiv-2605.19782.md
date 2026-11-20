---
title: "Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization"
description: "LLM discovery and optimization systems are increasingly applied across domains, implementing a common propose-evaluate-revise loop."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2605.19782) · [PDF](https://arxiv.org/pdf/2605.19782)

## 一句话摘要

LLM discovery and optimization systems are increasingly applied across domains, implementing a common propose-evaluate-revise loop.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM discovery and optimization systems are increasingly applied across domains, implementing a common propose-evaluate-revise loop. Such optimization or discovery progresses via context conditioning on received feedback from an environment. However, as modern LLM agents are increasingly complex in their structure, it is difficult to evaluate which components contribute the most, and when and how this exploration may fail. We answer these questions through three controlled experiments. Our findings: (1) In pure black-box optimization, LLMs act as greedy optimizers. (2) In zero-shot kernel generation, providing explicit input-size information has no measurable effect, models converge to the same kernel parameters regardless of size or temperature, as though the size instruction were invisible. Moreover, when tasked to perform kernel optimization for uncommon kernel sizes, performance sharply degrades regardless of the language used. (3) In feedback-loop kernel optimization, CUDA improves monotonically under iterative feedback, while TVM IR actively degrades, which demonstrates that kernel optimization degrades when models operate with low-density language. Our results conclude that LLMs in code optimization tasks highly depend on pretrained priors rather than provided feedback or agentic structure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dmitry Redko (Applied AI Institute), Albert Fazlyev (AI Talent Hub, ITMO University), Konstantin Sozykin (Applied AI Institute), Maria Ivanova (YSDA, Applied AI Institute), Evgeny Burnaev (Applied AI Institute), Egor Shvetsov (Applied AI Institute)
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
