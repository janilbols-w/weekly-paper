---
title: "A Matter of Stages: Energy-Latency Trade-offs in Multimodal LLM Serving"
description: "Online serving of multimodal large language models requires deciding whether to separate visual encoding (E), prefill (P), and decode (D) across GPUs and how to configure their frequencies."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.21165) · [PDF](https://arxiv.org/pdf/2611.21165)

## 一句话摘要

Online serving of multimodal large language models requires deciding whether to separate visual encoding (E), prefill (P), and decode (D) across GPUs and how to configure their frequencies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Online serving of multimodal large language models requires deciding whether to separate visual encoding (E), prefill (P), and decode (D) across GPUs and how to configure their frequencies. EPD disaggregation enables independent stage control, but it also changes communication and queueing behavior. Lowering one stage's frequency can increase queueing and prolong execution across the EPD pipeline. Consequently, reducing power at one stage does not necessarily reduce total GPU energy per request. In this paper, we systematically characterize fused and EPD-disaggregated serving across four multimodal models under a fixed three-GPU budget, followed by single-stage and uniform downclocking experiments across 18 workload combinations. We find that disaggregation reduces GPU energy per successful request by 13.3-37.0% at nearly identical output-token throughput, but increases mean TTFT. Downclocking exhibits distinct stage sensitivities, and aggressive frequency reductions can offset power savings through queueing and longer execution. Across the evaluated workloads, uniform downclocking to 80% reduces GPU energy by 11.7-18.6% with modest mean-latency changes. Guided by these findings, we develop a budgeted frequency exploration strategy to select energy-efficient configurations under latency constraints. Evaluation shows that four probes can identify the lowest-energy feasible configuration among 25 measured candidates across all 288 evaluated positive-margin SLO scenarios. These results provide practical guidance for energy-efficient multimodal serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yifan Sun, Jiantong Jiang, Zhexiang Zhang, Xu Bai, Feng Liu, Rajkumar Buyya, Adel N. Toosi
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
