---
title: "Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG"
description: "Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades inference efficiency."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05152) · [PDF](https://arxiv.org/pdf/2609.05152)

## 一句话摘要

Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades inference efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades inference efficiency. Soft context compression encodes each document into a substantially shorter embedding sequence. However, most existing approaches are trained by distilling outputs from uncompressed RAG systems, inherently limiting their performance relative to the original model. To address this limitation, we propose DEX-Comp, a two-stage training recipe: Pure Distillation warm-starts the compression model on the uncompressed RAG's correct responses only, and Hard Exploration then runs reinforcement learning solely on queries the uncompressed RAG fails, forcing the model to explore computation patterns better suited to compressed representations. On five open-domain QA benchmarks at retrieval depths from top-5 to top-30, DEX-Comp compresses retrieved contexts by $16\times$ and accelerates inference by $4\times$--$24\times$, while achieving performance comparable to or exceeding the uncompressed RAG baseline across retrieval depths. Ablations and evaluations across diverse datasets and backbones further confirm the contribution of each stage and the generalization of our approach.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuyu Guo, Shuo Zhang, Zhaochun Ren
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
