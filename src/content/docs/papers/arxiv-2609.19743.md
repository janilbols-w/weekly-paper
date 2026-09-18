---
title: "Syndrome Decoding for Silent Data Corruption in Quantized Integer GPU Arithmetic"
description: "Quantized neural network inference runs integer matrix multiplications on GPU tensor cores, and the INT32 accumulators inside those cores have neither parity nor ECC."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.19743) · [PDF](https://arxiv.org/pdf/2609.19743)

## 一句话摘要

Quantized neural network inference runs integer matrix multiplications on GPU tensor cores, and the INT32 accumulators inside those cores have neither parity nor ECC.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantized neural network inference runs integer matrix multiplications on GPU tensor cores, and the INT32 accumulators inside those cores have neither parity nor ECC. A transient fault in this datapath returns a valid but wrong integer and raises no interrupt. Checksum based Algorithm Based Fault Tolerance (ABFT) can detect such silent data corruptions (SDCs), but its verdict is binary. It cannot identify the corrupted element or its magnitude, and unweighted row and column checksums are blind by construction to errors that cancel on both axes. We present SProbe, a trailing verification kernel that reads the output of an unmodified vendor GEMM. A randomized Freivalds gate with three independent evaluation points in a 61 bit prime field misses a nonzero error with probability at most $2^{-141}$. When the gate fires, per row power sum syndromes over three primes are decoded with the Reed Solomon chain of Berlekamp Massey, Chien search, and Forney, recovering the column and exact magnitude of up to four colliding errors per row. SProbe then repairs the accumulator in place or recomputes the GEMM. On an NVIDIA H100, SProbe detects every injected fault across seven fault classes and four matrix sizes, including constructed patterns that TR-ABFT never detects and patterns that a weighted grid code detects but cannot correct. The gate costs 49% of the cuBLASLt GEMM time at N=16384 and 11% at N=65536. In an INT8 medical LLM, protection eliminates all observed silent corruptions at a 30% throughput cost. Our measurements also show that recomputation is faster than in place recovery in every configuration we tested, that diagnosis rather than repair dominates recovery cost, and we report the defects we found while validating the verifier itself.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance, silent data corruption
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pranav Napolean, Vikas Srivastava, Napolean Periathambi
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
