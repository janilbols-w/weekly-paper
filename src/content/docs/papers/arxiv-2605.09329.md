---
title: "Test-Time Speculation"
description: "Speculative decoding accelerates LLM inference by using a fast draft model to generate tokens and a more accurate target model to verify them."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2605.09329) · [PDF](https://arxiv.org/pdf/2605.09329)

## 一句话摘要

Speculative decoding accelerates LLM inference by using a fast draft model to generate tokens and a more accurate target model to verify them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference by using a fast draft model to generate tokens and a more accurate target model to verify them. Its performance depends on the $\textit{acceptance length}$, or number of draft tokens accepted by the target. Our studies show that the acceptance length of even state-of-the-art speculators, like DFlash, EAGLE-3, and PARD, degrades with generation length, reaching values close to 1 (i.e., no speedup) within a few thousand output tokens, making speculators ineffective for long-response tasks. Acceptance lengths decline because most speculators are trained offline on short sequences, but are forced to match the target on much longer outputs at inference, well beyond their training distribution. To address this issue, we propose $\textit{Test-Time Speculation (TTS)}$, an online distillation approach that continuously adapts the speculator at test time. TTS leverages the key insight that the token verification step already invokes the target model for each draft token, providing the training signal needed to adapt the draft at no additional cost. Treating the draft as the student and the target as the teacher, TTS adjusts the draft over several speculation rounds, with each update improving the draft's accuracy as generation proceeds. Our results across ten models from the Qwen-3, Qwen-3.5, DeepSeek-R1, GPT-OSS, MiniMax, and Llama3.1 families show that TTS improves acceptance lengths over state-of-the-art speculators by up to $72\%$ and $41\%$ on average, with the benefits scaling with generation lengths.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Avinash Kumar, Sujay Sanghavi, Poulami Das
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
