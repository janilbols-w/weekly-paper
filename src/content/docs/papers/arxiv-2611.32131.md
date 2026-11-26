---
title: "Rethinking Reasoning Effort Training in Large Language Models: On-Policy Distillation or Reinforcement Learning?"
description: "Large language models have shown strong capabilities on complex tasks, yet how to control their reasoning effort remains a significant challenge for practical deployment."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.32131) · [PDF](https://arxiv.org/pdf/2611.32131)

## 一句话摘要

Large language models have shown strong capabilities on complex tasks, yet how to control their reasoning effort remains a significant challenge for practical deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models have shown strong capabilities on complex tasks, yet how to control their reasoning effort remains a significant challenge for practical deployment. This paper provides a systematic investigation of reasoning-effort training, contrasting reinforcement learning (RL) with on-policy distillation (OPD). We find that compressing reasoning and separating effort tiers are governed by different signals. Length-penalized RL reliably compresses a single policy, reducing thinking on AIME25 by 70\% without accuracy loss, but collapses the tiers when they are trained jointly. Multi-teacher OPD separates them: across 33 benchmarks, low and medium use 58\% and 43\% fewer thinking tokens than high, while high improves on the reference policy by 3.1 points. We trace this difference to the training signal. A sequence-level reward cannot tell tier-specific behavior from shared behavior, whereas OPD supplies a tier-specific target at every visited state, including the decision to stop. Building on this analysis, we show that a single token-level KL anchor on the high tier is sufficient to learn separated tiers within one RL stage, and that natural-language effort instructions make this separation emerge from the start of training, yielding a policy competitive with multi-teacher OPD at matched thinking length. Finally, the separation built by dense targets holds only on the states seen in training: it does not carry over to unseen agentic tasks, where effort acts mainly through the number of interaction turns, whereas the compression induced by sequence-level rewards does.

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

- 作者：Tianliang Lv, Hao Li, Xinchao Xu, Zhengkun Zhang, Ju Huo
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
