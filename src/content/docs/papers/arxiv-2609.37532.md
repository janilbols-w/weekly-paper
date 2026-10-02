---
title: "DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification"
description: "Growing large language model applications demand efficient inference."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.37532) · [PDF](https://arxiv.org/pdf/2609.37532)

## 一句话摘要

Growing large language model applications demand efficient inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Growing large language model applications demand efficient inference. At high concurrency, block-diffusion speculative decoding suffers from verification padding, rejected candidates, and incompatibility between variable prefixes and fixed-shape graphs. Uniform truncation sacrifices acceptable tokens. We present DScale, preserving drafter architecture, weights, and full draft length. A separate 112K-parameter predictor requires neither confidence calibration nor hardware speed-curve preparation. Path-aware tiles reduce padding. Dynamic verify-length (DVL) allocation packs scored prefixes into half the native verification capacity. Fixed-address workspaces propagate changing boundaries through verification and acceptance while reusing captured graphs. On A100-40GB with tensor parallelism 1, Qwen3-8B and Qwen3-4B cover four datasets and concurrency 8-32, reusing each target's frozen predictor. Geometric-mean throughput gains across these configurations are respectively 43.9% and 48.8% over DFlash, 22.2% and 37.7% over DSpark, and 24.4% and 32.0% over Domino, with lower request latency. Cumulative ablations show that adding the three mechanisms successively increases geometric-mean throughput, while budget adjustment improves accepted-token retention. GPU profiling shows that complete decode-step time on GSM8K decreases by 30.8-52.5% relative to DFlash

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rongjian Chen, Minxian Xu, Zhengxin Fang, Kejiang Ye, Chengzhong Xu
- 发布：2026-09-29；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
