---
title: "When Lower Reconstruction Loss Hurts: Distributionally Robust Refinement for Low-Bit LLM Quantization"
description: "Weight-only post-training quantization (PTQ) relies heavily on reconstruction loss minimization to preserve model quality at low precision."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.11226) · [PDF](https://arxiv.org/pdf/2610.11226)

## 一句话摘要

Weight-only post-training quantization (PTQ) relies heavily on reconstruction loss minimization to preserve model quality at low precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-only post-training quantization (PTQ) relies heavily on reconstruction loss minimization to preserve model quality at low precision. We show that the weights favored by minimizing this loss need not yield better model performance on new tasks. In fact, we find that lower reconstruction loss can even degrade model performance on the same calibration data. Our analysis further shows that weights with lower reconstruction loss on calibration data can have higher loss than other weights when the distribution of input activations changes. Motivated by these observations and our analysis, we propose Distributionally Robust Quantization (DRQ), a post-hoc refinement process that minimizes worst-case reconstruction loss over a constrained set of input activation distributions. DRQ refines the integer codes representing quantized weights within the existing quantization grid, keeping quantization parameters and inference operators unchanged. Extensive experiments show that DRQ improves models quantized by six representative PTQ methods, including AWQ, GPTQ, and ParoQuant, and delivers gains across both dense and mixture-of-experts large language models. These results establish DRQ as a general post-hoc refinement framework for weight-only PTQ, achieving better downstream performance without adding inference overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanlong Zhao, Xiaoyuan Cheng, Huihang Liu, Baihua He, Xinyu Zhang, Harrison Bo Hua Zhu, Wenlong Chen, Li Zeng, Zhuo Sun
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
