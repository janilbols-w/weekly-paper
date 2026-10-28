---
title: "From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn"
description: "For efficiency, industrial large language model (LLM) labelers often pack many candidate labels into one prompt and generate a YES/NO answer for each, even when each decision depends only on the entity and one candidate."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.36383) · [PDF](https://arxiv.org/pdf/2610.36383)

## 一句话摘要

For efficiency, industrial large language model (LLM) labelers often pack many candidate labels into one prompt and generate a YES/NO answer for each, even when each decision depends only on the entity and one candidate.

## 为什么值得关注

待编辑增强。

## 摘要原文

For efficiency, industrial large language model (LLM) labelers often pack many candidate labels into one prompt and generate a YES/NO answer for each, even when each decision depends only on the entity and one candidate. Generating these independent decisions as one answer list couples them, spends decoding on the list, and relies on the list being well-formed. In this paper, we present an end-to-end recipe that reformulates the labeler as semantic scoring, fine-tuning it on single-candidate prompts to return each decision as one answer-token score from a prefill-only pass. We also adapt Multiple-Item Scoring (MIS) to score hundreds of candidates in one sequence with attention masked between them. Deployed for profile qualification labeling at LinkedIn, semantic scoring changes at most 0.01% of decisions when candidates are reordered and matches the agreement with reference labels that packed generation reaches only with about 4.7x as many training pairs. The MIS-based stack raises throughput over the deployed stack by 1.24x offline and 1.9x in model serving under a one-second p99 latency target. For offline batch inference, we implement MIS-based scoring as a reusable, model-agnostic Ray Data API proposed for upstream adoption. Model serving uses MIS support contributed to SGLang.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jian Sheng, Sriram Vasudevan, Sundara Raman Ramachandran, Yang Hu, Junyu Zhou, Xiaojing Ma, Haolan Qin, Tiffany Zhou, Vedant Vipul Jhaveri, Ashwini Bhingare, Chinmay Kini, Qing Lan, Xiaoqing Wang, Suleyman Cetintas, Fedor Borisyuk
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
