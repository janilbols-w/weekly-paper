---
title: "AI-Assisted Design of a Post-Quantum Cryptographic Accelerator: A Deployed-Silicon Case Study"
description: "Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.04058) · [PDF](https://arxiv.org/pdf/2609.04058)

## 一句话摘要

Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely. The standard acceptance gate cannot detect an entire class of ML-DSA defects. Signing resamples until a candidate meets its norm bounds, so the executed path varies with the message, whereas known-answer tests (KATs) sample fixed values and reach only the depths their seeds trigger. Our accelerator passed its full KAT regression while carrying a norm check that outran block-RAM latency, leaving each candidate's final coefficients unverified; the escape surfaced at reject-loop iteration 5. The blind spot lies in the instrument, not the engineer; care cannot remove it. We replace that gate. A byte-exact golden-reference oracle paired with randomized adversarial soak drives the rejection loop past any fixed vector, closing the gap: 301,343 data-dependent signings, zero escapes. Because the gate judges artifacts and never authors, trust becomes separable from authorship, making AI authorship an answerable question. We report 232 logged experiments in which an agentic large language model drove a unified ML-KEM-768 and ML-DSA-65 accelerator with on-chip key custody from RTL to PCIe bring-up on one Kintex-7 XC7K160T, shipped at 98.5% slice occupancy. Success was 71.6%, following a hardware-coupling gradient, 77-85% for documentation and research against 50-53% for synthesis and bring-up, which observability can explain: failure concentrates where corrective signals are physical-side only. That so unreliable an author produced an artifact byte-exact across all six FIPS operations -- its deployed baseline surviving the same 779,945-check zero-failure soak -- is the claim.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jungmin Park, Eunha Kim, Wooseop Kim, Seongjoon Cho, Byungho Cha
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
