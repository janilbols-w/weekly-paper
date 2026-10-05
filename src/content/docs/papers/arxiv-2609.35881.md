---
title: "GenoTrace: Inheritable Watermarks for Genome Foundation Model Distillation"
description: "Can a genome model retain a detectable record of the synthetic sequences used to train it?"
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35881) · [PDF](https://arxiv.org/pdf/2609.35881)

## 一句话摘要

Can a genome model retain a detectable record of the synthetic sequences used to train it?

## 为什么值得关注

待编辑增强。

## 摘要原文

Can a genome model retain a detectable record of the synthetic sequences used to train it? We study watermark inheritance through distillation with GenoTrace, a codon-aware extension of green-list watermarking. Two token-level factors modulate the teacher's generation bias using codon position and organism-specific codon usage. The resulting sequences train a smaller student, whose outputs are audited without an active watermark processor. In a three-seed GenomeOcean-500M-to-100M experiment, the joint configuration achieves a mean audit score of 17.88 and 94.5% detection at a fixed threshold. It retains 49.0% detection after key-aware token substitution, compared with 0% for the available single-seed plain-watermark comparator, and 47.0% after combined mechanism-targeted nucleotide edits. Additional experiments establish inherited signal across five organism-conditioned datasets and teacher-student size ratios up to 40. Component ablations and computational sequence-quality assays reveal distinct operating points for detection strength and coding coverage. GenoTrace provides a practical token-level construction and an empirical account of how genomic structure shapes inherited watermark signals. The findings concern shared-tokenizer distillation and the tested editing procedures, with calibration and biological utility treated as separate evaluation requirements.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guang Yang, Fengchen Liu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
