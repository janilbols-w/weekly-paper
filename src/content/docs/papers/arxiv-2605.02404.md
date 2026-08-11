---
title: "Statistically-Lossless Quantization of Large Language Models"
description: "Model quantization has become essential for efficient large language model deployment, yet existing approaches present clear trade-offs: methods such as GPTQ and AWQ achieve practical compression but are lossy, while lossless techniques preserve fidelity but lack inference acceleration."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.02404) · [PDF](https://arxiv.org/pdf/2605.02404)

## 一句话摘要

Model quantization has become essential for efficient large language model deployment, yet existing approaches present clear trade-offs: methods such as GPTQ and AWQ achieve practical compression but are lossy, while lossless techniques preserve fidelity but lack inference acceleration.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model quantization has become essential for efficient large language model deployment, yet existing approaches present clear trade-offs: methods such as GPTQ and AWQ achieve practical compression but are lossy, while lossless techniques preserve fidelity but lack inference acceleration. This paper explores the middle ground of statistically-lossless compression, examining three complementary aspects of what losslessness means for quantized LLMs. First, task-lossless compression preserves zero-shot benchmark accuracy within natural sampling variance and is achievable at aggressive bitwidths. Second, we formalize the stricter notion of distribution-lossless compression, requiring the quantized model's next-token distribution to be practically indistinguishable from the original, and propose the Expected Acceptance Rate (EAR), the maximum token-agreement probability under optimal coupling, as a directly interpretable fidelity metric. For example, EAR >= 0.99 means 99% agreement. Third, we prove a gamma-squared variance law showing that symmetric quantization inflates noise variance by gamma^2 relative to asymmetric quantization, making asymmetric quantization a prerequisite for distribution-lossless fidelity but not for task-level preservation. Through SLQ, a layer-wise non-uniform method with asymmetric quantization and wide bitwidth search, we obtain task-lossless compression at well below 4 bits per parameter, as low as 3.3 bits depending on the model, distribution-lossless compression at 5-6 bits per parameter on average, and inference speedups of 1.7-3.7x compared to FP16 using optimized kernels. Source code is available at [https://github.com/IST-DASLab/SLQ](https://github.com/IST-DASLab/SLQ).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Michael Helcig, Eldar Kurtic, Dan Alistarh
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/IST-DASLab/SLQ](https://github.com/IST-DASLab/SLQ)
- 阅读深度：metadata
