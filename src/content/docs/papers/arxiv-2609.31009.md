---
title: "G$^2$PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation"
description: "Post-training quantization (PTQ) is a practical approach to reducing the memory and computational footprint of large language models (LLMs) without retraining."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.31009) · [PDF](https://arxiv.org/pdf/2609.31009)

## 一句话摘要

Post-training quantization (PTQ) is a practical approach to reducing the memory and computational footprint of large language models (LLMs) without retraining.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) is a practical approach to reducing the memory and computational footprint of large language models (LLMs) without retraining. GPTQ-based methods have become the de facto standard, yet they suffer from two complementary limitations. Methods with local, layer-wise objectives lack global supervision; while methods with global objectives fix their Hessian estimates at the start and ignore first-order gradients, so their guidance grows stale as quantization proceeds. This paper presents G$^2$PTQ, a unified PTQ framework with Generalized Gradient Compensation that integrates both first- and second-order information under a globally supervised, block-wise optimization objective. By refreshing gradient and Hessian estimates before quantizing each Transformer block, G$^2$PTQ avoids the staleness of prior global methods. Furthermore, to stabilize the exact first-order compensation, we introduce a trust-region scaling mechanism that dynamically bounds the gradient step to prevent exploding weight updates. Finally, we derive efficient implementations for block-wise Hessian approximation and exact gradient compensation. Experimental results on various model families and bit-widths demonstrate that G$^2$PTQ enables better alignment with the full-precision model, outperforming state-of-the-art baselines. Code is available at: https://github.com/G2PTQ/G2PTQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ruikang Liu, Haoli Bai, Yuxuan Sun, Qian Zhang, Wenzheng Cai, Yanqi Hao, Feiyu Wang, Weidong Zhong, Zhuang Wang, Tong Yang, Xiangsheng Zhou
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/G2PTQ/G2PTQ](https://github.com/G2PTQ/G2PTQ)
- 阅读深度：metadata
