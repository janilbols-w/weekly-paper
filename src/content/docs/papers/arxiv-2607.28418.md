---
title: "WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning"
description: "Pruning is a promising approach for improving the efficiency of large language models (LLMs)."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.28418) · [PDF](https://arxiv.org/pdf/2607.28418)

## 一句话摘要

Pruning is a promising approach for improving the efficiency of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Pruning is a promising approach for improving the efficiency of large language models (LLMs). Static structured pruning is hardware-friendly, but its input-agnostic computation allocation often degrades model quality at high sparsity. Dynamic pruning adapts computation to individual tokens, but coarse-grained layer-level routing limits allocation flexibility, and finer-grained decisions introduce irregular execution that can offset computational savings. To address these challenges, we present WIDE, the first end-to-end differentiable framework that combines token-wise structured dynamic width pruning with GPU kernel co-design for both prefill and decoding. WIDE uses differentiable routers to select GQA-aligned query-head groups and GPU-tile-aligned FFN-channel groups for each token. To execute these decisions efficiently, it reorders routing masks to cluster active tokens within each group, enabling hardware-agnostic block-level skipping and architecture-aware skipping of inactive loads and tensor-core operations. Experiments on the Llama3 and Qwen3 families demonstrate improved quality retention over representative static and dynamic pruning methods. At 50\% target routing sparsity, WIDE improves Llama3.1-8B average zero-shot accuracy by up to 20.26 points over the strongest dynamic-depth baseline under calibration-only settings, while retaining 97.6\%/88.2\% of dense Qwen3-14B likelihood/generation performance after LoRA tuning. Separate latency benchmarks demonstrate end-to-end speedups of up to $1.68\times$ for prefill and $1.55\times$ for decoding over the dense baseline. These results demonstrate that pruning--kernel co-design pushes the frontier of token-wise dynamic structured pruning, combining improved quality retention with practical acceleration across both prefill and decoding. Our code is avaliable at \url{https://github.com/EIT-NLP/LLM-Pruning/tree/main/WIDE}.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Haozhe Hu, Hao Wu, Peiran Yin, Chao Han, Yunpu Ma, Xiaoyu Shen
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EIT-NLP/LLM-Pruning/tree/main/WIDE}](https://github.com/EIT-NLP/LLM-Pruning/tree/main/WIDE})
- 阅读深度：metadata
