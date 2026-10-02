---
title: "Behavioral Capacity Certificates for Quantized Language Models"
description: "Activation and key-value cache precision change what a quantized language model computes without altering its stored weights."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.37887v1) · [PDF](https://arxiv.org/pdf/2609.37887v1)

## 一句话摘要

Activation and key-value cache precision change what a quantized language model computes without altering its stored weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Activation and key-value cache precision change what a quantized language model computes without altering its stored weights. Direct weight-code bounds, however, assign identical complexity to deployments that behave differently and charge separately for weight codes that behave identically. Behavioral Capacity Certificates (BCC) charge for behavior using the aggregate prior mass of complete implementations---weights, scales, activation and cache rules---that induce the same bounded loss. When quantization merges implementations, this shared mass lowers the complexity penalty, and a break-even law determines when the saving survives the cost of validating it. BCC supports a three-step deployment workflow, and our experiments verify each step. First, a forward-only screen shortlists per-layer bit-widths by how often candidate perturbations preserve the reference predictions, with quality comparable to Hessian-guided selection at lower preprocessing cost. Second, margin-certified cells identify weights that can be pruned or sign-flipped without changing the deployed behavior: every permitted combination preserves all declared predictions, and on OLMoE-1B-7B and SmolLM2-1.7B, independent probes bound the probability that any permitted combination changes a prediction on new text. Third, BCC bounds the population loss of the deployed model, nonvacuously for complete decoders and more tightly than the compressed-code route. At equal cache memory, giving keys higher precision than values yields lower NLL and higher prediction agreement on GPT-2, Qwen2.5, and SmolLM2, together with a tighter complexity bound in the GPT-2 audit.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Arian Eamaz, Mojtaba Soltanalian
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/eamaz/bcc](https://github.com/eamaz/bcc)
- 阅读深度：metadata
