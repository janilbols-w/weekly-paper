---
title: "Weakly Supervised Distillation of Hallucination Signals into Transformer Representations"
description: "Existing hallucination detection methods for large language models (LLMs) rely on external verification at inference time, requiring gold answers, retrieval systems, or auxiliary judge models."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.06277) · [PDF](https://arxiv.org/pdf/2604.06277)

## 一句话摘要

Existing hallucination detection methods for large language models (LLMs) rely on external verification at inference time, requiring gold answers, retrieval systems, or auxiliary judge models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing hallucination detection methods for large language models (LLMs) rely on external verification at inference time, requiring gold answers, retrieval systems, or auxiliary judge models. We ask whether this external supervision can instead be distilled into the model's own representations during training, enabling hallucination detection from internal activations alone at inference time. We introduce a weak supervision framework that combines three complementary grounding signals: substring matching, sentence embedding similarity, and an LLM as a judge verdict to label generated responses as grounded or hallucinated without human annotation. Using this framework, we construct a 15000-sample dataset from SQuAD v2 (10500 train/development samples and a separate 5000-sample test set), where each example pairs a LLaMA-2-7B generated answer with its full per-layer hidden states and structured hallucination labels. We then train five probing classifiers: ProbeMLP (M0), LayerWiseMLP (M1), CrossLayerTransformer (M2), HierarchicalTransformer (M3), and CrossLayerAttentionTransformerV2 (M4), directly on these hidden states, treating external grounding signals as training-time supervision only. Our central hypothesis is that hallucination detection signals can be distilled into transformer representations, enabling internal detection without any external verification at inference time. Results support this hypothesis. Transformer-based probes achieve the strongest discrimination, with M2 performing best on 5-fold average AUC/F1, and M3 performing best on both single-fold validation and held-out test evaluation. We also benchmark inference efficiency: probe latency ranges from 0.15 to 5.62 ms (batched) and 1.55 to 6.66 ms (single sample), while end-to-end generation plus probe throughput remains approximately 0.231 queries per second, indicating negligible practical overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shoaib Sadiq Salehmohamed, Jinal Prashant Thakkar, Hansika Aredla, Shaik Mohammed Omar, Naveen Bera, Pulijala Sai Nikhila, Kondaguduru Abhiram, Shaik Gayaz Ali, Shalmali Ayachit
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
