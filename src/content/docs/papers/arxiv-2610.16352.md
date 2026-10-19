---
title: "LoongSage: A Production-Grade, High-Efficiency Agentic RL Framework for Frontier LLMs with Validated Recipes"
description: "Reinforcement learning (RL) has emerged as a critical phase in the post-training pipeline of large language models (LLMs)."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.16352) · [PDF](https://arxiv.org/pdf/2610.16352)

## 一句话摘要

Reinforcement learning (RL) has emerged as a critical phase in the post-training pipeline of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) has emerged as a critical phase in the post-training pipeline of large language models (LLMs). As the frontier of LLM capabilities shifts from static reasoning to agentic tasks--characterized by external tool invocation, multi-turn interactions, and long-horizon decision-making--existing mainstream RL frameworks have grown increasingly unwieldy, raising the overhead of adoption, usage, and debugging. To address these challenges, we present LoongSage, an agent-native, fully asynchronous RL framework with a lightweight core of roughly 14K lines of code. Built upon Megatron for distributed training and SGLang for high-throughput inference, LoongSage centralizes orchestration within a single controller process and encapsulates all GPU-resident components as Ray actors. It introduces AgentFlow, a unified execution paradigm that orchestrates both white-box and black-box agents. For asynchronous execution, it integrates sliding-window strategies that bound trajectory staleness, and employs TransferMesh, a topology-aware synchronization mechanism that routes weights after each step over the fastest transport available to each receiver. Beyond agentic RL, LoongSage incorporates a memory-efficient Teacher Manager that decouples the scaling of teacher models from GPU memory constraints, natively supporting Multi-Teacher On-Policy Distillation. Extensive evaluations across four complete training runs, spanning complex reinforcement learning and multi-teacher distillation, demonstrate that task rewards improve steadily while the train-inference gap is kept under continuous control, and the fully asynchronous pipeline removes synchronous idle bubbles, sustaining hardware utilization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：LoonSage Team, Bowei Song, Caiwei Zhao, Chuwen Liu, Dechuang Gu, Dong Fang, Feiyu Xie, Huaiyu Li, Hui Zhang, Jian Tian, Jian Wang, Jie Zhao, Liguang Li, Maoyun Wang, Meiyan Yang, Minghan Zhu, Pai Liu, Pandeng Yao, Renbao Tian, Ru Yang, Shuai Jia, Shuai Tan, Shuailong Li, Shuliang Li, Teng Jin, Tianze Yang, Wenbo Cui, Wenjing Bai, Wenkang Wu, Xiaowei Jiang, Xiaoyi Dong, Yanpeng Wang, Yanwen Wang, Yaohui Ma, Yawen Wang, Yihang Zhang, Yingjie Yan, Zhanbiao Lian, Zhenyu Lu, Zhida Hu, Zhihui Hao, Zhihui Hu, Zhiwen Xiao, Zhiyi Gao, Zhongwei Qi, Zhuangzhuang Wu, Ziqian Liu, Ziyue Zheng
- 发布：2026-10-12；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
