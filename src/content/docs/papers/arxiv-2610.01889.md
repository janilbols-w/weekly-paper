---
title: "Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2"
description: "Should low-precision transformer inference use stochastic rounding (SR) or round-to-nearest (RN)?"
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.01889) · [PDF](https://arxiv.org/pdf/2610.01889)

## 一句话摘要

Should low-precision transformer inference use stochastic rounding (SR) or round-to-nearest (RN)?

## 为什么值得关注

待编辑增强。

## 摘要原文

Should low-precision transformer inference use stochastic rounding (SR) or round-to-nearest (RN)? The answer depends on where in the network you look. We isolate this effect by holding the numerical format fixed and varying only the rounding rule at individual operation sites. To enable experiments at freely chosen precisions, we extend the PRISM vectorized rounding library to arbitrary virtual precision via a variable-precision stochastic rounding (VPSR) algorithm, proving that the rounding decision is evaluated exactly in hardware floating point. We develop two analyses providing complementary insight into this site-level trade-off. First, a probabilistic forward-error bound for linear projections shows that SR's error envelope grows as $O(\sqrt{n} u)$ in reduction length $n$, versus $O(n u)$ for RN, a gap that widens rapidly at low precision and is most pronounced in the long multilayer perceptron (MLP) down-projection. Second, a second-order decomposition of expected cross-entropy loss change at the output softmax into signed drift, drift curvature, and a Fisher-weighted variance penalty reveals why the two sites behave oppositely: MLP noise is predominantly a uniform logit shift to which softmax is invariant, so SR's variance is largely discounted; head noise is non-uniform across the vocabulary and is not. On DistilGPT-2 at $t=6$ significand bits, observations match theory: SR in the MLP raises perplexity to 1.15x the full-precision reference, versus 2.21x for RN. At the language-model head, the ordering reverses because SR introduces non-uniform variance, whereas deterministic RN carries none. In a mixed-precision configuration (MLP output at $t=6$), assigning SR to the MLP and RN to the head brings perplexity within 1.10x of the full-precision reference, a 28% reduction over matched-bit RN.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yohan Chatelain, Pablo de Oliveira Castro
- 发布：2026-10-01；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/big-data-lab-team/fuzzy-llm](https://github.com/big-data-lab-team/fuzzy-llm)
- 阅读深度：metadata
