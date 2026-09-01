---
title: "Learning-Theoretic Foundation for General Coded Computing: The Straggler Setting"
description: "Coded computing has emerged as a powerful paradigm for mitigating the impact of straggling workers in distributed computing systems."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2608.28910) · [PDF](https://arxiv.org/pdf/2608.28910)

## 一句话摘要

Coded computing has emerged as a powerful paradigm for mitigating the impact of straggling workers in distributed computing systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Coded computing has emerged as a powerful paradigm for mitigating the impact of straggling workers in distributed computing systems. However, existing coded-computing schemes are predominantly designed for the exact recovery of highly structured computations, such as polynomial evaluation and matrix multiplication, and typically rely on strict recovery thresholds. These assumptions significantly limit their applicability to modern machine-learning workloads, particularly deep neural networks (DNNs), whose computations generally lack rigid algebraic structure and, in many applications, require only accurate approximations rather than exact recovery. To address this gap, we revisit coded computing from a learning-theoretic perspective and introduce General Coded Computing (GCC). Rather than adopting existing algebraic tools, GCC formulates coded computing through a natural end-to-end mean-squared error loss that directly measures the discrepancy between the desired computations and their recovered estimates. By deriving suitable upper bounds and restricting the encoder and decoder to a reproducing kernel Hilbert space (RKHS) with mild smoothness constraints, we show that both the encoder and decoder admit specific representations as linear combinations of RKHS kernel functions. This representation allows the corresponding coefficients to be computed efficiently. Moreover, this framework enables us to establish theoretical performance guarantees for GCC under two complementary straggler regimes. In the worst-case setting with $N$ worker nodes, and at most $S$ stragglers, we show that the end-to-end loss decays at least at rate $O(S^3N^{-3})$ for standard configurations. We then study a probabilistic setting in which each worker independently straggles with probability $p$. We prove that the expected loss can still converge at rate $O(\log_{1/p}^3(N)N^{-3})$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: straggler
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Parsa Moradi, Behrooz Tahmasebi, Mohammad Ali Maddah-Ali
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
