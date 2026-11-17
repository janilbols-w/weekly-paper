---
title: "Choosing Quantized Code LLMs by File Size and Energy per Solved Task"
description: "A developer running a code assistant on a laptop downloads one model file, and local inference moves the energy of every request onto that machine."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.17605) · [PDF](https://arxiv.org/pdf/2611.17605)

## 一句话摘要

A developer running a code assistant on a laptop downloads one model file, and local inference moves the energy of every request onto that machine.

## 为什么值得关注

待编辑增强。

## 摘要原文

A developer running a code assistant on a laptop downloads one model file, and local inference moves the energy of every request onto that machine. A common rule says a larger model at lower precision tends to beat a smaller one at higher precision. We ran 24 GGUF files of Qwen2.5-Coder at four sizes on a fanless MacBook Air M2 and priced each in energy per solved task on 542 EvalPlus tasks. The result is a selection guide indexed by Ollama's listed file size, with an evidence label on each pick. At 1 and 2 GB it picks the q4_K_M files of the 1.5B and 3B models, both on the correctness and energy frontier under every accounting. At 3 GB as listed, the larger-model rule picks 7B-q2_K, the only measured 7B file that fits, and there it does not pay. That file brings no significant gain in solves over the 2 GB pick, 3B-q4_K_M, and the 90% CI limits any 3B-q4_K_M deficit to 2.4 points. Yet 7B-q2_K needs 2.03 times the energy per solved task on CPU, GPU and memory rails, or 1.66 to 1.81 times on whole-system power. On HumanEval+, five alternating session pairs give a ratio of 1.925 against 1.956 in the main grid. At 8 GB, 7B-q6_K buys a significant gain over the 2 GB pick at a higher energy price. From 1.5B up, q4_K_M trails the highest precision measured at its size by less than 3 points (90% CI). We release per-task results, power logs and the analysis script.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aditi Patodiya
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
