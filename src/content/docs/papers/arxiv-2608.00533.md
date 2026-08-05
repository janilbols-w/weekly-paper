---
title: "Native Multilingual Chain-of-Thought Reasoning in Low-Resource Southeast Asian Languages"
description: "Large Language Models have achieved substantial progress in reasoning capabilities."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.00533) · [PDF](https://arxiv.org/pdf/2608.00533)

## 一句话摘要

Large Language Models have achieved substantial progress in reasoning capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models have achieved substantial progress in reasoning capabilities. Yet in low-resource native settings, many suffer from cross-lingual collapse, reverting to English during intermediate steps that require complex logical reasoning. This presents a cold-start bottleneck for policy optimization, whereas standard fine-tuning risks catastrophic forgetting due to cross-lingual representation drift. To address these challenges, we introduce the Onramp-Sequence Cross-Distillation (OSCD), a post-training algorithm that projects high-resource reasoning trajectories into low-resource vocabulary subspaces during generative training rollouts via an integrated translator agentic loop, ensuring the stable and efficient translation of dynamically generated reference samples for fine-tuning. This is coupled with joint-embedding semantic alignment of both reference and target-language reasoning traces, thereby bridging the pairwise cross-lingual representational gaps. Comprehensive evaluations using the AIME25 and HMMT25 benchmarks demonstrate that OSCD yields up to 3.2 times overall improvements in native Southeast Asian languages for mathematical reasoning, of which the joint-embedding semantic alignment component contributes up to 6.4% improvements in linguistic debiasing over translation-only baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sean Gip Lim, William Chandra Tjhi, Hai Leong Chieu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
