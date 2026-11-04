---
title: "CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents"
description: "The rapid growth of automated code generation has created a pressing need for automated code review."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.02566) · [PDF](https://arxiv.org/pdf/2611.02566)

## 一句话摘要

The rapid growth of automated code generation has created a pressing need for automated code review.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even expert reviewers disagree. Existing code review benchmarks lack standardization and rely largely on noisy human review comments scored with text-similarity metrics, which reward surface overlap and fail to measure precision. We introduce \texttt{CR-Bench}, a defect-centric evaluation framework that recasts SWE-Bench issues as pull-request review tasks with full repository context. After filtering for review-detectable defects and grounding each to a single originating pull request, \texttt{CR-Bench} contains 584 instances, with a 174-instance \texttt{CR-Bench-Verified} subset derived from SWE-Bench Verified. Each instance pairs a pull request with a known defect, its ground-truth fix, and a taxonomy label for bug category, impact, and severity. We propose two complementary metrics: \emph{Known-Defect Detection Rate} (KDDR), which measures whether an agent identifies the labeled defect, and \emph{Usefulness Rate}, which measures the fraction of review comments that are actionable. We evaluate eight code review agents over four backbones, plus commercially available Gemini Code Assist, using three independent LLM judges. Even the strongest systems detect only about one-third of known defects (KDDR $\approx$ 33\%), and Gemini Code Assist detects 8.1\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kristen Pereira, Neelabh Sinha, Rajat Ghosh, Debojyoti Dutta
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
