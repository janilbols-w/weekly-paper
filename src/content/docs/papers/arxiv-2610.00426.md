---
title: "IrekoGPT: Turning Structured Pruning into Post-Hoc Slimmable LLMs"
description: "We introduce IrekoGPT, a post-hoc method for converting pretrained LLMs into slimmable models whose width can be adjusted at inference time."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.00426) · [PDF](https://arxiv.org/pdf/2610.00426)

## 一句话摘要

We introduce IrekoGPT, a post-hoc method for converting pretrained LLMs into slimmable models whose width can be adjusted at inference time.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce IrekoGPT, a post-hoc method for converting pretrained LLMs into slimmable models whose width can be adjusted at inference time. Building on SliceGPT, we retain its projection matrices without pruning them, allowing a single model to expose nested subnetworks at different widths. We improve robustness by calibrating each layer across multiple compression ratios, and correct downstream linear layers through gradient-free ridge regression. Across Llama and Qwen models, preliminary results show improvements over naive PCA-based slimming, with the largest gains at high compression. Code is available at https://github.com/aimagelab/IrekoGPT

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Pietro Moriello, Pietro Buzzega, Angelo Porrello, Simone Calderara
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/aimagelab/IrekoGPT](https://github.com/aimagelab/IrekoGPT)
- 阅读深度：metadata
