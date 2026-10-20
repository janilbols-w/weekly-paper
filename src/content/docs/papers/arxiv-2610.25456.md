---
title: "System X: An LLM Decision Model That Replies from Its Own KV Cache"
description: "Decision models return probabilities over supplied options, but a deployed agent may also need to reply in words."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.25456) · [PDF](https://arxiv.org/pdf/2610.25456)

## 一句话摘要

Decision models return probabilities over supplied options, but a deployed agent may also need to reply in words.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decision models return probabilities over supplied options, but a deployed agent may also need to reply in words. The present study introduces System X, a large language model (LLM) decision model that adds a text-reply option to the LLM-as-Jev readout. When this option wins, or confidence is low, the same model continues from the decision's key-value (KV) cache, avoiding a repeated prompt prefill. Qwen3-0.6B has been fine-tuned with LoRA on Reason-9k and Bitext reply rows. JevBench accuracy shows no statistically significant change (55.4% to 54.5%, p=0.87), while expected calibration error falls from 0.292 to 0.169. Held-out Bitext routing accuracy reaches 98.3%. Cache reuse saves 15-37% of latency on an Apple M4 Pro, with token-identical replies in the FP32 demonstration cases. Scoring options on copies of the prompt cache matches full-sequence scoring to within 1.4e-6 in probability. Adding dialogue, industry and complaint data (System X+) improves support-task results but lowers IFEval accuracy from 55.5% to 45.0%. System X v4 uses Qwen3-1.7B, rebalanced data and teacher-rewritten reply targets. Against its base LLM, JevBench accuracy rises from 55.0% to 61.0% (p=0.04), with no statistically significant IFEval change (p=0.71). A matched latency test on unadapted Qwen3-1.7B saves 17-39%. One LLM judge prefers v4 replies to an unadapted 1.7B second call (31 to 11 pairs, p=0.003); the other's preference is not significant. These reply comparisons also differ in prompts and generation limits. State conflicts and unsupported reply details remain failure modes. Further studies with several seeds, human raters and real support data are recommended.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
