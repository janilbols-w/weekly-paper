---
title: "Rethinking Edge-Device Collaborative LLM Inference for 6G AI Edge: An Empirical Evaluation"
description: "6G ubiquitous intelligence requires generative AI capabilities that far exceed the compute, memory, and energy budgets of mobile terminals."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.27994) · [PDF](https://arxiv.org/pdf/2611.27994)

## 一句话摘要

6G ubiquitous intelligence requires generative AI capabilities that far exceed the compute, memory, and energy budgets of mobile terminals.

## 为什么值得关注

待编辑增强。

## 摘要原文

6G ubiquitous intelligence requires generative AI capabilities that far exceed the compute, memory, and energy budgets of mobile terminals. By pushing large language model (LLM) inference to proximate network edge, 6G is shifting to the AI Edge era via four edge-device collaborative paradigms: edge inference, model routing, model split, and speculative decoding. However, existing evaluations are predominantly conducted in idealized datacenter settings, masking the practical challenges posed by heterogeneous hardware and stochastic wireless channels at 6G AI Edge. This article presents the first unified, hardware-in-the-loop empirical study that re-examines these paradigms under practical network conditions. Our stage-wise latency evaluation reveals that network dynamics can inflate Time-to-First-Token (TTFT) by up to 6x, while massive tensor transmissions delay speculative decoding by 246 ms and consume over 150 ms in model split. Because no single paradigm universally dominates across all performance dimensions, we advocate for a context-aware adaptive orchestration framework that dynamically selects collaboration strategies based on network conditions, terminal capabilities, and task semantics, and outline a research roadmap toward 6G AI Edge deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Cheng Wu, Xinchen Lyu, Chenshan Ren, Ziyao Yan, Qimei Cui, Xiaofeng Tao, Yang Yang
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
