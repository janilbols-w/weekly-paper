---
title: "CipherGenome: Homomorphic Inference for Genomic Mixture-of-Experts"
description: "Genome foundation models are growing into sparse mixture-of-experts (MoE) networks whose expert weights no longer fit on the machines that hold the sequences, yet sending a private genome to rented accelerators exposes it: we show that a single server hosting one expert recovers the input nucleotides with 99.8% top-1 accuracy."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.35883) · [PDF](https://arxiv.org/pdf/2609.35883)

## 一句话摘要

Genome foundation models are growing into sparse mixture-of-experts (MoE) networks whose expert weights no longer fit on the machines that hold the sequences, yet sending a private genome to rented accelerators exposes it: we show that a single server hosting one expert recovers the input nucleotides with 99.8% top-1 accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Genome foundation models are growing into sparse mixture-of-experts (MoE) networks whose expert weights no longer fit on the machines that hold the sequences, yet sending a private genome to rented accelerators exposes it: we show that a single server hosting one expert recovers the input nucleotides with 99.8% top-1 accuracy. We present CipherGenome, a protocol that keeps the embedding, attention and router of a 15.1B-parameter MoE genome model on a trusted thin client and outsources every expert projection, 95.8% of the parameters, to untrusted and possibly colluding GPU servers under module-LWE encryption. The design exploits three structural facts: expert layers are linear between two SwiGLU gates, expert weights are public, and GPU integer tensor cores can evaluate a ciphertext-weight product exactly modulo $2^{48}$ in a single GEMM. The client evaluates the nonlinearity exactly and re-encrypts with fresh secrets, so no polynomial approximation or bootstrapping is ever needed. On 72 windows from 12 bacterial genomes, encryption adds $2.54 \times 10^{-4}$ nats per token of KL divergence (95% CI upper bound $3.95 \times 10^{-4}$), below a pre-registered non-inferiority margin and indistinguishable from bf16 inference, while the same inversion attack falls to chance level. A reusable public hint cuts end-to-end latency by 3.54 times, wire compression reduces traffic 6.8 times, per-layer padding reduces routing leakage from 54.9% to 8.9% accuracy, and HE-compatible int4 experts remain non-inferior to their plaintext counterparts. Per expert and token, the server-side cost is more than six orders of magnitude below a CKKS baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Guang Yang, Fengchen Liu
- 发布：2026-09-27；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
