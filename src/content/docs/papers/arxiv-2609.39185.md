---
title: "Low-Discrepancy Dither for Quantized Recurrent State Caches"
description: "Mamba-style and hybrid language models compress their past into a fixed-size recurrent state that is rewritten at every generated token."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.39185) · [PDF](https://arxiv.org/pdf/2609.39185)

## 一句话摘要

Mamba-style and hybrid language models compress their past into a fixed-size recurrent state that is rewritten at every generated token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mamba-style and hybrid language models compress their past into a fixed-size recurrent state that is rewritten at every generated token. Storing this state in low precision saves memory bandwidth, but every rounding error is fed back into the next update and can accumulate over long generations. Production systems round the state stochastically; we ask which rounding rule such caches should use. We find that a deterministic golden-ratio Weyl dither, which needs no random numbers, consistently brings the quantized model closer to the full-precision one than stochastic rounding, across pure and hybrid models, storage formats, and long decoding horizons, at no extra cost. Round-to-nearest behaves differently: because it discards small updates, its error keeps growing, so it can look best in short evaluations yet falls far behind over long generations. A discrepancy analysis explains this ordering, and we document implementation pitfalls that silently remove the benefit.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Snigdha Chandan Khilar
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
