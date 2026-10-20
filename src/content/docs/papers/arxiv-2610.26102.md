---
title: "Provable Adversarial Detection: Prime Quantization meets Gromov--Wasserstein"
description: "Adversarial vulnerability persists across modern vision architectures from CNNs to vision language models (VLMs), yet existing detection methods rely on heuristics without theoretical guarantees."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.26102) · [PDF](https://arxiv.org/pdf/2610.26102)

## 一句话摘要

Adversarial vulnerability persists across modern vision architectures from CNNs to vision language models (VLMs), yet existing detection methods rely on heuristics without theoretical guarantees.

## 为什么值得关注

待编辑增强。

## 摘要原文

Adversarial vulnerability persists across modern vision architectures from CNNs to vision language models (VLMs), yet existing detection methods rely on heuristics without theoretical guarantees. We address the fundamental question of when adversarial perturbations can be provably detected from a geometric perspective. Our key insight is that adversarial perturbations cannot simultaneously preserve geometric structure across spaces with fundamentally different properties. Accordingly, we construct two such complementary metric spaces. First, we use a standard CNN embedding space $Z$, where adversarial samples exhibit significant displacement patterns. Second, we build a novel prime-quantized space $P$, that absorbs small perturbations through number-theoretic discretization, resulting in minimal displacement, while preserving discriminability. We then leverage the geometric discrepancies across spaces $Z$ and $P$ to detect adversarial samples. To the best of our knowledge, we establish the first rigorous separation theory for adversarial detection, proving that adversarial samples create unavoidable geometric inconsistencies across both spaces. Our framework provides theoretical guarantees including pixel-level absorption bounds, neighborhood diameter concentration, Gromov-Wasserstein (GW) separation theorems, and practical risk control. Extensive experiments validate our theoretical predictions and achieve consistently strong detection performance across a wide range of attack types and model families.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Manohar Kaul, Sadbhavana Babar, Aditya Ramesh, Aditya Saibewar, Fumiyoshi Kasahara, Maki Inui, Hiroaki Kurihara
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
