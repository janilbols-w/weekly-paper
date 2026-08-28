---
title: "Accelerating Diffusion Language Models via Structured Suffix Modeling"
description: "Diffusion Language Models (DLMs) exhibit strong parallel decoding capabilities by denoising multiple tokens in a single generation step."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.23167) · [PDF](https://arxiv.org/pdf/2608.23167)

## 一句话摘要

Diffusion Language Models (DLMs) exhibit strong parallel decoding capabilities by denoising multiple tokens in a single generation step.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Language Models (DLMs) exhibit strong parallel decoding capabilities by denoising multiple tokens in a single generation step. However, this parallelism comes with substantial computational overhead, as each step requires interactions with all suffix tokens. Existing methods typically reduce this cost by retaining only a local suffix window as a substitute for the full suffix. Despite their effectiveness, these methods overlook the structural heterogeneity across suffix regions and re-initialize suffix tokens with identical representations at each timestep. To this end, we propose a structured suffix modeling method for efficient DLM inference. Specifically, we divide the suffix into three regions, i.e., the local, middle, and tail regions, and retain different numbers of suffix tokens in each region according to their structural roles. Moreover, we incorporate the decoding results from the previous step into the suffix token representations at the current step, allowing them to carry evolving denoising information across generation steps. Notably, our method is training-free and orthogonal to several existing acceleration techniques, such as parallel decoding strategies and KV cache. Empirical results across multiple benchmarks on three DLMs demonstrate that our method can further accelerate DLM inference and improve performance in most cases. In particular, in long-sequence inference, our method achieves up to a \(72.81\times\) speedup when combined with other acceleration techniques. Our code is available at https://github.com/zifengcheng/SSM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zifeng Cheng, Keda Li, Zhiwei Jiang, Cong Wang, Fei Shen, Qing Gu
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/zifengcheng/SSM](https://github.com/zifengcheng/SSM)
- 阅读深度：metadata
