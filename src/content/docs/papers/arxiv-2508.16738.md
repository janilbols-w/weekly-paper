---
title: "zkPHIRE: A Programmable Accelerator for ZKPs over HIgh-degRee, Expressive Gates"
description: "Zero-Knowledge Proofs (ZKPs) have emerged as a powerful tool for secure and privacy-preserving computation."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2508.16738) · [PDF](https://arxiv.org/pdf/2508.16738)

## 一句话摘要

Zero-Knowledge Proofs (ZKPs) have emerged as a powerful tool for secure and privacy-preserving computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Zero-Knowledge Proofs (ZKPs) have emerged as a powerful tool for secure and privacy-preserving computation. ZKPs enable one party to convince another of a statement's validity without revealing anything else. This capability has profound implications in many domains, including machine learning, blockchain, image authentication, and electronic voting. Despite their potential, ZKPs have seen limited deployment because of their exceptionally high computational overhead, which manifests primarily during proof generation. To mitigate these overheads, a (growing) body of researchers has proposed hardware accelerators and GPU implementations of both kernels and complete protocols. Prior art spans a wide variety of ZKP schemes that vary significantly in computational overhead, proof size, verifier cost, protocol setup, and trust. The latest and widely used ZKP protocols are intentionally designed to balance these trade-offs. One particular challenge in modern ZKP systems is supporting complex, high-degree gates using the SumCheck protocol. We address this challenge with a novel programmable accelerator to efficiently handle arbitrary custom gates via SumCheck. Our accelerator achieves upwards of $1000\times$ geomean speedup over CPU-based SumChecks across a range of gate types. We include this unit in zkPHIRE, a programmable, full-system accelerator that accelerates the HyperPlonk protocol. zkPHIRE achieves $1486\times$ geomean speedup over CPU and $11.87\times$ geomean speedup over the state-of-the-art at iso-area. Together, these results demonstrate compelling performance while scaling to large problem sizes (upwards of $2^{30}$ constraints) and maintaining small proof sizes ($4-5$ KB).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alhad Daftardar, Jianqiao Mo, Joey Ah-kiow, Benedikt B\"unz, Siddharth Garg, Brandon Reagen
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
