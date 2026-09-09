---
title: "SymbolicLight V1: Spike-Gated Dual-Path Language Modeling at High Encoder Spike Sparsity"
description: "Natively trained spiking language models must preserve information across time while operating through sparse binary activations, a combination that has produced a persistent quality gap relative to dense Transformers."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.21333) · [PDF](https://arxiv.org/pdf/2605.21333)

## 一句话摘要

Natively trained spiking language models must preserve information across time while operating through sparse binary activations, a combination that has produced a persistent quality gap relative to dense Transformers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Natively trained spiking language models must preserve information across time while operating through sparse binary activations, a combination that has produced a persistent quality gap relative to dense Transformers. We present SymbolicLight V1, a spike-gated dual-path language model that couples binary Leaky Integrate-and-Fire (LIF) dynamics with a continuous residual stream. Its Dual-Path SparseTCAM mixer combines a first-order exponential-decay state with windowed local attention on the continuous residual stream, followed by a context-conditioned decoding head. We train four 194M-parameter models from scratch on a 3B-token, 10-domain Chinese-English corpus. On a fixed token-weighted evaluation set the runs reach perplexity (PPL) 8.88-8.93 (mean 8.904, sample standard deviation 0.019). Separation of this set from the training streams has not been verified. Training-time encoder probes have a mean zero-spike fraction of 89.96%; this is not a whole-model sparsity measure. Code tokens are 43.7% of that set; the unweighted mean of the ten domain PPLs is 29.38. Under the same corpus, tokenizer, token budget, and hardware, the token-weighted mean is 7.7% above GPT-2 201M (PPL 8.27). Across five zero-shot benchmarks the two 200M-scale models show no clear accuracy separation. Under sampling with temperature 0.7 and top-k 50, SymbolicLight produces lower 4-gram repetition; an entropy-modulated rule reverses that ranking. On an RTX 2080 Ti, measured generation throughput is 22.8 versus 91.5 token/s; post-generation power readings give rough energy estimates of 2,848 versus 905 mJ/token, without power integration over generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ting Liu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
