---
title: "Stateless Language Agents: Scaling Long-Horizon Automated Research"
description: "Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay growing histories, duplicate one another's work, or stop experimenting while token consumption continues."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.07625) · [PDF](https://arxiv.org/pdf/2610.07625)

## 一句话摘要

Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay growing histories, duplicate one another's work, or stop experimenting while token consumption continues.

## 为什么值得关注

待编辑增强。

## 摘要原文

Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay growing histories, duplicate one another's work, or stop experimenting while token consumption continues. Yet most evaluations use short budgets or benchmarks that saturate early, leaving these failure modes untested. We trace these failures to two choices: where research state lives and who decides what to try next. We introduce Stateless Language Agents (SLAs), built on the principle of stateful search with stateless agents: no agent carries its conversation across invocations; instead, the harness owns the research state (candidate solutions and measured outcomes) and reconstructs a fresh and role-specific context for every invocation. What each agent sees becomes an explicit design choice rather than a history that grows with the run. We implement this principle in the SLA framework, where a stateless Advisor reads harness-summarized evidence across search directions and assigns concrete experiments to parallel Workers. We evaluate SLA against three recent frameworks on software engineering, kernel optimization, and algorithm design at budgets of up to one billion tokens. SLA achieves the best final result on every task and reaches the strongest kernel baseline's final performance with over 84% fewer tokens. Ablations from shared checkpoints show that focused contexts and explicit assignments each contribute to SLA's progress, with effects that can compound over full runs, while the Advisor consumes less than 0.6% of tokens. These results argue for SLAs, which keep durable research state out of agent conversations, and show that short evaluation horizons can misjudge research systems and their components.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 17 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qizheng Zhang, Changxiu Ji, Isaac Sun, Yuetai Li, Shubhangi Upasani, Sherry Ruan, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Yoonho Lee, Yuzhen Mao, Genghan Zhang, Rulin Shao, Qiuyang Mang, Andy Dimnaku, Changran Hu, Radha Poovendran, Kunle Olukotun
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
