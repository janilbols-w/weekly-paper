---
title: "GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs"
description: "Genome foundation models are most useful where sequences are generated, yet the largest models need datacenter accelerators and a place to send private DNA."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.35882v1) · [PDF](https://arxiv.org/pdf/2609.35882v1)

## 一句话摘要

Genome foundation models are most useful where sequences are generated, yet the largest models need datacenter accelerators and a place to send private DNA.

## 为什么值得关注

待编辑增强。

## 摘要原文

Genome foundation models are most useful where sequences are generated, yet the largest models need datacenter accelerators and a place to send private DNA. We ask whether a 15-billion-parameter genome mixture-of-experts (MoE) model can instead run on volunteers' web browsers, with the experts spread across many untrusted devices, without changing its predictions and without revealing the sequence to any single device. We build a system in which a trusted coordinator runs attention and routing while browser workers run every expert feed-forward network through hand-written WebGPU kernels, and we protect the expert inputs with real-valued Lagrange coded computing: each worker receives only a Gaussian-padded share, computes the expert's linear maps, and the coordinator decodes from any two of three workers. On GenomeOcean-MoE (8 experts, top-2 routing, 24 layers), the browser path matches native llama.cpp at every quantization level, the distributed path stays at the BF16 numerical noise floor (KL 0.0036 nats per token), and an unfitted latency model predicts decode time within 0.74% (median) under emulated wide-area links. We first show that plaintext expert inputs are not private: a probe recovers the token from a single vector at every depth, and one worker can identify the source genome from 300 unordered tokens with 92% accuracy. With coded experts, an adaptive attacker trained on shares falls to the most-frequent-token baseline, one worker's information about each token is bounded below one bit per forward pass, and the fidelity cost stays below the BF16 noise floor; in Chrome, coded decoding runs at 220 to 376 ms per token, depending on how much of the routing is hidden, and continues without replicas when a worker fails.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guang Yang, Fengchen Liu
- 发布：2026-09-27；更新：2026-09-27
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
