---
title: "Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation"
description: "LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2611.18471) · [PDF](https://arxiv.org/pdf/2611.18471)

## 一句话摘要

LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory. In deployed agent systems, the same execution may be exposed through composed tools, delegation boundaries, or compacted histories, changing what execution evidence is directly observable to the verifier. It therefore remains unclear whether correct verifier judgments persist across such abstraction boundaries. We introduce Verification Transport, a reliability test that measures judgment stability under abstraction-induced changes in execution observability. We construct matched native, abstracted, and restored views of the same frozen executions while holding the task, realized trajectory, outcome, ground truth, evaluation criterion, and verifier fixed. Across four agent-evaluation benchmarks, seven verifier backbones, four verification protocols, and three abstraction boundaries, we find substantial transport failure, reaching about 31% under macro abstraction and delegation. Verification protocols exhibit distinct failure modes: direct verification more often produces incorrect verdicts, whereas evidence-grounded and deliberative protocols tend to abstain under limited observability. This suggests that lower transport failure rates do not necessarily imply greater reliability. Restoring the corresponding execution provenance recovers 85.5% of transport failures, while recovery is lower when provenance is lossy or unavailable. These results show that native-view accuracy alone is insufficient to characterize verifier reliability when execution evidence crosses abstraction boundaries.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Disha Sheshanarayana, Sai Linisha Reddy Goli
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
