---
title: "Beyond Update Counts: A Control Map for Evaluating Test-Time Model Updates"
description: "Test-time updating lets a language model change persistent state after training---such as model weights, adapter parameters, or a memory module---before or while answering queries."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.36109) · [PDF](https://arxiv.org/pdf/2610.36109)

## 一句话摘要

Test-time updating lets a language model change persistent state after training---such as model weights, adapter parameters, or a memory module---before or while answering queries.

## 为什么值得关注

待编辑增强。

## 摘要原文

Test-time updating lets a language model change persistent state after training---such as model weights, adapter parameters, or a memory module---before or while answering queries. Existing evaluations often compare systems using update count or frequency and performance measured immediately afterward. These summaries omit what is updated, where, when, and in what order. The same total can therefore hide an important difference: one system may answer after one update while another answers after two. We introduce the Control Map, an evaluation framework that records the committed updates preceding each scored answer and separately evaluates behavioral changes, immediate learning (acquisition), later recall (retention), preservation of unrelated behavior (locality), and performance in new settings. We prove when counts alone determine final state and show, under stated assumptions, how differences between pre-answer histories limit differences in average scores. Using ControlMap, our experiments reveal three insights. First, update scheduling matters: at a 760M-parameter checkpoint, 24 schedules with the same update count yield 19.7%--34.2% accuracy. Second, learning an edit does not guarantee that it lasts or remains contained: all six selected CounterFact LoRA settings learn the new information, while ROME retains edits at all 13 operating points but fails locality at each. Third, no editor performs best consistently across models, benchmarks, and tests. Evaluations should therefore report update histories and assess acquisition, retention, and locality separately.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zehao Zhao, Shangjian Yin, Rui Liu, Chongyang Bai, Mark Ibrahim, Kavosh Asadi, Yuchen Lu, Hang Cui, Hamed Firooz
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
