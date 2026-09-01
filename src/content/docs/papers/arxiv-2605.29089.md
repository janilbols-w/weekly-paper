---
title: "OISD: On-Policy Internal Self-Distillation of Language Models"
description: "Recent reinforcement learning (RL) post-training approaches primarily optimize the final output policy using sparse outcome-level rewards, while largely overlooking predictive signals encoded in intermediate representations."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.29089) · [PDF](https://arxiv.org/pdf/2605.29089)

## 一句话摘要

Recent reinforcement learning (RL) post-training approaches primarily optimize the final output policy using sparse outcome-level rewards, while largely overlooking predictive signals encoded in intermediate representations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent reinforcement learning (RL) post-training approaches primarily optimize the final output policy using sparse outcome-level rewards, while largely overlooking predictive signals encoded in intermediate representations. In this paper, we introduce a new paradigm called on-policy internal self-distillation and propose the OISD framework, which improves reasoning by transferring on-policy predictive signals from the final layer to intermediate representations. During rollout and Group Relative Policy Optimization (GRPO) optimization, the final layer acts as both the policy and a detached internal teacher for selected intermediate layers, which are guided to align with it through two complementary mechanisms: logit alignment, which transfers high-level reasoning behaviors (how to think), and attention alignment, which enforces consistent attention patterns (where to look) from the final layer to the selected intermediate layer, both without requiring external privileged information. Our OISD, together with GRPO, employs signed advantage-weighted Jensen--Shannon alignment to distill informative intermediate representations while preserving policy consistency under a unified acting policy. Experimental results demonstrate the effectiveness of OISD, with substantial and consistent improvements over strong reasoning RL baselines across four mathematical reasoning tasks. The code will be released at https://github.com/THE-MALT-LAB/OISD

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xinyu Liu, Darryl Cherian Jacob, Yang Zhou, Jindong Wang, Pan He
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/THE-MALT-LAB/OISD](https://github.com/THE-MALT-LAB/OISD)
- 阅读深度：metadata
