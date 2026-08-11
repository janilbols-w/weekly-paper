---
title: "Language-Specialized Multi-Teacher On-Policy Distillation for Multilingual LLM-Based ASR"
description: "Modern LLM-based ASR systems have established multilingual capability as a standard feature, leveraging large-scale multilingual corpora and LLMs' cross-lingual knowledge to achieve competitive performance across multilingual benchmarks."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03610) · [PDF](https://arxiv.org/pdf/2608.03610)

## 一句话摘要

Modern LLM-based ASR systems have established multilingual capability as a standard feature, leveraging large-scale multilingual corpora and LLMs' cross-lingual knowledge to achieve competitive performance across multilingual benchmarks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM-based ASR systems have established multilingual capability as a standard feature, leveraging large-scale multilingual corpora and LLMs' cross-lingual knowledge to achieve competitive performance across multilingual benchmarks. However, jointly modeling languages with heterogeneous acoustic, phonological, and lexical characteristics inevitably introduces optimization conflicts, undermining language-wise specialization. To address this challenge, we propose Language-Specialized Multi-Teacher On-Policy Distillation (LS-MOPD), which decouples language-specific knowledge acquisition from multilingual capability integration: language-specialized teachers are independently optimized via reinforcement learning (RL), with their expertise then integrated into a generalist multilingual student through language routing and token-level multi-teacher distillation, thereby reducing direct cross-lingual optimization conflicts. We further explore static and dynamic acoustic-prefix configurations to examine how teacher-student prefix consistency influences the efficacy of on-policy distillation. Experiments on benchmarks covering Mandarin, Mandarin subdialects, Cantonese, and English demonstrate that LS-MOPD substantially outperforms RL baselines and surpasses the empirical performance envelope defined by the best-performing RL teachers on nearly all benchmarks, revealing its potential to generalize beyond all teachers in multilingual ASR.

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

- 作者：Yuan Xie, Jiaqi Song, Xianliang Wang, Ming Lei, Jie Gao, Jie Wu
- 发布：2026-08-05；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
