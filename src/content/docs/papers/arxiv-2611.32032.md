---
title: "Provenance-Isolated Epistemic Quorums: Execution-Bound Evidence Certification and Plausible-World Safety Gating in Agentic Control Planes"
description: "Agreement among large language models is not physical evidence for mutating production infrastructure."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](http://arxiv.org/abs/2611.32032v1) · [PDF](https://arxiv.org/pdf/2611.32032v1)

## 一句话摘要

Agreement among large language models is not physical evidence for mutating production infrastructure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agreement among large language models is not physical evidence for mutating production infrastructure. Because generative models share pretraining priors and conform to peer rationales during deliberation, voting ensembles correlate errors instead of providing independent fault tolerance; yet attaching rigid deterministic checks to unconstrained agent outputs paralyzes incident remediation. We present Provenance-Isolated Epistemic Quorums (PIEQ), an execution-bound certification layer that keeps every language model strictly outside the trusted computing base. PIEQ unifies assumption-based truth maintenance, physical provenance isolation, control-theoretic plausible-world safety shielding, and linearizable concurrency governance around three distinct obligations: certifying diagnostic preconditions from disjoint physical failure domains, gating candidate mutations across all unrefuted fault worlds while falling back to read-only diagnostic probes under ambiguity, and binding admission certificates to target execution through snapshot barriers, revision checks, authorization freshness, trusted temporal-precondition policies, and capability-tiered enforcement. Across formal guarantees, automated etcd fault suites, frozen software benchmarks, and live language-model runs, PIEQ achieves zero within-assumption unsafe admissions and zero false-precondition commits, converting occasional agent proof omissions into recoverable false blocks rather than unsafe actions. On a physical PostgreSQL/Patroni cluster, PIEQ gates supervised failovers alongside Patroni and etcd's native split-brain protection and enforces a full Tier E2 contract inside a single serializable PostgreSQL transaction for bounded capacity reservations. All benchmarks are author-labeled, live model snapshots are unpinned, and Tier E2 physical failover promotion as well as multi-host hardware fault isolation remain open work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jun He, Deying Yu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/openkedge/openkedge/tree/main/research/pieq](https://github.com/openkedge/openkedge/tree/main/research/pieq)
- 阅读深度：metadata
