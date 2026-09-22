---
title: "LLMs Anchor on Chief Complaint and Fail to Integrate Evidence in Sequential Clinical Triage"
description: "Triage in the emergency department (ED) is a sequential decision process that unfolds turn by turn."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.22904) · [PDF](https://arxiv.org/pdf/2609.22904)

## 一句话摘要

Triage in the emergency department (ED) is a sequential decision process that unfolds turn by turn.

## 为什么值得关注

待编辑增强。

## 摘要原文

Triage in the emergency department (ED) is a sequential decision process that unfolds turn by turn. Existing evaluations of large language models (LLMs) for triage use completed retrospective records and report performance close to that of physicians. We implement a methodology for evaluating LLMs on sequential triage, the task of predicting a triage acuity label from a growing prefix of a nurse-patient conversation. We evaluate six LLMs at five sequential checkpoints on two corpora: 425 LLM-generated (SIMULATED) and 50 physician-authored (CLINICIAN) conversations, both labelled under the Emergency Severity Index (ESI). Every model, measured by quadratic weighted kappa (QWK), degrades from moderate-to-substantial agreement on completed records to fair-to-moderate agreement at every sequential checkpoint. Controlled perturbations show that the label at every checkpoint is anchored on the chief complaint exchanges, and prompting interventions fail to lift this plateau. Models extract clinically relevant content from later turns, yet the surprisal of the true label rises across the checkpoints. So the model fails to integrate the evidence. Three expert clinicians on the same conversations reach a QWK of 0.887-0.929, while the best model reaches 0.295. Predictions concentrate at ESI-2 and ESI-3, and models agree with each other more than with the ground truth, so ensembling worsens the failure. Deploying LLMs for ED triage based on offline benchmarks alone misses this sequential failure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dipankar Srirag, Haokai Zhao, Ashutosh Kumar, Eleanor Hopper, Michael Dalton, Quoc Dung Nguyen, Aditya Joshi, Salil S. Kanhere, Padmanesan Narasimhan
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
