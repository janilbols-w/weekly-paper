---
title: "LitSeg: Narrative-Aware Document Segmentation for Literary RAG"
description: "Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external knowledge, particularly for long-tail domains such as literary works."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.27156) · [PDF](https://arxiv.org/pdf/2605.27156)

## 一句话摘要

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external knowledge, particularly for long-tail domains such as literary works.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external knowledge, particularly for long-tail domains such as literary works. However, the critical step of document segmentation in RAG remains largely underexplored. Existing strategies typically either ignore semantics or overlook the complicated narrative structures of literary works, often resulting in chunks with fragmented plots and unclear references that hinder retrieval and generation performance. To address this, we propose LitSeg, a novel narrative-theory-guided segmentation framework. By employing multi-stage prompting, LitSeg explicitly extracts valid events, clarifies narrative structures, and locates turning points to inform segmentation. To alleviate the computational overhead of multi-stage inference with large-scale models, we further introduce LitSeg-Lite, a lightweight single-pass chunker fine-tuned on LitSeg-generated data via a two-stage training strategy, distilling the complex process into a single inference pass. Extensive experiments demonstrate that compared to baselines, our methods yield high-quality text chunks that are narratologically coherent and self-contained. This improved segmentation quality enhances retrieval accuracy and context relevance, and boosts downstream QA performance. Ablation studies validate the efficacy of narratological guidance and data distillation, and efficiency analysis shows that LitSeg-Lite matches the teacher at a substantially lower inference cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruikang Zhang, Zhanni Chen, Yiqiao Cai, Qi Su
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
