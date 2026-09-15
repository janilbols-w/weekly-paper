---
title: "HumorGen: Cognitive Synergy for Humor Generation in Large Language Models via Persona-Based Distillation"
description: "Humor generation poses a significant challenge for Large Language Models (LLMs), because their standard training objective (next-token prediction) inherently conflicts with the surprise and incongruity required for comedy."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.09629) · [PDF](https://arxiv.org/pdf/2604.09629)

## 一句话摘要

Humor generation poses a significant challenge for Large Language Models (LLMs), because their standard training objective (next-token prediction) inherently conflicts with the surprise and incongruity required for comedy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Humor generation poses a significant challenge for Large Language Models (LLMs), because their standard training objective (next-token prediction) inherently conflicts with the surprise and incongruity required for comedy. To bridge this gap, we introduce the Cognitive Synergy Framework, a methodology for generating highquality humor data inspired by psychological theories of humor. Utilizing a Mixtureof-Thought (MoT) approach, we deploy six cognitive personas (e.g., The Absurdist, The Cynic) to synthesize diverse comedic perspectives for a given prompt. This framework produces a theory-grounded dataset, which we use to fine-tune a 7B-parameter student model. We further evaluate two alignment strategies, Direct Preference Optimization (DPO) and an offline group-relative variant O-GRPO, finding that neither improves over SFT. However, our 7B HumorGen model variants significantly outperform larger instruction-tuned baselines and achieve top-tier open-weight performance while remaining competitive with frontier proprietary systems. These results suggest that cognitively driven data curation is more critical than alignment algorithms or model scale for humor generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Edward Ajayi, Prasenjit Mitra
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
