---
title: "Simplify, Agree, Distill: Label-Free Self-Distillation with Stepping Stones"
description: "Can a language model teach itself to reason without labels?"
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.18916) · [PDF](https://arxiv.org/pdf/2611.18916)

## 一句话摘要

Can a language model teach itself to reason without labels?

## 为什么值得关注

待编辑增强。

## 摘要原文

Can a language model teach itself to reason without labels? On-policy self-distillation (OPSD) uses the model as its own teacher, but strengthens that teacher with a ground-truth solution. The natural label-free substitute, voting over the model's attempts, fails precisely on hard problems: attempts disagree, and their most common answer is often wrong. We propose STONE, a label-free alternative that moves agreement to easier related problems. The model writes these stepping stones, keeps those it solves consistently, and shows the teacher their worked solutions, with final answers removed; the student sees only the original problem. No step reads a label, and inference needs no extra context or model calls. Across five math benchmarks, the proposed method achieves the highest average accuracy for Qwen3-4B and Qwen3-8B in thinking mode. Without thinking mode, it gains 13.2 and 22.7 points, 2.5 and 2.7 times the gains of OPSD with ground-truth solutions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dingyang Chen, Jinfeng Xiao, Zhenyu Zhang, William Hu, Ziyu Wang, Yang Liu, Shirley Zhang, Yuan Ling, Xinyang Shen, Qi Zhang, Peijie Qiu
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
