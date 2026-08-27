---
title: "MODE: Modality-Decomposed Expert-Level Mixed-Precision Quantization for MoE Multimodal LLMs"
description: "Mixture-of-Experts Multimodal Large Language Models (MoE-MLLMs) offer remarkable performance but incur prohibitive GPU memory costs, making compression essential."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.17118) · [PDF](https://arxiv.org/pdf/2606.17118)

## 一句话摘要

Mixture-of-Experts Multimodal Large Language Models (MoE-MLLMs) offer remarkable performance but incur prohibitive GPU memory costs, making compression essential.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts Multimodal Large Language Models (MoE-MLLMs) offer remarkable performance but incur prohibitive GPU memory costs, making compression essential. Among PTQ methods, expert-level mixed-precision quantization has proven effective for MoE-LLMs, yet suffers notable degradation on MoE-MLLMs due to two overlooked biases in expert importance estimation. (1) At the cross-modal level, the numerical dominance of vision tokens causes expert selection frequency to be dominated by vision tokens, masking experts that are critical to the text modality; (2) at the intra-vision level, the large proportion of redundant vision tokens further skew frequency statistics, obscuring experts critical for informative visual content. To bridge gaps, we propose MODE, a modality-decomposed expert-level mixed-precision quantization framework for MoE-MLLMs that decomposes expert selection frequency by modality, filters redundant vision tokens to obtain denoised visual frequency, and further evaluates quantization sensitivity per modality as a complementary signal to frequency-based estimation. These signals are integrated into an Integer Linear Programming formulation to assign per-expert bit-widths under a given budget. Extensive experiments show that MODE is particularly well-suited for MoE-MLLMs, limiting average performance loss to within 2.9% at W3A16, with larger gains at the extreme 2-bit setting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanteng Chen, Nanxin Zeng, Peisong Wang, Zhilei Liu, Yuantian Shao, Shiqiang Lang, Tao Liu, Chuangyi Li, Qinghao Hu, Gang Li, Jing Liu, Jian Cheng
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
