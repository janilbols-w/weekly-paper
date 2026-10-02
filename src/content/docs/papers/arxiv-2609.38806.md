---
title: "Blackboard Intelligence Can Surpass Autoregressive on Globally Constrained Problems"
description: "Next-token prediction has driven remarkable progress in large language models, yet a growing body of evidence suggests that they can struggle on problems governed by complex global constraints."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.38806) · [PDF](https://arxiv.org/pdf/2609.38806)

## 一句话摘要

Next-token prediction has driven remarkable progress in large language models, yet a growing body of evidence suggests that they can struggle on problems governed by complex global constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Next-token prediction has driven remarkable progress in large language models, yet a growing body of evidence suggests that they can struggle on problems governed by complex global constraints. In this work, we focus on this regime and ask whether some of these limitations arise from the inference interface induced by next-token prediction itself. We study this question through blackboard intelligence: an inference-time perspective in which a model works on a fixed, revisable canvas and searches over candidate solution states rather than committing to a causal, left-to-right trajectory. We instantiate this idea with diffusion language models, whose any-order prediction interface naturally exposes predictions over partially filled solution states. Our key observation is that mean confidence, a simple model-internal quantity available from the standard masked diffusion objective, provides a useful proxy for global coherence and can guide inference-time search and revision. Empirically, across ZebraLogic, Nurse Rostering, and Job-Shop Scheduling, Blackboard consistently improves inference while holding the fine-tuned LLaDA-8B-Instruct checkpoint fixed and substantially outperforms same-scale autoregressive baselines, reaching 90.4% accuracy on ZebraLogic-Hard, 76.4% exact feasibility on Nurse Rostering, and 80.2% optimality on JSSP. Stronger autoregressive search and refinement also fail to close the gap on ZebraLogic-Hard, while Blackboard surpasses tested frontier LLMs there and on JSSP despite their substantially greater scale and strong test-time reasoning. We open-source our codebase at https://github.com/jwoosang1/blackboard-intelligence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Woosang Jeon, Jaeyeon Kim, Sham Kakade, Yilun Du, Amrit Singh Bedi, Arun Kumar Chithanar, Chul Lee, Taehyeong Kim, Sitan Chen
- 发布：2026-09-30；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jwoosang1/blackboard-intelligence](https://github.com/jwoosang1/blackboard-intelligence)
- 阅读深度：metadata
