---
title: "OmniInfer: System-Wide Acceleration Techniques for Optimizing LLM Serving Throughput and Latency"
description: "Large Language Models drive a wide range of modern AI applications but impose substantial challenges on large-scale serving systems due to intensive computation, strict latency constraints, and throughput bottlenecks."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2511.22481) · [PDF](https://arxiv.org/pdf/2511.22481)

## 一句话摘要

Large Language Models drive a wide range of modern AI applications but impose substantial challenges on large-scale serving systems due to intensive computation, strict latency constraints, and throughput bottlenecks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models drive a wide range of modern AI applications but impose substantial challenges on large-scale serving systems due to intensive computation, strict latency constraints, and throughput bottlenecks. We introduce OmniInfer, a unified system-level acceleration framework designed to maximize end-to-end serving efficiency through fine-grained optimization of expert placement, cache compression, and scheduling. OmniInfer integrates three complementary components: OmniPlacement for load-aware Mixture-of-Experts scheduling, OmniAttn for sparse attention acceleration, and OmniProxy for disaggregation-aware request scheduling. Built atop vLLM, OmniInfer delivers system-wide performance gains through adaptive resource disaggregation, efficient sparsity exploitation, and global coordination across prefill and decode phases. Evaluated on DeepSeek-R1 within a 10-node Ascend 910C cluster, OmniInfer achieves 616 QPM, where the unified framework reduces TPOT by 36\%, and the superimposition of OmniProxy further slashes TTFT by 38\%. The project is open-sourced at [this https URL](https://gitee.com/omniai/omniinfer).

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

- 作者：Jun Wang, Yunxiang Yao, Wenwei Kuang, Runze Mao, Zhenhao Sun, Zhuang Tao, Ziyang Zhang, Dengyu Li, Jiajun Chen, Zhili Wang, Kai Cui, Congzhi Cai, Longwen Lan, Ken Zhang
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
