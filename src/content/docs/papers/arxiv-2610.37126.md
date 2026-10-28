---
title: "Mechanistic Failure Modes of Weight Pruning in Transformer Language Models"
description: "Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.37126) · [PDF](https://arxiv.org/pdf/2610.37126)

## 一句话摘要

Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pruned language models are judged almost entirely by accuracy and perplexity, which assumes that preserved output behaviour implies preserved internal computation. We test this assumption with a factorial pruning study on GPT-2, crossing two importance criteria (magnitude, random), two component types (attention heads, MLP neurons) and three sparsity levels (3%, 50%, 70%). Using the fully characterised indirect object identification (IOI) circuit as ground truth, we measure circuit integrity with activation patching, path patching and direct logit attribution. We find two qualitatively distinct failure modes. Magnitude head pruning >= zeroes the circuit: output-facing heads are removed, and the model falls to near-chance. Magnitude neuron pruning at 30% inverts it: all 26 circuit heads remain intact, but Name Mover contributions flip sign, and the model systematically prefers the wrong name (17.7% accuracy). Perplexity ranks it as less damaged than random head pruning (74.6 vs 140.1). A replication of the Greater-Than circuit shows that the critical component type depends on the circuit's architecture. These results show that output metrics and structural checks can both miss mechanistic damage, motivating circuit-level causal analysis as a complementary evaluation of compressed language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nabeelah Faumi, Deshan Sumanathilaka
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
