---
title: "Revisiting Lossy Verification in Speculative Decoding: Mechanisms, Trade-offs, and Failure Modes"
description: "Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently verified in parallel by a larger target model."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2607.26627) · [PDF](https://arxiv.org/pdf/2607.26627)

## 一句话摘要

Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently verified in parallel by a larger target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently verified in parallel by a larger target model. Recent approaches introduce lossy verification schemes to further improve efficiency by relaxing strict distributional matching. Yet such relaxation silently rewrites the decoding distribution, and the resulting acceleration can come at the cost of unstable, sometimes severely degraded generation quality. In this work, we present a principled analysis of the distributions induced by lossy verification methods. We show that many seemingly distinct approaches differ only superficially and can be unified into two categories: truncation-based verification and collaborative verification. We further construct a diagnostic evaluation framework across curated benchmarks. For truncation-based methods, we identify a fundamental pitfall-performance can degrade significantly compared to the true truncation sampling baseline due to distributional distortion. For collaborative verification, we reveal that well-designed relaxation principles, namely overshoot suppression and supervision quality, matter far more than the linear interpolation between draft and target. Our code is available at https://github.com/ZhouYuxuanYX/Fast-HSD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tianyu Wang, Yuxuan Zhou, Heng Li, Wenbin Wang, Zikai Xiao, Chunrui Zheng, Junyuan Shang
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ZhouYuxuanYX/Fast-HSD](https://github.com/ZhouYuxuanYX/Fast-HSD)
- 阅读深度：metadata
