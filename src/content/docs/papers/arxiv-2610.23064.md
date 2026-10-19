---
title: "BaGuaLu-2: Taming Dynamic Memory Fluctuation for Efficient MoE Model Training over 10,000 GPUs"
description: "Fine-grained Mixture-of-Experts (MoE) is the de facto architecture for scaling large language models."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.23064) · [PDF](https://arxiv.org/pdf/2610.23064)

## 一句话摘要

Fine-grained Mixture-of-Experts (MoE) is the de facto architecture for scaling large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-grained Mixture-of-Experts (MoE) is the de facto architecture for scaling large language models. However, dynamic expert load imbalance causes severe memory fluctuations that degrade training efficiency. Existing systems rely on static memory provisioning: they either over-provision, leaving GPU memory idle during normal execution, or under- provision, inviting out-of-memory crashes and costly manual rollbacks when load spikes occur. To address these challenges, we propose BaGuaLu-2, a large-scale MoE training system that eliminates this dilemma through flexible provisioning. By transforming memory allocation from a static, one-time tuning choice into a continuous and fine-grained control. BaGuaLu-2 grants exact activation memory on demand for each training batch. Furthermore, it offsets any dynamic management overhead through system optimizations. BaGuaLu-2 demonstrates exceptional scalability, training a model with 1040 billion parameters across 12,288 GPUs while sustaining over 2 EFlops at 35% MFU. Compared with state-of-the-art systems, BaGuaLu-2 delivers 1.14x and 1.13x average throughput improvements over Megatron-Kuai and AdaPipe, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mingshu Zhai, Minkun Guo, Hongrui Lian, Shuangyu Li, Qi Zhang, Chen Hu, Xiawei Du, Yuyang Jin, Zan Zong, Jidong Zhai
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
