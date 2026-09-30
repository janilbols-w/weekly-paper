---
title: "IndexRAG: Index-Time Reasoning for Multi-Hop Retrieval-Augmented Generation"
description: "Multi-hop question answering (QA) requires reasoning across multiple documents, yet existing retrieval-augmented generation (RAG) approaches address this either through graph-based methods requiring additional online processing or iterative multi-step reasoning."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2603.16415) · [PDF](https://arxiv.org/pdf/2603.16415)

## 一句话摘要

Multi-hop question answering (QA) requires reasoning across multiple documents, yet existing retrieval-augmented generation (RAG) approaches address this either through graph-based methods requiring additional online processing or iterative multi-step reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-hop question answering (QA) requires reasoning across multiple documents, yet existing retrieval-augmented generation (RAG) approaches address this either through graph-based methods requiring additional online processing or iterative multi-step reasoning. We present IndexRAG, a novel approach that shifts cross-document reasoning from online inference to offline indexing. IndexRAG identifies bridge entities shared across documents and generates bridging facts as independently retrievable units, requiring no additional training or fine-tuning. Experiments on three widely-used multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA, MuSiQue) show that IndexRAG improves F1 over Naive RAG by 4.6 points on average, while requiring only single-pass retrieval and a single LLM call at inference time. When combined with IRCoT, IndexRAG achieves the best average performance among all evaluated methods, including graph-based baselines such as HippoRAG2 and FastGraphRAG, while relying on a flat vector index. Our code is available at https://github.com/Continuum-AI-Corp/IndexRAG .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: online inference
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhenghua Bao, Yi Shi
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Continuum-AI-Corp/IndexRAG](https://github.com/Continuum-AI-Corp/IndexRAG)
- 阅读深度：metadata
