---
title: "AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling"
description: "Long-context decoding repeatedly reads a growing KV cache."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2611.26106v1) · [PDF](https://arxiv.org/pdf/2611.26106v1)

## 一句话摘要

Long-context decoding repeatedly reads a growing KV cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context decoding repeatedly reads a growing KV cache. FP4 reduces cache storage and traffic but needs block scaling to handle its limited dynamic range. Applying FP4 to multi-head latent attention (MLA) requires reconciling different K/V scaling requirements on a shared latent. Existing approaches address this mismatch through dequantization or separate encodings, adding execution or storage overhead. We present AscMLA, which combines asymmetric K/V scaling with pipelined scale delivery to process a single FP4 payload directly. AscMLA uses 38.2% less cache memory than FP8 and achieves geometric-mean speedups of 1.35x over TRT-LLM's FP8 and 1.26x over CAKE's NVFP4 MLA kernels.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zechun Zhou, Zhiyong Zheng, Xiaomin Zhang, Lin Ye, Han Li, Jingwei Sun, Guangzhong Sun, Jing Li
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
