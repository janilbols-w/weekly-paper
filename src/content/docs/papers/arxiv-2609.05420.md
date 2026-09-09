---
title: "Sustained 70B-Class AWQ Inference on a Single NVIDIA L20: Throughput, Stability, Energy, and Quality Characterization"
description: "Serving 70B-class open-weight language models is usually associated with 80GB accelerators, tensor-parallel multi-GPU systems, or vendor-managed inference profiles."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.05420) · [PDF](https://arxiv.org/pdf/2609.05420)

## 一句话摘要

Serving 70B-class open-weight language models is usually associated with 80GB accelerators, tensor-parallel multi-GPU systems, or vendor-managed inference profiles.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving 70B-class open-weight language models is usually associated with 80GB accelerators, tensor-parallel multi-GPU systems, or vendor-managed inference profiles. This technical report evaluates whether a single NVIDIA L20 48GB GPU can sustain a useful 70B-class quantized serving workload. We measure Qwen2.5-72B-Instruct-AWQ served with vLLM 0.8.5.post1 and AWQ Marlin on one L20. Under a fixed workload of approximately 512 input tokens and 256 output tokens, a 24-hour concurrency-10 soak completed 36,740/36,740 requests with no request failures and no vLLM CUDA OOM, traceback, or killed-process signatures. The system sustained 108.84 output tokens/s, with p95 time-to-first-token of 6.61s and p95 end-to-end latency of 23.54s. GPU-board power sampled through nvidia-smi produced an estimated 7.92 kWh over the run, corresponding to 0.330 output tokens/J and 1.008 total tokens/J. Repeated fixed-shape runs at concurrency 1, 4, 8, and 16 completed 12/12 runs successfully; the concurrency-16 condition averaged 127.22 +/- 12.68 output tokens/s over three runs. The same AWQ endpoint also produced absolute quality scores of 0.8130 on MMLU, 0.8309 on CMMLU, and 0.8082 on GSM8K, plus 80/80 MT-Bench answer generations and a 60-item 8K LongBench subset. The evidence supports a narrow claim: a carefully configured single L20 can serve Qwen2.5-72B-Instruct-AWQ as a throughput-oriented 70B-class endpoint under the tested fixed-shape workload. It does not prove lossless AWQ quality retention, low-latency interactive serving, broad production SLA coverage, or equivalence to a BF16/FP16 baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yin Li
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
