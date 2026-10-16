---
title: "Rethinking Calibration for High-Sparsity LLM Pruning: From Single Sources to Capability Coverage"
description: "Post-training LLM pruning relies on a small calibration set, usually chosen heuristically and judged by WikiText perplexity or by mean accuracy on general-domain commonsense benchmarks."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.03328) · [PDF](https://arxiv.org/pdf/2606.03328)

## 一句话摘要

Post-training LLM pruning relies on a small calibration set, usually chosen heuristically and judged by WikiText perplexity or by mean accuracy on general-domain commonsense benchmarks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training LLM pruning relies on a small calibration set, usually chosen heuristically and judged by WikiText perplexity or by mean accuracy on general-domain commonsense benchmarks. This single-axis view hides capability-specific effects: at 60\% sparsity, strategies separated by $2.85$ points in averaged commonsense accuracy diverge by $51.9$ points in code retention, and across 15 sources no single one preserves all capabilities. We treat calibration as a capability-coverage problem. Balanced, a uniform four-way mixture under a fixed budget, tests the principle on real corpora: it outperforms every evaluated single source, and its margin over C4 grows from $+4.6$ points at 30\% sparsity to $+18.8$ at 60\%. The advantage holds across model scale and a second model family, and transfers to held-out benchmarks disjoint from calibration construction. When aligned corpora are unavailable, IGSP approximates that mixture from the base model and the evaluation taxonomy alone, outperforming prior self-generation methods by $7.23$--$12.79$ points on the LLaMA main suite. On Qwen2.5-7B, IGSP exceeds Balanced on both the main suite and held-out benchmarks. Capability coverage is a first-order design variable for high-sparsity pruning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hu Xu, Zhaolong Xing, Congcong Liu, Jiaxing Wang, Zhida Jiang, Junshi Huang, Zhen Chen, Jianfeng Xu
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
