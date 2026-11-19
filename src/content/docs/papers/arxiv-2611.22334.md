---
title: "BQ-LoRA: Binary-Quantized Low-Rank Adapters as Implicit Regularizers for Parameter-Efficient Fine-Tuning"
description: "Parameter-efficient fine-tuning of quantized large language models is dominated by QLoRA, which combines 4-bit weight quantization with FP16 low-rank adapters."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.22334) · [PDF](https://arxiv.org/pdf/2611.22334)

## 一句话摘要

Parameter-efficient fine-tuning of quantized large language models is dominated by QLoRA, which combines 4-bit weight quantization with FP16 low-rank adapters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Parameter-efficient fine-tuning of quantized large language models is dominated by QLoRA, which combines 4-bit weight quantization with FP16 low-rank adapters. We ask whether the FP16 adapter precision is necessary. Replacing it with a single binary bit per adapter parameter, combined with a learned per-layer scale $s$ and a Scaled Straight-Through Estimator, reduces adapter storage by 13-16x. We introduce two variants -- NormScale, which binarizes under a norm-preserving scale with a clipped STE, and LearnThresh, which makes the binarization threshold learnable -- unified under a framework we call BQ-LoRA. Our main theoretical contribution is a tight characterization of the BQ-LoRA hypothesis class: it has bounded entrywise norm, a typical-set spectral norm bound that is $\Theta(r)$ times sharper than the worst case, a full-rank, near-isotropic update, and consequently a Rademacher complexity that yields an explicit $\tilde{O}(s_{\max}\alpha\sqrt{d_{out}/(rn)})$ generalization bound. FP16 LoRA has no comparable a priori norm or isotropy control. On Qwen2.5 (1.5B-72B), BQ-LoRA exceeds QLoRA's benchmark averages at every scale by 0.8-3.5 points; on LLaMA-2 (7B/70B) it remains competitive at the same storage reduction but does not uniformly lead the strongest FP16-adapter baselines (LoftQ at 7B, QLoRA at 70B). On Qwen2.5-7B the binary adapter preserves the 4-bit base WikiText-2 PPL within 0.06 (9.86 vs. 9.80) while QLoRA worsens it by 0.59. The reduction applies to inference-time adapter storage and serving; training memory matches QLoRA and step time rises by under 4%. We translate the storage saving into a deployment study, BQ-SGMV, by extending Punica's SGMV kernel with a binary inner-product primitive: the same A100-80GB holds 15.6x more adapters in HBM, and our research prototype eliminates cache misses under a skewed synthetic workload.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Juyoung Park, Heejun Lee
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
