---
title: "MedAction: Towards Active Multi-turn Clinical Diagnostic LLMs"
description: "Most existing LLM diagnoses are evaluated on static, single-turn settings where complete patient information is provided upfront, an oversimplification of real clinical practice."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.07305) · [PDF](https://arxiv.org/pdf/2605.07305)

## 一句话摘要

Most existing LLM diagnoses are evaluated on static, single-turn settings where complete patient information is provided upfront, an oversimplification of real clinical practice.

## 为什么值得关注

待编辑增强。

## 摘要原文

Most existing LLM diagnoses are evaluated on static, single-turn settings where complete patient information is provided upfront, an oversimplification of real clinical practice. We study active diagnosis: the real-life clinical process of starting from initial observation, ordering tests, interpreting results, and updating a differential diagnosis across multiple turns. Through systematic analysis, we identify three recurring failure modes in current LLMs: ungrounded test ordering, unreliable diagnostic update, and degraded multi-turn coherence. Together, these failures reveal a core deficit: existing medical training data teaches models to reason from complete information but not to act under evolving, partial evidence. To address this gap, we introduce MedAction, a tree-structured distillation pipeline that synthesizes diverse and high-quality multi-turn diagnostic trajectories via LLM-environment interaction. We propose two knowledge-graph-grounded metrics to filter trajectory quality: Disease Trajectory Consistency (DTC), which tracks whether the model's hypothesis converges toward the correct diagnosis, and Reasoning-Action Consistency (RAC), which verifies that belief updates are driven by gathered evidence. Using this pipeline, we construct MedAction-32K, a dataset of 32,681 trajectories from 2,896 PMC cases. Fine-tuning an 8B model on MedAction-32K achieves state-of-the-art performance among open-source models on both MedR-Bench and our curated MedAction-300-Hard benchmark, pushing the edge for open-source medical LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hsin-Ling Hsu, Zizheng Wang, Donghua Zhang, Nai-Chia Chen, Jerry Wang, Jun-En Ding, Chia-Hsuan Hsu, Guoan Wang, Feng Liu, Fang-Ming Hung, Chenwei Wu, Liyue Shen
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
