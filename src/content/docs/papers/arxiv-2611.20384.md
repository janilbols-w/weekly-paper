---
title: "JointQ: Joint Scale-and-Integer Quantization for Large Language Models"
description: "GPTQ is the de facto standard solver for layer-wise post-training quantization (PTQ) of large language models, yet the solver itself has received less attention than weight preprocessing and cross-layer objectives."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.20384) · [PDF](https://arxiv.org/pdf/2611.20384)

## 一句话摘要

GPTQ is the de facto standard solver for layer-wise post-training quantization (PTQ) of large language models, yet the solver itself has received less attention than weight preprocessing and cross-layer objectives.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPTQ is the de facto standard solver for layer-wise post-training quantization (PTQ) of large language models, yet the solver itself has received less attention than weight preprocessing and cross-layer objectives. We target a bottleneck of GPTQ: its greedy procedure optimizes continuous group scales separately from the assignment of discrete integers. Evaluating each integer candidate with its closed-form optimal scale has been used for per-channel quantization; JointQ extends it to group-wise quantization, where a row's scales are coupled through the Hessian, and applies it to refine the GPTQ solution. Each local-search move changes one integer and recomputes its group's optimal scale in closed form, accounting for the other groups through the full Hessian; all scales are periodically re-solved jointly. The search starts from a row-wise selection among scale-refitted candidates including the GPTQ solution, so unregularized JointQ never has a larger layer-wise calibration error than GPTQ. JointQ preserves the GPTQ output format and is thus a drop-in replacement. Across four models and four settings, JointQ improves six-task average zero-shot accuracy over vanilla GPTQ in 14 of 16 comparisons and perplexity in 12 of 16. The mean accuracy gain increases from 0.0044 in W4G128 to 0.1559 in W3 per-channel, and JointQ also improves average accuracy over GPTQ with MSE-based scale search and activation ordering in all eight per-channel comparisons, though rarely in G128. An ablation shows that JointQ's diagonal Tikhonov regularization mitigates severe W3 per-channel perplexity degradation, so the largest gains are not due to the local search alone. Overall, JointQ's primary empirical benefit is downstream accuracy preservation in challenging low-bit and large-group regimes. Code is available in the OneComp library at https://github.com/FujitsuResearch/OneCompression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Keiji Kimura, Yuma Ichikawa
- 发布：2026-11-16；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/FujitsuResearch/OneCompression](https://github.com/FujitsuResearch/OneCompression)
- 阅读深度：metadata
