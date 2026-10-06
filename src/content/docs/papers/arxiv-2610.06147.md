---
title: "Efficient Test-time Adaptation through Candidate Verification and Divergence Shifts"
description: "Vision-language models (VLMs) achieve strong zero-shot transferability but remain vulnerable to target-domain shifts at inference time."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.06147) · [PDF](https://arxiv.org/pdf/2610.06147)

## 一句话摘要

Vision-language models (VLMs) achieve strong zero-shot transferability but remain vulnerable to target-domain shifts at inference time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) achieve strong zero-shot transferability but remain vulnerable to target-domain shifts at inference time. Test-time adaptation (TTA) offers a practical remedy, yet most existing VLM-TTA methods follow a prediction-side adaptation paradigm. They use test samples to adjust logits, prototypes, caches, priors, or feature statistics, often incurring additional computational overhead. In this paper, we take a different perspective and reframe VLM-TTA as candidate verification rather than prediction adjustment. We propose Test-Time Correction (TTC), a hypothesis-based correction framework guided by a simple principle: hypothesize, reconstruct, correct. Given a test feature and its top-k candidate labels, TTC treats each candidate label as a hypothesis, reconstructs the feature within the corresponding latent subspace stored in a memory bank, and measures the resulting divergence shift. This shift quantifies how much the candidate subspace and its relations to other candidates change after the hypothetical insertion of the test feature. A correct candidate hypothesis induces only a small shift, whereas an incorrect one perturbs the subspace more strongly. TTC therefore corrects the prediction by selecting the candidate with the minimum aggregated divergence shift. This training-free candidate-verification mechanism avoids iterative optimization and provides a favorable accuracy-efficiency trade-off. Across five TTA settings and 15 benchmark datasets, including zero-shot classification, domain generalization, few-shot classification, base-to-novel generalization, and cross-dataset evaluation, TTC consistently improves accuracy over state-of-the-art VLM-TTA methods while achieving up to 2x speedup, over 3x lower CPU memory usage, and up to 1.4x lower GPU memory usage than the lowest-memory training-free baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Seungmin Oh, Seunghun Kang, Jongbin Ryu
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
