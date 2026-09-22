---
title: "Efficient LLM Distillation for Bangladesh Legal Context: A Smartphone-Compatible Retrieval-Augmented Generation Model"
description: "Legal information in Bangladesh is inaccessible to most citizens."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.24177) · [PDF](https://arxiv.org/pdf/2609.24177)

## 一句话摘要

Legal information in Bangladesh is inaccessible to most citizens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Legal information in Bangladesh is inaccessible to most citizens. Statutory text is English-only, trained lawyers are concentrated in urban centres, and cloud-dependent AI fails where mobile connectivity is unreliable, a setting in which hallucinated legal text causes direct harm. The system addresses statutory interpretation only; queries that require judicial precedent or case-law reasoning fall outside its scope. We target the statutory access gap by compressing a 9-billion-parameter Gemma-2 teacher into a 2-billion-parameter student through two-phase progressive knowledge distillation. Phase 1 performs supervised fine-tuning on 9,429 quality-gated legal question-answer pairs (65% acceptance from 14,514 generated queries); Phase 2 minimises sparse Kullback-Leibler divergence against the teacher's top-50 per-token logits at temperature tau = 4.0, implemented via QLoRA (4-bit NF4, rank-32 LoRA adapters). Prior legal language models target general legal English; this system specialises in Bangladeshi statutory law. Every response is grounded through hybrid retrieval combining dense semantic search (60%) and BM25 (40%) across 36,029 statutory passages from the Bangladesh Constitution and national legislation. On a 50-query English benchmark, the distilled model reaches ROUGE-L 0.4715 and BERTScore F1 0.5679, a 103% ROUGE-L and 143% BERTScore gain over the retrieval-augmented undistilled baseline (ROUGE-L 0.2323, BERTScore 0.2340). The adapter quantises to 1.6 GB (GGUF Q4_K_M) and runs at 4-8 tokens per second on a Pixel 6 with no network access. Cross-lingual evaluation on 50 Bangla queries yields ROUGE-L 0.4083 and BERTScore 0.8133, showing effective retrieval from Bangla input against an English-only corpus. In a single-evaluator pilot, a practising lawyer rated 50 responses at a weighted mean of 4.16/5 (90% rated 4 or 5), supporting utility beyond text-overlap metrics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：MD. Nafis Kamal, Mahadi Hasan Fahim, Talha Ridwan, Nadifa Zaman, Fariha Roushon Florin, Farig Yousuf Sadeque, Saadat Rafid Ahmed
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
