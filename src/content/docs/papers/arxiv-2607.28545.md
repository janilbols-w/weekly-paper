---
title: "ORCA-bench: How Ready Are Language Model Agents for Oncall?"
description: "Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2607.28545) · [PDF](https://arxiv.org/pdf/2607.28545)

## 一句话摘要

Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs 1,079 RCA tasks with six days of metrics, logs, and traces collected from an OpenTelemetry-instrumented microservice system under continuous simulated user load. Agents investigate this recorded history through real observability interfaces---Prometheus, Jaeger, and OpenSearch via Grafana---with full access to application source code. Tasks systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's $\kappa_w = 0.91$). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard---a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access reduces RCA accuracy and increases the hallucination rate for every evaluated model. These results come from a curated 50 GB / six-day testbed of standalone tasks on a system whose code and instrumentation are public. Since real production systems are orders of magnitude larger, more dynamic, and more idiosyncratic, the gap we report underscores the engineering work still needed before agents can be entrusted with production reliability. We release the public set at https://hub.harborframework.com/datasets/orca-bench/orca-bench.

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

- 作者：Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
