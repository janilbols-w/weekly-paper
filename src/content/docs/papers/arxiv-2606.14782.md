---
title: "Last But Not Least: Boundary Attention CalibratiON for Multimodal KV Cache Compression"
description: "Multimodal Large Language Models (MLLMs) achieve strong vision-language reasoning but incur large KV caches and high decoding latency with long visual contexts."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.14782) · [PDF](https://arxiv.org/pdf/2606.14782)

## 一句话摘要

Multimodal Large Language Models (MLLMs) achieve strong vision-language reasoning but incur large KV caches and high decoding latency with long visual contexts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal Large Language Models (MLLMs) achieve strong vision-language reasoning but incur large KV caches and high decoding latency with long visual contexts. Existing compression methods rely on observation window attention for stable token importance estimation, yet this aggregation can dilute sparse critical evidence and discard answer-relevant tokens under aggressive compression. We identify last query attention as a complementary signal for recovering such evidence, though its irrelevant signals may introduce additional noise. We propose BACON, a plug-and-play method that calibrates observation window attention with last query evidence while suppressing noise through intra-layer coherence and inter-layer persistence. Across diverse benchmarks, models, budgets, and compression methods, BACON improves multimodal KV-cache compression by 7.5% on average under the most aggressive budget, with gains up to 30.9%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Chen, Yuheng Wu, Kelu Yao, Xiaogang Xu, Xiaobin Hu, Dongman Lee
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
