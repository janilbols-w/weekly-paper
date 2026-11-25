---
title: "Seeing Is Not Acting: WARD Diagnoses the Evidence-to-State-to-Action Gap in Longitudinal Clinical Agents"
description: "Large language models for longitudinal clinical care must revise their assessments and actions as patient information accumulates."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.29243) · [PDF](https://arxiv.org/pdf/2611.29243)

## 一句话摘要

Large language models for longitudinal clinical care must revise their assessments and actions as patient information accumulates.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models for longitudinal clinical care must revise their assessments and actions as patient information accumulates. However, benchmarks centered on isolated responses or final task outcomes provide limited insight into intermediate failures in evidence use, state updating, and action selection. We introduce WARD, a benchmark for evaluating how clinical agents translate accumulating evidence into patient-state judgments and timely, safe actions. WARD comprises 4,560 clinical tasks across seven clinical output domains, organized into 240 checkpoints from 40 longitudinal clinical trajectories spanning 95 hospitalizations. Its Longitudinal Track evaluates these tasks under controlled cumulative evidence. Its Interactive Track evaluates end-to-end, tool-mediated clinical management across 271 verifiable evidence items and 141 reference transitions. Across 12 models with scorable checkpoint outputs, evidence recognition consistently outpaces downstream state and action decisions, with linked-evidence nonresponse reaching 74.47--90.90\%. Models also struggle to retain and update information over time, while in the Interactive Track only 11.46\% of executed actions advance a reference transition. These results reveal a persistent evidence-to-state-to-action gap and highlight the need for process-level evaluation of longitudinal clinical agents.Code and data: https://github.com/Dingsuper-creator/WARD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chao Ding, Yidong Jiang, Junzhi Ning, Juncheng Wu, Yuhan Wang, Renjie Lu, Minjia Yuan, Gaopeng Wang, Liyang Wang, Pengcheng Chen, Dong Yin, Meiping Wang, Jinru Ding, Yuyin Zhou
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Dingsuper-creator/WARD](https://github.com/Dingsuper-creator/WARD)
- 阅读深度：metadata
