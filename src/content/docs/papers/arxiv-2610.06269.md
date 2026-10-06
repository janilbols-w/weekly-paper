---
title: "Evolving in Thought Space: Training a Small Model at Test Time Unlocks Better Discoveries"
description: "Open-ended scientific discovery often requires repeatedly proposing and evaluating candidate solutions."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.06269) · [PDF](https://arxiv.org/pdf/2610.06269)

## 一句话摘要

Open-ended scientific discovery often requires repeatedly proposing and evaluating candidate solutions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Open-ended scientific discovery often requires repeatedly proposing and evaluating candidate solutions. LLM-based systems can support this process by generating and refining executable solutions from verifier feedback. Methods such as TTT-Discover use test-time training (TTT) to update the solution-generating LLM from verifier feedback, adapting its generation policy to improve subsequent proposals on the target problem. However, this becomes expensive when reliable execution requires a large model, since training must maintain gradients, optimizer states, and policy statistics while repeatedly generating long, structured outputs. It also complicates credit assignment: outcome-level verifier feedback must jointly evaluate the high-level strategy and its low-level implementation. In this work, we introduce Guidance-TTT, which separates these roles. A compact guidance model is trained at test time to propose high-level strategic changes, while a frozen execution model implements them as complete executable solutions. At each step, the system selects a promising previously discovered solution, proposes a change, executes and verifies it, and updates only the guidance model using an adaptive group-relative RL objective. This concentrates test-time learning on short strategic decisions while retaining the implementation capability of a substantially stronger model without adapting it. Without web access, Guidance-TTT produces strong solutions across four distinct domains: combinatorial optimization (Polyomino Packing), heuristic programming (AHC058), machine learning (Lasso), and GPU kernel optimization (TriMul). Across these tasks, it outperforms the best solutions reported in prior work while remaining competitive with state-of-the-art results on public online leaderboards. Code is available at https://github.com/Human-Agent-Society/reef/tree/guidance-ttt-support.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chonghe Jiang, Ao Qu, Siyuan Liu, Ruoyun Ma, Zijian Zhou, Dingyi Zhuang, Bo Liu, Han Zheng, Hanfei Yu, Baichuan Mo, Jinhua Zhao, Paul Pu Liang
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Human-Agent-Society/reef/tree/guidance-ttt-support](https://github.com/Human-Agent-Society/reef/tree/guidance-ttt-support)
- 阅读深度：metadata
