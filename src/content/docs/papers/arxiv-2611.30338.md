---
title: "Learning Teacher Output Preferences from Final Responses for Reasoning Distillation"
description: "Many large language models (LLMs) use chain-of-thought (CoT) to solve complex problems, but hide their CoT traces to prevent reasoning capabilities from being distilled."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.30338) · [PDF](https://arxiv.org/pdf/2611.30338)

## 一句话摘要

Many large language models (LLMs) use chain-of-thought (CoT) to solve complex problems, but hide their CoT traces to prevent reasoning capabilities from being distilled.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many large language models (LLMs) use chain-of-thought (CoT) to solve complex problems, but hide their CoT traces to prevent reasoning capabilities from being distilled. While recent studies have shown that hidden CoTs can be reconstructed, existing methods typically require training a separate attacker for each target LLM. This paper studies model-agnostic CoT reconstruction, aiming to reconstruct hidden CoT traces from arbitrary target LLMs using only input prompts and visible final responses. We propose Final-Output Preference Learning (FOPL), which trains a single reconstruction model that generalizes to unseen LLMs without target-specific adaptation. To achieve this, the reconstruction model must learn which reasoning patterns match a given final response without knowing the target LLM's identity. We address this using preference optimization, training the reconstruction model to prefer native CoTs over synthetic alternatives for the same question and final response. By learning these preferences from LLMs with accessible CoTs, the reconstruction model learns to distinguish reasoning patterns based on visible responses. Experiments show that reconstructed CoTs capture distinct reasoning patterns across LLM families, including a family unseen during training. Moreover, students trained on reconstructed CoTs match or outperform those trained on native CoTs across several reasoning benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongli Shen, Shaopeng Fu, Qinbo Zhang, Jian Li, Di Wang
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
