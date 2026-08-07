---
title: "Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More"
description: "Kubernetes, as a container orchestration engine, has been widely used in cloud-native ecosystems for several years."
---

**评分：40/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.00742) · [PDF](https://arxiv.org/pdf/2608.00742)

## 一句话摘要

Kubernetes, as a container orchestration engine, has been widely used in cloud-native ecosystems for several years.

## 为什么值得关注

待编辑增强。

## 摘要原文

Kubernetes, as a container orchestration engine, has been widely used in cloud-native ecosystems for several years. In supercomputing ecosystems, especially where bare-metal performance for compute and network devices are considered, the adoption is somewhat limited. However, with the increasing diversity of use cases such as AI, secure and confidential computing for sensitive data, and mixed workload orchestration, a traditional, single-tenant batch computing system does not offer the flexibility and reproducibility to which public cloud users are accustomed. Note that Kubernetes is not considered a replacement for batch scheduling systems, which have powerful features for large-scale MPI jobs with thousands of network end points. Rather, it is a complementary service provided as part of a national AI Research Resource. We evaluate Kubernetes deployment on a Hewlett Packard Enterprise (HPE) Cray EX supercomputerwith HPE Slingshot interconnect, called Isambard-AI, with co-design use cases. One is a Trusted Research Environment used for medical and health sciences. The other combines KubeRay, Ray, and vLLM to provide a distributed, sandboxed, persistent AI model hosting service targeting multi-tenant confidential computing. We discuss challenges and lessons learned, and where further development is needed to offer a production Kubernetes-as-a-Service on HPE Cray EX (and later) platforms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jake Watson, Sadaf R Alam, Christopher Woods, Abdelwahab Kawafi, Thomas Green, Ian Johnson, Ellis Pires, Jessica R. Jones, Utz-Uwe Haus
- 发布：2026-08-01；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
