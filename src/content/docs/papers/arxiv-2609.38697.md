---
title: "Cascadia: A Control-Plane-Free Alternative to Hyperconverged AI Infrastructure"
description: "We present Cascadia, a system for serving large language models on fleets of commodity Intel AIPCs using their CPU, integrated-GPU, and NPU resources."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.38697) · [PDF](https://arxiv.org/pdf/2609.38697)

## 一句话摘要

We present Cascadia, a system for serving large language models on fleets of commodity Intel AIPCs using their CPU, integrated-GPU, and NPU resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present Cascadia, a system for serving large language models on fleets of commodity Intel AIPCs using their CPU, integrated-GPU, and NPU resources. Every node embeds ingress, scheduling, and execution; inference requests require no dedicated routing control plane. Nodes join a libp2p QUIC mesh using CA-issued ed25519 admission certificates, gossip signed capabilities, exchange live load over direct peer streams, and route OpenAI-compatible requests to eligible peers. An operator-run certificate authority handles admission and fleet management outside the inference path. Three serving modes share one interface: whole-model execution on one node, load-balanced replicas, and pipeline-sharded chains using the compilation and speculative decoding mechanism of our companion paper. Optional KV-cache mobility reuses compatible conversation prefixes after a routing move, with cold recomputation on a miss. Signed response receipts and hash-chained logs support provenance and audit. A three-node Phi-3.5-mini NPU testbed delivered 3.10x the response throughput of its one-node configuration under ten concurrent requests; a separate four-node deployment recorded 4.06x the throughput of direct single-node serving. Paired latency observations, runtime measurements, and internal functional checks characterize the tested configurations. We compare Cascadia with IBM, Nutanix, VMware, and HPE platforms on deployment footprint, hardware requirements, scheduling, scaling, licensing, and trust, using vendor documentation. The paper repository provides benchmark scripts, curated measurements, and a claim-to-evidence map.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Matias Parij, Pawan Paudel, Tate Berenbaum, Muthaiah Venkatachalam
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
