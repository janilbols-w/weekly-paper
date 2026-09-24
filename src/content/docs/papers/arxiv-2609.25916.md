---
title: "Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization with Cross-Layer Refinement"
description: "Mixed-precision weight quantization is commonly formulated as a Multiple-Choice Knapsack Problem (MCKP), yet existing solvers rely on scalar sensitivity proxies that collapse each weight matrix's Hessian into a single number and treat every module independently."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.25916) · [PDF](https://arxiv.org/pdf/2609.25916)

## 一句话摘要

Mixed-precision weight quantization is commonly formulated as a Multiple-Choice Knapsack Problem (MCKP), yet existing solvers rely on scalar sensitivity proxies that collapse each weight matrix's Hessian into a single number and treat every module independently.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixed-precision weight quantization is commonly formulated as a Multiple-Choice Knapsack Problem (MCKP), yet existing solvers rely on scalar sensitivity proxies that collapse each weight matrix's Hessian into a single number and treat every module independently. We prove that even the optimal scalar proxy incurs multiplicative distortion up to $\sqrt{\kappa(\mathbf{A})\kappa(\mathbf{B})}$ relative to the full activation-aware quadratic, where $\kappa(\mathbf{A})$ and $\kappa(\mathbf{B})$ denote the condition numbers of the input- and output-side Hessian factors. This bound varies from $10^1$ to $10^{13}$ for typical LLM modules, making inter-module sensitivity ranking unreliable. To address these limitations, we propose Cross-layer Activation-aware Sensitivity Allocation (CASA), a two-phase method. In Stage 1, the scalar proxy is replaced by an activation-aware metric derived from the Kronecker-factored Hessian, reducing the MCKP to a form whose continuous relaxation admits a closed-form solution. In Stage 2, a cross-layer-aware local search evaluates bit-width updates using the end-to-end model loss. Experiments on multiple LLMs across different bit budgets show that CASA achieves lower perplexity than the latest scalar-proxy baselines, especially at ultra-low bit-widths ($<3$ bits per weight). Moreover, the performance gain in zero-shot accuracy tracks the per-model average condition-number over modules, confirming the distortion bound as a practical indicator of scalar-proxy failure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Akihiro Yoshida, Yuma Ichikawa
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
