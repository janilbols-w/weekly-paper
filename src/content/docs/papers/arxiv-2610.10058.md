---
title: "Cache the Encoder Within:Compact, Reusable Memory across LLM Queries"
description: "Repeated queries over shared documents incur redundant encoding, while caching model states introduces persistent storage costs."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.10058) · [PDF](https://arxiv.org/pdf/2610.10058)

## 一句话摘要

Repeated queries over shared documents incur redundant encoding, while caching model states introduces persistent storage costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Repeated queries over shared documents incur redundant encoding, while caching model states introduces persistent storage costs. Building on CoMem's intermediate-state interface, EncBank treats a pretrained LLM's lower layers as a reusable document encoder and compactly stores their outputs for an adapted upper-layer reader. A self-distilled suffix adapter is shared across storage precisions within each backbone, without quantization-specific retraining. Across five benchmark suites on three Qwen backbones spanning different sizes and full-attention and hybrid architectures, 4-bit storage keeps each reported benchmark aggregate within one score point of native-precision EncBank. In a fixed Qwen3-8B workload, it retains 28.1% of the native-precision persistent GPU store. Separate native-precision controls yield a 1.40x selected-pack prefill speedup over same-evidence, same-adapter text replay, at a 3.12-point RULER accuracy cost. A native-precision Qwen3.8-27B configuration also passes 70 of 89 Terminal-Bench 2.1 tasks. EncBank thus combines reusable computation with compact memory, while task fidelity and end-to-end benefits remain dependent on the workload, preparation costs, and reuse frequency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hanzuo Liu, Chunyu Liu, Chaofan Lin, Alex Lamb, Mingyu Gao
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
