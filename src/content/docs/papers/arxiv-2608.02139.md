---
title: "Self-Improving Large Language Models via Progressive Experience Evolution"
description: "Large language models (LLMs) capable of self-improvement require not only effective policy optimization, but also a principled mechanism for transforming transient interaction experience into persistent model capabilities."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.02139) · [PDF](https://arxiv.org/pdf/2608.02139)

## 一句话摘要

Large language models (LLMs) capable of self-improvement require not only effective policy optimization, but also a principled mechanism for transforming transient interaction experience into persistent model capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) capable of self-improvement require not only effective policy optimization, but also a principled mechanism for transforming transient interaction experience into persistent model capabilities. Existing self-improvement paradigms remain fragmented: test-time methods can explicitly extract experience but cannot internalize it into model parameters, whereas training-time optimization methods can update model parameters but lack an explicit mechanism for accumulating transferable experience. Bridging these two paradigms requires a critical intermediate stage that remains underexplored, namely \emph{experience distillation}. To address this gap, we propose \textbf{SPEE} (\textbf{S}elf-\textbf{P}rogressive \textbf{E}xperience \textbf{E}volution), a unified post-training framework that sequentially performs explicit experience evolution followed by implicit policy optimization. During explicit experience evolution, SPEE reflects on trajectories collected from multiple interactions to extract, verify, and progressively evolve transferable experience, which is subsequently internalized into the policy through privilege-guided On-Policy Self-Distillation (OPSD). During implicit policy optimization, reward-driven reinforcement learning leverages these internalized priors to explore novel solution strategies. In the experience evolution stage, a continuously evolving global experience pool consolidates knowledge from both successful and failed trajectories, filters out low-utility experience, and mitigates post-hoc rationalization induced by individual trajectories. Experiments on five mathematical reasoning benchmarks demonstrate that SPEE consistently outperforms both test-time and training-time self-evolution baselines across three model scales. The source code is available at https://github.com/rrrsj/SPEE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Shijie Ren, Xiting Wang, Meng Li, Yujie Guo, Yunhang Yao, Ziheng Peng, Xunlong Wang, Yuetan Chen, Haoyang Zhou, Yunlong Liang, Fandong Meng
- 发布：2026-08-03；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/rrrsj/SPEE](https://github.com/rrrsj/SPEE)
- 阅读深度：metadata
