---
title: "TRIAGE: Reliability- and Load-Conditioned Escalation for Two-Tier LLM Serving with a Semantic Evidence Judge"
description: "Two-tier LLM serving escalates selected requests from a small model to a large one, but prompt-based routers cannot see whether retrieved evidence supports an answer, and they treat the GPU cost of an escalation as constant."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.01174) · [PDF](https://arxiv.org/pdf/2611.01174)

## 一句话摘要

Two-tier LLM serving escalates selected requests from a small model to a large one, but prompt-based routers cannot see whether retrieved evidence supports an answer, and they treat the GPU cost of an escalation as constant.

## 为什么值得关注

待编辑增强。

## 摘要原文

Two-tier LLM serving escalates selected requests from a small model to a large one, but prompt-based routers cannot see whether retrieved evidence supports an answer, and they treat the GPU cost of an escalation as constant. We study TRIAGE, which conditions escalation on a post-generation reliability state and on a load-dependent GPU price, and we report both what held and what did not on one A40 serving Qwen2.5-7B and 32B (AWQ) under VLLM. Escalation cost rose 21.9x from 1 to 10 requests/s but showed no monotone dependence on KV-cache headroom, and a pre-registered claim that the reliability state detects corrupted evidence (AUROC>=0.70) was falsified at 0.571, although any prompt-only router scores exactly 0.500 by construction. Post hoc, a semantic evidence judge raised detection to 0.846 (0.926 on never-served items) and predicted wrong small-model answers at AUROC 0.90-0.96 on RGB and three RouterBench model pairs; the resulting cascade stayed within about 3 pp of GPT-4 at 79.5% lower API cost for GPT-3.5->GPT-4, yet fell below random routing for open-model pairs with 2-3x price ratios. End to end, the 7B->32B pair showed only a +2.88 pp held-out gap, so the allocator rightly declined to escalate and the headline is a null that a small pre-launch gate failed to expose.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Basavaraj R M, Aryan Bharat Kumar
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
