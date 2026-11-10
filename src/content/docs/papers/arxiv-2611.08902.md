---
title: "Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving"
description: "Prefix caching lets an LLM agent's follow-up turns reuse cached KV, but a burst can tip an engine into a trap in which every turn misses and the backlog does not drain, at a load it served before."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.08902) · [PDF](https://arxiv.org/pdf/2611.08902)

## 一句话摘要

Prefix caching lets an LLM agent's follow-up turns reuse cached KV, but a burst can tip an engine into a trap in which every turn misses and the backlog does not drain, at a load it served before.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix caching lets an LLM agent's follow-up turns reuse cached KV, but a burst can tip an engine into a trap in which every turn misses and the backlog does not drain, at a load it served before. In registered paired tests on two engines, two GPUs and two models (passed at 9 of 10 rates), a 200-session burst left the engine at zero hits to the end in all 30 runs, while every matched no-burst run stayed good and a session cap prevented the trap in all 30 capped runs. We analyse an idealization of the trapped state exactly: for a fluid FIFO server on which every turn misses, we prove that along FIFO orbits its cycles obey a linear renewal recursion. As is classical, the trap drains if and only if arrivals are below the all-miss capacity; above it, a Perron root fixes the dynamics: every trapped state converges to a known self-similar regime in which the gap between turns grows linearly and the turns served are young and short. For our workload the backlog grows at 0.6 to 0.8 of the excess load and sessions complete faster than the all-miss capacity, a youth premium with turn-count and cost-growth factors, so in the model a trap's measured throughput overstates the recovery threshold. Retrospectively, with nothing fitted to trap data, the theory matches 57 stuck runs: the mean served prompt within 3% in 50 runs, completions above the all-miss capacity in every run, and the pooled gap growth. Blind in outcome, 4 runs trapped by a tool slowdown met 4 of 5 pre-set scores, cut traps persisted, and with a 20-step budget, trapped runs completed below the all-miss capacity, as predicted. Of two exits, refusing arrivals sheds sessions; a session cap restores reuse: in registered tests it rescued 9 of 9 established traps at the same load without shedding, and the engine stayed good after release. We do not prove that the engine converges to the model.

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

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Akshat Valse, Ali Jannesari
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
