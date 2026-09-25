---
title: "Automated Extraction of Records of Processing Activities (RoPA) Using Hybrid RAG and Locally Deployed Large Language Models"
description: "Vietnam's Personal Data Protection Law (Law No."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.27359) · [PDF](https://arxiv.org/pdf/2609.27359)

## 一句话摘要

Vietnam's Personal Data Protection Law (Law No.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vietnam's Personal Data Protection Law (Law No. 91/2025/QH15) and Decree No. 356/2025/ND-CP, effective January 1, 2026, require organizations to establish and maintain Records of Processing Activities (RoPA). Manual RoPA preparation is labor-intensive, while cloud-hosted large language models (LLMs) may conflict with data-sovereignty requirements. We propose RoPA Manager, a system for automated RoPA information extraction using hybrid retrieval that combines lexical ranking over tsvector, dense-vector search, Reciprocal Rank Fusion (RRF), and locally deployed LLMs. We introduce a Vietnamese RoPA benchmark with 32 organizations, 77 processing activities, 12 field groups, and 4,338 reference values. Evaluation is reported at three distinct levels. The automated scorer, tested on perturbed data without invoking an LLM, achieved F1 = 0.9493 [0.9436, 0.9548]; this measures scorer robustness rather than end-to-end extraction accuracy. End-to-end extraction achieved token coverage of 50.04-55.25% against the reference labels. Two independent experts reviewed 1,558 reference values (35.9% of the benchmark), found no incorrect values, and achieved 99.68% agreement with PABAK = 0.9936. Value-level precision was not measured. Across 32 paired scenarios on a 24 GB GPU, locally deployed Qwen3.5-27B-GPTQ-Int4 showed no statistically significant difference from cloud-based DeepSeek-V4-Flash (difference 0.20 percentage points in favor of DeepSeek, 95% CI [-0.93, 1.32], p = 0.72), while Gemma-4-31B performed significantly worse (p < 0.01).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：To Duy Hinh, Nguyen Le Quoc Anh, Phan Van Tri, Khuong Nguyen-An
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
