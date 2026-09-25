---
title: "ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning"
description: "ZOCheck 面向零阶 LLM 微调，用 CPU 影子进程持续重放轻量级种子与标量日志，在不占用 GPU 关键路径的情况下生成并异步持久化一致恢复镜像。摘要报告其相对异步全状态 checkpoint 可将 checkpoint 开销最高降低 219.7 倍、平均恢复延迟降低 1.55 倍，并保持精确恢复。"
---

**评分：52/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.27189) · [PDF](https://arxiv.org/pdf/2609.27189)

## 一句话摘要

ZOCheck 面向零阶 LLM 微调，用 CPU 影子进程持续重放轻量级种子与标量日志，在不占用 GPU 关键路径的情况下生成并异步持久化一致恢复镜像。摘要报告其相对异步全状态 checkpoint 可将 checkpoint 开销最高降低 219.7 倍、平均恢复延迟降低 1.55 倍，并保持精确恢复。

## 为什么值得关注

它把零阶优化可重放的更新结构转化为低干扰容错机制，为显存受限微调补上 checkpoint 与故障恢复能力；基于故障率选择快照策略的成本模型也有助于基础设施侧做恢复成本权衡。

## 摘要原文

Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored. Unlike first-order training, ZO progress can be represented by lightweight seed-and-scalar step logs, yet naive log-only recovery still incurs replay cost that grows with training progress, and shortcut replay does not preserve the executed floating-point trajectory. We present ZOCheck, a fault-tolerant ZO training system that exploits this replayable structure through a CPU shadow process that continuously replays logged updates, materializes consistent recovery images off the GPU critical path, and persists them asynchronously. ZOCheck therefore combines non-blocking checkpointing during training with fast recovery from a near-current state. We also develop a cost model for choosing the snapshot policy under realistic failure rates. Experiments show that ZOCheck reduces checkpoint overhead by up to 219.7x and recovery latency by 1.55x on average compared with asynchronous full-state checkpointing, translating into up to 21.3x lower end-to-end wasted time across the evaluated failure rates, while preserving exact recovery behavior.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- quantitative claim detected
- no code link detected in metadata
- 限制：适用范围集中在可由种子与标量日志重放的零阶微调，不能直接外推到常规一阶训练。收益依赖故障率、CPU 重放速度和持久化环境，摘要未给出所有实验配置与资源开销细节。

## 元数据

- 作者：Minqiu Sun, Xin Huang, Luanzheng Guo, Nathan R. Tallent, Kento Sato, Dong Dai
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
