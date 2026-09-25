---
title: "Co-occurrence Patterns of LoRA Adapters in Production Diffusion Model Inference Services"
description: "Low-rank adaptation (LoRA) has become a key technology for serving large-scale personalized large language models and diffusion models in the cloud."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.23321) · [PDF](https://arxiv.org/pdf/2609.23321)

## 一句话摘要

Low-rank adaptation (LoRA) has become a key technology for serving large-scale personalized large language models and diffusion models in the cloud.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-rank adaptation (LoRA) has become a key technology for serving large-scale personalized large language models and diffusion models in the cloud. However, the co-occurrence patterns, resource contention relationships, and evolutionary regularities of adapters under production inference workloads have not been systematically or quantitatively studied. Based on GenTD26, Alibaba's production diffusion model inference dataset, this paper adopts a graph-theoretic framework to construct an adapter co-occurrence network and conducts a characterization from both static structure and dynamic evolution. Our main findings are as follows. (1) The co-occurrence network is extremely sparse, and adapter usage frequency follows a significant heavy-tailed distribution. (2) Introducing the first adapter incurs a 66.1% execution-latency overhead, with diminishing marginal costs afterwards. (3) Co-occurrence relationships are driven by base models: in 90.6% of multi-adapter requests, all adapters share the same dominant base model; 66.2% of significant co-occurrence edges connect same-model adapter pairs; and in 85.8% of multi-adapter requests, all adapter pairs form significant co-occurrence edges. (4) The adapter ecosystem exhibits a core-periphery bipolar structure, with a weekly Jaccard similarity of 0.696 at the model level and a churn rate of 54.5% for the top-10 hottest models within a 12-hour window. Based on these findings, we propose a preloading strategy built on top-k co-occurrence statistics; offline experiments show that it covers 81.0% of test-set co-occurrence pairs at k=3, and sensitivity analyses across frequency thresholds and time windows verify the robustness of the conclusions. These results provide a data-driven basis for cache preloading, adaptive scheduling, and GPU memory management in LoRA inference services.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tao Zhang, Bin Liao, Tao Zhou, Yanping Liu
- 发布：2026-09-20；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
