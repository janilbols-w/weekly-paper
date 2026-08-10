---
title: "MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation"
description: "Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.07463) · [PDF](https://arxiv.org/pdf/2608.07463)

## 一句话摘要

Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis. However, generating mirror reflections remains challenging because the content within a mirror must remain consistent with the surrounding scene. Existing VDMs are not specifically designed to model scene-to-mirror relationships, which can lead to reflections with incorrect content or inconsistent spatial arrangements. We observe that mirror reflection generation involves two complementary challenges: determining what scene content should be reflected and how the reflected content should be spatially arranged within the mirror region. Motivated by this observation, we propose MirrorWorld, a reflection-aware video inpainting framework that models scene-to-mirror relationships during generation. Specifically, we introduce Semantic Relation Distillation (SRD), which transfers relational information from a frozen visual foundation model to encourage semantic associations between visible scene content and mirror regions. We further propose Geometric Transformation Alignment (GTA), which learns a transformation that guides the spatial arrangement of reflected content. The two components play complementary roles, with SRD modeling what should be reflected and GTA modeling how it should be arranged. To facilitate research on this problem, we construct a benchmark for video mirror reflection generation by repurposing four existing video mirror datasets into a unified reflection reconstruction task. Experimental results show that MirrorWorld achieves improved reflection reconstruction quality over representative image-based reflection generation methods and strong video inpainting baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
