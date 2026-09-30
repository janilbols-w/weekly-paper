---
title: "SCORAS-MoE: Joint Compression and Resource-Adaptive Deployment of MoE-VLMs in LEO Satellite Networks"
description: "Deploying large vision-language models (VLMs) onboard satellites enables onboard data processing and reduces raw data downlink."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.36763) · [PDF](https://arxiv.org/pdf/2609.36763)

## 一句话摘要

Deploying large vision-language models (VLMs) onboard satellites enables onboard data processing and reduces raw data downlink.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying large vision-language models (VLMs) onboard satellites enables onboard data processing and reduces raw data downlink. However, onboard inference faces two resource challenges. Limited onboard memory and energy require model compression and distributed deployment. Dynamic resource availability requires fast deployment decisions as illumination, battery levels, and communication conditions change. We present SCORAS-MoE, a joint compression and deployment framework for mixture-of-experts (MoE) VLMs in low Earth orbit (LEO) satellite networks. To address limited resources, SCORAS-MoE measures the perturbation of the routed MoE output caused by low-rank approximation, assigns higher ranks to more sensitive experts, and distributes compressed model shards across satellites for cooperative inference. The compressed models yield profiles of measured accuracy and inference energy. To adapt to dynamic resources, the online scheduler selects profile compositions and shard placements in each slot. For each candidate composition, it reduces placement to a minimum-cost assignment problem solved by the Hungarian algorithm, while enumerating the compositions yields the optimal deployment for the current-slot objective. Experiments on Qwen3-VL-30B-A3B-Instruct show that allocating ranks based on output perturbation is particularly effective under aggressive compression, with an absolute gain of $3.7\%$ in mean accuracy over uniform rank allocation when expert projections retain $30\%$ of their original parameters. The fixed-profile scheduler achieves higher throughput with fewer service switches and lower battery impact than the evaluated proximal policy optimization (PPO) and evolutionary baselines, with respective speedups of $8.7\times$ and $183.5\times$. Adaptive profile selection further improves the balance between service quality and energy use.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tong Quan, Yuanlong Wan, Huasen He, Yunpeng Hou, Shuangwu Chen, Xiaofeng Jiang, Jian Yang
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
