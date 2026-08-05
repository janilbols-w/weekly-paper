---
title: "RAG Strategies for Natural Language-Based SQL Query and REST API Call Generation"
description: "Enterprise software systems commonly expose business functionality through both relational databases and REST APIs."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.07086) · [PDF](https://arxiv.org/pdf/2602.07086)

## 一句话摘要

Enterprise software systems commonly expose business functionality through both relational databases and REST APIs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Enterprise software systems commonly expose business functionality through both relational databases and REST APIs. Accessing these interfaces requires specialized technical knowledge, as users must determine whether a request requires a database query or an API operation and understand the corresponding schemas, endpoints, and parameters. This creates demand for natural language interfaces that translate user requests into SQL queries and REST API calls. While large language models (LLMs) show promise for structured code generation, they typically lack reliable knowledge of enterprise-specific schemas, endpoints, and documentation. Retrieval-augmented generation (RAG) addresses this limitation by grounding generation in external documentation. However, prior work largely studies SQL query generation and REST API call generation separately, despite enterprise documentation environments often containing both database schemas and API specifications. We systematically evaluate standard RAG, Self-RAG, and CoRAG across SQL query generation, REST API call generation, and a combined task requiring routing between both operation types. Using SAP Transactional Banking as a realistic enterprise use case, we constructed an execution-validated dataset and compared retrieval strategies under database-only, API-only, and mixed-documentation settings. Retrieval augmentation proved essential for reliable enterprise structured generation, substantially improving performance over a no-retrieval baseline. CoRAG achieved the best results in the combined SQL query and REST API call setting, with statistically significant improvements in exact-match accuracy over standard RAG, primarily driven by stronger SQL query generation under mixed-documentation retrieval conditions. Overall, findings show that retrieval strategy substantially affects structured generation performance under mixed-documentation settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tim Schlippe, Simon Martin, Michael Marketsm\"uller
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
