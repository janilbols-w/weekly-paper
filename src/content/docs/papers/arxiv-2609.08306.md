---
title: "HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving"
description: "We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.08306) · [PDF](https://arxiv.org/pdf/2609.08306)

## 一句话摘要

We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence. Existing defenses embed traps inside model memory or rebuild deception at the protocol layer, leaving the serving tier unprotected and feeding nothing back into detection. HoneyRoute couples (i) a streaming router (a frozen 0.8B-embedding backbone with per-domain MLP heads), (ii) a dual-implementation honeypot (a rule/prompt-engineered code honeypot or a dedicated same-family replica), and (iii) an analysis loop that converts trapped interactions into attacker fingerprints for router retraining. On a production trace plus a seven-domain attack corpus, the router reaches F1=.911 at 38 ms median added latency, matching 96% of a two-tier guard-LLM cascade's F1 at 1/385 of its latency with 0% evasion under 13 adversarial transformations; diverting the malicious share cuts production-model token consumption under concurrent flooding with real GCG-suffix payloads by 97.8%; the trained replica agrees with the production model on 92.9% of benign holdout requests, while naive unconditional bait injection collapses to 7.6% and selective camouflaged injection recovers to 88.9%, mapping the recoverable fidelity-traceability frontier; and a loop-trained correction head cuts misrouting of legitimate security research 9x while raising detection F1 to .933.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Han Jin
- 发布：2026-09-08；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
