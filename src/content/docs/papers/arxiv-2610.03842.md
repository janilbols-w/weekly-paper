---
title: "KVE-KD: Key Visual Evidence-Guided Knowledge Distillation for Vision-Language Models"
description: "Knowledge distillation is crucial for deploying vision-language models on resource-constrained devices."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.03842) · [PDF](https://arxiv.org/pdf/2610.03842)

## 一句话摘要

Knowledge distillation is crucial for deploying vision-language models on resource-constrained devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation is crucial for deploying vision-language models on resource-constrained devices. However, existing methods typically impose uniform supervision across visual tokens or rely on static token selection, which confuses task-relevant cues with background noise and degrades cross-modal reasoning. To address this limitation, we propose Key Visual Evidence-guided Knowledge Distillation (KVE-KD), a framework that dynamically focuses feature distillation on task-relevant visual tokens identified by the teacher model. Specifically, KVE-KD appoints the final pre-generation textual token as a unified semantic anchor and identifies the target cross-modal fusion layer by analyzing changes in the anchor representation through iterative visual-token contribution removal. Within this layer, KVE-KD ranks visual tokens via the anchor-conditioned attention distribution and selects the most informative visual tokens as key visual evidence with normalized entropy. The key visual evidence subsequently guides focused visual feature distillation, making the student align closely with the teacher's task-relevant visual representations while suppressing irrelevant background information. Extensive experiments on six benchmarks demonstrate that KVE-KD outperforms state-of-the-art cross-modal distillation methods, with particularly pronounced gains on tasks requiring complex reasoning and fine-grained visual understanding. Importantly, these improvements are achieved without introducing any inference-time overhead. The source code is available at https://github.com/zhangjianbin07/KVE-KD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jianbin Zhang, Xin Sun, Shanwen Wang, Wei Ye, Susanto Rahardja
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zhangjianbin07/KVE-KD](https://github.com/zhangjianbin07/KVE-KD)
- 阅读深度：metadata
