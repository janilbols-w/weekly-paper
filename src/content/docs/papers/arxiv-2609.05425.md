---
title: "Measurement-Driven Diagnosis and Mitigation of Host-CPU Co-location Interference in Single-GPU LLM Serving on a Multi-GPU Server"
description: "Host CPUs in GPU servers are often under-used during LLM inference."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.05425) · [PDF](https://arxiv.org/pdf/2609.05425)

## 一句话摘要

Host CPUs in GPU servers are often under-used during LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Host CPUs in GPU servers are often under-used during LLM inference. Co-locating CPU workloads can improve resource use, but it can also seriously hurt serving quality. Existing work mainly improves LLM serving engines or studies CPU-GPU boundary delays. It gives limited guidance on how external CPU workloads affect the serving path and how operators should choose protection policies. This paper studies host-CPU co-location interference in single-GPU LLM serving. We show that the main observed problem is not slower GPU kernels. Instead, CPU workloads amplify long tails in CPU-side serving stages before GPU work is submitted. To capture this effect, we introduce the Core Path Tail Index (CPTI) and Core Tail Suppression (CTS). Based on these metrics, we build CoTail, a measurement-driven diagnostic procedure that screens workload risk, profiles serving-stage tails, selects OS-level protections, and validates decode SLO compliance. In our primary setup, unprotected nginx co-location reduces throughput by 78.8%, increases TTFT by 429.5%, and increases TPOT by 362.4%. CoTail-guided protections improve nginx throughput by up to 4.4x and reduce TPOT by 4.5x. Under a common-baseline deployment SLO, CoTail satisfies all 12 oracle-feasible held-out cases, compared with 10/12 for Always-rt and 11/12 for Macro-only. It also reduces RT usage from 28 to 22 cases and lowers mean co-tenant slowdown from 56.65% to 51.21%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Guanjie Cheng, Guowei Li, Yingying Wen, Xinkui Zhao, Zhe Liu, Shuiguang Deng
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
