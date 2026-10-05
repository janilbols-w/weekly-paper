---
title: "All Work And No Play Makes Jack a Dull Boy: Understanding and Preventing Catastrophic Strategy Collapse in RLVR"
description: "During post-training of large language models (LLMs) with Reinforcement Learning with Verifiable Rewards (RLVR), GRPO-style algorithms can exhibit severe late-stage collapse."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02835) · [PDF](https://arxiv.org/pdf/2610.02835)

## 一句话摘要

During post-training of large language models (LLMs) with Reinforcement Learning with Verifiable Rewards (RLVR), GRPO-style algorithms can exhibit severe late-stage collapse.

## 为什么值得关注

待编辑增强。

## 摘要原文

During post-training of large language models (LLMs) with Reinforcement Learning with Verifiable Rewards (RLVR), GRPO-style algorithms can exhibit severe late-stage collapse. Prompt-based probing reveals that this is not benign strategic pruning, but a harmful contraction of effective strategy capacity that makes distinct reasoning strategies increasingly inaccessible. To characterize this phenomenon, we define strategies through trajectory-level policy-update interactions and develop a unified theoretical framework combining optimization dynamics and information theory. We prove that major RLVR objectives progressively concentrate probability mass onto a single strategy, while sustaining nontrivial task accuracy requires a minimum strategy capacity. The conflict between these two results provides a mechanistic explanation for catastrophic collapse. We further derive the {Mirrored Entanglement Index (MEI)} as a lightweight online warning signal. To prevent collapse, we propose \textbf{Mesh Learning}, which exposes multiple reasoning strategies and prevents any single strategy from dominating optimization. Across AIME26, AIME25, MATH-500, GPQA, and LiveCodeBench, Mesh Learning consistently outperforms strong baselines across Qwen and Phi model families, with gains of up to 13.4 pp and 11.5 pp, respectively. These results establish strategy preservation as a key principle for stable RLVR. Code is available at https://github.com/Ayanami-0123/Open-Mesh-Learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Qiyuan Huang, Tianshi Xu, Meng Li
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Ayanami-0123/Open-Mesh-Learning](https://github.com/Ayanami-0123/Open-Mesh-Learning)
- 阅读深度：metadata
