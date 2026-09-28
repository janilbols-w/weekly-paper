---
title: "The Right Information Extraction Pipeline Depends on the Document: Accuracy-Energy Trade-offs for Small, Local Models"
description: "Whether an information extraction pipeline should process page images or parsed text depends on the document, and the answer flips across the layout spectrum."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.31341) · [PDF](https://arxiv.org/pdf/2609.31341)

## 一句话摘要

Whether an information extraction pipeline should process page images or parsed text depends on the document, and the answer flips across the layout spectrum.

## 为什么值得关注

待编辑增强。

## 摘要原文

Whether an information extraction pipeline should process page images or parsed text depends on the document, and the answer flips across the layout spectrum. We study this trade-off under a constraint that rules out (closed) cloud services: privacy-sensitive documents processed on-premise by small ($\le 8\mathrm{B}$ parameter) text-only and vision--language models, evaluated on both accuracy and energy over a design space spanning input representation, model family, and inference configuration. Benchmarking on the near-plain-text Kleister-NDA contracts and the layout-rich VRDU forms, we find that batching is the dominant energy lever, cutting energy per page by 38-85% at no cost in accuracy, while FP8 quantization saves 27-32% when requests are served one at a time but less than 1mWh per page (9-19%) once batching is applied. Preprocessing dominates what remains: neural OCR costs $17\times$ more energy per page than classical OCR and never reaches the Pareto frontier. Which representation wins flips with the type of document: vision--language models on layout-rich documents and small text-only models with a cheap parser on near-plain text, where they are both more accurate and cheaper than any vision--language configuration. Our work yields concrete guidelines for energy-efficient, privacy-compliant local information extraction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Christoph Walser, Mauricio Fadel Argerich, Jonathan F\"urst
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
