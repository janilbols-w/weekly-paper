---
title: "Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual LLM Inference on NVIDIA Blackwell"
description: "Low-bit LLM quantization is useful only if a model preserves service-relevant accuracy, executes through supported GPU kernels, and meets measured memory and latency limits."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.21974) · [PDF](https://arxiv.org/pdf/2611.21974)

## 一句话摘要

Low-bit LLM quantization is useful only if a model preserves service-relevant accuracy, executes through supported GPU kernels, and meets measured memory and latency limits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit LLM quantization is useful only if a model preserves service-relevant accuracy, executes through supported GPU kernels, and meets measured memory and latency limits. We study Qwen3-8B on NVIDIA B200 with vLLM, including INT2/INT3, GPTQ, NVFP4, and mixed-precision configurations. We verify native packed execution and precision on all 144 fused linear modules and evaluate Korean, English, numerical, and reasoning quality under preregistered gates. Packed INT2 and INT3 execute, but all seven tested INT2 grids degenerate on generation. Isolated module-restoration effects are strongly non-additive; Korean and reasoning sensitivity rankings disagree, and a promising INT4/INT8 development candidate fails independent final evaluation. A configuration with 16-bit activations, 98 NVFP4 weight-only modules, 46 INT8 modules, and an INT8 output head passes all gates on the untouched FINAL-81 set (5,168 items): 5.917 GiB of weight-loading memory (limit 5.98), Korean teacher-correct retention 0.904 (gate 0.90), and TPOT ratio 0.939 relative to BF16. It improves paired accuracy over NVFP4 W4A4 by +1.4 percentage points (Bonferroni-adjusted interval [+0.2, +2.6]), compared with +3.4 points on the selection set. This comparison changes both activation precision and INT8 protection; exploratory analyses suggest that the activation change contributes substantially, but the isolated allocation effect is not established. Final checkpoints were not retained, and bitwise rebuild reproducibility remains unverified.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hyojung Han
- 发布：2026-11-16；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
