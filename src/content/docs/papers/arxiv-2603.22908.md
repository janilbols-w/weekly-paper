---
title: "Adaptive Dual-Teacher Distillation with Subnetwork Rectification for Bridging Semantic Gaps in Black-Box Domain Adaptation"
description: "Assuming that neither source data nor source model parameters are accessible, black-box domain adaptation (BBDA) represents a highly practical yet challenging setting, where transferable knowledge is limited to the predictions of a black-box source model."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.22908) · [PDF](https://arxiv.org/pdf/2603.22908)

## 一句话摘要

Assuming that neither source data nor source model parameters are accessible, black-box domain adaptation (BBDA) represents a highly practical yet challenging setting, where transferable knowledge is limited to the predictions of a black-box source model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Assuming that neither source data nor source model parameters are accessible, black-box domain adaptation (BBDA) represents a highly practical yet challenging setting, where transferable knowledge is limited to the predictions of a black-box source model. Existing approaches exploit such knowledge via pseudo-label refinement or by leveraging vision-language models (ViLs), but they often fail to reconcile the inherent discrepancy between task-specific knowledge from black-box models and language-aligned semantic priors of ViLs, resulting in suboptimal integration and degraded adaptation performance. To address this challenge, we propose adaptive Dual-Teacher Distillation with Subnetwork Rectification (DDSR), a framework that explicitly reconciles these complementary yet inconsistent knowledge sources. DDSR employs an adaptive prediction fusion strategy to integrate predictions from the black-box source model and a ViL, generating reliable pseudo-labels for the target domain. A subnetwork-based regularization mechanism mitigates overfitting to noisy supervision by enforcing output consistency and gradient divergency. Furthermore, progressively improved target predictions iteratively refine both pseudo-labels and ViL prompts, enhancing semantic alignment. Finally, class-wise prototypes are used to further optimize target predictions via self-training. Extensive experiments on multiple benchmark datasets demonstrate that DDSR consistently outperforms state-of-the-art methods, including those with access to source data or source model parameters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhe Zhang, Jing Li, Wanli Xue, Xu Cheng, Jianhua Zhang, Qinghua Hu, Shengyong Chen
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
