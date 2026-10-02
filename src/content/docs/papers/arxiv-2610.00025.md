---
title: "Measuring the Microtask Eligibility Gap: When Is an Off-the-Shelf SLM Enough for an Agent Harness?"
description: "Agent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting tools, ranking past turns."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00025) · [PDF](https://arxiv.org/pdf/2610.00025)

## 一句话摘要

Agent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting tools, ranking past turns.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting tools, ranking past turns. We ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantization changes the answer. We build a benchmark of 4 such microtasks with fixed prompts and automatic metrics, each with a pre-specified threshold $\tau$ anchored to a cheap non-LLM baseline and a CI-aware eligibility rule (a configuration passes only if its confidence bound clears $\tau$). Sweeping Qwen3 0.6/1.7/4/8B at their best (FP16, greedy, one frozen prompt, no tuning), we find an eligibility gap: 0 of 16 (4 tasks $\times$ 4 models) configurations pass (verified by checking the raw outputs and parser behavior). A logprob decision-threshold diagnostic (T1/T3/T4; T2 via a context-length/cascade probe) separates the failures into capability deficits and failures that can be addressed by changing the decoding threshold (4 regimes). Quantization to 4-bit (RTN/GPTQ/AWQ) does damage that depends on model size and moves no configuration into eligibility (certified on the reconstructable hard-label tasks T1/T3, diagnostic/windowed robustness on T2/T4), so the gap tracks model size more than precision; it replicates on Llama-3.x (12/12 ineligible) and is robust to the anchor choice (a $\tau$-sweep) and to prompt wording (0/112 eligible across the original plus 3 neutral paraphrases per cell). The practical implication: place SLMs behind a baseline that meets the CI-backed threshold, and use the SLM only where the baseline fails to meet the threshold; e.g. a 4B re-ranker over a BM25 shortlist beats BM25 ($+0.047$ [0.020, 0.073], without itself certifying eligibility).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jundong Hu, Shekar Ramachandran
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
