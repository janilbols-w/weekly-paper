---
title: "Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding"
description: "Decoder hidden states from different layers of large language models (LLMs) often encode complementary information."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.12939) · [PDF](https://arxiv.org/pdf/2610.12939)

## 一句话摘要

Decoder hidden states from different layers of large language models (LLMs) often encode complementary information.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decoder hidden states from different layers of large language models (LLMs) often encode complementary information. However, existing speculative decoding methods typically rely on a small set of target-model layers chosen using fixed, position-based heuristics. Selecting an optimal subset of layers is inherently a combinatorial problem, making exhaustive evaluation infeasible even for moderately deep models. In this work, we present a principled framework for multi-layer hidden-state selection for speculative decoding based on two complementary criteria: informativeness, measured through matrix-entropy analysis, and diversity, quantified using centered kernel alignment (CKA). We investigate layer-wise Shannon entropy, aggregate entropy under hidden-state concatenation, and pairwise CKA dynamics across depth, revealing distinct geometric and informational compartments within decoder representations. Motivated by these findings, we propose entropy and CKA-based layer selection algorithms that favor hidden-state sets that are both highly informative and minimally redundant. As part of this framework, we introduce token-entropy filtering, which removes hidden states associated with low predictive-entropy tokens, thereby improving the quality of layer-selection statistics. In EAGLE3-style speculative decoding, our selected sets outperform fixed baseline choices, including the default $[2, N//2, N-3]$ rule, while providing a clearer explanation of why some defaults can remain competitive. Our results provide a practical recipe for multi-layer hidden-state selection for speculative decoding, insights into the geometry and information in LLM decoder states, and a foundation for extending similar analysis to related applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani, Risheek Garrepalli, Mingu Lee
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
