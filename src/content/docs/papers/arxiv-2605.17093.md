---
title: "HEED: Density-Weighted Residual Alignment for Hybrid Vision-Language Model Distillation"
description: "Distilling vision-language models into faster hybrid architectures, such as 3:1 Mamba-2/attention mixes, is now standard practice for making inference efficient."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.17093) · [PDF](https://arxiv.org/pdf/2605.17093)

## 一句话摘要

Distilling vision-language models into faster hybrid architectures, such as 3:1 Mamba-2/attention mixes, is now standard practice for making inference efficient.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distilling vision-language models into faster hybrid architectures, such as 3:1 Mamba-2/attention mixes, is now standard practice for making inference efficient. Aggregate benchmarks suggest that this works but they hide selective failures. When we distill Qwen3-VL-8B-Instruct into a 3:1 Mamba-2/attention hybrid, student model stays within 2 points of the teacher across visual reasoning benchmarks like MMStar, MMBench, and MMMU-Pro, while dropping 13 points on optical-character-recognition and document tasks. The student can still understand the scene but loses the fine-grained text needed to answer. We localize much of the failure to a specific kind of position. In a high-resolution image, most patches are sky, wall, or smooth texture, while a small fraction carries text, edges, object boundaries, or other local details. In a token-level diagnostic, the top 10% highest-density patches have 3.6x larger residual drift than the bottom 10% lowest-density patches and 3.5x larger teacher-masking answer contribution. Uniform weighting devotes many loss terms to low-information background patches, whereas sparse answer bearing patches receive no special protection. The required intervention is minimal: we replace uniform residual alignment with density-weighted residual alignment, using patch self-dissimilarity as a training-free proxy for position importance. We call this HEED. Compared with normal end-to-end distillation, HEED increases performance by 8.7 points on OCRBench v2 and 5.13 points on a 10-benchmark average. The gain is realized on different teacher models. After standard post-training, the student reaches teacher-level performance on the 10-benchmark average. HEED adds no parameters and no inference-time cost. Hence, the student maintains the hybrid architecture's 4.12x throughput and 68% memory saving at 128k context. Code is available at https://github.com/jha-lab/HEED.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yihao Liang, Niraj K. Jha
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jha-lab/HEED](https://github.com/jha-lab/HEED)
- 阅读深度：metadata
