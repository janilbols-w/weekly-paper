---
title: "Intelligence per Watt: Measuring Intelligence Efficiency of Local AI"
description: "Large language model (LLM) queries are predominantly processed by frontier models in centralized cloud infrastructure."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2511.07885) · [PDF](https://arxiv.org/pdf/2511.07885)

## 一句话摘要

Large language model (LLM) queries are predominantly processed by frontier models in centralized cloud infrastructure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) queries are predominantly processed by frontier models in centralized cloud infrastructure. Demand growth strains this paradigm faster than providers can scale. Two advances create an opportunity to rethink it: small, local LMs (<=20B active parameters) now achieve competitive performance to frontier models on many tasks, and local accelerators (e.g., Apple M4 Max) can host these models at interactive latencies. This raises the question: can local inference viably redistribute demand from centralized infrastructure? This requires measuring both whether local LMs can accurately answer real-world queries and whether they can do so efficiently on power-constrained devices (e.g., laptops). We propose intelligence per watt (IPW), task accuracy per unit of power, as a unified metric for the capability and efficiency of local inference across model-accelerator configurations. We evaluate 20+ state-of-the-art local LMs, 8 hardware accelerators (local and cloud), and 1M real-world single-turn chat and reasoning queries. For each query, we measure accuracy (local LM win rate against frontier models), energy, latency, and power. We find three key results. First, local LMs successfully answer 88.7% of these queries, with accuracy varying by domain. Second, longitudinal analysis from 2023-2025 shows IPW improved 5.3x, driven by both algorithmic and accelerator advances, with locally-serviceable query coverage rising from 23.2% to 71.3%. Third, local accelerators achieve at least 1.4x lower IPW than cloud accelerators running identical models, revealing significant headroom for local accelerator optimization. These findings demonstrate that local inference can meaningfully redistribute demand from centralized infrastructure for a substantial subset of queries, with IPW serving as the critical metric for tracking this transition.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jon Saad-Falcon, Avanika Narayan, Hakki Orhun Akengin, J. Wes Griffin, Herumb Shandilya, Adrian Gamarra Lafuente, Medhya Goel, Rebecca Joseph, Shlok Natarajan, Etash Kumar Guha, Shang Zhu, Ben Athiwaratkun, John Hennessy, Azalia Mirhoseini, Christopher R\'e
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
