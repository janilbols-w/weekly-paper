---
title: "Coverage-Aware Reasoning with Medical Tokens for Diagnosis Prediction"
description: "Large language models (LLMs) offer promising potential for next-visit diagnosis prediction, owing to their ability to integrate longitudinal clinical evidence and reason over it in natural language."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.10641) · [PDF](https://arxiv.org/pdf/2610.10641)

## 一句话摘要

Large language models (LLMs) offer promising potential for next-visit diagnosis prediction, owing to their ability to integrate longitudinal clinical evidence and reason over it in natural language.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) offer promising potential for next-visit diagnosis prediction, owing to their ability to integrate longitudinal clinical evidence and reason over it in natural language. However, reinforcement learning for LLM reasoning commonly rewards each trajectory according to the correctness of its final answer. In next-visit diagnosis prediction, multiple diagnoses can be simultaneously valid, but independently rewarding one diagnosis per trajectory does not distinguish repeated hits from coverage of different diagnoses. The policy can therefore concentrate on a few correct diagnoses, leaving others uncovered. Meanwhile, LLM tokenizers can split ICD codes into several generic tokens with limited clinical meaning, requiring multiple decoding steps to predict each diagnosis and hindering reasoning over a large disease vocabulary. To address both challenges, we propose CARing, a framework that represents diagnoses with compositional Semantic IDs (SIDs) and optimizes reasoning trajectories for multi-label coverage. Concretely, we first encode ontology-enriched disease semantics into compact SIDs through residual quantization, and ground the resulting SID tokens in natural language and longitudinal EHR contexts through multi-task alignment and reasoning-enriched training to unlock transferable LLM reasoning. CARing further improves unordered multi-label prediction through a coverage reward for reinforcement learning and multi-positive supervision. At inference time, the model supports both efficient direct constrained decoding and multi-chain reasoning with rank fusion. On MIMIC-III and MIMIC-IV, CARing exceeds all EHR-trained baselines in weighted F1 and attains the highest top-k recall at every reported cutoff, including R@30 of 46.04% and 46.52% in reasoning mode. Our codes and logs are available at https://github.com/zmlxzyh/CARing-Codes-Logs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Kaisong Zhang, Haotian Fang, Junmeng Zhou, Hang Lv, Yulan Pan, Yanchao Tan
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zmlxzyh/CARing-Codes-Logs](https://github.com/zmlxzyh/CARing-Codes-Logs)
- 阅读深度：metadata
