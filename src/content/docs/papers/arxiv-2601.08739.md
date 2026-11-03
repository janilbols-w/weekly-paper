---
title: "Ctrl-G: Controlling Structural and Interaction Exposure in Knowledge Graph Augmented LLM Reasoning"
description: "Knowledge graphs (KGs) provide structured evidence for Web question answering with large language models (LLMs), but sending retrieved evidence to a remote LLM can expose sensitive graph information."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.08739) · [PDF](https://arxiv.org/pdf/2601.08739)

## 一句话摘要

Knowledge graphs (KGs) provide structured evidence for Web question answering with large language models (LLMs), but sending retrieved evidence to a remote LLM can expose sensitive graph information.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge graphs (KGs) provide structured evidence for Web question answering with large language models (LLMs), but sending retrieved evidence to a remote LLM can expose sensitive graph information. Existing privacy treatments use entity anonymization and relation-centric abstraction to preserve reasoning cues, but transmitted topology remains visible and disclosure accumulates across repeated calls. Distinctive topology can support re-identification of masked entities (structural exposure), while successive calls accumulate additional paths and exploration traces into a broader view of the KG (interaction exposure). Simply sending less evidence is insufficient because restricted, stepwise views may omit the bridge paths required for multi-hop reasoning. To address this, we propose Ctrl-G, to the best of our knowledge the first KG-RAG framework to jointly control structural and interaction exposure to a remote LLM while supporting accurate multi-hop reasoning. To control structural exposure, Ctrl-G locally constructs query-conditioned sanitized views through structural aggregation and pruning, limiting the graph evidence transmitted to a remote LLM. A hierarchical controller couples remote planning with local connected-path exploration across topic entities, using question indicators and retrieved experience to prune candidates while grounding and verifying retained evidence against the original KG. To control interaction exposure, local experience memory reuses abstract, verified reasoning traces to guide exploration modes and depths and gate remote LLM calls, reducing repeated disclosure across questions. Ctrl-G achieves the highest accuracy among the compared methods on five of six benchmarks, exceeding the strongest baseline by up to 13.8 points across model configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingyu Tan, Xiaoyang Wang, Qing Liu, Xiwei Xu, Xin Yuan, Liming Zhu, Wenjie Zhang
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
