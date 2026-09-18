---
title: "Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation"
description: "Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.20441) · [PDF](https://arxiv.org/pdf/2609.20441)

## 一句话摘要

Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Geospatial foundation models can provide strong flood-segmentation performance, but their size limits deployment on memory-constrained edge hardware. We distill a 300-million-parameter Prithvi-EO-2.0 teacher, fine-tuned on the 252 manually labeled Sen1Floods11 training scenes, into a 0.7-million-parameter EfficientViT-B0 student. The teacher supervises additional unlabeled Sentinel-2 imagery, allowing the student training set to grow without new manual annotations. At the matched budget of 252 scenes, teacher-supervised training is competitive with direct training and improves STURM-Flood performance across tested configurations; a geometry-matched control shows that label source alone does not explain the difference. Scaling the teacher-supervised pool to 2,500 scenes narrows the remaining student--teacher gap: the float student reaches 0.787 water intersection over union on the Sen1Floods11 test split against 0.822 for the teacher, matches the teacher on STURM-Flood under our evaluation protocol, and remains below it on WorldFloods-v2. After activation replacement and quantization-aware training, the student runs as a 1.5-megabyte 8-bit integer (INT8) TensorRT engine on a Jetson Xavier NX at 5.57 milliseconds of graphics processing unit (GPU) compute per 512-by-512 image, with approximately 14 megabytes of runtime device memory. A fixed modified normalized difference water index (MNDWI) threshold is competitive with both models on the two clean external benchmarks, so we interpret those benchmarks as generalization tests rather than as evidence of learned-model superiority over a spectral rule. The results support the conclusion: foundation-model supervision can amplify a fixed manual annotation budget into a substantially larger training set and yield a compact, deployable edge model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fabian Schmalstieg, Karsten Mueller, Wojciech Samek
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
