---
title: "Sensitivity Inflation from Cross-Record Precision Routing in Private Quantized Fine-Tuning"
description: "Private fine-tuning of large language models increasingly pairs DP-SGD with low-rank adapters on frozen, quantized backbones, and every such stack inherits one unstated premise: frozen layers keep each record's clipped gradient a function of that record alone."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.01411) · [PDF](https://arxiv.org/pdf/2611.01411)

## 一句话摘要

Private fine-tuning of large language models increasingly pairs DP-SGD with low-rank adapters on frozen, quantized backbones, and every such stack inherits one unstated premise: frozen layers keep each record's clipped gradient a function of that record alone.

## 为什么值得关注

待编辑增强。

## 摘要原文

Private fine-tuning of large language models increasingly pairs DP-SGD with low-rank adapters on frozen, quantized backbones, and every such stack inherits one unstated premise: frozen layers keep each record's clipped gradient a function of that record alone. We show that LLM.int8 breaks this premise. It routes outlier activation columns to a higher-precision path using a union over the whole batch, so one record decides how every other record's activations are computed, even though the weights are frozen and the quantization scales are per row. We bound the resulting sensitivity inflation, state a record-isolation contract that restores the standard bound, and define record-owned precision dispatch that meets it with the same GEMMs as batched LLM.int8, so isolation needs no extra arithmetic. We then audit the native CUDA stack (bitsandbytes, PEFT, Opacus) against four matched controls. A constructed LoRA-Opacus witness reaches $15.0\times$ the add/remove bound. On pretrained OPT-125M with natural text, other records alter 20% of record-layer precision splits at batch size 16. An exploratory re-clipping analysis finds 10 of 64 candidate neighbors above the bound once every gradient is clipped; the top pair, revalidated natively, reaches $1.065C$ while every control stays within $C$, and forcing one layer's outlier mask removes the excess. A two-million-draw audit of the released adapters yields $\varepsilon$ lower bounds ($3.25$ at $\delta=10^{-5}$) below the advertised guarantee ($4.38$). Resolving an excess this small at the release level would take about 200 times more draws, whereas checking the sensitivity contract directly exposes it in a few native runs, which makes contract checking the practical audit for private quantized training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Annan Zhang, Shengjie Song, Wenshuai Yao, Lihao Zhang, Tianmiao
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
