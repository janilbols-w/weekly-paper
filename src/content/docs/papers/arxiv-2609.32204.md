---
title: "DegreeSpar: Structured Degree Sparsity for Efficient Secure Transformer Inference"
description: "Secure Transformer inference protects sensitive inputs but incurs substantial cryptographic overhead, with nonlinear operations such as Softmax and GeLU becoming major bottlenecks."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32204) · [PDF](https://arxiv.org/pdf/2609.32204)

## 一句话摘要

Secure Transformer inference protects sensitive inputs but incurs substantial cryptographic overhead, with nonlinear operations such as Softmax and GeLU becoming major bottlenecks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Secure Transformer inference protects sensitive inputs but incurs substantial cryptographic overhead, with nonlinear operations such as Softmax and GeLU becoming major bottlenecks. Existing compression methods reduce nonlinear complexity, sequence-dependent computation, or model structure through separately defined compression variables. Under aggressive compression, however, these independently optimized perturbations can accumulate: at a matched compression level, stacking representative approximation, token-pruning, and model-pruning methods reduces ViT-S accuracy from 80.20% to 76.41%. We introduce DegreeSpar, which formulates secure Transformer compression as structured sparsification over nonlinear polynomial degrees. Polynomial degree directly controls the cost of secure nonlinear evaluation, while computation-aligned zero-degree structures expose token-level and model-dimension computation as removable within the same optimization space. DegreeSpar further incorporates approximation-aware training for low-degree Softmax and GeLU, enabling aggressive degree reduction and creating the optimization headroom required for structured computation removal. Across vision and language Transformers, DegreeSpar consistently improves the accuracy-latency trade-off across model scales, tasks, and sequence lengths, achieving speedups from 2.29x to 6.63x over the corresponding baselines. Under the same network setting, DegreeSpar achieves 92.68% accuracy on BERT/SST-2 in 110.55 s, compared with 92.66% in 167.26 s for CipherPrune, the closest prior hybrid secure-inference approach. These results establish structured polynomial degree as an effective shared optimization space for secure Transformer compression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yifei Cai, Zhuoran Li, Xiaozuo Shen, Hongyi Wu, Chunsheng Xin
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
