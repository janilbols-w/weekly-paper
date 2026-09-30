---
title: "MoRE: Scaling mixture of experts with hardware-aware low-rank routing"
description: "Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.36301) · [PDF](https://arxiv.org/pdf/2609.36301)

## 一句话摘要

Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts. In this regime, the standard linear router becomes a bottleneck: with $M$ experts and hidden dimension $h$, its per-token cost $\Theta(Mh)$ dominates the MoE layer once $M$ is large. We introduce MoRE (Mixture of Rank-reduced-routed Experts), which factorizes the router weight matrix at rank $r$ and reduces the routing cost to $O((h + M)r)$. We prove that rank logarithmic in $M$ suffices for routing expressivity when the number of active experts is fixed, and is necessary up to precision factors. We also prove that logarithmic rank preserves load balance in a Gaussian memorization model, and training on a synthetic phonebook task shows that low rank does not hurt memorization. At matched active FLOPs, the factorization allows a factor of $\Theta(h/r)$ more experts. To realize this gain in wall-clock time, we design a fused Triton kernel at inference that avoids expensive memory operations on HBM. Empirically, MoRE improves memorization on the phonebook task and performance on knowledge-intensive Q\&A benchmarks after pretraining, while matching reasoning ability. Code available at https://github.com/Matheart/MoRE_code.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Honam Wong, Surbhi Goel, Enric Boix-Adser\`a
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Matheart/MoRE_code](https://github.com/Matheart/MoRE_code)
- 阅读深度：metadata
