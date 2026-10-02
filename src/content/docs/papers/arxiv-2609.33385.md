---
title: "OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading"
description: "OLED-MoE 利用扩散式 LLM 相邻去噪迭代间的专家路由局部性，以 token 置信度预测并保留高复用专家，避免传统层间预取带来的额外传输；对未命中专家则用 CPU-GPU 协同执行补偿。摘要报告其相对现有卸载系统将 TPOT 改善 1.23 至 7.93 倍、专家缓存利用率提升 1.44 至 4.23 倍，并在仅使用 40% 专家 GPU 显存时将相对全驻留的 TPOT 增幅控制在 23%。"
---

**评分：57/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.33385) · [PDF](https://arxiv.org/pdf/2609.33385)

## 一句话摘要

OLED-MoE 利用扩散式 LLM 相邻去噪迭代间的专家路由局部性，以 token 置信度预测并保留高复用专家，避免传统层间预取带来的额外传输；对未命中专家则用 CPU-GPU 协同执行补偿。摘要报告其相对现有卸载系统将 TPOT 改善 1.23 至 7.93 倍、专家缓存利用率提升 1.44 至 4.23 倍，并在仅使用 40% 专家 GPU 显存时将相对全驻留的 TPOT 增幅控制在 23%。

## 为什么值得关注

它把 MoE 专家卸载策略从自回归解码的层间预取改写为适合 dLLM 迭代结构的跨迭代保留，为显存受限设备部署大规模 MoE 扩散模型提供了更贴合执行模式的缓存与计算协同方案。

## 摘要原文

Semi-autoregressive diffusion large language models (dLLMs) improve decoding parallelism through iterative block-wise denoising, but scaling them with mixture-of-experts (MoE) layers introduces a large expert parameter footprint that exceeds memory-constrained GPU capacity. Expert offloading is a natural remedy, yet existing MoE serving systems target autoregressive decoding and rely on intra-iteration layer-wise prefetching: while computing one layer, they predict and load experts for subsequent layers. Under dLLM inference, block-wise routing expands the active expert working set within each iteration, making such prefetches difficult to complete in time and costly when mispredicted. Consequently, existing prefetch-based solutions often degenerate into on-demand expert loading with high decoding latency. We propose OLED-MoE, an expert offloading system that shifts the optimization target from intra-iteration prefetching to inter-iteration expert retention. Its key insight is that adjacent denoising iterations exhibit strong expert routing overlap, and token confidence indicates which experts are likely to be reused. OLED-MoE uses confidence-guided inter-iteration prediction to retain high-value experts in GPU memory without introducing extra prefetch traffic. It further compensates unavoidable cache misses through CPU-GPU cooperative execution, jointly considering dynamic expert computation load and predicted future reuse. Across diverse dLLM workloads, OLED-MoE reduces time per output token (TPOT) by 1.23x-7.93x and improves expert cache utilization by 1.44x-4.23x over state-of-the-art offloading systems. Notably, OLED-MoE approaches full-residency performance while using only 40% of the expert GPU memory, incurring merely 23% higher TPOT despite a 60% reduction in expert memory footprint. OLED-MoE's source code is publicly available at https://github.com/flashserve/OLED-MoE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- quantitative claim detected
- code/artifact link detected
- 限制：方案依赖相邻去噪迭代具有稳定的专家复用局部性，路由变化较大的工作负载可能削弱预测价值。摘要未列出具体模型、硬件、互连和并发配置，CPU-GPU 协同的资源占用以及最高加速的适用范围仍需结合正文验证。

## 元数据

- 作者：Jingyuan Xiao, Jiayue Wang, Yitao Hu, Xinning Wang, Shi Chen, Ziqi Gong, Zhengchao Wang, Guotao Yang, Sheng Chen, Keqiu Li
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flashserve/OLED-MoE](https://github.com/flashserve/OLED-MoE)
- 阅读深度：abstract
