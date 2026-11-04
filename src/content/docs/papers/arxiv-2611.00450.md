---
title: "From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory"
description: "Retrieval-augmented generation (RAG) helps large language models (LLMs) answer factual questions beyond their training data, but it adds storage and inference costs."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.00450) · [PDF](https://arxiv.org/pdf/2611.00450)

## 一句话摘要

Retrieval-augmented generation (RAG) helps large language models (LLMs) answer factual questions beyond their training data, but it adds storage and inference costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-augmented generation (RAG) helps large language models (LLMs) answer factual questions beyond their training data, but it adds storage and inference costs. Distilling previously retrieved information into parametric memories enables reuse without online retrieval. However, training the memory to mimic a retriever rewards accurate independent predictions, which do not necessarily improve the final output quality when combined with the LLM's existing predictions. To address this, we introduce ResMem, in which the LLM reads retrieved text offline to generate teacher targets. This design avoids storing massive token representations, unlike existing parametric memory approaches such as MLP Memory, which relies on k-nearest neighbor (kNN) datastores. Furthermore, by using the LLM as an offline teacher that reads privileged retrieved evidence alongside the input, we train a parametric memory to learn an additive logit residual. This residual aligns the predictions of a student sharing the same backbone with the teacher distribution, while self-distillation updates remain confined to the parametric memory. On a Wikipedia subset, ResMem reduces the storage retained for teacher construction by 94.7% compared with the evaluated kNN pipeline. Across five question answering datasets, ResMem raises mean token F1 from 32.83% for the frozen LLM to 34.48%. It also breaks 21% fewer of the LLM's correct answers than a kNN-trained memory. These findings validate our motivation of treating retrieval as a learning resource, with parametric memory shaped by how retrieved knowledge is used to inform the model's future predictions. Code and model weights are available at https://github.com/SSRand/From-Lookups-to-Lessons and https://huggingface.co/RandHan/ResMem-Mistral-7B-v0.3.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Changjiang Han, Bowei He, Ye Yuan, Weixu Zhang, Haolun Wu, Xue Liu, Jikun Kang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SSRand/From-Lookups-to-Lessons](https://github.com/SSRand/From-Lookups-to-Lessons)
- 阅读深度：metadata
