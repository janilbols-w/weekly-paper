---
title: "MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum"
description: "Turkish encoder models have adopted modern architectures while leaving the pretraining objective fixed at masked language modelling."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.25768) · [PDF](https://arxiv.org/pdf/2608.25768)

## 一句话摘要

Turkish encoder models have adopted modern architectures while leaving the pretraining objective fixed at masked language modelling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Turkish encoder models have adopted modern architectures while leaving the pretraining objective fixed at masked language modelling. This paper introduces MoganBert-TR, a 149M-parameter Turkish encoder foundation model trained from scratch on a language-specifically filtered corpus, together with an embedding model derived from it (MoganBert-Embed). MoganBert-TR is trained over 237.3B tokens with a two-stage CLM-to-MLM curriculum: causal language modelling first, masked language modelling for the remainder, with the transition made inside the stable phase of a WSD schedule. In a controlled ablation under an equal step budget, this design outperforms pure MLM by 2.7-3.7x on Turkish MS MARCO retrieval; the measured mechanism is embedding geometry, where a single direction absorbs 28.1% of the variance under pure MLM against 11.9% under the curriculum. Long-context extension and learning-rate decay are then split into two branches after a shared prefix: running the final portion of decay at 1024 context improves the TrGLUE average by 0.49 +/- 0.26 points across five paired seeds (p = 0.013) and beats a model-soup alternative by 0.75 points at ~4.3% additional cost. MoganBert-TR attains 78.41 on TrGLUE, the best among the Turkish ModernBERT models compared, and 77.73 on TabiBench, where it leads two of the eight categories with the largest margin on code retrieval (+3.62 points over TabiBERT). MoganBert-Embed, produced through teacher distillation and multi-signal contrastive fine-tuning, ranks first among student models on the MTEB(Turkish) overall average with 68.30 and reaches 99.5% of its 7.57B-parameter teacher's score with a 51x smaller backbone. The accompanying 50,048-token tokenizer outperforms all compared Turkish tokenizers on compression and fertility across two independent test sets. Weights, tokenizer, embedding model and evaluation code: https://huggingface.co/moganai

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Furkan Yilmaz, Habibe Aleyna Tasdemir, Muhammed Faruk Gozay
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
