---
title: "AgentDiff: Meaning-Bearing Rewrites Trigger Deeper Divergence than Presentation Changes in LLM Agents"
description: "LLM agents should respond to what an input means, not how it is presented."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2605.25981) · [PDF](https://arxiv.org/pdf/2605.25981)

## 一句话摘要

LLM agents should respond to what an input means, not how it is presented.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents should respond to what an input means, not how it is presented. We show that they do not treat these two kinds of variation equally. AgentDiff measures the difference between answer changes caused by meaning-bearing rewrites (paraphrase and synonym substitution) and presentation changes (reordering, formatting, and distractors), while matching perturbation severity. Across 68 model--benchmark--scaffold cells spanning ten LLMs from seven architecture families, three benchmarks, 1{,}530 original questions, and approximately 11{,}150 variants, meaning-bearing rewrites produce a $+19.69$ percentage-point higher inconsistency rate (paired $t=9.58$, $p<0.0001$; 64/68 cells positive). The result is stable under four severity proxies ($+18.9$ to $+20.9$~pp, all $p<0.0001$) and remains $+11.10$~pp on the 48 cells outside the qwen family. A fully held-out qwen2.5-14B-Instruct evaluation then tests the structure of this effect on 1{,}800 new trajectories: the pre-registered capable-and-tractable partition is positive in 3/4 held-out cells and remains sharply separated after pooling (Welch $t=3.81$, $p=9.6\!\times\!10^{-4}$). Trace analysis explains how the difference propagates. Meaning-bearing rewrites preserve the first action but reduce thought similarity from step 2 onward by $5.6$--$10.5$ points and extend the resulting cascade by $0.17$ steps (paired $t=7.69$, $p=2.5\!\times\!10^{-14}$), a pattern we call \emph{stealth divergence}. AgentDiff therefore establishes a reproducible directional robustness gap, identifies the regime in which it is most reliable, and connects final-answer inconsistency to a distinct trajectory-level signature. Code, perturbations, trajectories, and analysis scripts are released for review at https://anonymous.4open.science/r/agentdiff-emnlp-0BB4/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: trace analysis
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liyun Zhang, Jiayi Guo
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
