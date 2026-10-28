---
title: "DuplexTune: Coupled-State Replay for Memory-Efficient Mixture-of-Experts Adaptation"
description: "Sparse expert execution does not remove the stored states needed to adapt a mixture-of-experts language model."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.36009) · [PDF](https://arxiv.org/pdf/2610.36009)

## 一句话摘要

Sparse expert execution does not remove the stored states needed to adapt a mixture-of-experts language model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse expert execution does not remove the stored states needed to adapt a mixture-of-experts language model. We present DuplexTune, a framework for replaying coupled hidden states through pretrained attention and expert modules. Trainable width bridges connect two residual streams to the backbone. Bridge warm-up precedes backbone adaptation, with router weights kept frozen. We analyze the implicit state-recovery equation and identify the convergence and replay conditions needed for reconstruction. On Qwen1.5-MoE-A2.7B, the single-H800 evaluation reports 38.8 GB peak memory, versus 64.8 GB for supervised fine-tuning with checkpointing, and throughput of 25.1 versus 19.9 samples/s. DuplexTune achieves 67.2% MMLU, 75.6% GSM8K, and 7.69 MT-Bench, with a weaker multilingual score than the checkpointed baseline. The results characterize a configuration-dependent tradeoff among state storage, throughput, and adaptation quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Paul Raj, Simon Caldwell, Daniel Whitmore, Mutlu Mete
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
