---
title: "NOSA: Native and Offloadable Sparse Attention"
description: "Decoding throughput improvements from larger inference batches are limited by GPU memory, which is largely consumed by the key-value (KV) cache."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2510.13602) · [PDF](https://arxiv.org/pdf/2510.13602)

## 一句话摘要

Decoding throughput improvements from larger inference batches are limited by GPU memory, which is largely consumed by the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decoding throughput improvements from larger inference batches are limited by GPU memory, which is largely consumed by the key-value (KV) cache. Prior training-free KV cache offloading alleviates this by keeping redundant context on the CPU and fetching only a sparse subset for attention, but it often degrades long-generation quality due to training-inference mismatch on sparse patterns. Meanwhile, trainable sparse attention is incompatible with efficient offloading, as unconstrained KV accesses may force large CPU-to-GPU transfers and erase throughput gains. To this end, we propose NOSA, a trainable sparse attention mechanism natively designed for KV cache offloading. NOSA explicitly constrains the volume of CPU-GPU KV transfers, thereby achieving low communication overhead and high decoding throughput. We further build NOSI, a KV cache offloading inference system that fully unlocks NOSA's efficiency. Empirical results on 1,3,8B LLMs demonstrate that NOSA outperforms KV cache offloading baselines on general, long-input, and long-generation tasks, while boosting decoding throughput by up to 5.04x, 1.92x, and 1.83x over FullAttn, InfLLMv2, and ShadowKV, respectively. We release our code at https://github.com/thunlp/NOSA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yuxiang Huang, Pengjie Wang, Jicheng Han, Weilin Zhao, Zhou Su, Ao Sun, Hongya Lyu, Hengyu Zhao, Yudong Wang, Chaojun Xiao, Xu Han, Zhiyuan Liu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/thunlp/NOSA](https://github.com/thunlp/NOSA)
- 阅读深度：metadata
