---
title: "Depth Laws for the Precision Floor of Trained Neural Networks: Amplification, Residual Scaling, and a Quantization-Aware Training Paradox"
description: "How many bits does a network need before its accuracy collapses, and how does this grow with depth?"
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.32060) · [PDF](https://arxiv.org/pdf/2609.32060)

## 一句话摘要

How many bits does a network need before its accuracy collapses, and how does this grow with depth?

## 为什么值得关注

待编辑增强。

## 摘要原文

How many bits does a network need before its accuracy collapses, and how does this grow with depth? We study the precision floor, the perturbation level or bit-width at which accuracy falls halfway to chance, in MLPs, CNNs, Vision Transformers and nine pretrained language models, under post-training quantization (PTQ) and quantization- or noise-aware training (QAT). (i) A first-order theory sets the floor through one full-precision quantity, the predictive amplification $G$: $\eta_c=\Lambda/G$, and $G^2$ grows linearly in depth at a rate proportional to the squared residual branch scale. (ii) The predicted equality $\alpha_{PTQ}=\rho$ of depth exponents holds within 95% intervals in twelve of thirteen trained architectures and in GPT-2 from 12 to 48 layers, with $\Lambda=1.45\pm14\%$ across trained architectures. (iii) Residual branches scaled by $1/\sqrt{D}$ and pre-normalisation remove the depth penalty, and each quantizer turns noise into bits at a rate fixed by its step rule, giving $b_c=(\alpha/\gamma)\log_2 D+C$. (iv) A QAT paradox: noise-aware training roughly doubles the tolerable noise of shallow networks, but the gain decays with depth, so the depth law steepens ($\alpha_{QAT}/\alpha_{PTQ}=1.45$-$1.47$ on two datasets, ten seeds each). Decision margins, cross-layer error cancellation and heavy tails do not set the floor.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ahmad S. Tarawneh
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
