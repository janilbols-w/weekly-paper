---
title: "Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration"
description: "Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.34112) · [PDF](https://arxiv.org/pdf/2611.34112)

## 一句话摘要

Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead. Conditional computation mitigates this cost by deciding dynamically which internal experts, model endpoints, or specialized agents to invoke per request. Yet token-level gating in sparse neural architectures, query-level model cascades, and task-level multi-agent coordination have largely progressed in disconnected research silos, obscuring recurring system failures and transferable fixes. In this systematic review, we synthesize 2,289 studies published between 2017 and September 2026 (selected from 13,884 unique records) across 20 methodological families under a unified two-step inspect-then-allocate framework. Discrete hard selection accounts for 70%, 83%, and 91% of token-, query-, and task-scale literature respectively, and computational overhead appears as a top operational bottleneck across every layer. Engineering safeguards remain sharply asymmetric: intra-layer gating prioritizes load balancing while rarely incorporating uncertainty estimation, whereas model selection and agent orchestration rely on confidence thresholds and budget rules while confronting miscalibration and cascading errors. At the same time, publication volume is accelerating fastest in agentic task delegation, where routing mechanisms are least often isolated experimentally and methodological bias risk is highest.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dat Tat Mai, Hung Tran Quy, Thai Viet Pham, James Jin Kang
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
