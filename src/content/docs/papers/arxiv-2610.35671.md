---
title: "Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks"
description: "As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2610.35671) · [PDF](https://arxiv.org/pdf/2610.35671)

## 一句话摘要

As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks.

## 为什么值得关注

待编辑增强。

## 摘要原文

As frontier language models grow increasingly capable and autonomous, independent third-party evaluations are critical for characterizing their systemic safety risks. While closed-source releases are routinely accompanied by comprehensive system cards, open-weight models receive less scrutiny regarding frontier risks. To address this gap, we present an independent safety evaluation of DeepSeek V4.1 Flash-1017, the latest version of V4.1 Flash that departs from V4 with a new architecture, scaled-up training, and strong agentic capabilities. Drawing on the EU General-Purpose AI Code of Practice, we evaluate the model across 34 benchmarks, including 5 in-house suites, spanning evaluation integrity, loss of control, and harmful manipulation. Conforming to the AEF-1 standard, we compare V4.1 Flash-1017 against V4.1 Flash, earlier DeepSeek V4 models, and leading closed-source systems (GPT-6 Astra, GPT-5.6 Sol, and Gemini 3.8 Flash). Overall, V4.1 Flash-1017 shows substantial safety improvements over the V4 generation and approaches or matches leading closed-source baselines on several dimensions, while still exhibiting notable behaviors that warrant continued attention. Building on our findings, we highlight three key observations and recommendations. First, because safety can shift and even regress across minor updates, developers should integrate safety evaluation into incremental releases. Second, as final-turn outputs and end-state checks alone cannot reliably detect loss-of-control behaviors, deployments require process-level observability across both reasoning traces and action logs. Third, because public benchmarks elicit strong evaluation awareness and face data contamination risks, developing private benchmarks is essential for trustworthy frontier evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yao Huang, Zhiyuan Zeng, Yu Wang, Zhitong Zhu, Dingcheng Duan, Hao Li, Shangzhi Xu, Yifan Wang, Jinzhe Tu, Shukun Xiong, Yihe Zang, Han Yan, Hongchang Yang, Fuyu Gu, Wei Xu, Yinpeng Dong, Xiaojian Li
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
