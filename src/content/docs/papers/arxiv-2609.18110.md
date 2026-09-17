---
title: "SSD-LLaMA: SSD-Native Inference for Trillion-Parameter MoE at 1+ Token/s on a Consumer PC"
description: "Frontier open-weight language models increasingly use Mixture-of-Experts (MoE) architectures to expand model capacity while activating only a small subset of experts per token."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.18110) · [PDF](https://arxiv.org/pdf/2609.18110)

## 一句话摘要

Frontier open-weight language models increasingly use Mixture-of-Experts (MoE) architectures to expand model capacity while activating only a small subset of experts per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Frontier open-weight language models increasingly use Mixture-of-Experts (MoE) architectures to expand model capacity while activating only a small subset of experts per token. Local inference must nevertheless keep the complete expert pool available, which remains far beyond consumer-grade RAM and VRAM capacity even after quantization. SSDs provide practical capacity at this scale, but turning that capacity into executable model memory requires efficient expert delivery, coordinated management of SSD, RAM, and VRAM, and CPU--GPU hybrid execution under bounded bandwidth. We present \textit{SSD-LLaMA}, an SSD-native local MoE inference system that addresses these challenges with an SSD I/O pipeline optimized for expert delivery, a native three-tier storage hierarchy that delivers and retains experts dynamically, and balanced CPU--GPU hybrid execution. \textit{SSD-LLaMA} executes every selected expert without pruning or substitution. Across three frontier MoE model families, \textit{SSD-LLaMA} improves prefill token rate by 1.52$\times$--4.19$\times$ and decode token rate by 2.10$\times$--15.58$\times$ over the evaluated baselines. We also achieve higher than 1 token/s for running trillion-parameter model with a single RTX 5090 and no more than 32GB RAM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fangzhou Liang, Yibin Shen, Jianmin Hu, Jiayang Xu, Hanchi Gao, Minxian Xu, Zili Meng
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
