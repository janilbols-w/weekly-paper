---
title: "Communicate the Change: Efficient Expert Parallelism via Activation Compression"
description: "Scaling has driven the success of large language models (LLM), with sparse mixture-of-experts (MoE) architectures enabling greater parameter capacity without a proportional increase in computation."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.22215) · [PDF](https://arxiv.org/pdf/2611.22215)

## 一句话摘要

Scaling has driven the success of large language models (LLM), with sparse mixture-of-experts (MoE) architectures enabling greater parameter capacity without a proportional increase in computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling has driven the success of large language models (LLM), with sparse mixture-of-experts (MoE) architectures enabling greater parameter capacity without a proportional increase in computation. At large scales, MoE models rely on expert parallelism to distribute experts across devices. Each MoE layer requires two synchronous collective communication steps during inference: dispatching hidden states to the activated experts and combining the resulting expert outputs. As compute throughput has outpaced interconnect bandwidth, these synchronous collectives have become a major bottleneck to MoE scaling and efficiency. We address this challenge with EchoMoE, a lightweight architecture modification that retrofits existing MoE models, requiring approximately 8,500x fewer training tokens than full pretraining. Motivated by the observation that transformer blocks update the residual stream incrementally, we use a hidden state from an earlier layer as a reference and communicate only the compressed difference between it and the current state, rather than communicating each hidden state in full. EchoMoE periodically refreshes these reference states and transmits only the compressed differences synchronously, reducing the traffic on latency-critical paths without significant computational overhead. EchoMoE reduces inter-node communication volume by 58% and improves throughput by 22.6%, while preserving average performance within 3.8 percentage points across 18 benchmarks. EchoMoE further improves inference throughput by up to 2.38x over bandwidth-constrained Ethernet, paving the way for wide-area distributed inference. EchoMoE also tolerates quantization of the communicated representations without measurable quality loss. We release an efficient implementation for applying EchoMoE to pretrained MoE models, together with an inference integration for vLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication, distributed inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Fengyuan Liu, Jay Gala, Siva Reddy, Dzmitry Bahdanau
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
