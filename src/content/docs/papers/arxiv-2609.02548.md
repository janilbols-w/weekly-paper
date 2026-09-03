---
title: "Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs"
description: "Modern large language models (LLMs) rely on reinforcement learning to build strong capabilities in individual domains, but integrating those capabilities into a single deployable model remains challenging."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.02548) · [PDF](https://arxiv.org/pdf/2609.02548)

## 一句话摘要

Modern large language models (LLMs) rely on reinforcement learning to build strong capabilities in individual domains, but integrating those capabilities into a single deployable model remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language models (LLMs) rely on reinforcement learning to build strong capabilities in individual domains, but integrating those capabilities into a single deployable model remains challenging. By routing each sample to the teacher whose domain matches it, existing approaches let a domain label decide which teacher provides supervision. However, domain expertise holds only on average: the matched teacher is not always correct on a given sample, while a teacher from another domain sometimes is. The reliable teacher therefore has to be identified per sample, not per domain. In this paper, we introduce Multi-Teacher Self-Distillation Policy Optimization (MT-SDPO), an on-policy distillation method that unifies several frozen teachers into one student model. MT-SDPO consists of three components: (1) self-anchors, where a rollout is supervised by a correct rollout from its own group; (2) answer-verified eligibility, where a teacher may supervise a sample only if its own answer passes a verifier; and (3) privileged distillation, which merges the anchor and all verified feedback into one context that an exponential moving average self-teacher reads and the student does not, thereby keeping one policy at deployment. Across five students from three model families, MT-SDPO lifts the weakest domain of Qwen3-8B by 14.79 points and narrows its domain gap by 74.7%, a better balance than serving one matched teacher per domain. Verified reliability, not domain membership, should decide who teaches. Code is available at https://github.com/hexixiang/MT-SDPO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xixiang He, Xingming Li, Baiqi Wu, Qiyao Sun, Xuanyu Ji, Ao Cheng, Qingyong Hu
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/hexixiang/MT-SDPO](https://github.com/hexixiang/MT-SDPO)
- 阅读深度：metadata
