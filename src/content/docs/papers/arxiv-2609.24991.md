---
title: "Who Pays for the KV Cache? Attributing Shared AI Inference Spend Across Kubernetes and LLM Provider Bills"
description: "Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.24991) · [PDF](https://arxiv.org/pdf/2609.24991)

## 一句话摘要

Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Organizations pay for AI through disconnected ledgers: Kubernetes allocations for self-hosted inference, gateway logs, and per-token bills from API providers. We present unalloc, an open-source tool that joins OpenCost, LiteLLM, OpenAI and Anthropic cost data into one exact ledger and reports the share of spend with no owner, and use it to study where attribution breaks at the seams between these systems. Five case studies run inference for real or simulate it: a vLLM-style serving simulator with paged KV memory and prefix caching; a PyTorch transformer serving a multi-tenant trace with a real KV cache; tensor- and pipeline-parallel inference on torch.distributed; the unmodified CLI against mock provider APIs; and four downstream use cases. At the seams, in a constructed multi-pod deployment scenario -- one month of synthetic OpenCost allocations, not observed billing data -- owner labels set only on LeaderWorkerSet leader pods leave 66% of that deployment's GPU bill unowned, and the natural fallback key assigns 61% of it to a Helm chart name while the headline unallocated share falls to 4%; enabling every source double counts all gateway spend; and reading one page of a billing API reports a quarter of spend. Inside a shared inference server the metering rule decides who pays: on an NVIDIA H100 running vLLM, a token meter assigns a retrieval-heavy tenant 12-14 percentage points more of the bill than an equal time-share meter at every load tested, while GPU utilization reads 97-99% across configured loads of 2 to 16 requests per second (3.7 to 26.9 completed requests per second; the configured rate counts session-initial arrivals only) and power draw tracks load. Neither meter is a ground truth; we position these results against recent Shapley-based energy attribution. Code, raw data, captured evidence, figures and the paper regenerate from the repository.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Timothy Urista
- 发布：2026-09-21；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/timurista/unalloc](https://github.com/timurista/unalloc)
- 阅读深度：metadata
