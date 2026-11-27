---
title: "FlashProve-Next: Verifiable Inference for Production LLM APIs"
description: "Clients of closed-weight LLM APIs cannot verify whether a provider ran the advertised model, precision, hidden prompt, and reasoning budget."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.33741) · [PDF](https://arxiv.org/pdf/2611.33741)

## 一句话摘要

Clients of closed-weight LLM APIs cannot verify whether a provider ran the advertised model, precision, hidden prompt, and reasoning budget.

## 为什么值得关注

待编辑增强。

## 摘要原文

Clients of closed-weight LLM APIs cannot verify whether a provider ran the advertised model, precision, hidden prompt, and reasoning budget. Existing approaches either trust hardware or third parties, or re-prove every layer of an integer surrogate at high cost while diverging from native floating-point serving. FlashProve-Next produces verifiable, zero-knowledge-masked proofs for individual LLM API responses without modifying native serving (bf16/fp8/mxfp4, random sampling, FlashAttention, CUDA graphs, batching, prefix caching) and without disclosing weights, hidden prompts, hidden reasoning, or activations (dense profiles fix coarse geometry; cross-architecture hiding is deferred). A non-depleting Reed-Solomon weight commitment model_id opens inside proofs via hidden column openings, while local per-operator rounding contracts remove integer surrogates and the refusal-bit leak. Cost-weighted spot-checking supports non-interactive public verification (NI-315, $\varepsilon \le 2^{-40}$, $Q \le 2^{64}$) and external-seed C_pre mode (ExtSeed-153, $\varepsilon \le 2^{-20}$, $Q_{\rm samp} \le 2^{30}$). Twenty-eight Lean 4 modules (696 declarations, zero sorry, standard axioms only) mechanize round-by-round soundness, bucketed sampling, $\mathbb{F}_{p^3}$ constrained-mask binding, causal masking, six IR gadgets, and executable FPN2 verifiers. Five-model Blackwell calibration gives zero false rejections across 1.85M GEMM/MoE blocks and 1.96M non-GEMM rows. Our zero-Phase-2 folded backend (folded ZK simulator open) proves Qwen3-0.6B ExtSeed-153 (1.47B cells, 8 MiB) in 450.2 s GPU (10.76 s CPU) at unique-decoding $Q=128$, passes a 14/14 cheating matrix, and scales to 36-layer Qwen3-4B (dev $4+2$) and live vLLM Qwen3-30B-A3B-FP8 Relation 6 (1.49 s prove, 23.4 ms Rust verify, public weight tiles). Rust fpn-verify checks 8 MiB FPN2 Relation 2 proofs in 10.1 ms on CPU.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Liang Song
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/s-JoL/FlashProve-Next](https://github.com/s-JoL/FlashProve-Next)
- 阅读深度：metadata
