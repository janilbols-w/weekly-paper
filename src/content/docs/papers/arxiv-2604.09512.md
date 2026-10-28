---
title: "Integrated electro-optic attention nonlinearities for transformers"
description: "Transformers achieve state-of-the-art performance in language processing and computer vision."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2604.09512) · [PDF](https://arxiv.org/pdf/2604.09512)

## 一句话摘要

Transformers achieve state-of-the-art performance in language processing and computer vision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformers achieve state-of-the-art performance in language processing and computer vision. Their computation increasingly depends on hardware that can keep pace not only with large matrix multiplications, but also with nonlinear operations like Softmax within the core attention mechanism. On digital accelerators, Softmax accounts for only a small fraction of total operations, yet it can disproportionately impact overall inference latency. Here, we use thin-film lithium niobate Mach-Zehnder modulators (MZM) as analog computing elements for low-latency Transformer attention. Our high-speed nonlinearities based on the intrinsic sinusoidal MZM response achieve performance close to digital baselines in Vision Transformers and GPT-2, even under 4-bit input and output quantization. We experimentally characterize the electro-optic response at symbol rates up to 10 GBaud and assess model robustness under corresponding noise conditions. Accounting for the full signal chain, our analysis indicates more than an order of magnitude lower latency relative to previous custom electronic and photonic Softmax implementations. These results establish analog electro-optic devices as nonlinear function units well suited for integration into emerging co-packaged electronic-photonic hardware, offering a path toward high-speed Transformer inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luis Mickeler, Kai Lion, Alfonso Nardi, Jost Kellner, Pierre Didier, Bhavin J. Shastri, Niao He, Rachel Grange
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
