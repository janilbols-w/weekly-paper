---
title: "PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling"
description: "Power sampling improves large language model (LLM) reasoning at test time by sampling from a sharpened version of the base model's distribution."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13171) · [PDF](https://arxiv.org/pdf/2610.13171)

## 一句话摘要

Power sampling improves large language model (LLM) reasoning at test time by sampling from a sharpened version of the base model's distribution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Power sampling improves large language model (LLM) reasoning at test time by sampling from a sharpened version of the base model's distribution. Its sampler, PowerMH, is slow because its Metropolis--Hastings (MH) updates are sequential: each accept/reject decision sets the state from which the next proposal is generated. Prior work reduces this cost by changing the sampler or the model (e.g., sequential Monte Carlo, approximate lookahead, distillation). We propose Predictive SubTree Prefetching (PreSTO), which accelerates PowerMH by prefetching future proposals and provably leaves its MH transition kernel unchanged. PreSTO views future MH outcomes as a tree of accept/reject decisions: in each model call, it generates the proposals of a \textit{prefetched subtree} of this tree in one batch, then follows the realized path with the original MH acceptance rule. We also observe that MH reaches only a sparse, nearly unary part of each prefetched subtree, we further design a \textit{predictive traversal rule} that chooses the subtree to maximize the predicted number of completed transitions. Across seven datasets and five base LLMs, PreSTO achieves median speedups of $1.71\times$, $1.91\times$, and $2.33\times$ on PowerMH and its follow-ups EntropyCut and MultiTryMH, respectively; on the first two, it makes a median of $3.9\times$ fewer model calls, each only $2.1\times$ longer. On LCB V6 with Qwen3.5-9B, the predictive traversal rule is a further $1.25\times$--$1.37\times$ faster than the default breadth-first traversal.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nan Jiang, Panagiotis Theodoropoulos, Wei Deng
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
