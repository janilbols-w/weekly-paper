---
title: "Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving"
description: "Serving open-weight language models on premises forces a trade-off between accuracy and computational cost."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2606.27457) · [PDF](https://arxiv.org/pdf/2606.27457)

## 一句话摘要

Serving open-weight language models on premises forces a trade-off between accuracy and computational cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving open-weight language models on premises forces a trade-off between accuracy and computational cost. Hosting models of different sizes lets easy queries go to a small, efficient model and hard ones to a large model. We present CRE-Router (Cluster, Route, Escalate), a two-stage method that decides which of these models answers each query. It clusters queries and routes each cluster to the model that best trades error against cost, under a budget on the time per output token (TPOT) or the end-to-end latency per request (E2EL). It then either accepts the answer or, when a quality estimator rejects it, escalates the query to the strong model. Routing decides before generation, so a hard query goes straight to the strong model; escalation decides after, so it can catch the errors routing cannot predict. It needs no annotation beyond task-correctness labels. We evaluate CRE-Router on TeleMath, TeleQnA and AIME, with pools of two to nine models served on A100 GPUs. CRE-Router is more accurate than the efficient models in its pool and comparable to the strong model it escalates to, at a lower cost per token. We also find that the choice of cost term decides which models serve the workload, that pricing each model per cluster shortens the wait per request, and that a change of hardware changes the best routing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yasmin Moslem, Magdalena Kacmajor, Vasudevan Nedumpozhimana, Ammar Abbas, Solmaz Panahi, David Lynch, Zhuangzhuang Nie, Alexandros Agapitos, Aleksandar Milenovic, Hongmeng Song, Yucheng Shi, Yue Pan, Patricia Buffini, John D. Kelleher
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
