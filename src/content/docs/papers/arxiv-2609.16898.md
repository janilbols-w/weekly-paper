---
title: "OptiPrime: Optimizing Private Inference through Protocol-Hardware Co-design"
description: "Private deep neural network (DNN) inference based on hybrid homomorphic encryption (HE) and multi-party computation (MPC) can protect user data with a formal guarantee, but at the cost of significant latency overhead due to HE."
---

**评分：49/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.16898) · [PDF](https://arxiv.org/pdf/2609.16898)

## 一句话摘要

Private deep neural network (DNN) inference based on hybrid homomorphic encryption (HE) and multi-party computation (MPC) can protect user data with a formal guarantee, but at the cost of significant latency overhead due to HE.

## 为什么值得关注

待编辑增强。

## 摘要原文

Private deep neural network (DNN) inference based on hybrid homomorphic encryption (HE) and multi-party computation (MPC) can protect user data with a formal guarantee, but at the cost of significant latency overhead due to HE. Customized HE accelerators have been proposed and have achieved orders-of-magnitude speedup for individual HE operations. However, when directly applying a commercial HE accelerator to state-of-the-art HE-MPC frameworks, we observe only limited end-to-end performance gain. This is because HE-MPC frameworks often require wireless transmission of input and output ciphertexts for each HE operation, leading to a severe network communication bottleneck. To overcome this challenge, we introduce OptiPrime, a protocol-hardware co-optimization framework for efficient private DNN inference. OptiPrime features a novel HE protocol for convolutions that substantially reduces the number of transmitted output ciphertexts and mitigates the network communication bottleneck. Meanwhile, as the new protocol introduces complex computation for fewer output ciphertext, we observe new memory access challenges due to a high volume of weight plaintexts and intermediate ciphertexts. Hence, we further propose a lightweight compression system for the weight plaintexts, reducing memory traffic by 10 times, as well as a specialized dataflow to maximize on-chip data reuse of intermediate ciphertexts. Extensive experiments show that our framework outperforms the Cheetah baseline by at most 5.7 times on CPUs and 4.2 times with an accelerator.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiangrui Yu, Ye Yu, Si Chen, Chenqi Lin, Wenxuan Zeng, Junfeng Fan, Mingyu Gao, Meng Li
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
