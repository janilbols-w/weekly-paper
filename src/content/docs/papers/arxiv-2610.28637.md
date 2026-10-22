---
title: "To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems"
description: "Disaggregated \\textsc{LLM} serving separates prefill and decode across node pools, placing a network fabric between \\textsc{KV}-cache computation and consumption."
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.28637) · [PDF](https://arxiv.org/pdf/2610.28637)

## 一句话摘要

Disaggregated \textsc{LLM} serving separates prefill and decode across node pools, placing a network fabric between \textsc{KV}-cache computation and consumption.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregated \textsc{LLM} serving separates prefill and decode across node pools, placing a network fabric between \textsc{KV}-cache computation and consumption. This breaks a key assumption of classical cache policies: a miss no longer incurs only local recomputation, but also network transfer to the decode node. Likewise, admitting a block to the global cache requires an additional transfer, so poor retention decisions waste both memory and bandwidth. We present \textbf{KVLearn}, a learning-based framework for cost-aware \textsc{KV}-cache retention in disaggregated serving. KVLearn includes: (i) a lightweight Prefix Reuse Predictor (\textsc{PRP}) that estimates reuse probability from structural and temporal prefix features without modifying model weights; (ii) a Cost-Aware Retention Score (\textsc{CARS}) that converts reuse probability into keep/admit decisions using recomputation, transfer, and storage costs; and (iii) an Adaptive Threshold Controller (\textsc{ATC}) that adjusts admission thresholds online from observed hit rates and memory pressure. We integrate KVLearn into a globally disaggregated serving topology and evaluate it on text and multimodal workloads, including large image/video-derived \textsc{KV} blocks with heterogeneous reuse patterns. KVLearn reduces end-to-end time-to-first-token by up to 56% versus No-Cache, 38% versus LRU-Pool, and 33% versus Mooncake-style baselines, while cutting inter-node \textsc{KV} transfer volume by up to 53% versus LRU-Pool. On MM-Session, throughput remains within ${\sim}5%$ of oracle. Code is available at https://github.com/FastLM/KVLearn.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Dong Liu, Yanxuan Yu, Eric Jiang, Shu Wang, Ying Nian Wu
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/FastLM/KVLearn](https://github.com/FastLM/KVLearn)
- 阅读深度：metadata
