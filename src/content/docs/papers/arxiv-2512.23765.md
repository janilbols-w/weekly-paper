---
title: "Entropy-Aware Token Rejection for Improving Speculative Decoding"
description: "Speculative decoding (SD) accelerates large language model (LLM) inference by using a lightweight draft model to propose tokens and a stronger target model to verify them."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2512.23765) · [PDF](https://arxiv.org/pdf/2512.23765)

## 一句话摘要

Speculative decoding (SD) accelerates large language model (LLM) inference by using a lightweight draft model to propose tokens and a stronger target model to verify them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding (SD) accelerates large language model (LLM) inference by using a lightweight draft model to propose tokens and a stronger target model to verify them. However, standard SD is mainly designed for acceleration, and its output quality is typically constrained by the target model. In this work, we propose Entropy-Aware Speculative Decoding (EASD), a lightweight and training-free extension of SD that improves reasoning quality through token-level entropy-guided rejection. EASD detects cases where both draft and target models exhibit high uncertainty while strongly overlapping in their top predictions. In such uncertain-agreement cases, EASD rejects the aligned token and resamples from the target distribution, preventing low-confidence errors from propagating. Experiments on challenging reasoning benchmarks show that EASD consistently improves accuracy over standard SD and reward-guided variants while maintaining comparable inference efficiency. Notably, EASD can surpass the standalone performance of the target model, suggesting that speculative decoding can serve not only as an acceleration method but also as an effective mechanism for improving reasoning quality. The code is available at https://github.com/ECNU-Text-Computing/EASD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tiancheng Su, Meicong Zhang, Guoxiu He
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ECNU-Text-Computing/EASD](https://github.com/ECNU-Text-Computing/EASD)
- 阅读深度：metadata
