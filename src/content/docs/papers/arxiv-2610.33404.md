---
title: "COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies"
description: "As LLMs scale, mixture-of-experts (MoE) architectures increase model capacity while keeping per-token computation manageable through sparse expert activation."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.33404) · [PDF](https://arxiv.org/pdf/2610.33404)

## 一句话摘要

As LLMs scale, mixture-of-experts (MoE) architectures increase model capacity while keeping per-token computation manageable through sparse expert activation.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLMs scale, mixture-of-experts (MoE) architectures increase model capacity while keeping per-token computation manageable through sparse expert activation. This sparsity also enables memory-efficient deployment by retaining most expert weights in CPU memory and transferring or executing only the routed experts on demand. Existing MoE offloading systems typically target specific model-platform configurations, yet differences in model sparsity, CPU and GPU throughput, VRAM capacity, and host-device bandwidth can change the policy ranking. Because implementing and exhaustively evaluating all candidate policies incurs substantial engineering cost, efficiently selecting the best-performing policy for each model-platform configuration remains a key challenge for practical MoE offloading. We present COPE (Composable Offloading Policy Emulator), which selects the best-performing MoE offloading policy for a target model-platform configuration before runtime integration. COPE comprises two components. Its Policy Matrix factors the design space into two independent axes, expert residency and MoE execution strategy, enabling mechanism reuse across candidate policies and exposing four new candidates. Its Virtual Heterogeneous Machine profiles combined-operator schedules on the target platform and combines these measurements with offline routing traces to estimate candidate performance. Compared with the evaluated baselines, COPE improves fastest-policy selection accuracy by 24%-100% and reduces performance-prediction error by $1.7\times$ to $6.8\times$. By identifying the preferred policy before integration, COPE further reduces policy-specific implementation effort by up to 74%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hanming Zhang, Erhu Feng
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
