---
title: "Beyond Token Alignment: Event Completion for Cross-Tokenizer On-Policy Distillation"
description: "On-policy distillation (OPD) transfers knowledge between language models through teacher supervision on student-generated trajectories."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.34738) · [PDF](https://arxiv.org/pdf/2609.34738)

## 一句话摘要

On-policy distillation (OPD) transfers knowledge between language models through teacher supervision on student-generated trajectories.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) transfers knowledge between language models through teacher supervision on student-generated trajectories. With different tokenizers, a single teacher token may require multiple student tokens to generate, creating intermediate states where the event is entered but not yet completed. Existing cross-tokenizer methods align tokens or text spans to construct comparable prediction targets. We study a complementary problem after partial generation: once the student produces a prefix of a teacher token, multiple next tokens may complete the same remaining bytes, but the teacher only specifies the required completion rather than how probability should be divided among these valid continuations. We introduce Event-Set Completion Distillation (ESCD), which complements cross-tokenizer probability alignment with completion-set supervision. ESCD aggregates prefix-related teacher events and supervises the total probability of byte-compatible one-step student completions, avoiding tokenizer-dependent probability splits among individual tokens. The method reuses student trajectories and predictions, requiring neither additional rollouts nor changes to the student vocabulary. Experiments demonstrate consistent gains in mathematics, code, and scientific reasoning across model families and tokenizers, extending to large-scale MoE distillation from a 1T teacher to a 35B student. Local analyses show that retaining completion sets better matches the reference supervision, while one-step completion covers over 99% of observed compatible teacher mass after partial event entry in the studied tokenizer pairs. These findings support event entry and event completion as complementary supervision targets for cross-tokenizer knowledge transfer. Code will be released on GitHub.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiacheng Liu, Jingwei Song, Qituan Zhang, Siheng Chen, Linfeng Zhang
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
