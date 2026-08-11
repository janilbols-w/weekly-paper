---
title: "UI-MOPD: Multi-Platform On-Policy Distillation for Unified GUI Agents"
description: "Recent advances in multimodal foundation models and agent systems have driven GUI agents from single-platform task execution toward cross-platform interaction."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.04425) · [PDF](https://arxiv.org/pdf/2607.04425)

## 一句话摘要

Recent advances in multimodal foundation models and agent systems have driven GUI agents from single-platform task execution toward cross-platform interaction.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in multimodal foundation models and agent systems have driven GUI agents from single-platform task execution toward cross-platform interaction. However, unified multi-platform GUI learning remains challenging: high-quality cross-platform trajectories remain scarce, while platforms share transferable capabilities but differ in action semantics and interaction conventions. Naively mixing supervision or merging specialized models can blur native behaviors and produce imbalanced performance. To address these challenges, we construct Uni-GUI, a high-quality dataset containing nearly 10K executable cross-platform interaction trajectories collected through a unified desktop-mobile harness. Building on Uni-GUI, we propose UI-MOPD, the first framework to introduce multi-teacher on-policy distillation (MOPD) into unified multi-platform GUI agent training. UI-MOPD trains a shared student on its own rollouts and dynamically routes each rollout to the corresponding platform-specialized teacher. At student-visited states, teacher guidance serves as a platform-conditioned behavioral anchor, enabling the integration of complementary desktop and mobile expertise without averaging their distinct interaction conventions. On OSWorld and MobileWorld, UI-MOPD achieves task success rates of 38.2% and 12.0%, respectively, outperforming parameter-matched integration strategies while preserving general GUI grounding. These results demonstrate that multi-teacher on-policy distillation provides an effective approach to building unified cross-platform GUI agents. Project page: https://elispectre.github.io/UI-MOPD/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Niu Lian, Tongbo Chen, Zhehao Yu, Chengzhen Duan, Fazhan Liu, Hui Liu, Pei Fu, Jian Luan, Heng Qu, Shu-Tao Xia, Jinpeng Wang
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
