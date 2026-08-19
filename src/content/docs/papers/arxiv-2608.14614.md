---
title: "DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs"
description: "As AI datacenters retire functional GPUs, vast quantities of still capable accelerators enter secondary markets."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.14614) · [PDF](https://arxiv.org/pdf/2608.14614)

## 一句话摘要

As AI datacenters retire functional GPUs, vast quantities of still capable accelerators enter secondary markets.

## 为什么值得关注

待编辑增强。

## 摘要原文

As AI datacenters retire functional GPUs, vast quantities of still capable accelerators enter secondary markets. This paper investigates whether these retired GPUs can find a productive afterlife to form a DumpsterCluster that can serve modern LLM inference, and under what conditions such repurposing is economically viable and environmentally sustainable. We physically built a 128-GPU DumpsterCluster from scratch using only second-hand components and ran it for one year. At current market prices (\$22K for the DumpsterCluster vs. \$600K for an 8-GPU B200 system), the economic advantages are substantial. Through pipeline-parallel optimizations, our V100 based DumpsterCluster achieves competitive LLaMA-70B throughput, validating production viability. However, our deployment reveals critical context dependencies. Older GPUs consume significantly more energy per token, making total cost of ownership favorable only in regions with inexpensive electricity. Under grid-average carbon intensity, second-hand systems can produce approximately 4x higher total carbon emissions per token for 8B models, and over 40x for 70B models, compared to current-generation hardware. These findings show that GPU afterlife is not universally sustainable - hardware repurposing must be strategically coupled with low carbon energy sources. When deployed in regions with favourable energy economics and clean electricity, second-hand GPUs offer a viable pathway for expanding AI capacity while advancing affordability, energy security, and environmental responsibility.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: total cost of ownership
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zeyu Cao, Xuan Guo, Cheng Zhang, Cheuk Hang Lau, Ilia Shumailov, Yiren Zhao
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
