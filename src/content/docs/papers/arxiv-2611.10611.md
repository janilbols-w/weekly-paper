---
title: "Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed"
description: "Reproducible evaluation, verifiable inference and on-policy reinforcement learning (RL) need an LLM engine to give a request the same output bits whichever requests share its batch."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.10611) · [PDF](https://arxiv.org/pdf/2611.10611)

## 一句话摘要

Reproducible evaluation, verifiable inference and on-policy reinforcement learning (RL) need an LLM engine to give a request the same output bits whichever requests share its batch.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reproducible evaluation, verifiable inference and on-policy reinforcement learning (RL) need an LLM engine to give a request the same output bits whichever requests share its batch. Batch-invariant kernels exist, but engines still select each kernel and its parameters from the batch. Two kernels that compute the same sum can round it differently. The engines' deterministic modes remove the choice by keeping one conservative kernel per operator and pay for it in latency. Many fast kernels are batch-invariant by themselves, so it is enough to fix the few batch-dependent values that kernel selection reads. Detent expresses kernel selection as a program that the engine executes. It finds the fewest values in this program that must be fixed and tunes them for the workload before deployment. On multi-GPU deployments of Llama-3.1-70B and Qwen3-30B-A3B in vLLM and SGLang, Detent is batch-invariant. Tuned per load, it serves at 1.04-1.17x the latency per output token of Stock (each engine with its standard settings), against 1.67-10.3x for the deterministic modes. In SGLang it matches the GSM8K accuracy of SGLang's deterministic mode. Detent covers multiple deployment combinations, including multiple engines, GPU generations, tensor-parallel degrees, and dense and MoE models. Seeded RL rollouts of models up to Llama-3.1-70B replay bit for bit under other batches and cache splits. A trainer on Detent's kernels and values matches every rollout logprob bit for bit at 1.03x Stock's rollout time per token. BF16 GRPO then stays stable where Stock's run collapses.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Peixu Xin (Independent Researcher, Boston University), Runchuan Feng (Independent Researcher, Boston University), Jiazhen Guo (Google), Kan Wu (RadixArk), Ming Yin (Princeton University, Georgia Institute of Technology)
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
