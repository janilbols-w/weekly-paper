---
title: "TS-DP: Reinforcement Speculative Decoding For Temporal Adaptive Diffusion Policy Acceleration"
description: "Diffusion Policy (DP) excels in embodied control but suffers from high inference latency and computational cost due to multiple iterative denoising steps."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2512.15773) · [PDF](https://arxiv.org/pdf/2512.15773)

## 一句话摘要

Diffusion Policy (DP) excels in embodied control but suffers from high inference latency and computational cost due to multiple iterative denoising steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Policy (DP) excels in embodied control but suffers from high inference latency and computational cost due to multiple iterative denoising steps. Existing diffusion model (DMs) acceleration methods improve inference speed by reducing computational overhead, as DMs for image generation are computation-bound. In this work, we reveal that DP are I/O bound, and thus propose using speculative decoding, a parallel computing framework, to accelerate DP for the first time. However, it is non-trivial to address the following challenges: (1) How to preserve the denoising quality of the base model at reduced computational cost under time-varying task difficulty in embodied settings; and (2) How to dynamically allocate computation according to task difficulty in such environments. Therefore, we propose Temporal-aware Reinforcement-based Speculative Diffusion Policy (TS-DP), the first framework that enables speculative decoding for DP with temporal adaptivity. First, to handle dynamic environments where task difficulty varies over time, we distill a Transformer-based drafter to imitate the base model and replace its costly denoising calls. Second, an RL-based scheduler further adapts to the time-varying task difficulty by adjusting speculative parameters to maintain accuracy while improving efficiency. Extensive experiments show that TS-DP achieves up to a 4.17x NFE reduction and a 3.2x wall-clock speedup with a draft acceptance rate of over 85% in simulation. Real-world experiments further demonstrate a 3.8x NFE reduction while improving success rates on real-time tasks (e.g., a 23% gain on the conveyor-belt task), reaching an inference frequency of 26 Hz and enabling real-time control while maintaining comparable task performance. The code is available at https://github.com/ChildTang/TS-DP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ye Li, Jiahe Feng, Yuan Meng, Kangye Ji, Chen Tang, Jiajun Fan, Xinwan Wen, Jiawei Li, Wenwu Zhu, Shu-Tao Xia, Xin Wang, Zhi Wang
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ChildTang/TS-DP](https://github.com/ChildTang/TS-DP)
- 阅读深度：metadata
