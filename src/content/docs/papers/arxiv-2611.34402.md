---
title: "Any-Rate: Half-Bit Multi-Precision LLM Quantization with Coded Bit-Planes"
description: "Nested multi-precision quantization derives multiple precisions from a single checkpoint by reading only the leading bits of each weight, which makes it attractive for on-device deployment under varying memory and energy budgets."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.34402) · [PDF](https://arxiv.org/pdf/2611.34402)

## 一句话摘要

Nested multi-precision quantization derives multiple precisions from a single checkpoint by reading only the leading bits of each weight, which makes it attractive for on-device deployment under varying memory and energy budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Nested multi-precision quantization derives multiple precisions from a single checkpoint by reading only the leading bits of each weight, which makes it attractive for on-device deployment under varying memory and energy budgets. However, existing methods offer only integer bits, leaving large accuracy gaps between adjacent precisions and severe degradation at 2 bits. To address this, we propose Any-Rate, which serves 2-8 bits from one checkpoint, in half-bit steps over 2-4 bits. Any-Rate restricts some bit-planes to extended Hamming codewords in 8-weight blocks (0.5 bits per weight), shares one LUT per row across precisions, and encodes all precisions jointly with a separate target for each, reducing the loss from sharing bit-planes. Across four LLMs, Any-Rate achieves state-of-the-art accuracy among multi-precision methods at 2 and 3 bits, keeping 69% of FP16 accuracy at 2 bits, and is within one point of the best at 4 bits. It decodes about as fast as existing kernels, and an LPDDR energy model estimates up to 27% less energy at equal accuracy. Code is available at https://github.com/hoonki2002/Any-Rate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hoonki Lee, Haechan Shin, Hyuntaek Jung, Yeonu Choi, Sangyeob Kim
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/hoonki2002/Any-Rate](https://github.com/hoonki2002/Any-Rate)
- 阅读深度：metadata
