---
title: "Latent Undertow: How Ordinary Typos Break Probes"
description: "LLMs handle ordinary typing variation fluently: a typo or missing punctuation leaves both user intent and the model's response substantively unchanged."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.15994) · [PDF](https://arxiv.org/pdf/2609.15994)

## 一句话摘要

LLMs handle ordinary typing variation fluently: a typo or missing punctuation leaves both user intent and the model's response substantively unchanged.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLMs handle ordinary typing variation fluently: a typo or missing punctuation leaves both user intent and the model's response substantively unchanged. Yet probes that detect malicious prompts by reading the model's hidden states tell a different story: the same edit rotates the readout vector by 43--56 at the perturbed token, decaying below 15% within ~10 downstream tokens. Stacking ~3 common typos per message cuts a single-position prompt-injection probe's TPR@FPR$=1% by 12.0pp, a gap recalibration alone cannot close. Multi-position aggregation cures localized perturbations (<= 0.5 loss) but only attenuates distributed ones, where even attention- and max-based aggregators still drop ~3.8pp. For single-position probes, we introduce a KV-cache fork: a short fixed suffix appended after the user message lets the probe read a few tokens downstream of the perturbation, exploiting its rapid spatial decay. This closes 95% of the gap (-0.6pp residual) -- an order of magnitude better than perturbation-augmented training (-3.7pp). The rotation-and-decay geometry replicates on Llama-3.1-8B, Qwen3-8B, and Gemma-4-E4B; probe evaluation is on Llama-3.1-8B. Code: https://github.com/eladd-ai/latent-undertow

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Elad David, Max Fomin, Amit LeVi
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/eladd-ai/latent-undertow](https://github.com/eladd-ai/latent-undertow)
- 阅读深度：metadata
