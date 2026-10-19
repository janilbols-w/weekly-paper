---
title: "Noise-shaped Sampling and Annealing for Scalable On-the-edge Training of Binary and Ternary AI Models"
description: "The training loss of binary and ternary neural networks, expanded as a multilinear polynomial over the discrete weights, is structurally equivalent to the energy of a hierarchical high-order Ising model."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.22621) · [PDF](https://arxiv.org/pdf/2610.22621)

## 一句话摘要

The training loss of binary and ternary neural networks, expanded as a multilinear polynomial over the discrete weights, is structurally equivalent to the energy of a hierarchical high-order Ising model.

## 为什么值得关注

待编辑增强。

## 摘要原文

The training loss of binary and ternary neural networks, expanded as a multilinear polynomial over the discrete weights, is structurally equivalent to the energy of a hierarchical high-order Ising model. We exploit this equivalence to apply Ising solvers to discrete-weight network training, while accounting for a fundamental difference in objectives: an Ising solver seeks the ground state of a fixed energy function, whereas training seeks solutions that generalize to unseen data. Our key contribution is $\Sigma\Delta$-Sampler, an optimizer that reconciles these objectives by embedding a stochastic sampling-and-annealing step as a noisy quantizer inside a first-order $\Sigma\Delta$ noise-shaping loop. The loop pushes noise from weight quantization, high-order frustration, and mini-batch sampling out of the low-frequency adaptation band, so that discrete weight updates follow the smooth descent trajectories embedded in the rugged loss landscape. We validate the framework on a planted quadratic unconstrained binary optimization (QUBO) benchmark with a known minimizer; on CIFAR-10, where a $13$M-parameter ternary model comes within $1\%$ of full-precision accuracy; on ImageNet-1k, where a ternary ResNet-18 comes within $0.4\%$ Top-5 accuracy of a ternary baseline; on class-incremental continual learning, where prior-task accuracy is preserved; and on MatMul-free language models up to $2.7$B parameters, where it outperforms a straight-through-estimator baseline under matched continued pre-training. Compared with standard quantization-aware training, $\Sigma\Delta$-Sampler reduces the training memory footprint by over $50\%$, delivers an order-of-magnitude speed-up, and reduces weight-update memory traffic by four orders of magnitude, making it attractive for on-device training and fine-tuning of large binary and ternary models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zihao Chen, Zhili Xiao, Rui-Jie Zhu, Yipeng Wang, Jason Eshraghian, Shantanu Chakrabartty
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
