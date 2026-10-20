---
title: "Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation"
description: "Federated learning (FL) is a distributed paradigm for Internet of Things (IoT) edge networks."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2610.25810) · [PDF](https://arxiv.org/pdf/2610.25810)

## 一句话摘要

Federated learning (FL) is a distributed paradigm for Internet of Things (IoT) edge networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Federated learning (FL) is a distributed paradigm for Internet of Things (IoT) edge networks. However, deploying Vision-Language Models (VLMs) over wireless edge networks presents distinct challenges: large model parameters increase uplink transmission latency over bandwidth-constrained fading channels, and non-independent and identically distributed (Non-IID) data exacerbates client drift. Existing feature alignment solutions often introduce auxiliary computations that consume time slots allocated for wireless parameter transmission, increasing the likelihood of straggler dropouts under system delay constraints. To address these issues, we propose DPGR-GCAM, a communication-efficient federated domain generalization framework. By employing a dual-parameter-efficient fine-tuning (PEFT) architecture, we design a channel-aware tiered transmission mechanism that adaptively truncates payloads to maximize node survival rates under fading conditions. To mitigate client drift, we introduce the Gradient-Conflict Aware Modulation (GCAM) mechanism. GCAM operates within the low-dimensional feature manifold to dynamically resolve multi-objective optimization conflicts with minimal edge computation latency, thereby reducing computation-induced network outages. Experiments demonstrate that DPGR-GCAM improves cross-domain generalization and sustains convergence under network fading scenarios with a 10\% client participation rate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: straggler
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuankun Xia, Hui Wang, Ling Yuan, Ziyu Hong, Di Yin, Yufeng Zhou
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
