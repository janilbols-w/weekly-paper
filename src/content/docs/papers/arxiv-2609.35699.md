---
title: "Distillation Defenses Easily Break After Reinforcement Learning"
description: "Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35699) · [PDF](https://arxiv.org/pdf/2609.35699)

## 一句话摘要

Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distillation attacks copy the reasoning capabilities of closed-source large language models, allowing bad actors to replicate state-of-the-art performance at low cost. Attackers systematically collect a large volume of frontier model reasoning traces and then train (i.e., "distill") their own models on these traces. Existing defenses against distillation attacks are typically evaluated immediately after distillation, implicitly assuming attackers do not train their models any further. In this paper, we argue that a more realistic threat model includes further training with reinforcement learning after distillation. A misspecified threat model can give a false sense of security -- some defenses that seem effective after distillation can be broken after subsequent reinforcement learning. Practically, reinforcement learning lowers the bar for a distillation attack to be effective. We show that simple attacks can steal reasoning capabilities from existing closed-source language models using data easily obtainable from current APIs, yielding reasoning improvements equivalent to more sophisticated attacks that extract the full hidden traces. Results indicate that any distillation defense that leaks sufficient information to reconstruct approximate reasoning traces is likely ineffective. We conclude by discussing broader implications and batch-level distillation defenses which could be more effective.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shidan Javaheri, Alexander Panfilov, Oliver Britton, Yarin Gal, Yonatan Gideoni
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
