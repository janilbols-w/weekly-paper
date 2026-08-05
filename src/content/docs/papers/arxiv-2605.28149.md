---
title: "Sign-Aware Gated Sparse Autoencoders: Modeling Anticorrelated Features with Bi-Jump-ReLU Activations"
description: "Sparse Autoencoders (SAEs) extract interpretable features from Large Language Model activations, but standard variants enforce non-negative latents, so a bidirectional semantic axis (e.g., \"pressure too high\" vs."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.28149) · [PDF](https://arxiv.org/pdf/2605.28149)

## 一句话摘要

Sparse Autoencoders (SAEs) extract interpretable features from Large Language Model activations, but standard variants enforce non-negative latents, so a bidirectional semantic axis (e.g., "pressure too high" vs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse Autoencoders (SAEs) extract interpretable features from Large Language Model activations, but standard variants enforce non-negative latents, so a bidirectional semantic axis (e.g., "pressure too high" vs. "pressure too low") must be split across two latents, wasting dictionary capacity on anticorrelated features. We propose the Sign-Aware Gated SAE (SA-GSAE), which combines two-sided gated sparsity, signed shrinkage-free magnitudes, and auxiliary gate supervision in a new Bi-Jump-ReLU activation, so that a single latent carries both polarities of one decoder direction; parameter accounting shows sign-awareness stays parameter-efficient even when anticorrelated pairs are rare. Across three mid-depth hookpoints on Pythia-1B and SmolLM3-3B (six cells, three seeds), a half-width SA-GSAE empirically dominates the aggregate mean frontier of a full-width Gated SAE on three of six cells, matches its R^2 within 0.025 on the remaining three, and cuts dead fraction by 0.35-0.82 absolute at matched L_0 = 64 on all six. Ablations show the two-sided gate and the auxiliary loss are essential whereas per-polarity asymmetry is not; we recommend the fully tied symmetric variant as the default. A blinded semantic audit finds nameable opposition between a latent's two sides is rare for SA-GSAE and all tested baselines, while sign-conditioned interventions show a single signed latent acts as a bidirectional causal dial where a pair of "opposite" non-negative latents does not; we scope interpretability claims accordingly. At full width, SA-GSAE is over-parameterized and its reported configuration exhibits a reproducible reconstruction collapse at the SmolLM3-3B residual-stream site; the recommended configuration (small threshold initialization with dead-latent threshold resets) prevents it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bartosz Wieciech, Zmnako Awrahman, Marcin Czelej, Victor Hugo Jaramillo Velasquez, Wioletta Stobieniecka
- 发布：2026-08-04；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
