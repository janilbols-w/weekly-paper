---
title: "DLoop: Looped Speculative Decoding"
description: "Speculative decoding accelerates autoregressive generation in large language models."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.07659) · [PDF](https://arxiv.org/pdf/2610.07659)

## 一句话摘要

Speculative decoding accelerates autoregressive generation in large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates autoregressive generation in large language models. In each drafting stage, a lightweight draft model proposes tokens that the target model subsequently verifies. With increasingly capable draft models, we find that the target model frequently accepts all tokens produced in a drafting stage. A verification nevertheless follows each drafting stage, resulting in unnecessary target-model forward passes even when drafting could have continued. Adaptive draft length methods decide during decoding how many draft tokens precede a verification, but they raise the speedup only for autoregressive draft models. For a parallel draft model, drafting further requires target-model hidden states for draft tokens that have not been verified. We propose DLoop, a looped form of speculative decoding that adaptively performs multiple drafting stages before verification. DLoop continues drafting while the draft model remains confident and verifies all accumulated draft tokens together. Loop-aware training keeps the draft model reliable in the additional drafting stages by exposing it to its own hidden states for unverified draft tokens. By spending additional draft-model forward passes, DLoop reduces the number of target-model forward passes required for verification. Across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction modules, DLoop improves the wall-clock speedup by 5 to 41 percent while preserving lossless decoding. Code will be available at https://github.com/naver-ai/DLoop.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Geonmo Gu, Byeongho Heo, HeeJae Jun, Yoohoon Kang, Sangmin Lee, Sangdoo Yun, Dongyoon Han
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/naver-ai/DLoop](https://github.com/naver-ai/DLoop)
- 阅读深度：metadata
