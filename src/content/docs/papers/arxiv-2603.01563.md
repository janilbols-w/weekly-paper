---
title: "Efficient Token-Level Policy Optimization for Masked Diffusion Models via Velocity Alignment"
description: "Reinforcement Learning with Verifiable Rewards (RLVR) successfully aligns autoregressive models in rigorous domains like mathematical reasoning and code generation."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2603.01563) · [PDF](https://arxiv.org/pdf/2603.01563)

## 一句话摘要

Reinforcement Learning with Verifiable Rewards (RLVR) successfully aligns autoregressive models in rigorous domains like mathematical reasoning and code generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning with Verifiable Rewards (RLVR) successfully aligns autoregressive models in rigorous domains like mathematical reasoning and code generation. However, applying RLVR to Diffusion Large Language Models (dLLMs) is hindered by intractable sequence-level likelihoods, forcing existing methods to rely on unstable, high-variance approximations. We propose Sequence Likelihood-Free Policy Optimization (LFPO), an efficient framework that circumvents this bottleneck by formulating policy alignment as discrete velocity alignment. Inspired by continuous flow matching, LFPO eschews trajectory-level estimation and directly optimizes denoising logits via contrastive token-level updates, providing a stable, low-variance surrogate. Furthermore, predicting terminal solutions from intermediate states implicitly straightens the generation trajectory, enabling high-quality sampling with significantly fewer denoising iterations. Extensive experiments on reasoning and coding benchmarks demonstrate that LFPO matches or exceeds the accuracy of likelihood-based baselines while substantially accelerating inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chenxing Wei, Jiazhen Kang, Hong Wang, Jianqing Zhang, Hao Jiang, Xiaolong Xu, Ningyuan Sun, Ying He, F. Richard Yu, Yao Shu, Bo Jiang
- 发布：2026-09-30；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
