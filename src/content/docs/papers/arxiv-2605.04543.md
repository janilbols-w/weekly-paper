---
title: "UniVer: A Unified Perspective for Multi-step and Multi-draft Speculative Decoding"
description: "Speculative decoding accelerates Large Language Models via draft-then-verify, where verification can be framed as an Optimal Transport (OT) problem."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2605.04543) · [PDF](https://arxiv.org/pdf/2605.04543)

## 一句话摘要

Speculative decoding accelerates Large Language Models via draft-then-verify, where verification can be framed as an Optimal Transport (OT) problem.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates Large Language Models via draft-then-verify, where verification can be framed as an Optimal Transport (OT) problem. Existing approaches typically handle multi-draft and multi-step aspects in isolation, applying either flat OT to single-step drafts or per-token rejection sampling to tree-structured candidates. This separation leaves the joint regime (where multi-step dependencies meet multi-draft branching) poorly optimized, as local verification rules fail to exploit the coupling between horizontal and vertical dimensions of candidate trees. In this paper, we propose a unified perspective that casts tree-based verification as a conditional OT problem. Our key insight is that vertical dependencies can be abstracted through prefix acceptance probabilities, which act as dynamic scaling factors to actively guide horizontal draft selection. Based on this principle, we introduce UniVer, a verification algorithm that jointly optimizes across tree levels by composing local optimal transport plans under prefix constraints. We prove that UniVer remains lossless and achieves the optimal acceptance rate under the proposed conditional framework. Extensive experiments across different tasks and models demonstrate that UniVer improves acceptance length by 4.2% to 8.5% over standard recursive rejection sampling without replacement, while maintaining exact distributional alignment with the target model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yepeng Weng, Qiao Hu, Takehisa Yairi
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
