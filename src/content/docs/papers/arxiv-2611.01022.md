---
title: "Jet-QSparse: Accelerating Agentic LLM Inference with 4-Bit Sparse Attention"
description: "Long-horizon reasoning and agentic workloads strain KV-cache capacity and decode attention throughput."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.01022) · [PDF](https://arxiv.org/pdf/2611.01022)

## 一句话摘要

Long-horizon reasoning and agentic workloads strain KV-cache capacity and decode attention throughput.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-horizon reasoning and agentic workloads strain KV-cache capacity and decode attention throughput. We present Jet-QSparse, a training-free method that combines compact NVFP4 cache storage with native FP4 query-key computation on Blackwell tensor cores. A dense scan scores the full key history and selects 128-token blocks for sparse FP16 value aggregation with FP32 accumulation, preserving higher precision in the output-forming step while enabling contiguous tile loads. Calibrated key centering and at most two BF16 pages per sequence and layer address quantization error; FP8 prefill uses a temporary arena while the persistent cache is packed directly from BF16 activations. Across four hybrid LLMs, a budget of 128 blocks per KV head shows no detected accuracy loss on the evaluated mathematical reasoning, coding, and agentic benchmarks, although some smaller budgets incur losses. With 64 blocks, Qwen3.8-27B achieves a $1.94\times$ end-to-end decode speedup over dense BF16 at 128K context and batch size 16 on one GB300, and the measured Qwen KV pools provide $2.58$-$2.76\times$ BF16's token capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haozhan Tang, Hao Kang, Meng Lu, Yecheng Wu, Zerui Wang, Seokho Han, Haocheng Xi, Shuo Yang, Song Han, Han Cai
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
