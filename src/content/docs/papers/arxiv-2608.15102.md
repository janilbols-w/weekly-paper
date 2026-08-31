---
title: "A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models"
description: "We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisition."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2608.15102) · [PDF](https://arxiv.org/pdf/2608.15102)

## 一句话摘要

We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisition.

## 为什么值得关注

待编辑增强。

## 摘要原文

We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisition. Inspired by the Declarative-Procedural framework, we analyze lexical, grammatical, and syntactic processing in a decoder-only English-German MoE Transformer trained under sequential language exposure. We construct a probe-based validation set and extract token-level routing distributions to quantify category-dependent specialisation using mutual information, routing entropy, and Jensen-Shannon distance. The curriculum-trained model exhibits a peak mutual information of 0.1148 at layer 5, indicating category-dependent differences in routing distributions across linguistic categories. Surprisingly, a no-curriculum baseline trained on mixed English-German data shows stronger aggregate specialisation, reaching a peak mutual information of 0.2599 at the same layer. These results suggest that interpretable linguistic organization emerges within MoE routing patterns even without sequential language exposure. A replication at a second training seed shows that the no-curriculum condition's specialisation concentrates on a single language whose identity is seed-dependent, whereas the curriculum consistently yields a stable, language-balanced routing profile; rather than uniformly increasing specialisation, staged bilingual exposure reduces single-language dominance. The official Github repository: https://github.com/Amrit828/DP-Theory-MOE-Interpretability-Research

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Amrit Gopinath, Raghul, Durairaj Thenmozhi
- 发布：2026-08-15；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Amrit828/DP-Theory-MOE-Interpretability-Research](https://github.com/Amrit828/DP-Theory-MOE-Interpretability-Research)
- 阅读深度：metadata
