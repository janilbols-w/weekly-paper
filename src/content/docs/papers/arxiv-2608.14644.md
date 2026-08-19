---
title: "DUET: Dual-Teacher On-Policy Distillation via Same-Weight Disagreement for Prohibition Compliance"
description: "Real-world LLM deployments increasingly rely on runtime-injected prohibitions--enterprise policies, PII redlines, tool boundaries--that vary per request and per tenant."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.14644) · [PDF](https://arxiv.org/pdf/2608.14644)

## 一句话摘要

Real-world LLM deployments increasingly rely on runtime-injected prohibitions--enterprise policies, PII redlines, tool boundaries--that vary per request and per tenant.

## 为什么值得关注

待编辑增强。

## 摘要原文

Real-world LLM deployments increasingly rely on runtime-injected prohibitions--enterprise policies, PII redlines, tool boundaries--that vary per request and per tenant. Conventional post-training is structurally ill-suited: SFT hides the violation signal in compliant labels, and DPO's sequence-level preferences mismatch token-localized violations. We propose DUET, a token-selective on-policy distillation method for prohibition compliance. DUET pairs a teacher that sees the prohibition (positive) with an identical-weight teacher that does not (negative). Because the two teachers differ only in prohibition visibility, their per-token disagreement isolates the prohibition's causal effect--yielding a clean supervision signal uncontaminated by model capacity or mismatch. This disagreement drives two complementary mechanisms: signal cleaning, which discards agreement tokens as redundant or prefix-corrupted, and preference-directed learning, which pushes the student away from the negative teacher and toward the positive one at token granularity, embedding DPO-style optimization directly into OPD without offline preference data. We construct an industrial Prohibition-Compliance benchmark spanning five task families covering explicit-refusal, paraphrase robustness, and over-refusal. Across 1.5B-8B Qwen variants, DUET achieves 72.3-85.2% violation compliance while preserving 88-93% normal utility, dramatically outperforming teacher model and other distillation baselines. External evaluation on SysBench confirms improved safety alignment with minimal degradation on GSM8K and MATH-500.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zihan Li, Feifei Li, Wenhui Que
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
