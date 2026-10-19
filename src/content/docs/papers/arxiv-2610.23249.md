---
title: "Who Pays for Efficient Inference? Confidence-Based Small-to-Large LLM Routing Across Tasks and Languages"
description: "Small-to-large language model routing can reduce inference cost by escalating difficult inputs while retaining easier ones on a smaller model."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.23249) · [PDF](https://arxiv.org/pdf/2610.23249)

## 一句话摘要

Small-to-large language model routing can reduce inference cost by escalating difficult inputs while retaining easier ones on a smaller model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small-to-large language model routing can reduce inference cost by escalating difficult inputs while retaining easier ones on a smaller model. Its success, however, depends on identifying examples that benefit from escalation, and the reliability of confidence across multilingual tasks remains unclear. We present a systematic evaluation of confidence-based routing across three model families, four languages, and three task types, covering 72 model, dataset, language, and scale configurations and 42,288 predictions. We compare global confidence routing with random routing, equal-quota confidence routing, and an oracle upper bound. Confidence identifies beneficial escalations on the Belebele reading comprehension and SIB-200 topic classification datasets, with mean correction-detection AUCs of 0.612 and 0.705. At 50% escalation, it improves over random routing by 1.40--4.67 percentage points on Belebele and 2.54--5.63 points on SIB-200. In contrast, the mean AUC on the MMLU-ProX-Lite knowledge and reasoning dataset is only 0.510, and routing provides no consistent improvement over random selection because small models often remain highly confident while incorrect. Global confidence routing also creates language escalation gaps up to 30.33 percentage points, whereas equal-quota routing removes this disparity with little aggregate accuracy cost. These results show that confidence routing is task-dependent and can allocate computation unevenly across languages. Code is available at https://github.com/sabbir5622r/multilingual-llm-routing

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Md Sabbir Hossen, Anichur Rahman, Pabon Shaha, Airin Afroj Aishi, Andrew H. Sung, Md Shohel Rana
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/sabbir5622r/multilingual-llm-routing](https://github.com/sabbir5622r/multilingual-llm-routing)
- 阅读深度：metadata
