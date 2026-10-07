---
title: "WASD: Wasserstein-based Knowledge Distillation for Large Language Models"
description: "Autoregressive large language models (LLMs) have rapidly advanced in capability, but their increasing scale comes with substantial computational and memory costs at inference time."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.07706) · [PDF](https://arxiv.org/pdf/2610.07706)

## 一句话摘要

Autoregressive large language models (LLMs) have rapidly advanced in capability, but their increasing scale comes with substantial computational and memory costs at inference time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive large language models (LLMs) have rapidly advanced in capability, but their increasing scale comes with substantial computational and memory costs at inference time. Knowledge distillation (KD) offers a practical solution by transferring knowledge from a large teacher model to a smaller student model via alignment of discrete probability distributions. However, existing KD methods for LLMs primarily rely on divergences that evaluate discrepancies through probability values at each vocabulary index, without explicitly leveraging token-level semantic information. We propose Wasserstein-based knowledge distillation (WASD) for LLMs, which incorporates token-level semantic information via the Wasserstein-based distance with a cost matrix derived from token embeddings. To ensure computational tractability, we adopt the Sinkhorn divergence and derive a gradient-equivalent objective that can be efficiently optimized without introducing additional networks. Experiments across multiple LLM families and scales show that WASD consistently improves distillation performance on diverse tasks, including instruction following, mathematical reasoning, and code generation. Our results highlight the importance of semantic information encoded in the token space for effective distribution alignment in LLM distillation. The implementation is publicly available at https://github.com/aailab-kaist/WASD .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Byeonghu Na, Donghyeok Shin, Yeongmin Kim, Mina Kang, Il-Chul Moon
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/aailab-kaist/WASD](https://github.com/aailab-kaist/WASD)
- 阅读深度：metadata
