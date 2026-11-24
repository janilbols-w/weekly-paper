---
title: "Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving"
description: "To meet the ever-increasing computing demands of large language model (LLM) services, modern cloud platforms have widely deployed neural processing units (NPUs)."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.16488) · [PDF](https://arxiv.org/pdf/2607.16488)

## 一句话摘要

To meet the ever-increasing computing demands of large language model (LLM) services, modern cloud platforms have widely deployed neural processing units (NPUs).

## 为什么值得关注

待编辑增强。

## 摘要原文

To meet the ever-increasing computing demands of large language model (LLM) services, modern cloud platforms have widely deployed neural processing units (NPUs). These NPU chips have been developed and evolved at an incredibly fast pace, this inevitably produces heterogeneous compute pools backed by different versions of NPU chips. Unfortunately, due to the lack of system and architecture support for managing NPU heterogeneity in the cloud, it is unclear how to best utilize heterogeneous NPUs to maximize the energy and cost efficiency for LLM services. In this paper, we first conduct a characterization study of various generations of real NPU chips to demonstrate the potential benefits on energy/cost efficiency and performance by utilizing heterogeneous NPU chips. To realize these benefits, we present NeuScale, an auto-scaling framework to automatically exploit heterogeneous NPUs for cloud platforms. NeuScale manages heterogeneous NPU resources with a new vPod abstraction, which abstracts the core hardware parameters of different NPU versions and provides compatibility with existing ML frameworks. It makes the best-fit vPod allocations for different LLM inference requests using an intuitive and lightweight roofline-based analysis. It supports fine-grained dynamic NPU resource provisioning by adjusting both the vPod configuration (i.e., scaling up/down) and the number of vPods (e.g., scaling in/out). To validate the benefits of NeuScale at scale, we implement it with a production-level NPU simulator. Our evaluation with popular LLMs shows that NeuScale can significantly improve cost efficiency and service-level objective (SLO) satisfaction rate by best utilizing heterogeneous NPU resources.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuqi Xue, Jichuan Chang, Jian Huang
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
