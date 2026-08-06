---
title: "RiboSphere: Learning Unified and Efficient Representations of RNA Structures"
description: "Accurate RNA structure modeling remains difficult because RNA backbones are highly flexible, non-canonical interactions are prevalent, and experimentally determined 3D structures are comparatively scarce."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2603.19636) · [PDF](https://arxiv.org/pdf/2603.19636)

## 一句话摘要

Accurate RNA structure modeling remains difficult because RNA backbones are highly flexible, non-canonical interactions are prevalent, and experimentally determined 3D structures are comparatively scarce.

## 为什么值得关注

待编辑增强。

## 摘要原文

Accurate RNA structure modeling remains difficult because RNA backbones are highly flexible, non-canonical interactions are prevalent, and experimentally determined 3D structures are comparatively scarce. We introduce RiboSphere, a framework that learns discrete geometric representations of RNA by combining vector quantization with flow matching. Our design is motivated by the modular organization of RNA architecture: complex folds are composed from recurring structural motifs. RiboSphere uses a geometric transformer encoder trained using mean-centered coordinates and random rotation augmentation to produce geometry-aware features, which are discretized with finite scalar quantization (FSQ) into a finite vocabulary of latent codes. Conditioned on these discrete codes, a flow-matching decoder reconstructs atomic coordinates, enabling high-fidelity structure generation. We find that the learned code indices are enriched for specific RNA motifs, suggesting that the model captures motif-level compositional structure rather than acting as a purely compressive bottleneck. Across benchmarks, RiboSphere achieves strong performance in structure reconstruction (RMSD 1.25,{\AA}, TM-score 0.84), and its pretrained discrete representations transfer effectively to inverse folding and RNA--ligand binding prediction, with robust generalization in data-scarce regimes. Code is available at https://github.com/Zhangz312/RiboSphere.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhou Zhang, Hanqun Cao, Cheng Tan, Fang Wu, Pheng Ann Heng, Tianfan Fu
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Zhangz312/RiboSphere](https://github.com/Zhangz312/RiboSphere)
- 阅读深度：metadata
