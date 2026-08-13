---
title: "RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation"
description: "We present RT-SEMamba, a fully causal speech enhancement (SE) model built upon causal time-frequency Mamba blocks."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.12099) · [PDF](https://arxiv.org/pdf/2608.12099)

## 一句话摘要

We present RT-SEMamba, a fully causal speech enhancement (SE) model built upon causal time-frequency Mamba blocks.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present RT-SEMamba, a fully causal speech enhancement (SE) model built upon causal time-frequency Mamba blocks. Unlike Transformer-based architectures that rely on a growing key-value cache, Mamba propagates a fixed-size recurrent state per layer, enabling memory- and bandwidth-efficient long-form inference. We further introduce a progressive knowledge distillation (KD) strategy that compresses an 8-layer teacher into a shallow 1-layer student by jointly distilling complex spectral outputs and intermediate representations. On Voicebank-DEMAND, the 8-layer RT-SEMamba achieves 3.32 PESQ with a 25 ms algorithmic latency constraint, and the distilled 1-layer student improves over a naive 1-layer baseline from 3.06 to 3.18 PESQ while preserving the same steady-state RTF, delivering a 2.75x speedup over the teacher. These results demonstrate that state-space models with progressive KD provide a competitive quality-latency trade-off for real-time SE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rong Chao, Sung-Feng Huang, Moreno La Quatra, Sabato Marco Siniscalchi, Wen-Huang Cheng, Szu-Wei Fu, Yu Tsao
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
