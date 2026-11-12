---
title: "Beyond Passive Imitation: On-Policy Mid-Training Distillation for Language Models"
description: "Continual pre-training (CPT) adapts large language models (LLMs) to specialized domains, yet its standard next-token prediction (NTP) objective treats every corpus token as a fixed target, regardless of its utility to the current model."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.13855) · [PDF](https://arxiv.org/pdf/2611.13855)

## 一句话摘要

Continual pre-training (CPT) adapts large language models (LLMs) to specialized domains, yet its standard next-token prediction (NTP) objective treats every corpus token as a fixed target, regardless of its utility to the current model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continual pre-training (CPT) adapts large language models (LLMs) to specialized domains, yet its standard next-token prediction (NTP) objective treats every corpus token as a fixed target, regardless of its utility to the current model. In a controlled study on the same 1B-token mathematical corpus, we observe sharply different outcomes across base models: NTP improves Llama-3.2-3B's performance on mathematical benchmarks but substantially degrades Qwen3-1.7B-Base's performance, indicating that, under a fixed training recipe, the same training sequences can have model-dependent effects. To address this problem, we introduce On-Policy Mid-Training Distillation (OPMD), which reformulates mid-training from offline text imitation into active, query-driven knowledge acquisition. At selected anchor positions, OPMD samples trajectories from the evolving student policy and applies dense token-level reverse-KL rewards from a frozen teacher, training the model on states it actually visits rather than only on ground-truth prefixes. This on-policy objective reduces the training-generation mismatch of teacher-forced NTP. On MATH-500 and Minerva, OPMD improves the Qwen student over its base performance and outperforms the evaluated NTP baseline, which degrades on both benchmarks. OPMD integrates into CPT pipelines without added inference-time overhead and offers a model-aware alternative to passive domain adaptation.

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

- 作者：Ruize Zheng, Xuyang Liu, Siyu Ren, Xiaobing Tu, Yinggui Wang, Jinkui Ren, Xiantao Zhang, Linfeng Zhang
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
