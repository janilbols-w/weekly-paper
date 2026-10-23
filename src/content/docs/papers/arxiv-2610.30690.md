---
title: "From Clinical Judgment to Checkable Rules: Clinician-Led Guardrails for Mental-Health Chatbots"
description: "Large language models (LLMs) deployed in mental-health contexts can be evaluated for safety failures, but the resulting judgments are often difficult to inspect or explain."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.30690) · [PDF](https://arxiv.org/pdf/2610.30690)

## 一句话摘要

Large language models (LLMs) deployed in mental-health contexts can be evaluated for safety failures, but the resulting judgments are often difficult to inspect or explain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) deployed in mental-health contexts can be evaluated for safety failures, but the resulting judgments are often difficult to inspect or explain. Common approaches to improving safety rely on prompt engineering, LLM-as-a-Judge, and Constitutional AI. In this work, we describe a clinician-led alternative in which two clinicians define, finalize, and adjudicate the four safety checks of a rule base, which is formally verified for internal consistency and applied as a guardrail over LLM outputs. Here and in the title, clinician-led refers to this rule base, not to the fact extractor or the uncertainty default, which are ours. Every verdict of the resulting verification layer is recomputable from a named rule and sixteen facts. Against an LLM judge matched in model, revision, quantization, rule text, and decoding but without the layer's computed 988/911 fact, the largest disagreement class, the satisfied-rule class, is structured: the Llama-3.3-70B judge, on its primary prompt, demands a crisis resource from 55 of the 65 replies (84.6%) that already contain one, while the same model, asked as a fact extractor, reports a recognized resource present on 54 of the 55. The verification layer never raises that demand, by construction. We report with equal prominence where this judge is stronger: fewer false crisis alarms on the one reference-scored check. We also report the measured cost (a specification revision raised block-class outcomes on held-out boundary prompts of an over-refusal benchmark from 6.0% to 16.0%, chiefly by changing fact extraction), the clinicians' decision to keep our uncertainty default, and the analysis of the result. The contribution is not a safer verdict. It is a guardrail whose disagreements with the judge localize to named rules and facts and whose measured costs trace to named facts and the uncertainty default.

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

- 作者：Chenhan Lyu, Kit Wislocki, Sarah Elizabeth Stoeckl, Maitreyi Sinha, Amir Rahmani
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
