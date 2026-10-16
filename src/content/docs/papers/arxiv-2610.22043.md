---
title: "Momentum, Commentary Tone, and Earnings Surprise in LLM Financial Forecasts"
description: "Which inputs drive a language model's financial forecast?"
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.22043) · [PDF](https://arxiv.org/pdf/2610.22043)

## 一句话摘要

Which inputs drive a language model's financial forecast?

## 为什么值得关注

待编辑增强。

## 摘要原文

Which inputs drive a language model's financial forecast? We construct synthetic earnings announcements that independently reverse 20-day momentum, non-informational commentary tone, and whether fixed actual EPS beats a manipulated consensus. Six instruction/chat checkpoint conversions from four families (0.49-7.61B base parameters) receive 2,016 prompts each under a direct-answer Q8_0 protocol. The design includes 24 numerical blocks, six commentary pairs, profits and losses, rising and falling annual EPS, and two surprise sizes. Both A/B answer assignments and U/D cover all 384 primary scenarios per conversion. We estimate matched changes in conditional answer-prefix scores, not calibrated market probabilities. Across these checkpoints, the primary EPS contrast ranges from -0.19 to 86.80 percentage points. The magnitude of the primary signed tone contrast exceeds that of EPS in 5 of six models, and momentum exceeds it in 5. Natural-word numerical diagnostic accuracy ranges from 51.0 to 95.8 percent. Answer-encoding, wording, context, and conversion controls qualify these results. The experiment measures observable input reliance and numerical recognition; it establishes neither an internal reasoning mechanism nor realized return predictability. Public benchmark prompts, recorded scores, and an interactive recorded-results explorer accompany the study.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Alina Khaybullina
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
