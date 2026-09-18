---
title: "ForeSight: Enhancing Risk Monitoring via Early Safety Signal Distillation"
description: "As large language models (LLMs) are increasingly deployed, the generation of harmful content has become a critical safety concern."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.13737) · [PDF](https://arxiv.org/pdf/2609.13737)

## 一句话摘要

As large language models (LLMs) are increasingly deployed, the generation of harmful content has become a critical safety concern.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) are increasingly deployed, the generation of harmful content has become a critical safety concern. Existing safeguards operate at the input, output, or streaming-generation stages, while early-risk methods that rely on surface tokens or output logits may suffer from weak initial signals, and internals-based detectors using dense representations may retain highly entangled and redundant safety-irrelevant information. It therefore remains unclear whether the earliest post-generation hidden states already contain reliable signals about final-response harmfulness. To address this gap, we propose ForeSight, a first-token output-risk forecasting framework that distills weak and redundant early safety signals into compact, layer-aware risk representations. Experiments on five safety benchmarks and two target models demonstrate that ForeSight achieves superior and efficient early-risk forecasting while relying solely on first-token hidden states. The code is available at: https://github.com/Scabbards1500/Foresight

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hanling Wang, Chenlong Wei, Ling Xu, Hanyan Niu, Qi Cao, Shizhou Huang, Yang Yang, Xiaohui Zhu, Yao Zhu
- 发布：2026-09-12；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Scabbards1500/Foresight](https://github.com/Scabbards1500/Foresight)
- 阅读深度：metadata
