---
title: "StoSignSGD: Unbiased Structural Stochasticity Fixes SignSGD for Training Large Language Models"
description: "Sign-based optimization algorithms, such as SignSGD, have garnered attention for their performance in distributed learning and training large foundation models."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2604.15416) · [PDF](https://arxiv.org/pdf/2604.15416)

## 一句话摘要

Sign-based optimization algorithms, such as SignSGD, have garnered attention for their performance in distributed learning and training large foundation models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sign-based optimization algorithms, such as SignSGD, have garnered attention for their performance in distributed learning and training large foundation models. Despite their empirical superiority, SignSGD is known to diverge on non-smooth objectives, which are ubiquitous due to ReLUs, max-pools, and mixture-of-experts. To overcome this limitation, we propose StoSignSGD, an algorithm that injects structural stochasticity into the sign operator while maintaining an unbiased update step. In the regime of (online) convex optimization, StoSignSGD rigorously resolves the non-convergence issues of SignSGD, achieving a sharp convergence rate matching the lower bound. For the more challenging non-convex non-smooth optimization, we introduce generalized stationary measures that encompass prior definitions, proving that StoSignSGD improves upon the best-known complexity bounds by dimensional factors. Empirically, StoSignSGD is stable and efficient across diverse large language model (LLM) training regimes. In aggressive low-precision pretraining, which spans both FP8 and the far more demanding FP4 regime where AdamW fails catastrophically, StoSignSGD stays stable and consistently performs the best. It attains a 1.44x to 2.14x speedup over established baselines under FP8. Under 4-bit precision, it improves downstream accuracy on the largest OLMo2-370M model by 1.13 points over the strongest stable baseline, and this advantage grows as both the model size and the data scale up. When fine-tuning 7B LLMs on mathematical reasoning tasks, StoSignSGD also delivers clear gains over both AdamW and SignSGD. Finally, to explain why it works, we develop a sign conversion framework that turns any general optimizer into its unbiased, sign-based counterpart. Using this framework, we decompose the core components of StoSignSGD and run a comprehensive ablation study to validate our design choices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dingzhi Yu, Rui Pan, Yuxing Liu, Difan Zou, Tong Zhang
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
