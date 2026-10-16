---
title: "Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving MLP Trimming"
description: "Structured pruning reduces LLM inference costs by removing model components to produce smaller dense models."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.19121) · [PDF](https://arxiv.org/pdf/2610.19121)

## 一句话摘要

Structured pruning reduces LLM inference costs by removing model components to produce smaller dense models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning reduces LLM inference costs by removing model components to produce smaller dense models. However, existing methods can cause reasoning performance to collapse on long-form reasoning tasks such as AIME. We propose \textit{LayerTrim}, a training-free structured pruning method that identifies redundant decoder layers and selectively trims their MLP features while preserving attention and decoder depth. LayerTrim is the first training-free structured pruning method designed to preserve long-form reasoning without gradients or recovery training. Across three reasoning language models and five benchmarks, LayerTrim outperforms existing structured pruning methods in most evaluated settings, improving average accuracy by up to 21.4 percentage points over RESP. On \texttt{Qwen3-14B}, LayerTrim achieves 1.24$\times$ faster prefill and 19.7\% lower peak GPU memory than the dense model, while better preserving reasoning ability. It also achieves the shortest average generation length among evaluated pruned models, while retaining the highest average accuracy. These results demonstrate that LayerTrim improves reasoning efficiency through both structural compression and reduced token generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Woosang Lim, Haneul Yoo, Vincent-Daniel Yun, Sungjoo Yoo
- 发布：2026-10-13；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
