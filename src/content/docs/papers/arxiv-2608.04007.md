---
title: "TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning"
description: "Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.04007) · [PDF](https://arxiv.org/pdf/2608.04007)

## 一句话摘要

Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions. However, existing reinforcement learning methods often rely on trajectory-level supervision, limiting fine-grained credit assignment in long-horizon TIR scenarios. On-policy self-distillation offers denser signals through teacher branches with privileged context, but existing approaches typically derive such context from ground-truth answers or retrieved skills, which may not reflect the states actually visited by the agent. Moreover, token-level supervision fails to capture the turn-level structure of tool interactions. To address this, we propose TurnSight, a turn-level hindsight self-distillation framework that derives supervision directly from execution-conditioned hindsight. It then constructs multiple hindsight views with different lookahead horizons and selects reliable supervision through cross-horizon directional agreement. Finally, the selected hindsight signal is normalized across sibling rollouts and used to adaptively modulate RL advantages while preserving their original optimization direction. Extensive experiments on three benchmarks demonstrate the effectiveness of TurnSight. Our codes are available at https://github.com/quchangle1/TurnSight.

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

- 作者：Changle Qu, Sunhao Dai, Hengyi Cai, Yuqi Zhou, Xinran Chen, Simon, Jun Xu
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/quchangle1/TurnSight](https://github.com/quchangle1/TurnSight)
- 阅读深度：metadata
