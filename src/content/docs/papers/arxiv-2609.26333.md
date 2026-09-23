---
title: "Disaggregated Quantization: Specializing LLM Prefill and Decode"
description: "Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.26333) · [PDF](https://arxiv.org/pdf/2609.26333)

## 一句话摘要

Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation. We propose "disaggregated quantization" (DQ), which specializes computation formats, weights and storage placement to both of these phases. On Qwen 3 and Gemma 3, removing activation quantization specifically on decode improves accuracy on decode-heavy tasks without increasing inference cost. Training separate compute-native prefill weights accelerates prompt processing relative to weight-only inference while matching or exceeding its accuracy at 2-3-bit decode on both decode-heavy and prefill-heavy tasks. With released Qwen3.8-27B GGUF decoders, training an NVFP4 prefiller improves 1-bit accuracy by 32.5 points on MMLU-Pro and 35.3 on MMMU-Pro without modifying the decode checkpoint. To accommodate the additional checkpoint on a single device, offloaded disaggregated prefill (ODP) streams its weights from SSD, amortizing loading over prompt length. On the same 27B model, ODP delivers a 1.78x time-to-first-token speedup over the weight-only baseline at 8K prompt length in llama.cpp. We evaluate accuracy under disaggregated serving in vLLM and further validate shared-weight format disaggregation through post-training quantization on models up to 2.8T parameters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Andrei Panferov, Maximilian Kleinegger, Sweta Priyadarshi, Tijmen Blankevoort, Dan Alistarh
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
