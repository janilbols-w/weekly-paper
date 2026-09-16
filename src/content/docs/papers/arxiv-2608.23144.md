---
title: "Activation-Weighted Seeded Residual Coding for Low-Bit LLM Weight Repair"
description: "Low-bit weight quantization saves storage but leaves errors that degrade LLM quality."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.23144) · [PDF](https://arxiv.org/pdf/2608.23144)

## 一句话摘要

Low-bit weight quantization saves storage but leaves errors that degrade LLM quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit weight quantization saves storage but leaves errors that degrade LLM quality. We introduce activation-weighted seeded residual coding (AWSRC), a compact repair codec for an existing quantization backbone. Given a reconstructed weight $W_0$, AWSRC encodes the residual $W-W_0$ using deterministic seed-generated bases. The sidecar stores seed selectors, low-bit coefficients, and scales rather than an explicit codebook. Two variants combine activation weighting with per-module byte quotas ($\mathrm{AWSRC\text{-}U}$), or blended activation/Fisher weighting with globally ranked progressive prefixes ($\mathrm{AWSRC\text{-}P}_{F}$) that support multiple byte budgets without refitting. On Qwen2.5-3B-Instruct, adding $0.162$ scope-bits/weight to an RTN-INT4 baseline closes $88.2\%$, $78.9\%$, and $71.3\%$ of the PPL, KL, and 11-task mean-accuracy gaps to BF16, respectively. AWSRC achieves the highest mean downstream accuracy in byte-matched residual-codec ablations and improves all metrics across model families with up to 32B parameters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zehao Liu, Chuangchuang Fang, Yang Ren
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
