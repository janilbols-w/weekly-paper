---
title: "CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs"
description: "Despite growing interest in on-device LLM deployment, large-scale Mixture-of-Experts (MoE) models remain impractical on resource-constrained devices, as sparse expert activation still requires all expert weights to be memory-resident."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2611.20119) · [PDF](https://arxiv.org/pdf/2611.20119)

## 一句话摘要

Despite growing interest in on-device LLM deployment, large-scale Mixture-of-Experts (MoE) models remain impractical on resource-constrained devices, as sparse expert activation still requires all expert weights to be memory-resident.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite growing interest in on-device LLM deployment, large-scale Mixture-of-Experts (MoE) models remain impractical on resource-constrained devices, as sparse expert activation still requires all expert weights to be memory-resident. To address this, we identify three key observations for on-device MoE inference: (a) cache hit rates are fundamentally bounded even under Belady's optimal policy; (b) these bounds are insufficient for low-latency on-device inference; and (c) prior cache-aware routing based on binary cache presence can induce routing instability. Based on these insights, we propose CECAR (Cache & Expert Co-Aware Routing), a MoE inference system that jointly considers expert routing and cache management. Unlike prior cache-aware routing methods, CECAR uses an ML-based cache policy to predict the expected reuse distance of each expert and prioritizes routing and execution toward experts with smaller predicted reuse distances. On the Qwen3-30B-A3B model, CECAR achieves 12.5 tokens/s on a consumer-grade GPU with only 16 GB of VRAM, where non-resident experts are fetched from SSD, delivering a 4.5x speedup over conventional MoE inference and exceeding the decode speed of baselines that keep the entire model fully resident in DRAM. Code is available at https://github.com/hoonki2002/CECAR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing, moe inference
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Byeongju Kim, Hoonki Lee, Byungjun Kim, Inyul Ra, Yongjin Kim, Yongseong Lee, Sangyeob Kim
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/hoonki2002/CECAR](https://github.com/hoonki2002/CECAR)
- 阅读深度：metadata
