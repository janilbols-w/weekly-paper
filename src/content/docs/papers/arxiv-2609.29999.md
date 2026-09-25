---
title: "GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS"
description: "Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.29999) · [PDF](https://arxiv.org/pdf/2609.29999)

## 一句话摘要

Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior. We present GHOST-Q, a cross-precision controlled evaluation of three 8B VLM families under FP16, INT8, and NF4 across utility and hallucination-sensitive benchmarks. Rather than comparing only aggregate accuracy, we pair FP16 and quantized predictions item by-item to quantify how compression redistributes grounding successes and failures. Five of six quantized variants preserve MMStar accuracy within $\pm2$ percentage points, yet 10 of 36 paired effects remain significant after false-discovery-rate correction, nine on hallucination-sensitive conditions. Same-device A100 profiling further demonstrates that substantial memory reduction does not necessarily mean lower inference latency. Finally, an open-ended AMBER audit reveals strong generation budget censoring whose severity varies by architecture and precision. These results show that quantized VLMs should be evaluated jointly for aggregate utility, grounding reliability, generation behavior, and realized deployment efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saim Rehman, Muhammad Shafique
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
