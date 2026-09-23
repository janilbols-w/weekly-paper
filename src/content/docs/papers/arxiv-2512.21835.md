---
title: "LOIP:Collaborative Lossless LLM Inference Serving with Offloading-based Pipeline Parallelism on Edge Devices"
description: "Providing lossless inference services of LLMs on edge devices remains challenging, especially given the extremely tight memory budgets."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2512.21835) · [PDF](https://arxiv.org/pdf/2512.21835)

## 一句话摘要

Providing lossless inference services of LLMs on edge devices remains challenging, especially given the extremely tight memory budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Providing lossless inference services of LLMs on edge devices remains challenging, especially given the extremely tight memory budgets. The existing offloading techniques inevitably introduce numerous loading bubbles, which further inflate the end-to-end latency of the entire inference pipeline. Meanwhile, dynamically fluctuating network bandwidth and diverse user request patterns pose additional obstacles to efficient lossless inference on edge devices. To address this, we propose LOIP, a collaborative lossless LLM inference system that employs an offloading-based interleaved pipeline parallelism to better overlap model offloading with computing and communicating. Specifically, LOIP first constructs an offloading-aware cost model to characterize inference latency and memory overhead under heterogeneous device capabilities and limited bandwidth. Based on this cost model, LOIP develops a fine-grained allocation scheduler that determines latency-efficient layer partitions across devices while explicitly accounting for offloading overhead, along with a unified memory architecture (UMA)-aware loading optimization using customized CUDA operators to reduce runtime loading overhead. LOIP further designs an online memory adaptation strategy to handle the increasing KV cache pressure and dynamic bandwidth fluctuations during inference. We implement LOIP with 2500+ lines of Python and 500+ lines of C++/CUDA code, and deploy it on five heterogeneous NVIDIA Jetson edge devices for lossless collaborative inference of LLaMA3.3-70B-Instruct. Extensive experiments demonstrate that LOIP achieves 8.8$\times$$\sim$20.3$\times$ speedups over the SOTA baselines under different bandwidth conditions and request patterns without compromising model accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading, unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingyu Sun, Xiao Zhang, Shen Qu, Yan Li, Mengbai Xiao, Yanwei Zheng, Yuan Yuan, Dongxiao Yu
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
