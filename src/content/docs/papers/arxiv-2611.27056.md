---
title: "A Continuous Relaxation of Quantization-Aware Training"
description: "Quantization is a critical piece of the deployment pipeline in the era of large generative models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.27056) · [PDF](https://arxiv.org/pdf/2611.27056)

## 一句话摘要

Quantization is a critical piece of the deployment pipeline in the era of large generative models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization is a critical piece of the deployment pipeline in the era of large generative models. Low-bit quantization, particularly 2-bits or sub-2-bits, is a notoriously difficult problem, particularly when using a channelwise quantization scheme which has been shown as a leading candidate for hardware-efficiency. The key challenges with low-bit quantization range from limited quantization levels to saddle points or flat regions in the loss surface. In this paper, we look at the problem of flat quantization loss surfaces through a lens of dynamically changing bitwidth. Unlike existing techniques which either change the bit-precision abruptly or keep it fixed, we propose to gradually alter the bitwidth as the model trains. To this end, we propose RelaxQAT, a continuous relaxation of the QAT process. We also provide simple theoretical and empirical insights behind why RelaxQAT helps the QAT performance. Our extensive experiments demonstrate up to 6.3% average accuracy gains on vision and up to 7.7% better average accuracy on natural language tasks, compared to the leading QAT methods.

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

- 作者：Kartikeya Bhardwaj, Mohammed Almousa, Chaitanya Mullapudi, Ananth Balasubramanian, Nithin Ramesan, Tuc Nguyen, Harris Teague
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
