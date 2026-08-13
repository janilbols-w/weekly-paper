---
title: "Pretraining large language models with MXFP4 on Native FP4 Hardware"
description: "Why does full-pipeline FP4 training of large language models often diverge, even when forward activations and activation gradients remain stable?"
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.09825) · [PDF](https://arxiv.org/pdf/2605.09825)

## 一句话摘要

Why does full-pipeline FP4 training of large language models often diverge, even when forward activations and activation gradients remain stable?

## 为什么值得关注

待编辑增强。

## 摘要原文

Why does full-pipeline FP4 training of large language models often diverge, even when forward activations and activation gradients remain stable? We address this question through a controlled study of MXFP4 quantization in transformer training, progressively enabling FP4 across forward propagation (Fprop), activation gradients (Dgrad), and weight gradients (Wgrad) while holding all other factors fixed. In full pretraining of Llama 3.1-8B on the C4 dataset, we observe that quantizing Wgrad is the primary driver of convergence degradation, whereas FP4 in Fprop and Dgrad alone introduces only modest additional token requirements. To interpret this behavior, we evaluate both structured and stochastic interventions under a controlled experimental setting. We find that stochastic rounding and randomized Hadamard rotations fail to stabilize training once Wgrad is quantized, whereas deterministic Hadamard rotations consistently restore stable optimization. These results suggest that FP4 training instability is driven by structured micro-scaling errors along sensitive gradient paths, rather than by insufficient stochasticity. We run experiments with native MXFP4 support on AMD Instinct MI355X GPUs, enabling controlled investigation of these effects without reliance on software emulation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Musa Cim, Sarthak Arora, Poovaiah Palangappa, Miro Hodak, Ravi Dwivedula, Meena Arunachalam, Mahmut Taylan Kandemir
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
