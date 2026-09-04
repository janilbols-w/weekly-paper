---
title: "EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation"
description: "Post-trained LLMs are often optimized to produce helpful, polite, and accommodating responses."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.26785) · [PDF](https://arxiv.org/pdf/2605.26785)

## 一句话摘要

Post-trained LLMs are often optimized to produce helpful, polite, and accommodating responses.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-trained LLMs are often optimized to produce helpful, polite, and accommodating responses. In adversarial negotiation, however, such behavior can become a vulnerability: emotionally framed language may influence an agent's bargaining decisions in ways that conflict with its user's objectives. We therefore introduce EmoDistill, an offline framework for distilling emotional negotiation skills from LLM-LLM interactions into smaller language-model agents. Here, an emotional negotiation skill is a state-conditioned behavior that determines which explicit emotion to invoke in a bargaining state and how to realize that emotion as an effective negotiation utterance. EmoDistill learns these two components separately: an Implicit Q-Learning (IQL) selector learns which emotion to express in each bargaining state, while a LoRA-adapted 7B policy learns emotion-conditioned expression through Supervised Fine-Tuning (SFT) and Judge Policy Optimization (JPO). Across four emotion-sensitive negotiation domains, the full EmoDistill policy achieves competitive utility and improves over vanilla and IQL-only baselines in most settings. Emotion-free ablations show that removing the explicit emotion channel substantially reduces overall negotiation utility, while transfer experiments reveal partial, domain-dependent transfer and robustness to unseen LLM counterparties.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yunbo Long, Haolang Zhao, Lukas Beckenbauer, Liming Xu, Alexandra Brintrup
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
