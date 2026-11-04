---
title: "SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding"
description: "Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.02501) · [PDF](https://arxiv.org/pdf/2611.02501)

## 一句话摘要

Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass. However, it remains unclear whether their released systems (stock) attain the full speedup that parallel drafting permits. We identify three challenges. First, with one request, each step accepts few tokens but reads every target weight. Second, with batching, per-request verification work roughly halves the speedup over autoregressive (AR) decoding. Third, speculative decoding is deployment-specific, and no universal optimization fits every serving regime, drafter, target model and GPU. To address these challenges, we present SpecPilot, an autonomous agentic loop that discovers algorithms and systems optimizations for each deployment. In each round, a cost model locates the largest gaps between the current system and its ceiling. Parallel agents explore directions and integrate the successful ones. Token forcing checks every output token against stock to detect reward hacking. A structured memory carries validated mechanisms to new rounds and deployments. SpecPilot discovered a general lossless 12-bit weight format, tree verification for hybrid recurrent targets, two-level verification and three batching mechanisms. We evaluate it across four target models, three drafters, two GPU platforms and five benchmarks. Without training or quality loss, it raises the speedup over AR from stock's 4.46$\times$ to 10.87$\times$ with one request, and from 1.94$\times$ to 3.93$\times$ with batching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kunjun Li, Wenhao Chai, Yihao Liang, Yuezhou Hu, Shuyao Xu, Yi Pan, William X. Zheng, Kannan Ramchandran, Kurt Keutzer, Jiantao Jiao
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
