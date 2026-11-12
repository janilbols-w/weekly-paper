---
title: "Total Variation Distance Estimation in Autoregressive Models"
description: "Modern LLM deployments use a number of implementation choices and inference optimizations (e.g., batching, custom kernels, and quantization) on top of fixed weights, so two engines serving \"the same model\" can produce meaningfully different distributions."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.19510) · [PDF](https://arxiv.org/pdf/2607.19510)

## 一句话摘要

Modern LLM deployments use a number of implementation choices and inference optimizations (e.g., batching, custom kernels, and quantization) on top of fixed weights, so two engines serving "the same model" can produce meaningfully different distributions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM deployments use a number of implementation choices and inference optimizations (e.g., batching, custom kernels, and quantization) on top of fixed weights, so two engines serving "the same model" can produce meaningfully different distributions. We study the problem of estimating the total variation (TV) distance between two length-$n$ autoregressive distributions to additive error $\varepsilon$, under three access models. (1) Under sample access, we use $\widetilde{O}(n^2 K/\varepsilon^2)$ queries, where $K$ is the maximum support of the next-token distribution. This improves upon the $\widetilde{O}(n^3 m/\varepsilon^5)$-query estimator of Meel et al. (2025), where $m \geq K$ is the total size of the token alphabet. (2) Under logit access, we use $O(n/\varepsilon^2)$ queries, and this is tight. (3) Under noisy logit access, we smoothly interpolate between the above two guarantees: if probability values are given to relative error $\sigma$, we use $\widetilde{O}((n+n^2\sigma^2)/\varepsilon^2)$ queries. We complement our theoretical results with an empirical evaluation of our algorithms, for example measuring the distance between SGLang and vLLM serving identical weights. Our experiments highlight the robustness and practicality of estimating the total variation distance, which remains estimable where the KL divergence is infinite. Our code is available at https://github.com/XunZhiyang/llm-tv-estimation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Eric Price, Kevin Tian, Zhiyang Xun, Yusong Zhu
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/XunZhiyang/llm-tv-estimation](https://github.com/XunZhiyang/llm-tv-estimation)
- 阅读深度：metadata
