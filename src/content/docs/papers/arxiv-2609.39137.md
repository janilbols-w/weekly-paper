---
title: "ID Balancing: Stable Training of Extremely Sparse MoE via PID-Based Load Control"
description: "Scaling Large Language Models (LLMs) via Mixture-of-Experts (MoE) enables massive parameter growth with nearly constant per-token computation."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.39137) · [PDF](https://arxiv.org/pdf/2609.39137)

## 一句话摘要

Scaling Large Language Models (LLMs) via Mixture-of-Experts (MoE) enables massive parameter growth with nearly constant per-token computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Scaling Large Language Models (LLMs) via Mixture-of-Experts (MoE) enables massive parameter growth with nearly constant per-token computation. However, further scaling the parameter count requires increasingly sparse routing, where expert load imbalance becomes more severe. This imbalance reduces parameter utilization and training efficiency, and can undermine training stability, becoming a bottleneck to reliable scaling. In this work, we unify two representative auxiliary-loss-free methods as incomplete Proportional-Integral-Derivative (PID) controllers: DeepSeek's loss-free method acts as a fixed-step integral controller, while Kimi K3's Quantile Balancing functions as a generalized proportional controller. Building on this control perspective, we propose ID Balancing, an Integral-Derivative controller. It scales its integral term with load error and activates its derivative term only when imbalance worsens, enabling stronger corrections for large or worsening errors and smaller updates near balance. Evaluated across Top-$10$, Top-$5$, and Top-$3$ routing over $768$ experts, ID Balancing reduces worst-case backbone MaxVio and training-average backbone MinVio by over $50\%$ and $12\%$, respectively, relative to the best baselines in the Top-$3$ setting. When the total parameter count increases from $18.9$B to $69.9$B (Top-$10$-of-$768$), ID Balancing's worst-case backbone MaxVio remains nearly unchanged and is approximately $89.6\%$ lower than that of the auxiliary-loss baseline. ID Balancing also maintains competitive language-modeling and downstream performance. The advantages of ID Balancing grow as sparsity increases, making it a promising solution for scaling larger, sparser MoE models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peng Jin, Zihan Qiu, Zekun Wang, Bo Zheng, Yang Xu, Tian Xie, Xiao Li, Huaqing Zhang, Haoran Lian, Rui Men, Dayiheng Liu
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
