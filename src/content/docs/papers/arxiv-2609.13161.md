---
title: "PDD: Unleashing Economical and Flexible Heterogeneous LLM Inference via Cross-Datacenter Prefill-Decode Disaggregation"
description: "Interconnecting geographically dispersed clusters over wide-area Ethernet provides a scalable and cost-effective alternative to dedicated intra-datacenter heterogeneous clusters for Large Language Model (LLM) inference."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2609.13161) · [PDF](https://arxiv.org/pdf/2609.13161)

## 一句话摘要

Interconnecting geographically dispersed clusters over wide-area Ethernet provides a scalable and cost-effective alternative to dedicated intra-datacenter heterogeneous clusters for Large Language Model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Interconnecting geographically dispersed clusters over wide-area Ethernet provides a scalable and cost-effective alternative to dedicated intra-datacenter heterogeneous clusters for Large Language Model (LLM) inference. However, this cross-datacenter disaggregation imposes heavy KV-cache transfers between clusters, causing substantial Time-to-First-Token (TTFT) latency, which is especially detrimental for agentic workloads characterized by long contexts, high cache hit rates, and short outputs. We propose PDD, a three-tier disaggregation architecture built upon prefill-decode (PD) disaggregation, consisting of Prefill, RelayDecode (RLD), and MainDecode (MD) instances. On Cluster A, Prefill instances perform the prefill computation, while RLD instances immediately receive the KV cache via high-speed RDMA and begin decoding, thereby overlapping the KV transfer to Cluster B over TCP-based Ethernet. MD instances on Cluster B receive the KV cache along with the tokens produced by RLD, and decoding is then seamlessly handed off from RLD to MD for completion. To maximize overall efficiency, PDD employs three core mechanisms: Decode-side RadixCache to alleviate bandwidth bottlenecks, an Extend-Decode Handoff mechanism for smooth control migration between RLD and MD, and multi-stage pipeline orchestration to manage complex inter-tier dependencies under high concurrency and long-term serving. We further design a low-cost, fine-grained heterogeneous deployment scheme that maximizes latency-masking efficiency at marginal cost. Compared to the intra-DC homogeneous PD baseline, PDD's cross-datacenter mapping of compute-intensive H100s and memory-bandwidth-optimized H200s achieves a Benefit-Cost Ratio (BCR) up to 37.5% higher in SLA-compliant goodput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefill-decode
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yida Wang, Xiuhong Li, Jianping Ma, Gan Sun, Yunshen Xu, Buhe Han, Jingxu Ng, Yuhao Luo, Ke Hong, Guohao Dai, Boxun Li, Yu Wang
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
