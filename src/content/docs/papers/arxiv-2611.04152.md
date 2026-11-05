---
title: "PACT: Certifying What Is Written in Parallel Decoding of Diffusion Language Models"
description: "Parallel decoding speeds up masked diffusion language models by writing several tokens per forward pass."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.04152) · [PDF](https://arxiv.org/pdf/2611.04152)

## 一句话摘要

Parallel decoding speeds up masked diffusion language models by writing several tokens per forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Parallel decoding speeds up masked diffusion language models by writing several tokens per forward pass. Published commit rules choose these tokens by testing the predicted distributions. Under sampling the written tokens are drawn, and these tests do not see them. We find that answer quality follows the reliability of the tokens actually written. An answer's log probability splits into this reliability and the dependence within each step. We propose PACT, a training-free commit rule that draws the tokens first, certifies the set it will write and spaces the positions of each step apart. This certificate holds at every temperature, and we show that no rule with the same guarantee commits more positions. Experiments use four models of the LLaDA and Dream families and HumanEval, MBPP, GSM8K, MATH500 and IFEval benchmarks. PACT reaches the quality of published commit rules with fewer forward passes. Spacing removes positions from each step, yet it usually lowers the total cost because later steps then write more tokens. At the same speed, published decoders also write a word twice in a row far more often than PACT. These results suggest that commit rules should certify the tokens they write. Code is available at https://github.com/LiZaiyuan0619/PACT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yanchao Li, Yusu Zhang, Jiaqing Xie, Yi Ban, Ben Gao, Zhongyu Huang, Tianfan Fu, Yuqiang Li
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LiZaiyuan0619/PACT](https://github.com/LiZaiyuan0619/PACT)
- 阅读深度：metadata
