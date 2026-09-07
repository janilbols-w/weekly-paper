---
title: "Golden Ruler: A Numeric Format Catalog with Bit-Exact Conformance Vectors for FP8, BF16, MXFP4, and Microscaling Formats"
description: "Numeric format proliferation in machine learning hardware -- FP8 (E4M3 and E5M2), BF16, MXFP4, microscaling block formats, and dozens of research variants -- has outpaced the availability of vendor-neutral, bit-exact reference material."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.09686) · [PDF](https://arxiv.org/pdf/2606.09686)

## 一句话摘要

Numeric format proliferation in machine learning hardware -- FP8 (E4M3 and E5M2), BF16, MXFP4, microscaling block formats, and dozens of research variants -- has outpaced the availability of vendor-neutral, bit-exact reference material.

## 为什么值得关注

待编辑增强。

## 摘要原文

Numeric format proliferation in machine learning hardware -- FP8 (E4M3 and E5M2), BF16, MXFP4, microscaling block formats, and dozens of research variants -- has outpaced the availability of vendor-neutral, bit-exact reference material. Engineers porting models across accelerators encounter silent divergences that are difficult to diagnose without a shared ruler. This paper describes a catalog of 109 numeric formats spanning 12 clusters (83 at v2; the count is a catalog invariant, not a fixed number), a suite of six bit-exact conformance packs covering GF16, MXFP4 element, BF16, FP8 E4M3, FP8 E5M2, and E8M0 block scale, and an IEEE P3109 v3.2.0 cross-walk that maps each pack to its corresponding standards-track configured format. Each pack is a self-contained JSON document with a SHA-256 fingerprint, a shared row schema, and an anchor vector that encodes 3.0 -- the identity phi^2 + 1/phi^2 = 3 -- as a cross-pack sanity check. Packs are cross-validated against ml_dtypes 0.5.4 (Google/JAX); any divergence is documented explicitly and interpreted as a spec-permitted interpretation gap rather than hidden. The work is framed as registry filling: it does not propose new formats, make model-accuracy claims, or assert superiority over any vendor's implementation. All artifacts are publicly available at https://github.com/gHashTag/t27 under an open license.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, microscaling
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Dmitrii Vasilev
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/gHashTag/t27](https://github.com/gHashTag/t27)
- 阅读深度：metadata
