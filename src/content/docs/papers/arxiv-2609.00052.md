---
title: "AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes"
description: "Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.00052) · [PDF](https://arxiv.org/pdf/2609.00052)

## 一句话摘要

Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Commercial LLM APIs advertise a specific foundation model, but the served backbone may be silently substituted, quantized, or wrapped, for example to save deployment costs. All existing audits decide backbone identity from the text-output channel, which is structurally fragile for agentic APIs because modern serving stacks (OpenAI, Anthropic, Gemini, Cloudflare Workers AI, LangGraph) discard text and expose only structured actions when the model calls a tool, and provider-injected system prompts can distort text distributions enough that text-channel tests falsely accuse honest providers of substituting the claimed model. We observe that recent agentic post-training internalizes tool-use directly into the weights, opening a new audit channel that the serving stack still exposes and that is largely invariant to deployment context. We introduce Agentic Provenance (AgentProv), the first action-based identity audit for agentic LLM APIs: AgentProv fingerprints a deployed model through its categorical tool-call distribution and decides identity via an MMD permutation test. AgentProv catches every substituted model (100% on 630 evaluated checkpoint pairs), while holding the false-positive rate under system-prompt injection at 7% (vs. 67% for MET and 53% for RUT). On third-party API endpoints, AgentProv's disagreements with MET are consistent with an independent token-count side-channel that detects provider-injected system prompts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xun Wang, Bihe Zhao, Michael Backes, Franziska Boenisch, Adam Dziedzic
- 发布：2026-08-30；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
