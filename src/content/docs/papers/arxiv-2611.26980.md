---
title: "Contexture: Runtime Context Eviction for High-Throughput Agent Serving"
description: "LLM agents such as Hermes, OpenClaw, and Codex repeatedly resend growing execution histories, increasing shared GPU key-value (KV) cache demand in high-bandwidth memory (HBM)."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2611.26980) · [PDF](https://arxiv.org/pdf/2611.26980)

## 一句话摘要

LLM agents such as Hermes, OpenClaw, and Codex repeatedly resend growing execution histories, increasing shared GPU key-value (KV) cache demand in high-bandwidth memory (HBM).

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents such as Hermes, OpenClaw, and Codex repeatedly resend growing execution histories, increasing shared GPU key-value (KV) cache demand in high-bandwidth memory (HBM). We show that shared KV capacity limits agent-serving throughput. Existing context-reduction methods lack global cache-state visibility, while runtime KV managers lack tool-execution information. Tracing tokens to their originating tool operations reveals that later operations supersede earlier outputs and associated turns, identifying 64% of recorded final-history tokens as removal candidates. We present Contexture, a harness- and model-agnostic architecture for runtime context eviction. Contexture separates the harness's full conversation history from the model's execution context, reducing subsequent requests' KV demand without modifying harness logic or model execution. It combines tool-execution information with global visibility into shared KV pressure and prefix residency: supersession identifies removal candidates, while runtime state determines when removal justifies sacrificing cached computation. This coordination reduces memory demand and decode KV traffic while limiting re-prefill interference with concurrent decoding, without additional model calls or training. Across two models, two harnesses, and two benchmarks, Contexture improves throughput under SLO by 20-73% over the best of no eviction, harness compaction, AgentDiet, and Continuum, and by 7-63% over observation masking in five of eight configurations, and reduces GPU energy per completed session by up to 11%. It also raises throughput under SLO by 23% over LMCache alone on H100. Live-agent experiments show a mean accuracy improvement of 1.4 percentage points over unloaded no eviction, with a worst-case loss of 3.7 points, while observation masking loses 3-28 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Colin Hong, Bryan Shan, Wei Siong Pang, Chengzhi Lu, Xu Guo, Nitin Shivaraman, Tao Luo, Esha Choukse, Kisson Lin, Dmitrii Ustiugov
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
