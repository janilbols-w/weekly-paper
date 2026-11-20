---
title: "Implementing Binary Transformers with Approximate Memories with Permutation Invariance Enabled Selective (PIES) Protection"
description: "Quantization is an effective technique to reduce memory storage, computation complexity and power for Transformers, and the binarization of the weights is important for meeting these requirements."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.23358) · [PDF](https://arxiv.org/pdf/2611.23358)

## 一句话摘要

Quantization is an effective technique to reduce memory storage, computation complexity and power for Transformers, and the binarization of the weights is important for meeting these requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization is an effective technique to reduce memory storage, computation complexity and power for Transformers, and the binarization of the weights is important for meeting these requirements. Approximate memory can further reduce the power for memory, but it also introduces errors. Current research for binary Transformers focuses on task performance, but the model dependable operation against errors on the memory has not been well studied. In this paper, we first evaluate the dependability of binary Transformers with the Bidirectional Encoder Representations from Transformers (BERT) as a case study. A large accuracy loss occurs only at high Bit Error Rates (e.g. BER = 5% or 10%). Then we propose a novel Permutation Invariance Enabled Selective (PIES) scheme to protect the binary weights at very low overhead. This scheme exploits the invariance of Transformers to permutations in the rows and columns to group the critical weights and perform selective protection on those weights. Simulation results show that PIES can recover most of the performance loss caused by bit errors at BERs as high as 10%, at an overhead significantly lower than traditional error correction schemes. These results confirm the feasibility of running binary Transformers using approximate memory with aggressive voltage scaling on resource-limited low power edge devices. The code for PIES is released on github (https://github.com/YangZhutian/binary-transformer-prefix-repair).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhen Gao, Xiao Yin, Kexin Liang, Pedro Reviriego, Shanshan Liu, Fabrizio Lombardi
- 发布：2026-11-17；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/YangZhutian/binary-transformer-prefix-repair](https://github.com/YangZhutian/binary-transformer-prefix-repair)
- 阅读深度：metadata
