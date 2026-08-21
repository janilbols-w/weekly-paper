---
title: "Learning how to Forget: Fine-tuning for Long-Context Sparse Attention"
description: "A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer language models without excessive hardware budgets."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.19920) · [PDF](https://arxiv.org/pdf/2608.19920)

## 一句话摘要

A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer language models without excessive hardware budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

A lot of prior work addressed key-value (KV) cache selection and compression by sparse attention to enable long-context inference for transformer language models without excessive hardware budgets. We provide a new method for fine-tuning models with sparse attention. It works for any KV cache policy, runs on a moderate hardware budget (e.g., a single Nvidia A100 GPU with 40 GB RAM), and allows the model to co-adapt with the policy, often outperforming models trained with exact attention (sequence parallelism). We also provide an efficient implementation of H2O sparse attention (the leading policy in our experiments) with dedicated scaled dot product attention kernel support. KeysAndValues (https://github.com/awslabs/keys_values), a new open source library for long-context inference and fine-tuning, provides easy-to-use and performant code for all methods discussed here.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Matthias Seeger, Zeyu Zhang, Vihang Patil, Konstantinos Benidis, Sebastian Schelter
- 发布：2026-08-20；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/awslabs/keys_values](https://github.com/awslabs/keys_values)
- 阅读深度：metadata
