---
title: "Codifying the Judge: Scalable Evaluation via Program Distillation"
description: "LLM-as-a-judge has become the standard for automated evaluation, but it suffers from high cost, inference latency, and opaque decisions---limitations that undermine its scalability and reliability."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.22561) · [PDF](https://arxiv.org/pdf/2607.22561)

## 一句话摘要

LLM-as-a-judge has become the standard for automated evaluation, but it suffers from high cost, inference latency, and opaque decisions---limitations that undermine its scalability and reliability.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-as-a-judge has become the standard for automated evaluation, but it suffers from high cost, inference latency, and opaque decisions---limitations that undermine its scalability and reliability. We address these with a simple, efficient alternative: program distillation. Instead of prompting an LLM at evaluation time, we distill its decision logic into a committee of programs that can score candidates directly. These programmatic judges offer transparency, are easily inspected or edited, and eliminate per-sample API costs. Building on this notion, we introduce PAJAMA, a system that synthesizes programs as judges, aggregates their decisions into a joint verdict, and incorporates a fallback mechanism to selectively escalate low-confidence cases to an LLM. Across five datasets and eight model families, we show that programmatic judges match the performance of a 13B-size LLM judge at 47x higher throughput. When using program outputs as routing signals, PAJAMA improves both accuracy and throughput and advances the Pareto frontier. Beyond evaluation, programmatic judges produce cheap and effective reward signals: on RewardBench, a reward model distilled from programs' verdicts outperforms one trained on a proprietary LLM's labels at two orders of magnitude lower API cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tzu-Heng Huang, Shengqi Qiu, Frederic Sala
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
