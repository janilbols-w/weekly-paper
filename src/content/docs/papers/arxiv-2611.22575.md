---
title: "Do LLMs Understand Network Traces? A Comparative Study of Reasoning over Raw and Filtered Traffic Data"
description: "The effective delivery and monitoring of ICT services rely heavily on network traffic analysis."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2611.22575) · [PDF](https://arxiv.org/pdf/2611.22575)

## 一句话摘要

The effective delivery and monitoring of ICT services rely heavily on network traffic analysis.

## 为什么值得关注

待编辑增强。

## 摘要原文

The effective delivery and monitoring of ICT services rely heavily on network traffic analysis. However, interpreting complex packet captures remains a challenging task that requires substantial technical expertise. Large language models (LLMs) offer promising opportunities to automate network traffic in- vestigation, yet their reliability in packet-level field extraction and flow-level sequence reconstruction remains an open research question. This study proposes a reproducible, question-answering- based evaluation methodology to assess the capabilities of LLMs in network trace analysis. Using real-world benign traffic from the CICIDS2017 dataset, we evaluate multiple models against a human-generated ground truth, comparing their performance on raw textual traffic dumps and protocol-filtered representations. Model responses are assessed through an automated LLM- as-a-judge pipeline, validated against human evaluations. The results demonstrate that protocol filtering significantly reduces prompt overhead while improving answer accuracy by reducing incorrect responses. These findings highlight the importance of protocol-aware traffic filtering as an effective optimization for improving the efficiency and reliability of LLM-assisted network management.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: trace analysis
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Irene Gos\'alvez-White, Roberto Mag\'an-Carri\'on, Carlota de la Vega-Soriano, Pedro Garc\'ia-Teodoro
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
