---
title: "COBALT: Contextual Bandit Learning with Offline Trajectories for Multi-Turn Code Generation"
description: "Training large language models (LLMs) for multi-turn code generation typically relies on online reinforcement learning (RL), in which models learn from repeatedly generated online rollouts."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.03806) · [PDF](https://arxiv.org/pdf/2602.03806)

## 一句话摘要

Training large language models (LLMs) for multi-turn code generation typically relies on online reinforcement learning (RL), in which models learn from repeatedly generated online rollouts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large language models (LLMs) for multi-turn code generation typically relies on online reinforcement learning (RL), in which models learn from repeatedly generated online rollouts. Although effective, online RL can be costly and unstable. In this paper, we present contextual bandit learning with offline trajectories (COBALT), a simple method that reuses offline multi-turn trajectories to efficiently train LLMs for multi-turn code generation. Building on the observation that multi-turn code generation is a one-step recoverable Markov decision process, COBALT first collects code generation trajectories using a reference LLM and divides them into partial trajectories. Then, during online bandit learning, the LLM is trained to complete each partial trajectory through single-step code generation. On LiveCodeBench, COBALT substantially improves R1-Distill 8B and Qwen3 8B by up to 9.0 and 6.2 absolute Pass@1 points and matches the performance of two multi-turn online RL baselines using GRPO and VeRPO. We also perform a perturbation-based analysis of in-context reward hacking and show that Cobalt can improve robustness to misleading execution feedback. Overall, our results demonstrate that Cobalt is a promising solution for multi-turn code generation. Our code and data are available at https://github.com/OSU-NLP-Group/cobalt.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ziru Chen, Dongdong Chen, Ruinan Jin, Yingbin Liang, Yujia Xie, Huan Sun
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/OSU-NLP-Group/cobalt](https://github.com/OSU-NLP-Group/cobalt)
- 阅读深度：metadata
