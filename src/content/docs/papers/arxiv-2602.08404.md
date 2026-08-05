---
title: "TEAM: Temporal-Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration"
description: "Diffusion large language models (dLLMs) have recently gained significant attention due to their inherent support for parallel decoding."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2602.08404) · [PDF](https://arxiv.org/pdf/2602.08404)

## 一句话摘要

Diffusion large language models (dLLMs) have recently gained significant attention due to their inherent support for parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) have recently gained significant attention due to their inherent support for parallel decoding. Building on this paradigm, Mixture-of-Experts (MoE) dLLMs with autoregressive (AR) initialization have further demonstrated strong performance competitive with mainstream AR models. However, we identify a fundamental mismatch between MoE architectures and diffusion-based decoding. Specifically, a large number of experts are activated at each denoising step, while only a small subset of tokens is ultimately accepted, resulting in substantial inference overhead and limiting their deployment in latency-sensitive applications. In this work, we propose TEAM, a plug-and-play framework that accelerates MoE dLLMs by enabling more accepted tokens with fewer activated experts. TEAM is motivated by the observation that expert routing decisions exhibit strong temporal consistency across denoising levels as well as spatial consistency across token positions. Leveraging these properties, TEAM employs three complementary expert activation and decoding strategies, conservatively selecting necessary experts for decoded and masked tokens and simultaneously performing aggressive speculative exploration across multiple candidates. Experimental results demonstrate that TEAM achieves up to 2.2x speedup over vanilla MoE dLLM, with negligible performance degradation. Code is released at https://github.com/PKU-SEC-Lab/TEAM-MoE-dLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Linye Wei, Zixiang Luo, Pingzhi Tang, Meng Li
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/PKU-SEC-Lab/TEAM-MoE-dLLM](https://github.com/PKU-SEC-Lab/TEAM-MoE-dLLM)
- 阅读深度：metadata
