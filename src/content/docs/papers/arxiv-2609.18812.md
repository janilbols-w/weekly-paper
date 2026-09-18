---
title: "WaveTLM: Reliable Time-Series Language Modeling through Task Compilation"
description: "Time-series language models provide a shared natural-language interface across temporal tasks, but plausible text does not guarantee reliable task outputs."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.18812) · [PDF](https://arxiv.org/pdf/2609.18812)

## 一句话摘要

Time-series language models provide a shared natural-language interface across temporal tasks, but plausible text does not guarantee reliable task outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time-series language models provide a shared natural-language interface across temporal tasks, but plausible text does not guarantee reliable task outputs. Responses may appear reasonable while hallucinating the required object: numerical sequences can violate shape, scale, channel order, or temporal alignment, and textual decisions can fall outside the legal label space. We formulate reliable time-series language modeling, separating task-object reliability from predictive quality. We introduce ExecTS-QA, a contract-grounded benchmark spanning forecasting, imputation, classification, anomaly detection, and waveform analysis. We further propose WaveTLM, a unified compiler-executor model whose task compiler transforms user requests, visible arguments, and wave-grounded evidence into typed task states, while task-native executors construct numerical tensors, legal decisions, or structured records. On ExecTS-QA, a single WaveTLM checkpoint achieves 99.40% contract-valid coverage, compared with 37.83% for the strongest evaluated string-first baseline, while retaining balanced predictive performance across all five task families. Evaluations on SciTS, TSQA, IRTS-ToolBench, and ARFBench provide additional evidence of transfer. The code, construction scripts, and ExecTS-QA dataset will be publicly released upon publication. These results show that task compilation can convert plausible language generation into reliable time-series outputs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiahui Chen, Bingke Zhu, Hongyu Pan, Yingying Chen
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
