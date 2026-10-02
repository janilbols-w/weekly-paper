---
title: "CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning"
description: "Recent years have witnessed the rapid adoption of reinforcement learning (RL) in large language model (LLM) post-training, with substantial gains in mathematical reasoning and code generation."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.02039) · [PDF](https://arxiv.org/pdf/2610.02039)

## 一句话摘要

Recent years have witnessed the rapid adoption of reinforcement learning (RL) in large language model (LLM) post-training, with substantial gains in mathematical reasoning and code generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent years have witnessed the rapid adoption of reinforcement learning (RL) in large language model (LLM) post-training, with substantial gains in mathematical reasoning and code generation. In practical systems, however, policy updates and differences between rollout and training engines can make sampled responses off-policy. Sequence-level masking addresses this mismatch by deciding whether an entire response should contribute to optimization. A common masking rule uses the length-normalized geometric mean of sampled token probability ratios. Its signed log-ratios can cancel across positions, concealing substantial bidirectional policy drift. We propose \emph{Cancellation-Aware Response Masking} (CARM), a sequence-level mask that takes the absolute value of each token log-ratio before averaging, preventing opposing probability changes from canceling. We prove that accepted responses satisfy a joint bound on the fraction of sampled-token ratios outside a prescribed band and their mean log-distance beyond its boundaries. Experiments on mathematical reasoning and code generation show that CARM improves mean@16 averaged over AIME 2024/2025/2026 and BeyondAIME by up to $3.13$ percentage points over geometric-mean masking, and increases average pass@1 across four code benchmarks by $2.88$ points over the strongest evaluated baseline. These findings support CARM as a theoretically grounded and effective method for response-level off-policy control in LLM reinforcement learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yafei Zhang, Songshuo Lu, Sicong Liao, Zhi Chen, Yaohua Tang
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
