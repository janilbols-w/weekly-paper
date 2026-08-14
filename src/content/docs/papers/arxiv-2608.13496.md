---
title: "YAVIN: A Unified Architecture for Secure Edge Processing in Memory"
description: "Secure, private multi-tenant execution spanning processors, memory, and accelerators remains one of the most significant challenges in modern edge computing systems."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.13496) · [PDF](https://arxiv.org/pdf/2608.13496)

## 一句话摘要

Secure, private multi-tenant execution spanning processors, memory, and accelerators remains one of the most significant challenges in modern edge computing systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Secure, private multi-tenant execution spanning processors, memory, and accelerators remains one of the most significant challenges in modern edge computing systems. Simultaneously, processing-in-memory (PIM) has emerged as an effective approach for reducing the Von Neumann bottleneck by moving computation closer to data. Existing trusted execution environments (TEEs) establish trust only within the processor, protecting data while it traverses untrusted resources such as the memory bus. Consequently, trusted computation cannot be performed directly within memory. We present YAVIN, a unified trusted computing base (TCB) that extends the TEE beyond the processor to encompass both processor execution and a dedicated memory region supporting trusted processing-in-memory execution while treating the memory bus as untrusted. Leveraging the dedicated protected memory regions already established by conventional TEE architectures, YAVIN enables data to be decrypted, processed, and re-encrypted by either processor or PIM execution while remaining within the TEE. To realize this unified TCB, YAVIN presents the first PIM implementations of the LightSaber KEM post-quantum cryptosystem and ASCON-128 authenticated encryption, co-designing both algorithms for efficient DRAM execution to establish and maintain shared cryptographic state. Finally, we demonstrate how cryptography-PIM co-design for tensor-based workloads reorganizes computation to satisfy the ordering constraints imposed by authenticated encryption with minimal performance overhead while simultaneously enabling bit-sliced ordering that limits temporary plaintext exposure. Compared to the latest PIM AES implementation, YAVIN achieves more than a 20x speedup while incurring only 34% and 9.3% overhead when executing INT8 and INT32 quantized edge-class LLMs, respectively, relative to plaintext execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shouzhi Fang, William C. Tegge, Md Omar Faruque, Peipei Zhou, Endadul Hoque, Alex K. Jones
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
