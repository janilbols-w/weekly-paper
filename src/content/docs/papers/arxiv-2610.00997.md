---
title: "Distilling Directional Verification"
description: "Knowledge distillation aims to transfer the factual knowledge of large language models to smaller models for efficient deployment."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.00997) · [PDF](https://arxiv.org/pdf/2610.00997)

## 一句话摘要

Knowledge distillation aims to transfer the factual knowledge of large language models to smaller models for efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation aims to transfer the factual knowledge of large language models to smaller models for efficient deployment. Yet a teacher may recall a relation in one direction while failing to generate the answer in the reverse direction. Distillation from its generated answers can therefore propagate this directional limitation to the student. The same teacher can nevertheless recognize such an answer by scoring the relation in the direction it knows. We introduce directional label distillation, in which frozen teachers score candidate answers in that known direction and the best-scoring candidate becomes the student's training target. On facts about parents and their children, known-direction scoring yields more accurate labels than scoring the requested direction, even after tuned corrections for name priors. With prior-corrected scores, the better direction depends on the facts rather than the template, and reverses on mined facts whose notable entity is the parent rather than the child. With the evaluated children's forward facts withheld, students trained on known-direction labels improve open-ended accuracy on their trained queries by 13 to 15 points over students trained on prior-corrected reverse labels. After generated answers are matched to a fixed name list by lexical similarity, students reproduce nearly all selected labels. Their accuracy largely follows label quality. The label advantage holds on unscreened queries and when candidates are retrieved without inserting correct answers. Our findings show that directional verification mitigates the transfer of errors from teacher-generated answers to students by providing more accurate training targets. Code is available at https://github.com/js-lee-AI/directional-verification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jungseob Lee, Sugyeong Eo, Seongtae Hong, Seungyoon Lee, Chanjun Park, Jaehyung Seo, Heuiseok Lim
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/js-lee-AI/directional-verification](https://github.com/js-lee-AI/directional-verification)
- 阅读深度：metadata
