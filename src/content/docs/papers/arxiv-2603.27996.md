---
title: "From Independent to Correlated Diffusion: Generalized Generative Modeling with Probabilistic Computers"
description: "Diffusion models have emerged as a powerful framework for generative tasks in deep learning."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2603.27996) · [PDF](https://arxiv.org/pdf/2603.27996)

## 一句话摘要

Diffusion models have emerged as a powerful framework for generative tasks in deep learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion models have emerged as a powerful framework for generative tasks in deep learning. They decompose generative modeling into two computational primitives: deterministic neural-network evaluation and stochastic sampling. Current implementations usually place most computation in the neural network, but diffusion as a framework allows a broader range of choices for the stochastic transition kernel. Here, we generalize the stochastic sampling component by replacing independent noise injection with Markov chain Monte Carlo (MCMC) dynamics that incorporate known interaction structure. Standard independent diffusion is recovered as a special case when couplings are set to zero. By explicitly incorporating Ising couplings into the diffusion dynamics, the noising and denoising processes exploit spatial correlations representative of the target system. The resulting framework maps naturally onto probabilistic computers (p-computers) built from probabilistic bits (p-bits), which provide orders-of-magnitude advantages in sampling throughput and energy efficiency over GPUs. We demonstrate the approach on equilibrium states of the 2D ferromagnetic Ising model and the 3D Edwards-Anderson spin glass, showing that correlated diffusion produces samples in closer agreement with MCMC reference distributions than independent diffusion. More broadly, the framework shows that p-computers can enable new classes of diffusion algorithms that exploit structured probabilistic sampling for generative modeling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nihal Sanjay Singh, Mazdak Mohseni-Rajaee, Shaila Niazi, Kerem Y. Camsari
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
