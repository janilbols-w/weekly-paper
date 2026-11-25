---
title: "BitShare: Sensitivity-Aware Binning and Bit Sharing for Compacting LLM Weight Storage"
description: "Decoding with large language models at small batch sizes is limited by memory bandwidth, so the bits stored per weight largely set its cost."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.28607) · [PDF](https://arxiv.org/pdf/2611.28607)

## 一句话摘要

Decoding with large language models at small batch sizes is limited by memory bandwidth, so the bits stored per weight largely set its cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decoding with large language models at small batch sizes is limited by memory bandwidth, so the bits stored per weight largely set its cost. Group-wise integer quantization stores every weight of a group at the same precision, although the input channels of a group differ in sensitivity. We present BITSHARE, a codebook-free weight format that keeps the integer grid and the dequantizer of group-wise quantization but varies precision within each group. Sensitivity-aware binning places the channels of each group into three bins at fixed positions, and static bit sharing with optimal bit-value allocation lets the less sensitive weights share their lower bits, each stored once per group or once per pair of weights. A sharing-aware version of GPTQ chooses every stored value, with no fine-tuning and no codebook. BITSHARE has two modes. BITSHARE-U gives every group the same layout, so its decoder routes bits by fixed wiring, while BITSHARE-N chooses a layout per group within the same bit budget. With calibration on the Pile and at the same storage, both modes have lower perplexity than GPTQ at 3 and 2 bits on WikiText-2 and C4. At 2 bits across Llama-2 and Llama-3 models, BITSHARE-N lowers WikiText-2 perplexity by up to 70% against SliM-LLM and up to 35% against GPTAQ. At the 2-bit perplexity of SliM-LLM, BITSHARE-U stores 13.6-19.4% fewer bits per weight, cutting DRAM weight traffic by the same fraction. A verified hardware decoder implementation synthesized in SkyWater 130 nm reconstructs BITSHARE weights at the throughput of INT-n and SliM-LLM decoders.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiuyu Ren, Sudipta Paria, Aritra Dasgupta, Swarup Bhunia
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
