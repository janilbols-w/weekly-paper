---
title: "Efficient INT8 Inference of Small NLP Models on Server CPUs with PyTorch Native Stack"
description: "Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the era of large language models."
---

**评分：55/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.18182) · [PDF](https://arxiv.org/pdf/2608.18182)

## 一句话摘要

Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the era of large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small NLP models, especially BERT-family encoders, remain important in industrial workloads such as classification, ranking, and retrieval even in the era of large language models. On server CPUs, INT8 quantization offers an attractive latency-throughput-cost trade-off, but users increasingly expect such acceleration to be available directly in the native PyTorch stack. We integrate SmoothQuant into TorchAO and optimize the resulting inference path for Intel Xeon CPUs through graph-level fusion in TorchInductor and efficient INT8 GEMM kernel selection across oneDNN-, AVX512_VNNI-, and AMX-based implementations. Across BERT, DistilBERT, and XLM-RoBERTa benchmarks, the approach delivers up to 5.8x end-to-end throughput speedup with negligible---and in some cases no measurable---accuracy loss relative to the FP32 baseline. We also validated our work by detailed performance analysis with roofline models. The implementation has been upstreamed to PyTorch and TorchAO, enabling out-of-the-box deployment with native PyTorch tooling

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Weiwen Xia, Yuxin Cui, E Cao
- 发布：2026-08-18；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
