---
title: "QTEA: Ternary LLMs with Sparse Residual Salient Weight and By-Column Optimization"
description: "Weight-only post-training quantization (PTQ) can alleviate the computational burden of serving large language models (LLMs) at scale."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.00224) · [PDF](https://arxiv.org/pdf/2609.00224)

## 一句话摘要

Weight-only post-training quantization (PTQ) can alleviate the computational burden of serving large language models (LLMs) at scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-only post-training quantization (PTQ) can alleviate the computational burden of serving large language models (LLMs) at scale. However, existing PTQ methods often fail to generalize across models and suffer severe accuracy loss below 2 bits. Many leverage unstructured sparsity to mitigate this loss, but at the cost of regularity and GPU-friendly execution. We present QTEA, a sub-2-bit PTQ framework that quantizes weights into ternary values and uses salient weights as residual error compensators. To maintain hardware efficiency, residuals are assigned to selected columns with semi-structured $1:4$ sparsity within the salient columns. We further add column-wise rescale refinement to GPTQ-style column-by-column quantization, alternately updating per-column scales and ternary assignments to reduce reconstruction error. We also identify order-dependent error propagation in GPTQ and introduce error decay to attenuate late-stage error accumulation. On Qwen3-14B, QTEA compresses all weights to an effective 1.7 bits per weight while improving average accuracy over the strongest ternary PTQ baseline by 16.7%. It also achieves 1.40$\times$ and 2.61$\times$ lower perplexity on WikiText and C4 respectively. This trend holds on Llama3-8B, where QTEA obtains a 6.6% accuracy gain and 1.34$\times$ / 1.95$\times$ lower perplexity on the same datasets. Finally, we develop a lookup-table based kernel that achieves 7.2$\times$ faster per-token generation over an FP16 baseline. Code is available at https://github.com/Intelligent-Microsystems-Lab/QTEA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yipin Guo, Arun M George, Jie Fu, Tareq Mahmoud, Sixue Xing, Siddharth Joshi
- 发布：2026-08-31；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Intelligent-Microsystems-Lab/QTEA](https://github.com/Intelligent-Microsystems-Lab/QTEA)
- 阅读深度：metadata
