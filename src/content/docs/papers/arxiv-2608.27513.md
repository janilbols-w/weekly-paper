---
title: "DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization"
description: "Softmax attention stores key and value vectors for every preceding token, causing inference memory to grow with sequence length."
---

**评分：60/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.27513) · [PDF](https://arxiv.org/pdf/2608.27513)

## 一句话摘要

Softmax attention stores key and value vectors for every preceding token, causing inference memory to grow with sequence length.

## 为什么值得关注

待编辑增强。

## 摘要原文

Softmax attention stores key and value vectors for every preceding token, causing inference memory to grow with sequence length. Recent language models incorporating Gated DeltaNet (GDN) or Kimi Delta Attention (KDA) reduce this cost by replacing the KV cache in most layers with fixed-size recurrent states. However, these recurrent states are commonly stored in FP32 and consume substantial GPU memory; their updates are memory-bandwidth bound and contribute significantly to decoding latency. To our knowledge, we are the first to study post-training quantization of recurrent states in GDN and KDA based language models. We find that uniform quantization provides a poor accuracy--storage trade-off: INT8 and FP8 already degrade accuracy on complex reasoning tasks, while INT4 and NVFP4 reduce it to near zero. We further find that most quantization-error energy is concentrated in a small subset of channels and that the relative decay strength of state channels remains stable across prompts and tasks. Motivated by these findings, DAMP uses both quantization-error energy and decay-based persistence to identify high-risk channels during offline calibration. It stores these channels at higher precision and the remainder in INT8. We evaluate DAMP on Qwen3.6-35B and Kimi-Linear-48B across six benchmarks covering mathematical reasoning, general reasoning, and code generation. At 9.9 bits per state value, DAMP maintains average accuracy close to the FP32 baseline. DAMP reduces recurrent-state storage by 69.1%, accelerates the recurrent-state update kernel by up to 2.01x, and lowers full-model TPOT by up to 10.9%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int4, int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tao Zhang, Jianchao Tan, Pingwei Sun, Yanqi Yu, Zixu Jiang, Yuchen Xie, Xunliang Cai, Ziqian Zeng
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
