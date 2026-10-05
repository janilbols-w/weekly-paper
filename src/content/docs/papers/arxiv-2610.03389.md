---
title: "From Patching to Pruning Visual Computation in Vision Language Models"
description: "Vision language models (VLMs) incur substantial inference cost because every visual token is processed by the attention and MLP projections of every decoder layer, even when token-specific visual computation is unnecessary at many depths."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.03389) · [PDF](https://arxiv.org/pdf/2610.03389)

## 一句话摘要

Vision language models (VLMs) incur substantial inference cost because every visual token is processed by the attention and MLP projections of every decoder layer, even when token-specific visual computation is unnecessary at many depths.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision language models (VLMs) incur substantial inference cost because every visual token is processed by the attention and MLP projections of every decoder layer, even when token-specific visual computation is unnecessary at many depths. We introduce Patch-to-Prune (P2P), inspired by Mechanistic Interpretability, a training-free framework that converts activation patching from a diagnostic tool into an inference-time computation bypass. P2P performs validation-guided forward and backward layer sweeps to identify decoder regions whose visual-token projection outputs can be replaced by fixed neutral proxy activation vectors within a user-specified accuracy tolerance. Unlike conventional token-pruning methods, P2P preserves the sequence length, token order, positional information, attention mask, and residual pathways, thereby pruning computation without removing tokens or modifying the pretrained model weights. We evaluate P2P on four VLMs from the Qwen2.5-VL and LLaVA families across seven multi-modal benchmarks using mutually disjoint calibration, validation, and test partitions. P2P at a 3% tolerance retains around 94% of dense accuracy while reducing FLOPs by 55%. Beyond these efficiency gains, our layer-wise analysis suggests that visual processing in VLMs is non-uniformly distributed across decoder depth: early and late layers often require little token-specific visual computation, whereas intermediate layers appear to perform most task-relevant visual integration, enabling later reasoning to rely largely on visual information already embedded in shared residual and textual representations. This makes P2P both an efficient inference framework and a causal lens into visual information processing in VLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rahul Chowdhury, Timothy A Rupprecht, Xuan Shen, Shaoyi Huang, Pu Zhao, Yanzhi Wang
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
