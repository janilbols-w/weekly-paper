---
title: "How far do on-premises open LLMs get on Text-to-SQL? A cross-family size and technique frontier on BIRD"
description: "Organizations that cannot send data to a cloud API need to know how well self-hosted open-weight models perform on Text-to-SQL and which inexpensive techniques justify their compute."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.29733) · [PDF](https://arxiv.org/pdf/2606.29733)

## 一句话摘要

Organizations that cannot send data to a cloud API need to know how well self-hosted open-weight models perform on Text-to-SQL and which inexpensive techniques justify their compute.

## 为什么值得关注

待编辑增强。

## 摘要原文

Organizations that cannot send data to a cloud API need to know how well self-hosted open-weight models perform on Text-to-SQL and which inexpensive techniques justify their compute. We benchmark Qwen2.5-Coder-Instruct (7B, 14B, 32B) and CodeLlama-Instruct (7B, 13B) self-hosted at 16-bit precision, Llama-3.1-8B and Llama-3.3-70B through an FP8 API, and Qwen2.5-Coder-32B through a second API on the BIRD development split (n = 1534), with one zero-shot prompt and the official execution-accuracy comparison on read-only databases. We ablate lexical and embedding schema linking, execution-guided self-correction and self-consistency, and test every within-model recipe difference with exact McNemar tests, Holm correction over 30 tests and a database-clustered bootstrap. Qwen2.5-Coder reaches 42.6%, 52.0% and 54.9%; CodeLlama-7B and -13B reach 23.7% and 26.3%. Self-correction is the only component with a consistent gain: within a run it adds 1.2 to 4.4 points at 1.1 to 1.9 times the tokens, and it is significant after Holm correction for every model except Llama-3.3-70B. Schema linking never helps significantly; lexical linking costs Llama-3.3-70B 4.2 points, and an embedding linker with higher table recall does not differ detectably from no linking. Self-consistency, run for one model, changed accuracy by at most 0.13 points at about five times the tokens. One API provider dropped spaces next to digits; after a whitespace repair the same model scored 54.5% through the API and 54.9% self-hosted, so an apparent three-point serving gap was mostly this defect. This version corrects six defects of v1, including writable databases, a stricter-than-official metric and a truncated API arm, and withdraws the v1 claim of a quantization penalty of about 13 points; all numbers are re-scored or re-run. Code, per-item predictions and analysis scripts are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Vladimir Beskorovainyi
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
