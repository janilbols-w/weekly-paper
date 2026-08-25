---
title: "LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks"
description: "Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.23200) · [PDF](https://arxiv.org/pdf/2608.23200)

## 一句话摘要

Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification. Yet successful execution experience is typically lost after a single run, forcing subsequent models to rediscover strategies and failure modes from scratch. We study whether such experience can instead be externalized and reused through EvoMap, where verifier-confirmed execution trajectories are consolidated into structured Gene. To evaluate this setting, we introduce the Long-Workflow Benchmark (LongWoF-Bench), comprising 778 machine-verifiable tasks across code generation, agent-environment synthesis, mathematical reasoning, and rule following. On the 252 tasks with verifier-confirmed Opus trajectories, evolved EvoMap Gene outperform Skill across all seven evaluated models by 8.7-15.5 percentage points, with the gains extending to consumer models from different model families. In contrast, reference-distilled Gene do not exhibit the same advantage, indicating that compact representation alone is insufficient and that Gene utility is closely associated with verified experience provenance. For Claude Opus, Gene reuse also completes 39 more tasks than Skill while reducing solve-time token consumption by 9.9%. Together, these results show that verified execution experience can be retained and shared as a reusable external resource, enabling models to improve long-workflow completion without repeatedly paying the full cost of experience discovery.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiao Zhang, Qumeng Sun, Jihao Li, Yiming Ren, Xiang Liu, Haoyang Zhang, Junjie Wang
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
