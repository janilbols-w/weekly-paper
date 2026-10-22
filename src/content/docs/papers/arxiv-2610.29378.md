---
title: "Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories"
description: "Quantization-aware training (QAT) aims to recover reasoning capabilities in low-bit large language models (LLMs)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.29378) · [PDF](https://arxiv.org/pdf/2610.29378)

## 一句话摘要

Quantization-aware training (QAT) aims to recover reasoning capabilities in low-bit large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization-aware training (QAT) aims to recover reasoning capabilities in low-bit large language models (LLMs). Existing recipes typically supervise the quantized student with the original full-precision model on fixed response sequences. However, the resulting low-bit quantized models still struggle on long-horizon reasoning tasks and often fail to terminate within a token budget that suffices for the full-precision model. We identify two challenges in closing this gap. First, fixed-response supervision leaves a mismatch between training prefixes and those encountered during student generation, and this trajectory divergence grows as responses lengthen. Second, on its own prefixes, the student underpredicts some next-token candidates and overpredicts others, and this distributional misalignment becomes more frequent at high-entropy prefixes. We present OnQ, a low-bit recovery pipeline that combines on-policy distillation and candidate-wise Dynamic KL. Starting from block-wise calibration, the quantized student generates responses and receives full-precision teacher supervision on its own prefixes. Dynamic KL weights forward and reverse KL by each candidate's teacher-student probability ratio to balance correction of under- and overprediction. Across Qwen3-1.7B, 4B, and 8B at 2- and 3-bit precision, OnQ achieves the highest nine-benchmark average, with the largest gains on long-horizon reasoning benchmarks. At 2 bits, it outperforms every baseline on every benchmark at every model size, improving the Qwen3-8B average by 10.26 points over the strongest baseline. It also produces shorter responses with fewer truncations and repetitive errors.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boyuan Zheng, Jing Xiong, Chenwei Wu, Hui Shen, Zesen Zhao, Hei Ting Una Chan, Xueshen Liu, Zhen Zhang, Liyue Shen, Zechun Liu, Z. Morley Mao
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
