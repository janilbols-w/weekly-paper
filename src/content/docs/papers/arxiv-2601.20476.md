---
title: "In-Context Learning for Diagram Code Generation: What is the Effect on Faithfulness and Quality?"
description: "We investigate how provision of in-context examples based on discourse similarity affects quality and hallucination in diagram code generation from educational materials."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2601.20476) · [PDF](https://arxiv.org/pdf/2601.20476)

## 一句话摘要

We investigate how provision of in-context examples based on discourse similarity affects quality and hallucination in diagram code generation from educational materials.

## 为什么值得关注

待编辑增强。

## 摘要原文

We investigate how provision of in-context examples based on discourse similarity affects quality and hallucination in diagram code generation from educational materials. Using a sample of texts as sources for diagram generation, we test two methods using a conventional text-to-diagram task format, instruction-based zero-shot generation and ICL with text-to-diagram examples, and an unconventional ICL method with a discourse analysis-to-diagram example, which requires a model to generate a diagram from a discourse analysis. We evaluate AI-generated diagrams for faithfulness to provided context and their quality outcomes using both human and automated evaluation. Bayesian data analysis of the human diagram evaluation shows that there is significant evidence that the unconventional task format improves context faithfulness in diagram generation compared to the zero-shot instruction with reducing the odds of context faithfulness hallucination by nearly $70\%$; however, we do not find the ICL having a significant effect on the diagram aesthetic presentation and superficial coherence. Evaluation with the LLM-as-a-judge G-Eval metric shows nearly 4.5-fold increased odds of the perfect faithfulness outcome for the novel ICL task. Our study provides a novel insight into ICL format effect on superficial fluency and faithfulness in context-grounded structured diagram code generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Evanfiya Logacheva, Arto Hellas, Tsvetomila Mihaylova, Juha Sorva, Ava Heinonen, Juho Leinonen
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
