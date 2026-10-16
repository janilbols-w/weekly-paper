---
title: "BASIS: Evaluating Belief-Aware Solutions in Interactive Settings beyond Instructions"
description: "Large language model (LLM) agents are increasingly capable of carrying out complex, long-horizon tasks, yet effective assistance requires more than faithfully executing user instructions."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2602.13832) · [PDF](https://arxiv.org/pdf/2602.13832)

## 一句话摘要

Large language model (LLM) agents are increasingly capable of carrying out complex, long-horizon tasks, yet effective assistance requires more than faithfully executing user instructions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents are increasingly capable of carrying out complex, long-horizon tasks, yet effective assistance requires more than faithfully executing user instructions. Users' requests reflect their current understanding of the problem, which may be incomplete, outdated, or incorrect. When this understanding diverges from the actual task state, literal instruction following can fail to accomplish the user's underlying goal. We introduce \textbf{BASIS} (\emph{\textbf{B}elief-\textbf{A}ware \textbf{S}olutions in \textbf{I}nteractive \textbf{S}ettings}), a benchmark that evaluates whether agents can infer the mental states underlying user requests, recognize belief-reality mismatches, and use this understanding to develop appropriate solutions. Rather than assessing mental-state inference solely through explicit questions, \textbf{BASIS} evaluates both the utility of such inferences and the quality of downstream solutions in user-agent interactions. Evaluation results show that current models often fail to account for users' mental states when generating solutions, and that solution quality is consistently higher when such information is explicitly elicited and made available during problem solving. We further investigate the practical value of mental-state consideration through comparisons with generic Chain-of-Thought prompting, controlled interventions on mental-state information, targeted training, and multi-agent collaboration experiments under partial observability. Together, these studies highlight the importance of not merely inferring others' mental states, but also using those understandings to provide grounded, goal-directed assistance.

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

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minyuan Ruan, Ziyue Wang, Kaiming Liu, Yunghwei Lai, Peng Li, Yang Liu
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
