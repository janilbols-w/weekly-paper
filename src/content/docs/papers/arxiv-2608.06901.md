---
title: "Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models"
description: "Vision-language models (VLMs) have achieved remarkable generalization across diverse multimodal tasks through large-scale pre-training, yet their rapidly increasing computational and memory requirements pose significant challenges for deployment in constrained environments."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.06901) · [PDF](https://arxiv.org/pdf/2608.06901)

## 一句话摘要

Vision-language models (VLMs) have achieved remarkable generalization across diverse multimodal tasks through large-scale pre-training, yet their rapidly increasing computational and memory requirements pose significant challenges for deployment in constrained environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) have achieved remarkable generalization across diverse multimodal tasks through large-scale pre-training, yet their rapidly increasing computational and memory requirements pose significant challenges for deployment in constrained environments. Existing pruning strategies often depend on task-specific criteria or LLM-oriented importance measures, making them unsuitable for task-agnostic pruning, where no task-specific samples are available at pruning time and the pruned model remains broadly applicable. We introduce a retraining-free VLM pruning framework called PORTA that derives a task- and modality-agnostic importance formulation based on activation variation, estimated from generic calibration data, which reliably captures feature-level representation utility across modalities. PORTA further incorporates an adaptive sparsity allocation mechanism that assigns layer-wise pruning ratios based on output feature variability, avoiding the limitations of uniform sparsity and reducing performance degradation at high compression levels. Extensive experiments across VLM architectures, such as CLIP, BLIP, and Qwen2-VL, demonstrate that PORTA achieves competitive downstream performance under high sparsity without requiring any retraining, supporting efficient VLM compression. Code is available at https://github.com/cau-hai-lab/PORTA.git.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Minseok Kang, Hyunwoo Kim, Chanyoung Kim, Minwoo Kim, Jaekoo Lee, Dahuin Jung
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/cau-hai-lab/PORTA.git](https://github.com/cau-hai-lab/PORTA.git)
- 阅读深度：metadata
