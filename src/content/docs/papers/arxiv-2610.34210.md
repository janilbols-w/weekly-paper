---
title: "MIS-VQA: An Annotation-Driven Surgical Vision-Language Dataset for Complex Surgical Understanding"
description: "Modern surgical AI increasingly requires multimodal understanding rather than isolated perception, yet existing datasets remain largely limited to single-task supervision such as recognition or templated question answering."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.34210) · [PDF](https://arxiv.org/pdf/2610.34210)

## 一句话摘要

Modern surgical AI increasingly requires multimodal understanding rather than isolated perception, yet existing datasets remain largely limited to single-task supervision such as recognition or templated question answering.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern surgical AI increasingly requires multimodal understanding rather than isolated perception, yet existing datasets remain largely limited to single-task supervision such as recognition or templated question answering. Current medical VQA resources often rely on synthetic templates, lack natural descriptive supervision, or provide sparse annotations that hinder reasoning about spatial relations and procedural context. We introduce MIS-VQA, a surgical vision-language dataset generated through an annotation-driven pipeline that converts heterogeneous surgical annotations into structured textual scene representations. Using EndoVis18 and CholecT50, we transform phase, instrument, interaction, triplet, and segmentation labels into unified contexts that guide large language models to generate clinically coherent question-answer pairs. MIS-VQA supports four response types-concise and detailed descriptions, perception-level grounding, and multi-step reasoning-enabling hierarchical evaluation from atomic visual grounding to compositional reasoning. To address annotation sparsity, we incorporate confidence-filtered segmentation and cross-annotation consistency checks, enabling spatially grounded supervision at scale. MIS-VQA establishes a unified benchmark for surgical vision-language understanding with spatial supervision and multi-tier reasoning evaluation. To demonstrate its utility, we introduce LLaVA-SurgXpert, a family of surgical vision-language models with visual encoders to analyze how visual representations influence multimodal reasoning. Experiments show consistent improvements over existing surgical VQA baselines while revealing capability gaps between perceptual grounding and higher-level reasoning hidden in prior benchmarks.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohamed Hamdy, Iheb Zouari, Fatmaelzahraa Ahmed, Muraam Abdel-Ghani, Muhammed Arsalan, Ponnuthurai Suganthan, Khalid Al-Jalham, Abdulaziz Al-Ali, Shidin Balakrishnan
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
