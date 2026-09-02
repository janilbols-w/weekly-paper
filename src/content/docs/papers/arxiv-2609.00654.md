---
title: "SciTrue: Reliable Scientific Claim Validation with Frontier and Open Language Models at the NTCIR SciClaimEval Task"
description: "We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\\cite{sciclaimeval}, which asks systems to verify scientific claims against the tables and figures of a paper."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.00654) · [PDF](https://arxiv.org/pdf/2609.00654)

## 一句话摘要

We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\cite{sciclaimeval}, which asks systems to verify scientific claims against the tables and figures of a paper.

## 为什么值得关注

待编辑增强。

## 摘要原文

We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\cite{sciclaimeval}, which asks systems to verify scientific claims against the tables and figures of a paper. Rather than tuning a single model, we benchmark eleven frontier and open multimodal models under one honest, per-sample protocol and combine them with light, transparent post-processing. On the official, blind test leaderboard (Section~\ref{sec:results}), SciTrue placed first by a clear margin in three of the four evidence-category/subtask combinations, and tied for first on the primary metric in the fourth. Three findings explain the result. First, strong instruction-tuned models are already competitive: Claude Opus~4.8 and Gemma-4-31B each exceed the strongest public baseline (o4-mini), and GPT-5.5 and Claude Fable~5 lead both subtasks (97.7 on Subtask~2). Second, the task's pairing structure is the largest lever: a \emph{leak-free pair prior} that recovers the Supported/Refuted pairing from the claim text alone (a visible field) and assigns Supported to the higher-confidence evidence raises Subtask-1 pair-accuracy from 72.2 to 93.5, far more than any model swap or ensemble weighting. Third, a case-by-case audit finds that most residual errors are visually-undetectable label-mapping swaps or dataset label noise, so measured accuracy understates the true ability and the fixable-by-modeling headroom is small. Controlled fine-tuning, distillation, and agentic consistency-checking support the same conclusions, and we document throughout a measurement leak---label information reaching a system through the packaging of the data rather than its content---in which the released file ordering encodes the label, including one instance that briefly misled our own pipeline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiming Bao, Ne\c{s}et \"Ozkan Tan, Siyuan Wang, Mark Gahegan
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
