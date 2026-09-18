---
title: "VisKG-LM: Compiling Knowledge Graphs into Visual Memory for Multiple-Choice Question Answering"
description: "Knowledge graphs are usually integrated into question answering by encoding a retrieved subgraph with a graph neural network and fusing it with the language model in the online inference path."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.19158) · [PDF](https://arxiv.org/pdf/2609.19158)

## 一句话摘要

Knowledge graphs are usually integrated into question answering by encoding a retrieved subgraph with a graph neural network and fusing it with the language model in the online inference path.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge graphs are usually integrated into question answering by encoding a retrieved subgraph with a graph neural network and fusing it with the language model in the online inference path. The same subgraph is therefore re-encoded from scratch every time a pair is scored, across training epochs, seeds, and evaluation runs, even though the knowledge graph never changes. We ask whether the retrieved knowledge graphs can instead be compiled once, offline, and then accessed as read-only memory. VisKG-LM shows that it can, by decoupling graph encoding from language reasoning. It serializes each retrieved candidate-specific subgraph as Relation-Labeled Paths and renders the result as an image whose two-dimensional layout preserves the branching structure of the paths. Each image is encoded once, offline, and cached for reuse. At inference, the language model contextualizes the question and candidate from text alone, and only its final layer consults the cached visual memory, reading both its global layout and its local relational detail. The graph information thus enters only after the text has been understood. On the test sets of CommonsenseQA, OpenBookQA, and MedQA-USMLE, VisKG-LMimproves over GreaseLM by $1.2$, $0.8$, and $4.3$ points, respectively, while matching or surpassing GraphVis, a $7$B vision-language model, with only about $400$M online parameters. Against a matched text-only control that receives the identical Relation-Labeled Paths, it gains $4.2$, $6.5$, and $5.1$ points across the three benchmarks. These gains show that the complete visual-memory interface adds value beyond path textualization alone and support compiled visual memory as an alternative to online graph propagation.

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

- taxonomy keywords: online inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yixin Peng, Er Jin, Shiwei Luo, Diego Collarana, Stefan Decker
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
