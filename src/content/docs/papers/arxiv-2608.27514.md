---
title: "Trajectory-Level Speculative Decoding for Diffusion Language Models"
description: "该方法把扩散语言模型的推测单元从单个 token 扩展为带位置与解掩码顺序的去噪轨迹，通过按置信度分层的树搜索起草轨迹，再用双向注意力掩码做分块并行验证，并利用跨块前瞻。摘要报告，其在 Fast-dLLM 双缓存基础上减少 30%–40% 去噪迭代，将每步 token 数从 2.6 提至 4.3。"
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.27514) · [PDF](https://arxiv.org/pdf/2608.27514)

## 一句话摘要

该方法把扩散语言模型的推测单元从单个 token 扩展为带位置与解掩码顺序的去噪轨迹，通过按置信度分层的树搜索起草轨迹，再用双向注意力掩码做分块并行验证，并利用跨块前瞻。摘要报告，其在 Fast-dLLM 双缓存基础上减少 30%–40% 去噪迭代，将每步 token 数从 2.6 提至 4.3。

## 为什么值得关注

扩散语言模型在低置信度时退化为单 token 更新，削弱并行生成优势。轨迹级推测针对这一结构性瓶颈设计，并给出精确性条件，使推测解码从自回归模型扩展到双向去噪过程。

## 摘要原文

Diffusion-based language models (dLLMs) enable parallel token generation through iterative denoising, but existing decoding strategies collapse to single-token generation under low confidence, severely limiting throughput. Unlike autoregressive models where speculative decoding operates on token sequences in a fixed left-to-right order, dLLMs require speculating over denoising trajectories-sequences of multi-token updates with explicit positions and unmasking orders. We develop a trajectory-level speculative framework that constructs draft denoising trajectories via confidence-stratified tree exploration and verifies them through blockwise parallel evaluation with bidirectional attention masking. Our method further introduces inter-block speculation, exploiting diffusion models' bidirectional structure to perform cross-block lookahead. We formally characterize when this approach is exact and identify trajectory drift as the fundamental cost of increased parallelism. Building on Fast-dLLM's dual-cache infrastructure, our framework reduces denoising iterations by 30-40% and increases tokens-per-step from 2.6 to 4.3, achieving 7-14x speedup over vanilla dLLMs and 1.3x over Fast-dLLM with less than 1% accuracy change across reasoning and code benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata
- 限制：摘要所报 7–14 倍加速是相对原始 dLLM，较 Fast-dLLM 为 1.3 倍，基线差异需区分；方案依赖 Fast-dLLM 的双缓存，且并行度增加会带来轨迹漂移。摘要未说明模型、硬件、序列长度和实现开放情况。

## 元数据

- 作者：Tianxiang Pan, Baitao Gong, Mo Guang, Hongwei Yong, Tianpeng Jiang, Yaqian Li, Zheng Cao, Kaiwen Long
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
