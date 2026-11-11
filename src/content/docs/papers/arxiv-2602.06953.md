---
title: "DAWN: Dependency-Aware Fast Inference for Diffusion LLMs"
description: "Diffusion large language models (dLLMs) have shown advantages in text generation, particularly due to their inherent ability for parallel decoding."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2602.06953) · [PDF](https://arxiv.org/pdf/2602.06953)

## 一句话摘要

Diffusion large language models (dLLMs) have shown advantages in text generation, particularly due to their inherent ability for parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) have shown advantages in text generation, particularly due to their inherent ability for parallel decoding. However, constrained by the quality--speed trade-off, existing inference solutions adopt conservative parallel strategies, leaving substantial efficiency potential underexplored. A core challenge is that parallel decoding assumes each position can be filled independently, but tokens are often semantically coupled. Thus, the correct choice at one position constrains valid choices at others. Without modeling these positional dependencies, parallel strategies produce deteriorated outputs. Motivated by this insight, we propose DAWN, a training-free, dependency-aware decoding method for fast dLLM inference. DAWN extracts dependency relations and leverages two key observations: (1) masked positions dependent on unmasked certain positions become more reliable; (2) coupled masked positions strongly influence each other's predictions. Given those findings, DAWN leverages a dependency graph to select more reliable unmasking positions at each iteration, achieving high parallelism with negligible loss in generation quality. Extensive experiments across multiple models and datasets demonstrate that DAWN speedups the inference by 1.80-8.06x over baselines while preserving the generation quality. Code is released at https://github.com/lizhuo-luo/DAWN.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Lizhuo Luo, Zhuoran Shi, Jiajun Luo, Zhi Wang, Shen Ren, Wenya Wang, Tianwei Zhang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/lizhuo-luo/DAWN](https://github.com/lizhuo-luo/DAWN)
- 阅读深度：metadata
