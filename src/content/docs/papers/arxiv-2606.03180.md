---
title: "GLINT: Sparsely Gated Vision-Language Alignment for Fine-Grained Radiology Representations"
description: "Vision-language models (VLMs) for radiology have emerged as a scalable paradigm by leveraging image-report pairs naturally produced in clinical workflows."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.03180) · [PDF](https://arxiv.org/pdf/2606.03180)

## 一句话摘要

Vision-language models (VLMs) for radiology have emerged as a scalable paradigm by leveraging image-report pairs naturally produced in clinical workflows.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) for radiology have emerged as a scalable paradigm by leveraging image-report pairs naturally produced in clinical workflows. However, this pairing reveals a mismatch in scale: each finding occupies only a small region of the image, yet supervision is provided only at the global image-report level. This poses a central challenge: prior approaches spread weight densely across all patches rather than concentrating on the sparse subset relevant to a given query. To address this, we present GLINT (Gated Language-Image alignmeNT), a framework that models this sparse correspondence. On the alignment side, we introduce Sparsely Gated Alignment, a novel architecture in which a sigmoid gate over a separate gate embedding space activates only the patches relevant to each textual query, yielding sparsity. On the representation side, we add Dense Feature Regularization, which anchors the trainable encoder's intermediate features to a frozen self-supervised learning (SSL) teacher, preserving the fine-grained patch features that the gate relies on. The same recipe applies to both 2D chest X-ray (CXR) and 3D chest computed tomography (CT), built with DINOv3 and V-JEPA 2.1, respectively. GLINT enables zero-shot classification, grounding, and segmentation from free-text queries, and to our knowledge is the first to demonstrate zero-shot segmentation on 3D CT volumes without mask supervision. Notably, the most pronounced gains arise on zero-shot grounding and segmentation, where sparse, query-specific localization is required, consistent with our design intent. In downstream evaluation, GLINT outperforms both SSL encoders and medical VLMs on classification, report generation, and segmentation. Code is available at https://github.com/deepnoid-ai/GLINT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jonggwon Park, Seongeun Lee, Junhyun Park, Hannah Yun, Hyunwoong Kim, Sohyun Jeong, Hyewon Kang, Byungmu Yoon, Kyoyun Choi
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/deepnoid-ai/GLINT](https://github.com/deepnoid-ai/GLINT)
- 阅读深度：metadata
