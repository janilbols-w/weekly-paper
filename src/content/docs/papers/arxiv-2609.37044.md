---
title: "Learning from Think-Mode Advantage via On-Policy Distillation"
description: "Explicit intermediate reasoning gives large language models (LLMs) a stronger problem-solving mode."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.37044) · [PDF](https://arxiv.org/pdf/2609.37044)

## 一句话摘要

Explicit intermediate reasoning gives large language models (LLMs) a stronger problem-solving mode.

## 为什么值得关注

待编辑增强。

## 摘要原文

Explicit intermediate reasoning gives large language models (LLMs) a stronger problem-solving mode. We study learning from this think-mode advantage via on-policy distillation (OPD). OPD preserves student-generated trajectories and provides dense token-level teacher targets at student-visited prefixes. Privileged reasoning is used during distillation rather than student inference. Uniform ThinkOPD, a natural think-enabled OPD baseline, conditions a fixed teacher on one shared think trace and uniformly distills every sibling student response. Although its prefixes are on-policy, the trace need not follow a route compatible with every complete response: the same privileged trace can induce different teacher-student discrepancies even when responses reach the same outcome. We summarize this interaction with trace-response divergence (TRD) and introduce ThinkOPD, which routes supervision at the response level by combining group-relative reward gain with a TRD-based compatibility proxy. Final response weights are normalized within each rollout group. Across mathematical reasoning and code generation, ThinkOPD outperforms Uniform ThinkOPD in both same-model settings and both cross-model teacher-student pairs, and it exceeds representative rationale and self-distillation baselines in a controlled comparison. Controlled interventions show that outcome benefit and the TRD-based proxy provide complementary routing signals in this setting. Think-enabled OPD provides a controlled setting for studying how teacher advantage becomes transferable along student responses.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wanqi Ren, Jianxiang Wang, Danxuan Liu, Linyi Ding, Huaixiao Tou
- 发布：2026-09-29；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
