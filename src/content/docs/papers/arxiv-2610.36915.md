---
title: "Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG"
description: "When the sources retrieved for a query disagree, the right response depends on why they disagree: a question with several valid answers, a contested topic, stale information and a false source each call for different behaviour."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.36915) · [PDF](https://arxiv.org/pdf/2610.36915)

## 一句话摘要

When the sources retrieved for a query disagree, the right response depends on why they disagree: a question with several valid answers, a contested topic, stale information and a false source each call for different behaviour.

## 为什么值得关注

待编辑增强。

## 摘要原文

When the sources retrieved for a query disagree, the right response depends on why they disagree: a question with several valid answers, a contested topic, stale information and a false source each call for different behaviour. Cattan et al. (2025) showed that telling a generator the conflict type improves its responses by about 24 points, but that predicting the type is hard even for frontier LLMs. We study whether typed decision models, which return probabilities over fixed options in a single forward pass instead of generating text, can do this classification fast and cheaply. Using the CONFLICTS benchmark and the original paper's prompt verbatim, we evaluate all 11 decision models served by one commercial inference gateway, from 7 providers, against Gemini models on identical inputs. Asked directly, the decision models reach 50.0--67.0% accuracy; 10 of the 11 match or exceed Gemini 2.5 Flash, the paper's model (61.3%), at 4--39x lower billed cost (2 were free) and 2.6--6.0x lower latency. The current Gemini 3.8 Flash (70.0%) is significantly more accurate than 8 of them, but sending each decision model's least confident quarter of queries to it gives a cascade statistically tied with it for 8 of the 11, at 25--37% of its cost. End to end, answers generated with the types of 10 of the 11 follow the expected behaviour as often as with the LLM's types. Decomposing the taxonomy into yes/no questions lowers accuracy for every model, and a repair fitted on one model does not transfer. Pre-specified diagnostics show that dates play no measurable role and that sensitivity to source order varies widely between models. Decision models detect a planted false source less reliably than the LLM as hard labels, but their probabilities still separate planted from clean sources. We release code, prompts and all model outputs at https://github.com/Parv17k/decision-models-conflict-typing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference gateway
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Parv Khatri, Harshul Jain, Mehak Kapoor, Tanya Sah
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Parv17k/decision-models-conflict-typing](https://github.com/Parv17k/decision-models-conflict-typing)
- 阅读深度：metadata
