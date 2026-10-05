---
title: "Latent-MOPD: Latent Multi-Teacher On-Policy Distillation"
description: "On-policy distillation (OPD) trains a student on the responses it generates."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02381) · [PDF](https://arxiv.org/pdf/2610.02381)

## 一句话摘要

On-policy distillation (OPD) trains a student on the responses it generates.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) trains a student on the responses it generates. Existing LLM multi-teacher OPD transfers what specialists predict through their output distributions. We introduce Latent-MOPD, to our knowledge the first representation-level multi-teacher OPD method for LLMs. It integrates existing specialists through both their predictions and the hidden states used to compute them, without additional teacher training. To coordinate representation supervision from multiple specialists, we select late-layer targets according to the teacher-student relationship, bridge unequal hidden widths with a shared projection, and group updates by domain. Each teacher's supervision gradually shifts from hidden states to token predictions, with both channels using the same routed specialist. In our main same-family setting, Latent-MOPD outperforms the token-only, representation-only and uniform-averaging baselines on all nine benchmarks across math, code and logic. With the same parameter count as each teacher, the student also surpasses the per-benchmark best teacher on a majority of these benchmarks. With larger, separately developed cross-family teachers, Latent-MOPD outperforms both single-channel baselines on all benchmarks. A same-family all-layer representation-only control remains stable with domain-pure updates but collapses when teacher domains are interleaved within an update. Our results show that a single student can integrate capabilities from several specialists through both their output distributions and internal representations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhengyu Fang, Seoyeon Hong, Jie Yang, Muyang Li, Koyoshi Shindo, Brandon Joseph Lwowski, Jing Li
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
