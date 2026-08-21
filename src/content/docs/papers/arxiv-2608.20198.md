---
title: "A Resource-Efficient CNN-Based EEG Auditory Attention Decoding ASIC"
description: "Following a target speaker in a noisy environment, commonly known as the cocktail party problem, remains particularly challenging for cochlear implant (CI) users."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.20198) · [PDF](https://arxiv.org/pdf/2608.20198)

## 一句话摘要

Following a target speaker in a noisy environment, commonly known as the cocktail party problem, remains particularly challenging for cochlear implant (CI) users.

## 为什么值得关注

待编辑增强。

## 摘要原文

Following a target speaker in a noisy environment, commonly known as the cocktail party problem, remains particularly challenging for cochlear implant (CI) users. Recent studies have explored EEG-based auditory attention decoding (AAD) using neural networks to enhance hearing assistance. This paper presents a resource-efficient ASIC for real-time EEG-based auditory attention decoding by integrating a quantized CNN inference engine and a Pearson-correlation classifier. The proposed architecture employs streaming execution, on-chip buffering, and memory-efficient dataflow to reduce hardware cost while maintaining real-time performance. The proposed ASIC has been fully implemented in GF22FDX 22-nm CMOS technology, occupying a total silicon area of 2.09 mm$^2$(1264$\mu$m x 1654$\mu$m), with the CNN inference engine and streaming classification engine requiring only 0.076 mm$^2$. Operating at a core voltage of 0.55 V, the design achieves a power consumption of 0.4941 mW and an inference latency of 7.34 ms, providing an energy-efficient hardware platform for EEG-based auditory attention decoding in hearing-assistance applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qier Ma, Richard George, Stefan Scholze, Jehn Constantin, Tobias Reichenbach, Christian Mayr
- 发布：2026-08-20；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
