---
title: "A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM"
description: "Chain-of-Thought (CoT) improves the reasoning ability of Large Language Models (LLMs) but incurs substantial computation and context costs."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.07821) · [PDF](https://arxiv.org/pdf/2609.07821)

## 一句话摘要

Chain-of-Thought (CoT) improves the reasoning ability of Large Language Models (LLMs) but incurs substantial computation and context costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Chain-of-Thought (CoT) improves the reasoning ability of Large Language Models (LLMs) but incurs substantial computation and context costs. Existing methods either lose intermediate information through hard pruning or lack a principled criterion for continuous compression. We present A*-Thought-V2, a geometric dynamics of LLM guided framework that models CoT as a hidden-state trajectory and replaces hard deletion with an explicit-implicit interleaved latent architecture. After projecting question, step, and solution representations into a 3D PCA space, it measures alignment between each local transition and global question-to-solution direction. Aligned steps remain explicit text, whereas deviating steps are compressed into continuous latent tokens. Directional angles capture both local semantics and reasoning dynamics: small angles indicate direct execution and answer formation, while large angles more frequently involve checking, correction, and branch exploration; their temporal variation reveals exploration, convergence, and refinement stages. To train this architecture, we introduce stepwise embedding forcing, which pools each redundant step into a single latent embedding, and label forcing, which supervises that latent token with a soft multi-modal vocabulary distribution instead of a hard one-hot label. Experiments on Qwen3.5-9B and Qwen3.6-27B across six in-domain and out-of-domain benchmarks show that A*-Thought-V2 improves average accuracy by up to 2.6% while reducing response length by up to half, increasing Accuracy per Computation Unit by 2.29$\times$, and reducing preprocessing and training time by 94.6% and up to 80.3%, respectively. Representation analyses suggest that latent states form a compact region distinct from textual states, while higher entropy at latent-token positions reflects broader soft targets that encourage richer step-level feature learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xiaoang Xu, Siyuan Liu, Shuo Wang, Junlan Feng, Fanyu Meng, Zhu Zhang, Jixun Wang, Xiaorong Wang, Zihan Zhou, Xin Li, Chaojun Xiao, Yiming Zhang, Huijia Wu, Liuyu Xiang, Peipei Li, Zhaofeng He
- 发布：2026-09-07；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AI9Stars/AStar-Thought](https://github.com/AI9Stars/AStar-Thought)
- 阅读深度：metadata
