---
title: "FusionEval: Benchmarking Model Fusion for Large Language Models"
description: "Model fusion aims to integrate the capabilities of multi-expert models into a single model."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.30162) · [PDF](https://arxiv.org/pdf/2610.30162)

## 一句话摘要

Model fusion aims to integrate the capabilities of multi-expert models into a single model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model fusion aims to integrate the capabilities of multi-expert models into a single model. Existing evaluations offer limited coverage of reasoning with long chains of thought and tool use, while strong average performance can mask substantial losses in individual expert capabilities. We introduce FusionEval, a benchmark that provides controlled expert pools, integrates fusion methods with and without additional training, and offers a unified evaluation suite. The pools contain domain experts independently trained from Qwen3 and Llama base models across math, code, science, instruction following, and tool use. The suite evaluates capability retention and computational cost on eight public benchmarks under comparable data access rules, reporting normalized average and worst performance, runtime, and peak GPU memory usage. Extensive experiments show that training-free methods preserve reasoning performance but substantially degrade tool use at both model scales. In contrast, MOPD preserves tool use and achieves a more balanced capability profile, but requires additional data preparation, inference, and training. Jointly retaining reasoning, instruction following, and tool use at low computational cost remains a challenge. We hope FusionEval supports future research on efficient model fusion that jointly preserves expert capabilities. Our code is available at https://github.com/Baicaihaochi/FusionEval_Benchmark.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shuo Cai, Yanggan Gu, Yuhang Liu, Su Lu, Yuanyi Wang, Yang Yu, Zhen Li, Zhitian Hou, Guanghao Zhu, Ming Li, Hongxia Yang
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Baicaihaochi/FusionEval_Benchmark](https://github.com/Baicaihaochi/FusionEval_Benchmark)
- 阅读深度：metadata
