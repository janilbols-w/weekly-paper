---
title: "Optimizing Denoising Trajectories in dLLMs: A Lightweight Evolutionary Heuristic Approach"
description: "Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to conventional Auto-Regressive (AR) Large Language Models (LLMs)."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.26052) · [PDF](https://arxiv.org/pdf/2609.26052)

## 一句话摘要

Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to conventional Auto-Regressive (AR) Large Language Models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to conventional Auto-Regressive (AR) Large Language Models (LLMs). By leveraging bidirectional attention and parallel decoding, dLLMs enable more efficient generation. However, they require a carefully designed denoising scheduler at inference time (absent during training) whose choice significantly impacts generation quality. While confidence-based heuristic schedulers have shown strong empirical performance, they suffer from two critical failure modes: EOS Overflow and Proximal Bias. Through in-depth analysis of the Transformer's attention patterns, we reveal that these failures stem from certain positions assigning disproportionately high attention weights to invalid tokens (e.g., [MASK] and [EOS]), which produce misleading confidence signals. Building on this insight, empirical evidence shows that valid attention scores can provide complementary guidance to conventional confidence-based heuristics, yet no single metric consistently excels across all scenarios, implying that the optimal denoising trajectory is highly context-dependent. To address this problem, we propose a lightweight evolutionary heuristic scheduler optimized using the Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Our scheduler dynamically integrates multiple heuristic features with a contextual mean-field embedding, while requiring only 393 trainable parameters. Evaluated on LLaDA and Dream across four reasoning and planning benchmarks, our method consistently outperforms strong baselines, including conventional heuristics, block auto-regressive methods, and recent State-Of-The-Art (SOTA) approaches. To the best of our knowledge, it represents the most parameter-efficient neural scheduler to date. Our code is available at https://github.com/RS2002/Evo-Denoise .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zijian Zhao, Dian Jin, Xialiang Tong, Sen Li, Mingxuan Yuan
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/RS2002/Evo-Denoise](https://github.com/RS2002/Evo-Denoise)
- 阅读深度：metadata
